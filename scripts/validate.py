#!/usr/bin/env python3
"""Validate catalog entries without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
APP_DIR = ROOT / "data" / "apps"
REQUIRED = {
    "slug",
    "name",
    "status",
    "category",
    "repoUrl",
    "license",
    "openSourceStatus",
    "maintainer",
    "paidAlternatives",
    "sourceDirectory",
    "muapiFit",
    "muapiMode",
    "muapiCapabilities",
    "muapiDocsUrl",
    "honestScope",
    "gaps",
    "externalDependencies",
    "vibeCodedEvidence",
    "vibeCodedEvidenceUrl",
    "lastVerified",
}
ALLOWED_STATUS = {"existing", "planned", "consolidate"}
ALLOWED_OPEN_SOURCE_STATUS = {"open-source", "license-needed", "planned"}
ALLOWED_FIT = {"high", "medium", "low"}
ALLOWED_MODE = {"required", "optional", "planned"}
ALLOWED_EVIDENCE = {"author-claimed", "maintainer-verified", "unverified"}
SLUG_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FORBIDDEN_TERMS = (
    "wavespeed.ai",
    "kie.ai",
    "fal.run",
    "runware.ai",
)


def is_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def add_error(errors: list[str], path: Path, message: str) -> None:
    errors.append(f"{path.relative_to(ROOT)}: {message}")


def validate_entry(path: Path, data: object, seen_slugs: set[str]) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return [f"{path.relative_to(ROOT)}: top-level value must be an object"]

    missing = REQUIRED - data.keys()
    if missing:
        add_error(errors, path, f"missing fields: {', '.join(sorted(missing))}")

    slug = data.get("slug")
    if not isinstance(slug, str) or not SLUG_PATTERN.fullmatch(slug):
        add_error(errors, path, "slug must be lowercase kebab-case")
    elif slug in seen_slugs:
        add_error(errors, path, f"duplicate slug: {slug}")
    else:
        seen_slugs.add(slug)
    if path.stem != slug:
        add_error(errors, path, "filename must match slug")

    for field in ("name", "category", "license", "maintainer", "honestScope"):
        if not isinstance(data.get(field), str) or not data[field].strip():
            add_error(errors, path, f"{field} must be a non-empty string")

    status = data.get("status")
    if status not in ALLOWED_STATUS:
        add_error(errors, path, f"status must be one of {sorted(ALLOWED_STATUS)}")

    source_status = data.get("openSourceStatus")
    if source_status not in ALLOWED_OPEN_SOURCE_STATUS:
        add_error(
            errors,
            path,
            f"openSourceStatus must be one of {sorted(ALLOWED_OPEN_SOURCE_STATUS)}",
        )

    repo_url = data.get("repoUrl")
    if repo_url is not None and not is_url(repo_url):
        add_error(errors, path, "repoUrl must be an https/http URL or null")
    if status == "planned" and repo_url is not None:
        add_error(errors, path, "planned entries must use repoUrl: null")
    if status != "planned" and repo_url is None:
        add_error(errors, path, "existing/consolidate entries need a repoUrl")

    if source_status == "open-source" and data.get("license") in {
        "TBD",
        "No license file found",
        "Unknown",
    }:
        add_error(errors, path, "open-source entries need a verified license value")
    if status == "planned" and source_status != "planned":
        add_error(errors, path, "planned entries must use openSourceStatus: planned")

    for field in ("paidAlternatives", "muapiCapabilities", "gaps", "externalDependencies"):
        value = data.get(field)
        if not isinstance(value, list) or any(
            not isinstance(item, str) or not item.strip() for item in value
        ):
            add_error(errors, path, f"{field} must be a list of non-empty strings")
    if not isinstance(data.get("paidAlternatives"), list) or not data["paidAlternatives"]:
        add_error(errors, path, "paidAlternatives must not be empty")
    if not isinstance(data.get("muapiCapabilities"), list) or not data["muapiCapabilities"]:
        add_error(errors, path, "muapiCapabilities must not be empty")

    source = data.get("sourceDirectory")
    if not isinstance(source, dict):
        add_error(errors, path, "sourceDirectory must be an object")
    else:
        for field in ("name", "url"):
            if not isinstance(source.get(field), str) or not source[field].strip():
                add_error(errors, path, f"sourceDirectory.{field} must be a string")
        if not is_url(source.get("url")):
            add_error(errors, path, "sourceDirectory.url must be a URL")
        if not isinstance(source.get("slugs"), list) or not source["slugs"]:
            add_error(errors, path, "sourceDirectory.slugs must be a non-empty list")

    if data.get("muapiFit") not in ALLOWED_FIT:
        add_error(errors, path, f"muapiFit must be one of {sorted(ALLOWED_FIT)}")
    if data.get("muapiMode") not in ALLOWED_MODE:
        add_error(errors, path, f"muapiMode must be one of {sorted(ALLOWED_MODE)}")
    if not is_url(data.get("muapiDocsUrl")):
        add_error(errors, path, "muapiDocsUrl must be a URL")
    if data.get("vibeCodedEvidence") not in ALLOWED_EVIDENCE:
        add_error(
            errors,
            path,
            f"vibeCodedEvidence must be one of {sorted(ALLOWED_EVIDENCE)}",
        )
    evidence_url = data.get("vibeCodedEvidenceUrl")
    if evidence_url is not None and not is_url(evidence_url):
        add_error(errors, path, "vibeCodedEvidenceUrl must be a URL or null")

    try:
        date.fromisoformat(str(data.get("lastVerified")))
    except ValueError:
        add_error(errors, path, "lastVerified must be an ISO date")

    serialized = json.dumps(data, ensure_ascii=False).lower()
    for term in FORBIDDEN_TERMS:
        if term in serialized:
            add_error(errors, path, f"contains forbidden internal routing term: {term}")

    return errors


def main() -> int:
    paths = sorted(APP_DIR.glob("*.json"))
    if not paths:
        print("No catalog entries found", file=sys.stderr)
        return 1

    errors: list[str] = []
    seen_slugs: set[str] = set()
    for path in paths:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            add_error(errors, path, f"invalid JSON: {exc}")
            continue
        errors.extend(validate_entry(path, data, seen_slugs))

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    print(f"Validated {len(paths)} catalog entries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

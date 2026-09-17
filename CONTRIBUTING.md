# Contributing

Thanks for helping build a useful catalog of open-source, vibe-coded SaaS alternatives.

## Add an entry

1. Add one JSON file under data/apps using the slug as the filename.
2. Follow data/schema/app.schema.json.
3. Link the actual repository or set repoUrl to null for a planned entry.
4. Verify the repository license. Use openSourceStatus license-needed when no license file is present.
5. Link the relevant Can I Vibecode It? source slugs when a matching record exists.
6. Describe the Muapi capabilities used and the smaller workflow implemented.
7. State the important gaps instead of claiming full product parity.
8. Run the validator:

~~~bash
python scripts/validate.py
~~~

## Evidence rules

Use the following values for vibeCodedEvidence:

- author-claimed: the project author or README explicitly claims AI-assisted or vibe-coded development;
- maintainer-verified: a maintainer has checked evidence beyond an unsubstantiated label;
- unverified: the project is relevant but the development method has not been confirmed.

Do not infer vibe-coded status from a project's name, use of an AI API, or a single generated asset.

## Muapi and security rules

- Use public Muapi documentation and public model/capability names.
- Never add API keys, tokens, private URLs, internal routing names, or provider relationships.
- Use official platform APIs and OAuth for publishing or account data.
- Do not encourage scraping, bypassing access controls, evading rate limits, or copying licensed catalogs.
- Keep claims bounded when a paid product's core value is proprietary data, distribution, infrastructure, or licensing.

## Pull request checklist

- [ ] The JSON filename matches slug.
- [ ] The repository URL and license status are accurate.
- [ ] The entry is an application or a clearly labeled planned application.
- [ ] Paid alternatives and source slugs are relevant.
- [ ] Muapi fit, capabilities, scope, gaps, and external dependencies are documented.
- [ ] Vibe-coded evidence is labeled honestly.
- [ ] python scripts/validate.py passes.

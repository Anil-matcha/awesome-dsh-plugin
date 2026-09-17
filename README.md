# Awesome VibeCoded SaaS

> Open-source, vibe-coded alternatives to paid SaaS — powered by Muapi.

A curated catalog of runnable open-source applications and build plans that turn paid SaaS workflows into focused, inspectable projects. The catalog starts with Muapi-backed image, video, audio, text, SEO, YouTube, social, and creator-commerce applications.

This is an application catalog, not a generic model list or a live proxy for arbitrary APIs. Each entry explains the paid product it relates to, the smaller workflow it actually covers, the Muapi capabilities it uses, and the gaps that remain.

## Why this exists

The best way to promote an API is to show it solving useful end-user problems. This repository connects:

1. A recognizable paid-SaaS workflow.
2. A runnable open-source project or an explicitly labeled planned build.
3. A clear Muapi integration.
4. An honest explanation of what is and is not replaced.

The catalog is inspired by the contribution format of [Can I Vibecode It?](https://github.com/canivibecodeit/canivibecodeit), which keeps one structured record per app and accepts additions through pull requests.

## Current catalog

The first seed contains 13 entries:

| Project | Status | Muapi fit | Related paid workflows |
|---|---|---|---|
| [Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | Existing | High | Midjourney, OpenArt, DreamStudio, Kling, Runway, Pika |
| [Open-Pomelli](https://github.com/SamurAIGPT/Open-Pomelli) | Existing | High | Canva, Adobe Express, Flair AI, Pebblely, PhotoRoom |
| [Vibe-Workflow](https://github.com/SamurAIGPT/Vibe-Workflow) | Existing | High | Krea, Wireflow, visual creative pipelines |
| [AI Clipping Generator](https://github.com/SamurAIGPT/ai-clipping-generator) | Existing | High | OpusClip, Revid AI, Descript, Pictory, VEED |
| [AI YouTube Shorts Generator](https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator) | Existing | Medium | OpusClip, Revid AI, short-form repurposing |
| [AI Faceless Video Generator](https://github.com/SamurAIGPT/AI-Faceless-Video-Generator) | Existing | High | Creatify, HeyGen, Synthesia, Vidnoz |
| [AI B-roll](https://github.com/Anil-matcha/AI-B-roll) | Existing | High | AI-assisted stock and generated video assets |
| [Open-VidIQ](https://github.com/SamurAIGPT/Open-VidIQ) | Consolidate | High | 1of10, Wholana, Vernigo, YouTube research |
| [social-post](https://github.com/SamurAIGPT/social-post) | Existing | Medium | Buffer, Postiz, FeedHive, Flick, Typefully |
| [my-podcast](https://github.com/SamurAIGPT/my-podcast) | Existing | Medium | ElevenLabs, Murf, Castmagic, Swell AI, Podcastle |
| [Amazon Product Studio](https://github.com/SamurAIGPT/amazon-product-studio) | Existing | High | Flair AI, Pebblely, PhotoRoom, Pixelcut |
| Open SEO / Open GEO | Planned | High | Ahrefs, Semrush, BrandGEO, Frase, Profound |
| Open YouTube Growth Radar | Planned | High | 1of10, Wholana, Vernigo, TranscriptAPI |

Entries with a verified MIT license are marked open-source. Projects without a repository license are included as portfolio candidates but marked license-needed in their metadata; they must not be described as legally open-source until a license is added.

Browse the structured records in [data/apps](data/apps). The source-directory snapshot and attribution are in [data/sources](data/sources).

## What belongs here

An entry should be:

- an end-user application, not only an SDK, model wrapper, prompt, or MCP server;
- open-source with a visible license, or clearly labeled as planned or license-needed;
- useful as a focused alternative to a paid SaaS workflow;
- runnable with documented setup and dependencies;
- honest about missing data, distribution, infrastructure, licensing, and platform integrations;
- materially powered by Muapi when it claims Muapi-backed status.

“Vibe-coded” describes the development method, not the quality or security of a project. Each record includes a vibe-coded evidence status: author-claimed, maintainer-verified, or unverified. We do not infer that status from the presence of AI-related code.

## Muapi positioning rules

Muapi-backed projects may use:

- image, video, audio, text, editing, and lipsync generation;
- SEO, SERP, keyword, rank, backlink, Lighthouse, and AI-visibility capabilities;
- YouTube analytics, metadata, subtitles, comments, publishing, and thumbnails;
- official social-platform connections and application-side orchestration.

Projects must use public Muapi capabilities and must not expose internal routing details, credentials, or provider relationships.

Do not claim to recreate a proprietary data index, licensed media catalog, social network, voice-cloning safety system, or full enterprise product when the project only implements a focused workflow.

## Repository structure

~~~text
data/apps/<slug>.json       # one promoted application or planned build
data/sources/*.json         # upstream directories and attribution
data/schema/app.schema.json # metadata contract
scripts/validate.py         # dependency-free validation
~~~

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md), add one metadata file under [data/apps](data/apps), and run:

~~~bash
python scripts/validate.py
~~~

Pull requests should add evidence, not just a product name. Include a repository link, license status, the related source-directory records, the Muapi capabilities used, the honest scope, and known gaps.

## Disclaimer

This project is not affiliated with or endorsed by the paid products named in the catalog. Product names are used only to describe compatibility, alternatives, or scope. Platform access must use official APIs and comply with each platform's terms.

## License

This catalog and its validation code are released under the [MIT License](LICENSE). Individual projects retain their own licenses.

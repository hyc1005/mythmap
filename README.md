# MythMap — Where the Mountains and Seas Begin

A bilingual atlas for exploring Chinese myths, discovering creatures and reading their sources.

[![Explore the demo](https://img.shields.io/badge/Demo-Explore_the_atlas-974932?style=for-the-badge)](https://hyc1005.github.io/mythmap/)
[![Build & verify](https://img.shields.io/github/actions/workflow/status/hyc1005/mythmap/deploy-pages.yml?branch=main&label=Build&style=for-the-badge)](https://github.com/hyc1005/mythmap/actions/workflows/deploy-pages.yml)

**English** · [简体中文](README.zh-CN.md)

## Understand it in 30 seconds

- **What it is**: Woodcut illustrations and interactive maps connecting myths from the *Classic of Mountains and Seas* and other ancient texts.
- **What you can do**: Watch stories, read source passages, filter creatures and deities, and inspect separate geographic evidence.
- **What it cannot prove**: Illustrations, narrative coordinates and modern place associations cannot establish where mythical events occurred.

![Home: the Pangu opening scene and chapter navigation](docs/media/home.webp)

## See what you can do

| Story playback | Bestiary |
| --- | --- |
| ![Story playback: Suiren making fire with playback controls](docs/media/story-playback.webp) | ![Bestiary: illustrated cards with book and body-form filters](docs/media/bestiary.webp) |
| Follow a story, pause or replay, and open its textual sources. | Filter by name, book or body form; namesakes retain separate accounts. |
| **Geographic evidence** | **12-second walkthrough** |
| ![Geographic evidence: real basemap and documented associations](docs/media/geographic-evidence.webp) | ![Walkthrough: story playback, bestiary and search](docs/media/tour.gif) |
| Inspect modern place references separately from narrative diagrams. | Recorded from the actual interface, showing playback and creature search. |

## Current scope

- **480 reading passages**: Southern 43, Western 82, Northern 92, Eastern 51 and Central 212. Completing the remaining thirteen books is deferred; see the [content inventory](docs/content-coverage.md) for scope and review status.
- **312 creature accounts and 72 deity accounts**: namesake groups, six body-form categories and combined book, feature and reading filters, with 24 name groups per batch.
- **Chinese and English**: story playback, source reading, search, favorites and reading-position recovery. The prologue and seven chapters are the project's narrative arrangement.

## Sources and licensing

The maintainer developed the code with generative models and releases it under [MIT](LICENSE). No additional reuse permission is granted for project paraphrases, model-generated translations or AI artwork. Source transcriptions, scans, fonts and geographic data retain their own conditions; see [asset provenance and licensing](ASSETS.md).

Translations are model-generated. Illustrations use OpenAI image generation, sometimes with existing project artwork as an internal style reference. Unverified models and third-party rights remain explicitly unresolved; neither professional translation review nor freedom from infringement is guaranteed.

Use [CITATION.cff](CITATION.cff) to cite the project and credit the relevant sources when citing individual texts, scans or map data. Geographic screenshots retain Tianditu attribution; their usage conditions remain an open licensing item.

## Development and maintenance

<details>
<summary>Repository map and data maintenance</summary>

| Path | Responsibility |
| --- | --- |
| [frontend/](frontend/) | React/Vite website; Pages publishes its build output |
| [frontend/src/](frontend/src/) | UI, state, localization and bestiary metadata |
| [frontend/public/data/](frontend/public/data/) | Runtime data and published artwork variants |
| [frontend/artwork-source/](frontend/artwork-source/) | Originals, prompts and reproducibility records |
| [data/](data/README.md) | Book builders, source snapshots and review records |
| [frontend/scripts/](frontend/scripts/README.md) | Verification, preview, image and font tools |
| [docs/](docs/README.md) | Data contracts, source inventories and documentation |

Short names, body forms and namesake groups live in `frontend/src/bestiary-metadata.json`, independently of generated source text. See the [API contract](docs/API_CONTRACT.md). Originals and scans stay in place; the [large-file inventory](docs/large-files.tsv) is an assessment, not a deletion or relocation list.

### Optional prototypes

`backend/`, `backend-java/` and `database/` are retained optional prototypes. The static site requires no backend or database. The development proxy still references Java, and CI still tests FastAPI; this change does not move them into legacy or another branch. See the [backend guide](backend/README.md), [Java launcher](backend-java/run.ps1) and [database guide](database/README.md).

</details>

<details>
<summary>Local development</summary>

Requires Node.js 22 or a newer compatible version.

```bash
cd frontend
npm ci
npm run dev -- --host 127.0.0.1
```

Open [127.0.0.1:5173](http://127.0.0.1:5173/). Development tries the optional Java API on port 8081, then falls back to bundled data. To use that API, run `backend-java/run.ps1` with JDK 17 or newer. Production uses bundled data unless `VITE_API_BASE_URL` is configured; that setting is public in the build output.

The geographic basemap uses a Tianditu **browser application** key in ignored `frontend/.env.local` as `VITE_TIANDITU_KEY`. Configure the provider's domain allowlist for `hyc1005.github.io,127.0.0.1`. Reading and local evidence remain available when the basemap is unavailable.

</details>

<details>
<summary>Build and complete verification</summary>

From `frontend/`:

```bash
npx playwright install chromium webkit
npm run build -- --base /mythmap/
npm run verify:data
npm run verify:cache
npm run verify:publish
node scripts/with-preview.mjs --base /mythmap/ -- node scripts/verify-bestiary.mjs
node scripts/with-preview.mjs --base /mythmap/ -- node scripts/verify-design.mjs
```

The [script index](frontend/scripts/README.md) lists the remaining reading, search, narrative and book checks. The preview wrapper assigns a free port and stops its own process after completion or failure. For manual preview, run `npm run preview:managed -- --base /mythmap/` and stop it with Ctrl+C; do not rebuild the same `dist/` while tests are using it. QA output stays in `output/qa/`. Routine verification uses Chromium and WebKit; Firefox is not part of the supported verification matrix.

</details>

<details>
<summary>Deployment and rollback</summary>

Select **GitHub Actions** in repository Settings → Pages, and set the Actions secret **TIANDITU_BROWSER_KEY**. Pushes to `main` that affect the frontend, data, backend/database or workflows run [.github/workflows/deploy-pages.yml](.github/workflows/deploy-pages.yml). Documentation-only pushes do not deploy; manual dispatch is also available.

Deployment waits for all required checks and publishes the same verified artifact. Do not commit `dist/`, dependencies, environment files or QA output. Roll back by reverting the relevant commit and pushing.

</details>

<details>
<summary>Historical coursework</summary>

[Course report](docs/coursework/课程报告.md) · [Presentation walkthrough](docs/coursework/答辩演示流程.md)

Retained historical material, separate from current development, deployment and primary navigation.

</details>

# MythMap — Where the Mountains and Seas Begin

One scroll of mountains and seas, seven chapters of myth. MythMap presents ancient Chinese mythology in a hand-printed woodblock style, exploring the world of the *Classic of Mountains and Seas* (Shan Hai Jing) through maps, animations, and illustrations of mythical beasts.

**[Try it live →](https://hyc1005.github.io/mythmap/)**

**English** | [中文版](./README.zh-CN.md)

## What You Can Explore

- **Myth World Map**: Starting from the Pangu creation prologue, browse seven story chapters with their locations and divine realms.
- **Story Animations**: Play, pause, replay, and view full-screen.
- **Bestiary**: Browse 32 mythical beasts, searchable by name, appearance, or chapter.
- **Source Citations**: Click any map location or beast card to read its description and the passages it cites.

Just open the page — it works on desktop and mobile. The map expresses chapter orientation and narrative relationships, not real distances or precise dates; the illustrations are artistic interpretations of the source texts.

---

## Development & Maintenance

The sections below are for running locally, deploying, and maintaining data.

### Tech Stack & Project Layout

The frontend uses **React 19**, **Vite 6**, **OpenLayers 10**, and **Remotion 4** for animations. The online version is built by GitHub Actions and hosted on GitHub Pages using built-in data — no backend or database required.

| Directory | Purpose |
| --- | --- |
| `frontend/src/` | App entry and shared state/helpers |
| `frontend/src/components/` | Map, gallery, search and reading panels |
| `frontend/src/animations/`, `frontend/src/styles/` | Story renderers and site styles |
| `frontend/public/data/` | Site data and published assets |
| `frontend/artwork-source/` | Illustration originals and backup assets |
| `frontend/scripts/` | Layout and narrative verification |
| `backend-java/` | Optional Java API |
| `backend/`, `database/` | Legacy FastAPI/PostGIS prototype and database tools |
| `data/`, `docs/` | Data maintenance tools and project materials |

### Running Locally

Requires Node.js 22 or a newer compatible version. From the `frontend/` directory:

```bash
npm ci
npm run dev -- --host 127.0.0.1
```

Open [the local dev page](http://127.0.0.1:5173/#world). In dev mode the app attempts to reach the optional API and falls back to built-in data automatically when it is not running.

The optional Java API requires JDK 17 or newer; run `run.ps1` in `backend-java/` (default port 8081). The production build does not request the API by default; external API configuration lives in `frontend/.env.example`, and `VITE_API_BASE_URL` is exposed in the build output.

### Build & Verification

From `frontend/`, build and run checks through the managed preview entry point. Tests use a dynamic port. The wrapper closes its preview process on completion, failure or interruption and verifies that the port is released:

```bash
npm run build -- --base /mythmap/
node scripts/with-preview.mjs --base /mythmap/ -- node scripts/verify-design.mjs
node scripts/with-preview.mjs --base /mythmap/ -- node scripts/verify-guided-tour.mjs
node scripts/with-preview.mjs --base /mythmap/ -- node scripts/verify-reading.mjs
node scripts/with-preview.mjs --base /mythmap/ -- node scripts/verify-resume.mjs
node scripts/with-preview.mjs --base /mythmap/ -- node scripts/verify-search.mjs
node scripts/with-preview.mjs --base /mythmap/ -- node scripts/verify-narrative.mjs
```

For manual preview, run `npm run preview:managed -- --base /mythmap/` on 127.0.0.1:4183 and press Ctrl+C when finished. An occupied port is rejected without stopping the existing process. Do not rebuild the same `dist/` while verification is running.

`verify:design` covers bilingual layouts at six viewport sizes, mobile panel focus and scroll locking, body contrast, six illustration samples, playback preservation and PNG paper color. `verify:layout` checks five viewport sizes, animation, fullscreen and details; `verify:narrative` also checks the complete narrative, assets and timeline. Screenshots are retained in `output/qa/`. Report local Firefox startup failures separately; CI retains checks in all three browser engines.

Before release, re-check animations, map fullscreen, beast search, detail closing, and citation links on desktop and mobile, and confirm refreshes work and no images return 404.

### GitHub Pages Deployment

The workflow lives at `.github/workflows/deploy-pages.yml`. In the repository **Settings → Pages**, select **GitHub Actions**; pushes to `main` that touch the frontend or the workflow build and publish automatically. Documentation-only changes do not trigger a web deployment.

The workflow handles the Pages sub-path automatically. Deployment waits for data, cache, backend, bilingual, exploration, cross-browser repair and full narrative checks, then publishes the verified `frontend/dist/` artifact without rebuilding it. Root-path builds are also checked. No need to commit build artifacts; to roll back, use `git revert` and push.

### Data & Artwork Maintenance

- Primary data lives in `frontend/public/data/`: `myth-world.json` plus `catalog.json`, `story-animations.json`, and `kuafu-journey.json` under `atlas/`.
- Citation and asset review uses `atlas/review.json` and `atlas/artwork-manifest.json`; original artwork is kept in `frontend/artwork-source/`.
- `data/build_myth_atlas.py` writes legacy output to `output/legacy-atlas/` and refuses to overwrite current website data.
- The optional static map is generated by `data/render_myth_atlas.py`, which requires Pillow, pyproj, and the specified Windows fonts, writing output to `output/atlas/`.
- Legacy API, database, and import tool documentation lives in each directory's own README.

`node_modules/`, `frontend/dist/`, `output/`, and local environment configuration are all Git-ignored.


Manual chapter navigation stays static until an animation is explicitly selected. Guided tours play available stories in chapter order and wait for the reader in text chapters. Mobile close-up and chapter overview controls preserve playback progress.

Entry details support explicit read marks, saved entries, and previous/next navigation within the opening list. A completion action at the end marks the entry read and continues. The bestiary filters by reading state; chapter entry panels provide a collection across chapters. Marks stay in this browser and are excluded from shared links; unavailable storage falls back to page memory.

Continue reading restores the latest entry and its section-relative position after artwork and fonts load. Reloading the same open entry also restores it, including an expanded Chinese original. Ordinary entry and shared links start at the beginning. Reading position is stored separately from read marks and saved entries in this browser.

Header search covers stories, creatures, sources, places and realms, including Chinese aliases. Source results open their associated entries. Search pauses background animation and resumes on close. The corrected nine-headed Xiangliu and three dedicated map marker samples use `src/refined-artwork.json`. Source PNGs and built-in image generation prompts are retained in `artwork-source/woodcut-refinement/`; run `python scripts/prepare-refined-artwork.py` to regenerate published assets.

Local handoff notes are excluded from Git. QA output, generated builds and browser caches are not release sources; original artwork stays versioned for reproducibility. Generation records use repository-relative paths.

### Geographic reference view

The header's **Geo** button opens a separate WGS84 reference atlas without replacing the narrative canvas. It uses local Natural Earth relief, land and river data, retaining a paper-and-ink palette. The 28 existing geographic hypotheses remain available, with three local-tradition associations added for Pangu and Jingwei. Sources document associations, not established historical event sites. Unlocated stories are never given invented coordinates.

The view follows the current story and displays one event at a time, with chapter-grouped event selection, event-scoped locality/type search, classified markers and linked source details, coordinates, a metric scale, great-circle two-point measurement, layer switches and filtered WGS84 GeoJSON export. Closing it preserves the original chapter, camera and playback; geographic query/view state survives reopening in this page session. No backend, API key or external tile requests are required.

Run `python scripts/prepare-geography.py` from `frontend/` to reproduce the regional relief from Natural Earth SR_50M 3.2.0 (Pillow required). The source ZIP is retained under ignored `output/geography-source/`; the generated image and `src/geography-basemap.json` are release sources. This is generalized modern terrain, not historical reconstruction or elevation-analysis data. Run `node scripts/with-preview.mjs --base /mythmap/ -- node scripts/verify-geography.mjs` after building; CI keeps Chromium, Firefox and WebKit checks.

Story animations use a shared 1.3x base rate in `src/playback.js`; the 1x/2x controls are relative to that base. `npm run verify:playback-speed` checks all three clocks. Local traditions and reviewed pilot evidence are maintained in `src/geography-associations.json`, preserving legacy candidate IDs and coordinates.

The geographic window can compare two accounts for the same event, including association type, account, review status, excerpts, sources and coordinate precision. Cards appear side by side on desktop and vertically on mobile. Comparison choices survive reopening, reset when changing events and remain independent of place search. No location rankings or invented narrative variants are supplied.

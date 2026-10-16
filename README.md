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

The exploration area starts in **Woodcut stories** mode and switches to **Real geography** within the same chapter navigation and fullscreen container. Geography uses continuous online OpenStreetMap tiles, with visible attribution and the map provider's boundary and place-name presentation. **China overview** includes the mainland, Taiwan, Hainan and southern maritime areas; **View event places** explicitly fits the current results. Switching events changes the association markers without automatically moving the camera.

The 28 existing geographic hypotheses and four Pangu/Jingwei local-tradition associations remain available. Sources document associations, not established historical event sites; unlocated stories are never given invented coordinates. Event-scoped search, classified markers, source details, account comparison, coordinates, metric scale, great-circle measurement and filtered WGS84 GeoJSON export are retained. The two map modes preserve independent cameras and geographic query/comparison state during this page session. Geography pauses story playback; returning preserves its progress. Chapter changes show a 1200 ms notice and pause the covered story. Unlocated events show a separate 2500 ms notice and a persistent explanation.

This remains a static GitHub Pages app with no backend or API key. The online basemap requires network access; failed tiles show an error with retry rather than substituting the old regional image. Browser caching is used without bulk download or prefetch, following the [OSM tile policy](https://operations.osmfoundation.org/policies/tiles/). Existing Natural Earth assets and `scripts/prepare-geography.py` are retained for reproducibility but are no longer the active basemap or an automatic fallback.

After building, run `node scripts/with-preview.mjs --base /mythmap/ -- node scripts/verify-geography.mjs` and `verify-map-frame.mjs` through the same wrapper. Geographic browser tests mock OSM tiles instead of requesting the public service; generated test screenshots are layout fixtures, not real geographic imagery. CI retains all three browser engines.

Story animations use a shared 1.3x base rate in `src/playback.js`; the 1x/2x controls are relative to that base. `npm run verify:playback-speed` checks all three clocks. Local traditions and reviewed pilot evidence are maintained in `src/geography-associations.json`, preserving legacy candidate IDs and coordinates.

On phones, place search and measurement/export tools start collapsed. Active search filters remain visible in the summary; closing tools exits measurement mode while retaining a labelled result. Selected places link the map, result list and evidence with explicit reading/back-to-map controls. Coincident records can be selected without shifting coordinates or the camera. Slow initial basemap loading is distinguished from missing evidence.

The geographic view can compare two accounts for the same event, including association type, account, review status, excerpts, sources and coordinate precision. Cards appear side by side on desktop and vertically on mobile. Comparison choices survive reopening, reset when changing events and remain independent of place search. No location rankings or invented narrative variants are supplied.

There are 32 geographic association records (28 legacy hypotheses and four local traditions). Reviewed pilot entries include traceable summaries and explicit limits, publisher, publication date where known, review date, passage locator and review scope. Indexed excerpts are distinguished from webpage text; shared quotations are not counted as independent narrative variants.

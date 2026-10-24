# MythMap — Where the Mountains and Seas Begin

One scroll of mountains and seas, seven chapters of myth. MythMap presents selected mountains, waters and creatures from the *Classic of Mountains and Seas* (Shan Hai Jing), alongside Chinese myths from other ancient texts, through woodblock-style maps, animations and illustrations.

**[Try it live →](https://hyc1005.github.io/mythmap/)**

**English** | [中文版](./README.zh-CN.md)

## What You Can Explore

- **Myth World Map**: Starting from the Pangu creation prologue, browse seven story chapters with their locations and divine realms.
- **Story Animations**: Play, pause, replay, and view full-screen.
- **Nanshan Jing reader**: 43 mountain and closing passages with bilingual explanations, edition text, commentary, scan links, search, saved entries and resume. See [content coverage](docs/content-coverage.md); the 18-chapter source-block inventory retains pending review states.
- **Xishan Jing reader**: 82 passages covering 77 named mountain stages, four range summaries and the closing total, with 508 independent cards. Edition totals and discrepancies remain visible; the other 16 books still require systematic completion.
- **Bestiary**: Browse 145 beast and bird records, searchable by name, appearance, or chapter; passage-specific namesakes remain distinct.
- **Source Citations**: Click any map location or beast card to read its description and the passages it cites.

Just open the page — it works on desktop and mobile. The map expresses chapter orientation and narrative relationships, not real distances or precise dates; the illustrations are artistic interpretations of the source texts.

This atlas does not contain the complete Shanhaijing. Previews, chapter entries, search results and details distinguish the Shanhaijing from other ancient texts; modern location evidence separately labels local traditions and geographic hypotheses. The [18-chapter inventory and first expansion batch](./docs/content-coverage.md) lists current entries, unexposed records and gaps. Its reference is the Wikisource transcription of the Sibu Congkan facsimile of the Ming Chenghua edition; this inventory does not claim a completed word-by-word collation.

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
node scripts/with-preview.mjs --base /mythmap/ -- node scripts/verify-onboarding.mjs
node scripts/with-preview.mjs --base /mythmap/ -- node scripts/verify-ux.mjs
node scripts/with-preview.mjs --base /mythmap/ -- node scripts/verify-discovery.mjs
node scripts/with-preview.mjs --base /mythmap/ -- node scripts/verify-narrative.mjs
```

For manual preview, run `npm run preview:managed -- --base /mythmap/` on 127.0.0.1:4183 and press Ctrl+C when finished. An occupied port is rejected without stopping the existing process. Do not rebuild the same `dist/` while verification is running.

`verify:design` covers bilingual layouts at six viewport sizes, mobile panel focus and scroll locking, body contrast, six illustration samples, playback preservation and PNG paper color. `verify:layout` checks five viewport sizes, animation, fullscreen and details; `verify:narrative` also checks the complete narrative, assets and timeline. Screenshots are retained in `output/qa/`. Local verification defaults and CI use Chromium and WebKit. Firefox is currently excluded from routine verification; the app is not guaranteed to run correctly in Firefox. Install the required engines with `npx playwright install chromium webkit`.

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

Story details include bilingual project-written overviews based on the cited excerpts. Returning from a search result restores the query, scope, loaded results, scroll position and focus. Browser back/forward supports search, details, chapters and map modes. Mobile chapter and entry navigation sits above the map and stays accessible while scrolling.

Search indexes overviews in the current language and Chinese, labels overview snippets and highlights matching terms. Stories with available animations offer Play this story and a return to the original reading position. Jingwei Fills the Sea, Jingwei and Mount Fajiu are explicitly linked through the cited text; related-entry round trips restore reading position and focus while preserving the background map. Each entry retains its own quotations and sources; no links are inferred from names.

Locating a story on the map carries that event into real geography. Geographic links use `mode=geography`, `event` and `reference` to restore the mode, event and selected record on reload or in another tab; invalid or unrelated records are ignored. These links exclude private reading marks; camera, geographic search and comparison choices remain page-session state.

Entry details support explicit read marks, saved entries, and previous/next navigation within the opening list. A completion action at the end marks the entry read and continues. The bestiary filters by reading state; chapter entry panels provide a collection across chapters. Marks stay in this browser and are excluded from shared links; unavailable storage falls back to page memory.

Continue reading restores the latest entry and its section-relative position after artwork and fonts load. Reloading the same open entry also restores it, including an expanded Chinese original. Ordinary entry and shared links start at the beginning. Reading position is stored separately from read marks and saved entries in this browser.

Header search covers stories, creatures, sources, places and realms, including Chinese aliases. Source results open their associated entries. Search pauses background animation and resumes on close. The corrected nine-headed Xiangliu and three dedicated map marker samples use `src/refined-artwork.json`. Source PNGs and built-in image generation prompts are retained in `artwork-source/woodcut-refinement/`; run `python scripts/prepare-refined-artwork.py` to regenerate published assets.

All 32 modern place associations are searchable under “Modern place references”. Results first open the story in woodcut mode; “Explore the real-world place” opens geographic evidence only when requested. Returning restores the query and focus. The header has a single Atlas link, with map modes selected inside the map. Neither place records nor original-text cards have a copy-link button. Place introductions tell a short story before explaining evidence boundaries, scope and limitations; research candidates are not presented as documented local variants. Endings stay with the story’s actions or images, without added morals or questions. Events without place records offer “Read this story” and “Browse events with place references”. Both languages support these actions, including Chinese place names in English search. `verify:place-search` checks these flows across eight bilingual layouts.

Clickable names on the woodcut map carry small red seals that declutter with their labels. Decorative landscapes and region headings have no seal. Hover and touch subtly strengthen the mark without moving the camera; there is no continuous animation. Previews start with a plain-language synopsis, keep portraits inside the card and provide an explicit close action and reading/playback targets of at least 44px. Fullscreen reserves a fixed preview area so dismissal preserves the canvas. Reading panels put the synopsis and original text before artwork and secondary controls; read/favorite marks and entry navigation appear at the end. Empty searches offer to widen the scope while keeping the keyword and show the number of matches in other types. `verify:exploration`, `verify:reading` and `verify:search` cover these bilingual interactions and layouts.

First-time homepage visitors without saved reading progress receive a four-step guide to reading, chapters, search and map modes. A 64% black spotlight leaves the real target usable. Opening content suspends the hints until that content closes. Visitors may advance without clicking targets, skip or press Escape; completion is saved locally. “How to explore” below the map reopens it, and the welcome card offers both languages. Direct chapter/story links and returning readers are not interrupted. Background playback pauses without losing progress, focus returns on exit, and cards avoid targets on narrow and landscape screens. `verify:onboarding` covers eight bilingual layouts, real controls, keyboard access, persistence/replay, modal continuation, direct links, reduced motion and unavailable storage.

Local handoff notes are excluded from Git. QA output, generated builds and browser caches are not release sources; original artwork stays versioned for reproducibility. Generation records use repository-relative paths.

### Geographic reference view

**Initial view** resets the regional center and scale without clearing the event, query or selected record. Nearby geographic records cluster within 36 screen pixels; count markers open a record selector without moving the camera. Grouping changes with zoom, and a grouped marker is a display anchor rather than a site coordinate. Location and GeoJSON retain original coordinates; measurement still uses the positions explicitly picked on the map, not an inferred event location. Place evidence and account comparisons show summaries first, with separate collapsible quoted passages, review sources and coordinate precision; review warnings stay visible.

The initial geographic view now centers on the Shaanxi–Henan area (110.5° E, 34.5° N) at zoom 5, showing an approximately 500 km scale line. Resizing or fullscreen preserves that regional scale. China overview remains a separate explicit action; it fits the entire national extent.

The exploration area starts in **Woodcut stories** mode and switches to **Real geography** within the same chapter navigation and fullscreen container. Geography uses official Tianditu HTTPS WMTS terrain (`ter_w`) and Chinese annotation (`cta_w`) layers, preserving their boundaries, labels and visible attribution. **China overview** keeps its center near Xi’an (108.94° E, 34.34° N) while fitting [73, 3, 136, 54] with 24 px padding. **View event places** explicitly fits the current results. Switching events changes the association markers without automatically moving the camera. User-positioned views survive mode and language changes; the nationwide view recalculates its scale on resize and fullscreen changes without moving its center.

The 28 existing geographic hypotheses and four Pangu/Jingwei local-tradition associations remain available. Sources document associations, not established historical event sites; unlocated stories are never given invented coordinates. Event-scoped search, classified markers, source details, account comparison, coordinates, metric scale, great-circle measurement and filtered WGS84 GeoJSON export are retained. The two map modes preserve independent cameras and geographic query/comparison state during this page session. Geography pauses story playback; returning preserves its progress. Chapter changes show a 1200 ms notice and pause the covered story. Unlocated events show a separate 2500 ms notice and a persistent explanation.

This remains a static GitHub Pages app without a backend. Set `VITE_TIANDITU_KEY` in ignored `frontend/.env.local` to a **browser application** key; server application keys cannot be used here. Allow `hyc1005.github.io,127.0.0.1` in the provider's domain whitelist and use `127.0.0.1` for local preview. Do not include a protocol, port or URL path in that field. For future deployment, configure the repository Actions secret **TIANDITU_BROWSER_KEY**; the workflow passes it into the production build and rejects publication without it. Pull requests use mock-only credentials and do not deploy. Browser keys appear in client requests, so access restrictions belong in the provider console. No key value belongs in source or handoff notes.

The online basemap requires network access. Missing credentials, authentication rejection, terrain failure and annotation failure have distinct messages; local evidence search remains available. Retry recreates both sources and cancels obsolete requests. There is no OSM or regional-image fallback. Both layers use levels 1–14 (terrain's maximum); annotation tiles retain their original rendering. Browser caching is used without nationwide download or prefetch. Original OSM coordinate-source links remain evidence links, not claims that Tianditu supplied those coordinates. Existing Natural Earth assets and `scripts/prepare-geography.py` are retained for reproducibility.

After building, run `node scripts/with-preview.mjs --base /mythmap/ -- node scripts/verify-geography.mjs` and `verify-map-frame.mjs` through the same wrapper. Geographic browser tests mock both Tianditu layers and reject OSM basemap requests; generated test screenshots are layout fixtures, not real geographic imagery. CI checks Chromium and WebKit and separately tests a root build without credentials.

Continue reading and guided-tour actions share one controlled component below the woodcut map, including fullscreen. Geography places continue reading below the coordinate readout and omits the tour action. Text chapters advance through the same action area. The chapter rail contains only its heading, introduction and directory; short landscape layouts abbreviate the resume label while retaining the entry name in its accessible name.

Story animations use a shared 1.3x base rate in `src/playback.js`; the 1x/2x controls are relative to that base. `npm run verify:playback-speed` checks all three clocks. Local traditions and reviewed pilot evidence are maintained in `src/geography-associations.json`, preserving legacy candidate IDs and coordinates.

On phones, place search and measurement/export tools start collapsed. Active search filters remain visible in the summary; closing tools exits measurement mode while retaining a labelled result. Selected places link the map, result list and evidence with explicit reading/back-to-map controls. Coincident records can be selected without shifting coordinates or the camera. Slow initial basemap loading is distinguished from missing evidence.

The geographic view can compare two accounts for the same event, including association type, account, review status, excerpts, sources and coordinate precision. Cards appear side by side on desktop and vertically on mobile. Comparison choices survive reopening, reset when changing events and remain independent of place search. No location rankings or invented narrative variants are supplied.

There are 32 geographic association records (28 legacy hypotheses and four local traditions). Reviewed pilot entries include traceable summaries and explicit limits, publisher, publication date where known, review date, passage locator and review scope. Indexed excerpts are distinguished from webpage text; shared quotations are not counted as independent narrative variants.

# MythMap — Where the Mountains and Seas Begin

A bilingual, woodcut-style atlas of the *Classic of Mountains and Seas* and Chinese myths from other ancient texts. Explore seven story chapters, source-linked reading, illustrations and a separate geographic evidence view.

**[Open the atlas](https://hyc1005.github.io/mythmap/)** · **English** | [中文版](README.zh-CN.md)

## Current scope

- All five mountain books have reading entries: Southern 43, Western 82, Northern 92, Eastern 51 and Central 212 — **480 passages** in total. The remaining thirteen books are outside this completed reading scope; see the generated [content inventory](docs/content-coverage.md).
- The bestiary indexes **312 creature accounts and 72 deity accounts** with short names, independent namesake records, six body-form groups and combined book, feature and reading filters. It loads 24 name groups per batch; 47 accounts retain an unresolved morphology label.
- Story playback, guided tours, search, saved/read marks and reading-position recovery work in Chinese and English. Geographic evidence keeps documented associations separate from narrative diagram positions.

Original names, quotations, IDs and source links are retained. English explanations and translations are project writing; illustrations are artistic interpretations. Neither a diagram position nor a geographic association proves an ancient event location.

## Repository map

| Path | Responsibility |
| --- | --- |
| [frontend/](frontend/) | React/Vite website; the only directory deployed to Pages |
| [frontend/src/](frontend/src/) | UI, state, localization and bestiary presentation metadata |
| [frontend/public/data/](frontend/public/data/) | Reviewed runtime data, scans and published illustration variants |
| [frontend/artwork-source/](frontend/artwork-source/) | Original artwork, prompts and reproducibility records |
| [frontend/scripts/](frontend/scripts/README.md) | Browser checks and preview tools; `assets/` and `fonts/` contain generators |
| [data/](data/README.md) | Current book builders, review records and source inventories; `archive/` holds retired preparation and basemap records |
| [docs/](docs/README.md) | Documentation index, API contract, generated coverage and historical coursework |
| [backend-java/](backend-java/run.ps1) | Optional local `/api/world` service used by the development proxy |
| [backend/](backend/README.md), [database/](database/README.md) | Optional FastAPI/PostGIS prototype and its tests/import tools |
| `.github/workflows/` | Verification and Pages deployment |
| `output/` | Ignored local QA, diagnostics and intermediate files |

The static site needs no backend or database. The optional services remain separate from the published frontend.

## Local development

Requires Node.js 22 or a newer compatible version.

```bash
cd frontend
npm ci
npm run dev -- --host 127.0.0.1
```

Open [127.0.0.1:5173](http://127.0.0.1:5173/). Development tries the optional Java API on port 8081, then falls back to bundled data. To use that API, run `backend-java/run.ps1` with JDK 17 or newer. Production uses bundled data unless `VITE_API_BASE_URL` is configured; that setting is public in the build output.

The geographic basemap uses a Tianditu **browser application** key in ignored `frontend/.env.local` as `VITE_TIANDITU_KEY`. Configure the provider's domain allowlist for `hyc1005.github.io,127.0.0.1`. Reading and local evidence remain available when the basemap is unavailable.

## Build and verify

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

## Deploy

Select **GitHub Actions** in repository Settings → Pages, and set the Actions secret **TIANDITU_BROWSER_KEY**. Pushes to `main` that affect the frontend, data, backend/database or workflows run [.github/workflows/deploy-pages.yml](.github/workflows/deploy-pages.yml). Documentation-only pushes do not deploy; manual dispatch is also available.

Deployment waits for all required checks and publishes the same verified artifact. Do not commit `dist/`, dependencies, environment files or QA output. Roll back by reverting the relevant commit and pushing.

## Maintain data and assets

Use [data/README.md](data/README.md) for book builders and review sources, [frontend/scripts/README.md](frontend/scripts/README.md) for image/font generators, and [docs/API_CONTRACT.md](docs/API_CONTRACT.md) for data contracts. Bestiary short names and classifications live in `frontend/src/bestiary-metadata.json`, separate from generated source data.

Course reports are retained under [docs/coursework/](docs/coursework/). Original artwork and facsimiles remain versioned for evidence and reproducibility; duplicate originals are excluded from the published build by the asset manifest. Local handoff notes and intermediate files are Git-ignored.

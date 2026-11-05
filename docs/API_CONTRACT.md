# API and data contract

> Updated 2026-11-05. GitHub Pages uses bundled data. The optional Java service supplies `/api/world` during development. See the [documentation index](README.md) for current maintenance entry points.

## Current frontend world data

`frontend/public/data/myth-world.json` contains `revision`, `coordinate_system`, `coordinate_note`, and ten required arrays: `stages`, `regions`, `terrain`, `places`, `relations`, `domains`, `beasts`, `natural_features`, `passages`, and `text_entities`. The current reader includes 480 passages across the five mountain books. Counts and source coverage are maintained in the generated [content inventory](content-coverage.md), rather than fixed to the early prototype dataset.

- `coordinate_system` is `diagram-units`. The OpenLayers `mythic-plane` uses a `[0, 0, 1200, 800]` layout extent. These x/y values are diagram positions, not WGS84 coordinates or measured distances.
- `atlas/catalog.json` separately holds source records, people, events and geographic candidates. Its `revision_id` is distinct from the world's `revision`; do not substitute one for the other. The current `events` array has 43 entries, including spatial records, and is not an animation count.
- `atlas/story-animations.json` and `atlas/kuafu-journey.json` describe animation assets and timing. Asset URLs may reference SVG, PNG or WebP. Preserve null geographic geometry and the distinction between source evidence and illustrative layout hints.
- Default production builds make no world API request. Development requests `/api/world`; production requests it only when `VITE_API_BASE_URL` is configured. The Vite development proxy targets the optional Java service at `127.0.0.1:8081`.
- The frontend accepts an API world only when its `revision` matches the bundled world, all ten arrays are present, and stage count and ordered stage IDs match. Required-field, coordinate, chapter and reference validation runs before replacing bundled data; failures leave bundled data in use. This does not verify the historical truth of a source.

## Optional Java endpoints

The Java service reads the configured world JSON file without translating it or modifying geographic records. `PORT` defaults to 8081; it binds to localhost. `MYTH_WORLD_PATH`, or the first command-line argument, selects the data file.

- `GET /api/world`: the world object above, without an `items` wrapper. Unknown subpaths return 404, unsupported methods return 405, and an unavailable data file returns 500. `OPTIONS` returns 204.
- `/health`: returns `{status:"ok",service:"myth-world-java"}`. This is a liveness response; it does not verify that the world data file exists.

Responses set `Cache-Control: no-cache` and CORS headers. `VITE_API_BASE_URL` is a public build-time setting, not a place for credentials.

## Bestiary presentation metadata

`frontend/src/bestiary-metadata.json` adds bilingual short names, independent namesake groups, body forms, features and quoted classification evidence. It does not rewrite source names, quotations, IDs or the API `kind`. The gallery combines 317 original beast records and 67 text deities, then presents 312 creature accounts and 72 deity accounts; 45 morphology classifications remain unresolved. Original names and aliases remain searchable.

## Language and assets

Localization is performed in the frontend, using `locale-en.json` and `locale-content-en.json`. It preserves IDs and original Chinese names and quotations; no language parameter is sent to the Java API. `?lang=en` or `?lang=zh` overrides the saved `shanhai-language` preference. English quotations are project translations, not a separately cited English edition.

The Lora and Source Sans 3 font files and their licenses are shipped locally. Large runtime images use lossy WebP (quality 83); card and preview images use separate 320/480px WebP variants; original PNGs remain in `frontend/artwork-source/optimized-originals/`. Update runtime references and `atlas/artwork-manifest.json` together when changing formats. The navigation SVG and reading-notes bookplate are decorative branding.

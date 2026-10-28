# API and data contract

> Updated 2026-10-28. GitHub Pages uses bundled data. The optional Java service remains the development `/api/world` provider; FastAPI/PostGIS is a separate prototype. See the [documentation index](README.md) for current maintenance entry points.

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

`frontend/src/bestiary-metadata.json` adds bilingual short names, independent namesake groups, body forms, features and quoted classification evidence. It does not rewrite source names, quotations, IDs or the API `kind`. The gallery combines 317 original beast records and 67 text deities, then presents 312 creature accounts and 72 deity accounts; 47 morphology classifications remain unresolved. Original names and aliases remain searchable.

## Language and assets

Localization is performed in the frontend, using `locale-en.json` and `locale-content-en.json`. It preserves IDs and original Chinese names and quotations; no language parameter is sent to the Java API. `?lang=en` or `?lang=zh` overrides the saved `shanhai-language` preference. English quotations are project translations, not a separately cited English edition.

The Lora and Source Sans 3 font files and their licenses are shipped locally. Large runtime images use lossy WebP (quality 83); card and preview images use separate 320/480px WebP variants; original PNGs remain in `frontend/artwork-source/optimized-originals/`. Update runtime references and `atlas/artwork-manifest.json` together when changing formats. The navigation SVG and reading-notes bookplate are decorative branding.

## Optional FastAPI atlas routes and limitations

`backend/app/atlas.py` also defines read-only `/api/atlas`, `/api/atlas/stages`, `/api/atlas/stages/{stage_id}/layers/{layer}`, `/api/atlas/entities/{entity_id}`, and `/api/atlas/divine-space`. Layers support `events`, `candidates`, `routes`, and `activities`; catalog, layer and entity calls accept an optional `revision_id` and return 409 for a mismatch. These routes are not used by the current frontend.

The routes read bundled files from `frontend/public/data`. The stages endpoint calculates total from the returned items, including the prologue. These endpoints are not substitutes for Java `/api/world`.

## Legacy FastAPI/PostGIS contract

### Shared vocabulary

- Themes: `山川地理`, `神祇`, `异兽`, `方国`, `神话事件`.
- Confidence: `clear` (one defensible modern correspondence), `disputed` (multiple candidate interpretations), `unlocated` (no defensible geometry).
- Geometry display: `point`, `area`, `illustrative`, or `none`. Illustrative points are never eligible for clustering.
- All API geometries use GeoJSON longitude/latitude in EPSG:4326.

### Entity fields

- Story: `id`, `title`, `theme`, `summary`, `chapter`, `quote`, `source_ids[]`, `person_ids[]`, `place_ids[]`.
- Person: `id`, `name`, `description`, `source_ids[]`.
- Place: `id`, `name`, `modern_name` (nullable), `description`, `confidence`, `candidate_ids[]`, `story_ids[]`, `source_ids[]`.
- Candidate: `id`, `place_id`, `label`, `geometry` (nullable GeoJSON), `display_mode`, `confidence`, `is_primary`, `reason`, `source_ids[]`.
- Story-place relation: `story_id`, `place_id`, `relation_type`, `quote`, `sequence`.
- Source: `id`, `title`, `creator`, `url` (nullable), `citation`, `accessed_on` (nullable).

### Endpoints

- `GET /api/stories?q=&theme=&person_id=&place_id=&confidence=` returns `{items: Story[], total: number}`. List stories include `people[]` summaries (`id`, `name`, `description`, `source_ids`) for the filter control; detail stories expand people and places.
- `GET /api/stories/{id}` returns one Story with expanded people, places, and sources; unknown IDs return 404.
- `GET /api/places?q=&theme=&story_id=&person_id=&confidence=&include_unlocated=` returns `{items: Place[], total: number}`. `include_unlocated` defaults to true.
- `GET /api/places/{id}` returns one Place with candidate interpretations, related stories, and sources; unknown IDs return 404.
- `GET /api/map/features?q=&bbox=&theme=&story_id=&person_id=&place_id=&confidence=` returns a GeoJSON FeatureCollection. Each feature represents a place candidate and includes `place_id`, `candidate_id`, `place_name`, `confidence`, `display_mode`, `is_primary`, `story_ids`; geometry may be Point or Polygon, never a fabricated coordinate.
- `GET /api/analysis/clusters?q=&theme=&story_id=&person_id=&place_id=&confidence=` returns `{parameters:{eps_m:250000,min_points:3,projection:"local azimuthal equidistant centered at 105E,35N"},eligible_count,clustered_count,noise_count,clusters:[{id,count,geometry,place_ids}],excluded:{unlocated,area,illustrative,disputed,multiple_candidates}}`. Only unique primary clear Point candidates are eligible. Empty clusters are valid.
- `GET /api/stats` returns totals by theme and confidence plus counts of stories, places, people, mapped candidates, and unlocated places.

For map and cluster endpoints, `q` matches place/modern names, candidate labels/reasons, and linked story title/summary/chapter/quote. `person_id`, `story_id`, and `place_id` scope to the same linked records. Places use the same relation rules, with `q` matching place/modern names and linked story text. Empty or omitted filters mean no restriction. Invalid filter values return 422. List ordering is deterministic by title/name then ID. Frontend map, place-list and analysis filters must be sent to the server so their result sets use the same scope.

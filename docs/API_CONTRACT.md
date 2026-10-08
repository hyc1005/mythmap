# API and data contract

> This contract describes the legacy FastAPI/PostGIS prototype in `backend/`. The current GitHub Pages site uses bundled frontend data and does not call these endpoints. See the root README for the current setup.

## Shared vocabulary

- Themes: `山川地理`, `神祇`, `异兽`, `方国`, `神话事件`.
- Confidence: `clear` (one defensible modern correspondence), `disputed` (multiple candidate interpretations), `unlocated` (no defensible geometry).
- Geometry display: `point`, `area`, `illustrative`, or `none`. Illustrative points are never eligible for clustering.
- All API geometries use GeoJSON longitude/latitude in EPSG:4326.

## Entity fields

- Story: `id`, `title`, `theme`, `summary`, `chapter`, `quote`, `source_ids[]`, `person_ids[]`, `place_ids[]`.
- Person: `id`, `name`, `description`, `source_ids[]`.
- Place: `id`, `name`, `modern_name` (nullable), `description`, `confidence`, `candidate_ids[]`, `story_ids[]`, `source_ids[]`.
- Candidate: `id`, `place_id`, `label`, `geometry` (nullable GeoJSON), `display_mode`, `confidence`, `is_primary`, `reason`, `source_ids[]`.
- Story-place relation: `story_id`, `place_id`, `relation_type`, `quote`, `sequence`.
- Source: `id`, `title`, `creator`, `url` (nullable), `citation`, `accessed_on` (nullable).

## Endpoints

- `GET /api/stories?q=&theme=&person_id=&place_id=&confidence=` returns `{items: Story[], total: number}`. List stories include `people[]` summaries (`id`, `name`, `description`, `source_ids`) for the filter control; detail stories expand people and places.
- `GET /api/stories/{id}` returns one Story with expanded people, places, and sources; unknown IDs return 404.
- `GET /api/places?q=&theme=&story_id=&person_id=&confidence=&include_unlocated=` returns `{items: Place[], total: number}`. `include_unlocated` defaults to true.
- `GET /api/places/{id}` returns one Place with candidate interpretations, related stories, and sources; unknown IDs return 404.
- `GET /api/map/features?q=&bbox=&theme=&story_id=&person_id=&place_id=&confidence=` returns a GeoJSON FeatureCollection. Each feature represents a place candidate and includes `place_id`, `candidate_id`, `place_name`, `confidence`, `display_mode`, `is_primary`, `story_ids`; geometry may be Point or Polygon, never a fabricated coordinate.
- `GET /api/analysis/clusters?q=&theme=&story_id=&person_id=&place_id=&confidence=` returns `{parameters:{eps_m:250000,min_points:3,projection:"local azimuthal equidistant centered at 105E,35N"},eligible_count,clustered_count,noise_count,clusters:[{id,count,geometry,place_ids}],excluded:{unlocated,area,illustrative,disputed,multiple_candidates}}`. Only unique primary clear Point candidates are eligible. Empty clusters are valid.
- `GET /api/stats` returns totals by theme and confidence plus counts of stories, places, people, mapped candidates, and unlocated places.

For map and cluster endpoints, `q` matches place/modern names, candidate labels/reasons, and linked story title/summary/chapter/quote. `person_id`, `story_id`, and `place_id` scope to the same linked records. Places use the same relation rules, with `q` matching place/modern names and linked story text. Empty or omitted filters mean no restriction. Invalid filter values return 422. List ordering is deterministic by title/name then ID. Frontend map, place-list and analysis filters must be sent to the server so their result sets use the same scope.

# Data contract (static build)

> Updated 2026-11-10. The site is a static bundle. There is no runtime world API and no optional backend service; all world data ships in `frontend/public/data/`.

## Frontend world data

`frontend/public/data/myth-world.json` contains `revision`, `coordinate_system`, `coordinate_note`, and ten required arrays: `stages`, `regions`, `terrain`, `places`, `relations`, `domains`, `beasts`, `natural_features`, `passages`, and `text_entities`. The current reader includes 480 passages across the five mountain books. Counts and source coverage are maintained in the generated [content inventory](content-coverage.md), rather than fixed to an early prototype dataset.

- `coordinate_system` is `diagram-units`. The OpenLayers `mythic-plane` uses a `[0, 0, 1200, 800]` layout extent. These x/y values are diagram positions, not WGS84 coordinates or measured distances.
- `atlas/catalog.json` separately holds source records, people, events and geographic candidates. Its `revision_id` is distinct from the world's `revision`; do not substitute one for the other. The current `events` array has 43 entries, including spatial records, and is not an animation count.
- `atlas/story-animations.json` and `atlas/kuafu-journey.json` describe animation assets and timing. Asset URLs may reference SVG, PNG or WebP. Preserve null geographic geometry and the distinction between source evidence and illustrative layout hints.
- The frontend validates the bundled world at build/test time with `world-validation.js`: required arrays, stage order, coordinate and reference checks. A failure is a data error, not a reason to fetch a replacement at runtime.

## Bestiary presentation metadata

`frontend/src/bestiary-metadata.json` adds bilingual short names, independent namesake groups, body forms, features and quoted classification evidence. It does not rewrite source names, quotations, IDs or `kind`. The gallery combines 317 original beast records and 67 text deities, then presents 312 creature accounts and 72 deity accounts; 45 morphology classifications remain unresolved. Original names and aliases remain searchable.

## Language and assets

Localization is performed in the frontend, using `locale-en.json` and `locale-content-en.json`. It preserves IDs and original Chinese names and quotations. `?lang=en` or `?lang=zh` overrides the saved `shanhai-language` preference. English quotations are project translations, not a separately cited English edition.

The Lora and Source Sans 3 font files and their licenses are shipped locally. Large runtime images use lossy WebP (quality 83); card and preview images use separate 320/480px WebP variants; original PNGs remain in `frontend/artwork-source/optimized-originals/`. Update runtime references and `atlas/artwork-manifest.json` together when changing formats. The navigation SVG and reading-notes bookplate are decorative branding.

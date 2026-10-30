# Optional PostGIS prototype database

This database belongs to the optional backend prototype. The published static site uses bundled frontend data and does not require PostgreSQL or PostGIS.

PostgreSQL with PostGIS is required. Create the database first, then from the repository root run:

```powershell
$env:DATABASE_URL = "postgresql://user:password@localhost:5432/shanhai"
psql $env:DATABASE_URL -v ON_ERROR_STOP=1 -f database/001_init.sql
python database/load_seed.py
```

`001_init.sql` enables PostGIS and creates the entity, relation, source-link, and spatial-index tables. The loader replaces the curated demo records in one transaction, so reruns are deterministic. It requires `psycopg[binary]` v3 and accepts either a libpq `postgresql://` URL or the backend's `postgresql+psycopg://` URL. To check the JSON and cross references without a database, run `python data/validate_seed.py`.

The schema stores geometries in EPSG:4326. Source records are linked through `story_sources`, `person_sources`, `place_sources`, and `candidate_sources`; cite the candidate source separately from the classical text source when explaining a modern location interpretation.

`load_myth_atlas.py` applies the atlas schema and `003_atlas_prologue.sql` migration, then replaces only the selected revision in one transaction. Removed features are removed from that revision; other revisions and legacy seed tables remain intact. Run import tests with `TEST_POSTGIS_URL` pointing to a disposable database named `atlas_review_*`.

## Prototype seed and source notes

This file documents the retained FastAPI/PostGIS prototype and its seed data. The current diagram-based web demo uses frontend/public/data/myth-world.json and atlas/catalog.json; its startup and deployment steps are in the root README. The former modern-coordinate ornament is retained for the prototype and is not the current page background.

`seed.json` is the deterministic demonstration dataset. It contains 24 story records, 38 distinct place records, and 16 people across all five API themes. Place confidence counts are 2 `clear`, 2 `disputed`, and 34 `unlocated`. Twenty-one records focus on the *Classic of Mountains and Seas*; three additional, clearly attributed records add the Pangu creation story and two Nüwa stories to support the narrative sequence. They come from later textual witnesses, not from the *Classic of Mountains and Seas* itself. The website orders these myths as a relative reading sequence, without assigning historical dates.

Location candidates are separate from places. They carry their own source links, reason, confidence, and display mode. Records whose source gives no defensible modern geometry link both the relevant chapter and `project-method`, which documents why no coordinate was created. The dataset includes:

- Two clear modern mountain correspondences (太华之山／华山 and 东山经泰山／现代泰山) with point coordinates from identified OpenStreetMap natural=peak nodes. The point marks each present-day summit and does not claim to define an ancient mountain boundary. The named ancient/modern correspondence and coordinate source are linked separately.
- Multiple coordinate-free Kunlun interpretations, each presented as a disputed scholarly proposal and linked to its supporting reference.
- Unlocated entries retained for search and story navigation without geometry.

There are five candidate records: 2 primary clear peak points and 3 coordinate-free interpretations (`display_mode=none`). The two eligible points do not meet the API's `min_points=3` clustering threshold, so an empty DBSCAN cluster list is the expected and reproducible result for the seed dataset.

Text source: [Chinese Text Project, 山海经](https://ctext.org/shan-hai-jing), which identifies its digital base text as following the 《四部丛刊初编》 edition where noted. The Huashan point uses [OpenStreetMap node 2260053296](https://www.openstreetmap.org/node/2260053296); the Taishan point uses [OpenStreetMap node 2338427466](https://www.openstreetmap.org/node/2338427466). The coordinates are WGS84 map features identified as modern mountain peaks. The Huashan correspondence is separately supported by [渭南市纪委华山简介](https://weinan.qinfeng.gov.cn/info/1095/36343.htm), and the Taishan correspondence by [泰安市人民政府泰山玉资料](https://www.taian.gov.cn/art/2013/10/21/art_55408_4070192.html). Kunlun interpretations are linked to the referenced historical-geography publications in the seed source catalog. Each absent/uncertain geometry also links `project-method`, the project's own documented admission rule; this identifies a data-method decision, not an external scholarly finding. These records demonstrate source separation; they are not a comprehensive critical edition.

The offline map backdrop is a locally drawn parchment-and-landscape ornament at `frontend/public/data/shanhai-ornament.svg`. Its mountains, contour flourishes, frame, and decorative labels have no geographic coordinates and do not represent ancient borders, routes, or proven locations. The graticule and any plotted candidate geometries remain in modern WGS84 coordinates; a marker appears only when the evidence record supplies defensible geometry. The map caption states this distinction in the interface.

Run `python data/validate_seed.py` to check counts, chapter/source links, referential integrity, geometry ranges, and candidate evidence requirements.

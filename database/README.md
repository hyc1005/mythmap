# Database setup

PostgreSQL with PostGIS is required. Create the database first, then from the repository root run:

```powershell
$env:DATABASE_URL = "postgresql://user:password@localhost:5432/shanhai"
psql $env:DATABASE_URL -v ON_ERROR_STOP=1 -f database/001_init.sql
python database/load_seed.py
```

`001_init.sql` enables PostGIS and creates the entity, relation, source-link, and spatial-index tables. The loader replaces the curated demo records in one transaction, so reruns are deterministic. It requires `psycopg[binary]` v3 and accepts either a libpq `postgresql://` URL or the backend's `postgresql+psycopg://` URL. To check the JSON and cross references without a database, run `python data/validate_seed.py`.

The schema stores geometries in EPSG:4326. Source records are linked through `story_sources`, `person_sources`, `place_sources`, and `candidate_sources`; cite the candidate source separately from the classical text source when explaining a modern location interpretation.

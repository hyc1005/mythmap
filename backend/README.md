# Backend service

FastAPI serves the story/place APIs and PostGIS map/cluster queries. The database schema and seed data are owned by `database/` and `data/`.

## Local setup

From the repository root, create a virtual environment, install `backend/requirements.txt`, and set `DATABASE_URL` to a PostgreSQL connection using psycopg 3, for example:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r backend/requirements.txt
$env:DATABASE_URL = "postgresql+psycopg://YOUR_USER:YOUR_PASSWORD@localhost:5432/shan_hai"
psql "$env:DATABASE_URL" -v ON_ERROR_STOP=1 -f database/001_init.sql
python database/load_seed.py
uvicorn app.main:app --app-dir backend --reload
```

The API is available at `http://127.0.0.1:8000`; interactive OpenAPI docs are at `/docs`. `CORS_ORIGINS` is a comma-separated allowlist and defaults to the Vite development origins. Settings can also be placed in `backend/.env`.

Create a local environment file from the example when environment variables are preferred:

```dotenv
DATABASE_URL=postgresql+psycopg://YOUR_USER:YOUR_PASSWORD@localhost:5432/shan_hai
CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
```

## API behavior

- List endpoints return all matching seed rows in deterministic name/title then ID order; the initial dataset is deliberately small enough that pagination is unnecessary.
- `theme` and `confidence` are validated against the shared vocabulary and invalid values return 422. Blank filters act as omitted filters.
- Place, map, and cluster filters use linked story relationships. Place text searches include names and linked story text; map and cluster searches also include candidate labels/reasons. The selected `person_id`, `story_id`, and `place_id` restrictions are applied consistently to matching linked stories.
- Map geometry is returned as GeoJSON in EPSG:4326. Null geometries and `none` display candidates are omitted; the API never makes coordinates for unlocated records.
- DBSCAN uses a local azimuthal equidistant projection centered at 105E,35N with `eps_m=250000` and `min_points=3`. The exclusion tally assigns one primary reason per excluded place in this order: unlocated, multiple candidates, disputed, area, illustrative, then other invalid/non-primary candidates as unlocated. Eligible points are unique primary clear Point candidates only.

## Checks

Install `backend/requirements-dev.txt`, then from the repository root run:

```powershell
python -m pytest backend/tests
python -m compileall -q backend/app
```

The focused tests cover filter construction and bbox validation. Full endpoint and spatial-query checks require a running PostgreSQL database with PostGIS initialized using `database/001_init.sql`.

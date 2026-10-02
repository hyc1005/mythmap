"""Idempotently replace seed records. Apply 001_init.sql before running."""
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "data"))
from validate_seed import main as validate_seed  # noqa: E402


def main():
    if not os.getenv("DATABASE_URL"):
        raise SystemExit("DATABASE_URL is required")
    validate_seed()
    import psycopg
    data = json.loads((ROOT / "data" / "seed.json").read_text(encoding="utf-8"))
    database_url = os.environ["DATABASE_URL"].replace("postgresql+psycopg://", "postgresql://", 1)
    with psycopg.connect(database_url) as conn:
        with conn.cursor() as cur:
            cur.execute("TRUNCATE story_people, story_places, story_sources, person_sources, place_sources, candidate_sources, place_candidates, stories, people, places, sources CASCADE")
            for row in data["sources"]:
                cur.execute("INSERT INTO sources VALUES (%s,%s,%s,%s,%s,%s)", tuple(row[k] for k in ("id","title","creator","url","citation","accessed_on")))
            for row in data["stories"]:
                cur.execute("INSERT INTO stories VALUES (%s,%s,%s,%s,%s,%s)", tuple(row[k] for k in ("id","title","theme","summary","chapter","quote")))
            for row in data["people"]:
                cur.execute("INSERT INTO people VALUES (%s,%s,%s)", tuple(row[k] for k in ("id","name","description")))
            for row in data["places"]:
                cur.execute("INSERT INTO places VALUES (%s,%s,%s,%s,%s)", tuple(row[k] for k in ("id","name","modern_name","description","confidence")))
            for row in data["candidates"]:
                geometry = row["geometry"]
                if geometry is None:
                    cur.execute("""INSERT INTO place_candidates(id,place_id,label,geometry,display_mode,confidence,is_primary,reason)
                        VALUES (%s,%s,%s,NULL,%s,%s,%s,%s)""",
                        (row["id"],row["place_id"],row["label"],row["display_mode"],row["confidence"],row["is_primary"],row["reason"]))
                else:
                    cur.execute("""INSERT INTO place_candidates(id,place_id,label,geometry,display_mode,confidence,is_primary,reason)
                        VALUES (%s,%s,%s,ST_SetSRID(ST_GeomFromGeoJSON(%s),4326),%s,%s,%s,%s)""",
                        (row["id"],row["place_id"],row["label"],json.dumps(geometry),row["display_mode"],row["confidence"],row["is_primary"],row["reason"]))
            for story in data["stories"]:
                for seq, place_id in enumerate(story["place_ids"], 1):
                    cur.execute("INSERT INTO story_places VALUES (%s,%s,%s,%s,%s)", (story["id"],place_id,"mentioned",story["quote"],seq))
                for source_id in story["source_ids"]:
                    cur.execute("INSERT INTO story_sources VALUES (%s,%s)", (story["id"],source_id))
            for person in data["people"]:
                for source_id in person["source_ids"]:
                    cur.execute("INSERT INTO person_sources VALUES (%s,%s)", (person["id"],source_id))
            for place in data["places"]:
                for source_id in place["source_ids"]:
                    cur.execute("INSERT INTO place_sources VALUES (%s,%s)", (place["id"],source_id))
            for candidate in data["candidates"]:
                for source_id in candidate["source_ids"]:
                    cur.execute("INSERT INTO candidate_sources VALUES (%s,%s)", (candidate["id"],source_id))
            for story_id, person_id in data["story_people"]:
                cur.execute("INSERT INTO story_people VALUES (%s,%s)", (story_id,person_id))
        conn.commit()
    print("Seed data loaded successfully.")


if __name__ == "__main__":
    main()

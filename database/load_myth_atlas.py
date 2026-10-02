"""Load an atlas revision without changing any legacy seed tables."""
import json
import os
from pathlib import Path

import psycopg

ROOT = Path(__file__).resolve().parents[1]


def main():
    url = os.getenv('DATABASE_URL')
    if not url:
        raise SystemExit('DATABASE_URL is required; existing tables are never replaced.')
    data = json.loads((ROOT / 'frontend/public/data/atlas/catalog.json').read_text(encoding='utf-8'))
    divine = json.loads((ROOT / 'frontend/public/data/divine-space.json').read_text(encoding='utf-8'))
    with psycopg.connect(url.replace('postgresql+psycopg://', 'postgresql://', 1)) as conn:
        with conn.cursor() as cur:
            cur.execute((ROOT / 'database/002_myth_atlas.sql').read_text(encoding='utf-8'))
            cur.execute('INSERT INTO myth_atlas_catalog VALUES (%s,%s::jsonb,%s::jsonb) ON CONFLICT (revision_id) DO UPDATE SET catalog=EXCLUDED.catalog,divine_space=EXCLUDED.divine_space',
                        (data['revision_id'], json.dumps(data, ensure_ascii=False), json.dumps(divine, ensure_ascii=False)))
            for feature in data['events'] + data['candidates'] + data['routes']:
                p = feature['properties']
                cur.execute('''INSERT INTO myth_atlas_features VALUES (%s,%s,%s,%s,%s,
                               CASE WHEN %s::text IS NULL THEN NULL ELSE ST_SetSRID(ST_GeomFromGeoJSON(%s::text),4326) END,%s::jsonb)
                               ON CONFLICT (revision_id,id) DO UPDATE SET stage_id=EXCLUDED.stage_id,
                               entity_id=EXCLUDED.entity_id,layer_role=EXCLUDED.layer_role,geometry=EXCLUDED.geometry,properties=EXCLUDED.properties''',
                            (data['revision_id'], feature['id'], p['stage_id'], p['entity_id'], p['layer_role'],
                             json.dumps(feature['geometry']) if feature['geometry'] else None,
                             json.dumps(feature['geometry']) if feature['geometry'] else None, json.dumps(p, ensure_ascii=False)))
    print('Atlas revision loaded; legacy tables unchanged.')


if __name__ == '__main__':
    main()

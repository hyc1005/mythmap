import copy
import json
import os
from urllib.parse import urlparse

import psycopg
import pytest

from database.load_myth_atlas import ROOT, load_revision


def test_postgis_revision_replacement_and_rollback():
    url = os.getenv('TEST_POSTGIS_URL')
    if not url:
        pytest.skip('Set TEST_POSTGIS_URL to a disposable atlas_review_* database')
    assert urlparse(url).path.lstrip('/').startswith('atlas_review_'), 'Use a disposable test database'
    data = json.loads((ROOT / 'frontend/public/data/atlas/catalog.json').read_text(encoding='utf-8'))
    divine = json.loads((ROOT / 'frontend/public/data/divine-space.json').read_text(encoding='utf-8'))
    with psycopg.connect(url) as conn:
        conn.execute('CREATE EXTENSION IF NOT EXISTS postgis')
        old_schema = (ROOT / 'database/002_myth_atlas.sql').read_text(encoding='utf-8').replace("'00',", '')
        conn.execute(old_schema)
        other = {**data, 'revision_id': 'review-preserved-revision'}
        load_revision(conn, other, divine)
        load_revision(conn, data, divine)
        assert conn.execute("SELECT count(*) FROM myth_atlas_features WHERE revision_id=%s AND stage_id='00'", (data['revision_id'],)).fetchone()[0] == 1
        removed = data['events'][0]['id']
        reduced = {**data, 'events': data['events'][1:]}
        load_revision(conn, reduced, divine)
        assert conn.execute('SELECT count(*) FROM myth_atlas_features WHERE revision_id=%s AND id=%s', (data['revision_id'], removed)).fetchone()[0] == 0
        assert conn.execute('SELECT count(*) FROM myth_atlas_features WHERE revision_id=%s', (other['revision_id'],)).fetchone()[0] > 0
        before = conn.execute('SELECT count(*) FROM myth_atlas_features WHERE revision_id=%s', (data['revision_id'],)).fetchone()[0]
        broken = copy.deepcopy(data)
        broken['events'][0]['properties']['stage_id'] = '99'
        with pytest.raises(psycopg.errors.CheckViolation):
            load_revision(conn, broken, divine)
        assert conn.execute('SELECT count(*) FROM myth_atlas_features WHERE revision_id=%s', (data['revision_id'],)).fetchone()[0] == before
        assert conn.execute('SELECT catalog FROM myth_atlas_catalog WHERE revision_id=%s', (data['revision_id'],)).fetchone()[0] == reduced
        conn.rollback()

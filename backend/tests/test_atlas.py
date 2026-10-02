import json
from pathlib import Path

from fastapi.testclient import TestClient
from shapely.geometry import shape

from backend.app.main import app

client = TestClient(app)
DATA = Path(__file__).resolve().parents[2] / 'frontend/public/data/atlas'


def test_seven_chapters_and_preserved_spatial_records():
    data = client.get('/api/atlas').json()
    assert [s['id'] for s in data['stages']] == [f'{i:02d}' for i in range(1, 8)]
    assert [len(s['event_ids']) for s in data['stages']] == [4, 5, 5, 5, 4, 5, 4]
    assert len(data['events']) == 39
    assert sum(e['properties']['stage_id'] is None for e in data['events']) == 7
    assert all(e['geometry'] is None for e in data['events'])


def test_stage_filter_cumulative_and_revision_guard():
    current = client.get('/api/atlas/stages/03/layers/events').json()
    assert len(current['features']) == 5
    cumulative = client.get('/api/atlas/stages/03/layers/events?cumulative=true').json()
    assert len(cumulative['features']) == 14
    assert client.get('/api/atlas/stages/08/layers/events').status_code == 404
    assert client.get('/api/atlas/stages/03/layers/unknown').status_code == 404
    assert client.get('/api/atlas?revision_id=unknown').status_code == 409
    assert client.get('/api/atlas/entities/../../secret').status_code == 404


def test_candidate_coordinates_are_modern_references_not_event_locations():
    data = client.get('/api/atlas').json()
    for f in data['candidates'] + data['routes']:
        assert f['properties']['analysis_eligible'] is False
        assert f['properties']['source_ids']
        if f['geometry']:
            assert shape(f['geometry']).is_valid
    ids = {c['id'] for c in data['candidates']}
    assert all(set(r['properties']['candidate_ids']) <= ids for r in data['routes'])
    tianchi = next(c for c in data['candidates'] if c['properties']['label'] == '天山天池')
    assert '阜康' in tianchi['properties']['modern_display_name']
    assert 88 < tianchi['geometry']['coordinates'][0] < 89
    yiyin = client.get('/api/atlas/entities/06-05').json()
    assert yiyin['candidates'][0]['properties']['label'] == '伊川县'


def test_distinct_yi_entities_and_west_queen_forms():
    data = client.get('/api/atlas').json()
    events = {e['id']: e for e in data['events']}
    assert events['04-02']['properties']['name'] == '大羿射日'
    assert events['04-02']['properties']['person_ids'] != events['06-01']['properties']['person_ids']
    assert events['07-01']['properties']['person_ids'] != events['08-07']['properties']['person_ids']
    assert '玉山' in events['08-07']['properties']['basis_note']


def test_unsupported_activity_polygons_and_old_ellipses_are_empty():
    for i in range(1, 8):
        assert not client.get(f'/api/atlas/stages/{i:02d}/layers/activities').json()['features']
        file = DATA.parent / 'stages' / f'{i:02d}.geojson'
        assert not json.loads(file.read_text(encoding='utf-8'))['features']
    divine = client.get('/api/atlas/divine-space').json()
    assert divine['coordinate_system'] == 'diagram-units'
    assert len(divine['places']) == 7
    assert '08' not in {s for p in divine['places'] for s in p['stages']}


def test_map_exports_have_complete_entity_ids_and_recomposable_layers():
    from PIL import Image, ImageChops
    import pytest

    exports = DATA.parents[3] / 'output/atlas'
    if not (exports / 'render-manifest.json').exists():
        pytest.skip('Optional static atlas exports: run python data/render_myth_atlas.py first')
    manifest = json.loads((exports / 'render-manifest.json').read_text(encoding='utf-8'))
    assert len(manifest['stages']) == 7
    all_ids = []
    for stage in manifest['stages']:
        assert stage['size'] == [2560, 1800]
        all_ids.extend(stage['entity_ids'])
        layers = [Image.open(exports / name).convert('RGBA') for name in stage['layers']]
        combined = Image.alpha_composite(Image.alpha_composite(layers[0], layers[1]), layers[2]).convert('RGB')
        actual = Image.open(exports / stage['map']).convert('RGB')
        assert ImageChops.difference(combined, actual).getbbox() is None
    assert len(all_ids) == len(set(all_ids)) == 32

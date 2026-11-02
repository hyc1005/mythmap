import argparse
import hashlib
import json
import math
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = 'v5.1.2'
SOURCES = ROOT / 'data/reference-maps/natural-earth-v5.1.2'
OUTPUT = ROOT / 'frontend/public/data/geography/natural-earth-50m-v5.1.2.geojson'
MANIFEST = OUTPUT.with_suffix('.sources.json')
EXPECTED_INPUTS = {'ne_50m_land.geojson': 'e874b27a51d146452be360cafb3cc50c86001074a67d534113e6534682f9826b', 'ne_50m_lakes.geojson': 'd350b75978b26fe839b797c2c529b2fb8f47fb3983c03f4964e36d5df9378a52', 'ne_50m_rivers_lake_centerlines.geojson': 'f286e0ce978fde999ca2d7a78c764be08542e19b63cded52b05c12d5173ccc51'}

def sha(data):
    return hashlib.sha256(data).hexdigest()

def source_records():
    result = []
    for name, expected in EXPECTED_INPUTS.items():
        raw = (SOURCES / name).read_bytes()
        assert sha(raw) == expected, name + ': original source hash differs'
        result.append({'path': (SOURCES / name).relative_to(ROOT).as_posix(), 'url': 'https://raw.githubusercontent.com/nvkelso/natural-earth-vector/v5.1.2/geojson/' + name, 'sha256': expected, 'bytes': len(raw)})
    return result

def rounded(value):
    if isinstance(value, float):
        return round(value, 5)
    if isinstance(value, (list, tuple)):
        return [rounded(v) for v in value]
    if isinstance(value, dict):
        return {k: rounded(v) for k, v in value.items()}
    return value

def build():
    import shapely
    from shapely.geometry import shape, mapping, box
    sources = source_records()
    features = []
    clip = box(-180, -85, 180, 85)
    for kind, name in [('land', 'land'), ('lake', 'lakes'), ('river', 'rivers_lake_centerlines')]:
        data = json.loads((SOURCES / ('ne_50m_' + name + '.geojson')).read_bytes())
        for index, feature in enumerate(data['features']):
            geometry = shape(feature['geometry'])
            assert geometry.is_valid
            geometry = geometry.intersection(clip).simplify(0.01, preserve_topology=True)
            if geometry.is_empty:
                continue
            props = feature['properties']
            record = rounded({'type': 'Feature', 'id': f'ne50-{kind}-{index}', 'properties': {'kind': kind, 'name_en': props.get('name_en') or props.get('name') or '', 'name_zh': props.get('name_zh') or '', 'scalerank': props.get('scalerank', 0), 'min_zoom': props.get('min_zoom', 0), 'min_label': props.get('min_label', 6), 'featurecla': props.get('featurecla', '')}, 'geometry': mapping(geometry)})
            assert shape(record['geometry']).is_valid
            features.append(record)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps({'type': 'FeatureCollection', 'features': features}, ensure_ascii=False, separators=(',', ':')) + '\n').encode('utf-8')
    OUTPUT.write_bytes(raw)
    manifest = {'schema_version': 1, 'dataset': 'Natural Earth 1:50m physical vectors', 'version': VERSION, 'retrieved_on': '2026-11-02', 'crs': 'EPSG:4326', 'terms_url': 'https://www.naturalearthdata.com/about/terms-of-use/', 'rights': 'Natural Earth declares its raster and vector data public domain; existing project artwork conditions remain unchanged.', 'sources': sources, 'processing': {'tool': 'Python + Shapely', 'shapely_version': shapely.__version__, 'geos_version': shapely.geos_version_string, 'clip_bbox': [-180, -85, 180, 85], 'simplification_degrees': 0.01, 'preserve_topology': True, 'coordinate_decimals': 5, 'script_sha256_lf': sha(Path(__file__).read_bytes().replace(b'\r\n', b'\n'))}, 'output': {'path': OUTPUT.relative_to(ROOT).as_posix(), 'sha256': sha(raw), 'bytes': len(raw), 'features': dict(Counter(f['properties']['kind'] for f in features))}, 'interpretation': 'Modern geographic reference rendered in an antique style; not a reconstruction of ancient geography.', 'rebuild': 'Install the recorded Shapely version, then python data/build_geography_basemap.py'}
    MANIFEST.write_bytes((json.dumps(manifest, ensure_ascii=False, indent=2) + '\n').encode('utf-8'))

def check():
    sources = source_records()
    manifest = json.loads(MANIFEST.read_bytes())
    assert manifest['version'] == VERSION and manifest['crs'] == 'EPSG:4326'
    assert manifest['sources'] == sources
    assert manifest['processing']['script_sha256_lf'] == sha(Path(__file__).read_bytes().replace(b'\r\n', b'\n'))
    raw = OUTPUT.read_bytes()
    assert manifest['output']['sha256'] == sha(raw) and manifest['output']['bytes'] == len(raw)
    data = json.loads(raw)
    assert data['type'] == 'FeatureCollection' and len(data['features']) == 2293
    assert len({f['id'] for f in data['features']}) == len(data['features'])
    assert dict(Counter(f['properties']['kind'] for f in data['features'])) == manifest['output']['features']
    def coordinates(value):
        if isinstance(value[0], (int, float)):
            assert len(value) == 2 and all(math.isfinite(v) for v in value)
            assert -180 <= value[0] <= 180 and -85 <= value[1] <= 85
        else:
            for part in value:
                coordinates(part)
    for feature in data['features']:
        assert feature['geometry']['type'] in ['Polygon', 'MultiPolygon', 'LineString', 'MultiLineString']
        coordinates(feature['geometry']['coordinates'])
    print('PASS Natural Earth v5.1.2: 3 pinned sources, 2293 valid-range features, unique IDs and output provenance')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Rebuild with the recorded Shapely version; --check needs only the Python standard library.')
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    if not args.check:
        build()
    check()

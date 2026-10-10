"""Build the seven-chapter atlas from preserved report records and modern references."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import time
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / 'frontend/public/data'
ATLAS = PUBLIC / 'atlas'
RAW = ROOT / 'data/myth-atlas-inputs'
REVISION = 'myth-atlas-2026-09-30-v1'
TITLES = ['创世阶段', '三皇五氏', '炎黄时期', '五帝后期', '禹夏时期', '夏商之际', '周穆王西巡']
SUBTITLES = ['混沌初分 · 天地成形', '取火构木 · 文明起源', '部落传说 · 战争与追寻', '颛顼尧舜 · 日月与息壤', '治水涂山 · 禹启叙事', '有穷少康 · 夏商之际', '西征山海 · 昆仑瑶池']
PEOPLE = {
    '01-01': ['盘古'], '01-02': ['女娲'], '01-03': ['女娲'], '01-04': ['共工'],
    '02-01': ['伏羲'], '02-02': ['伏羲', '女娲'], '02-03': ['神农'], '02-04': ['燧人'], '02-05': ['有巢'],
    '03-01': ['黄帝', '炎帝'], '03-02': ['黄帝', '蚩尤'], '03-03': ['刑天'], '03-04': ['精卫'], '03-05': ['夸父'],
    '04-01': ['共工', '颛顼'], '04-02': ['大羿'], '04-03': ['嫦娥'], '04-04': ['鲧'], '04-05': ['尧', '舜'],
    '05-01': ['禹'], '05-02': ['禹', '相柳'], '05-03': ['禹', '涂山女'], '05-04': ['涂山女', '启'],
    '06-01': ['后羿（有穷氏）'], '06-02': ['寒浞'], '06-03': ['少康'], '06-04': ['成汤'], '06-05': ['伊尹'],
    '07-01': ['周穆王', '西王母（穆天子传）'], '07-02': ['周穆王', '西王母（穆天子传）'],
    '07-03': ['周穆王', '黄帝'], '07-04': ['周穆王'], '08-06': ['烛龙'], '08-07': ['西王母（山海经）'],
}
NAMES = {name: 'person-' + hashlib.sha256(name.encode('utf-8')).hexdigest()[:12] for name in dict.fromkeys(n for group in PEOPLE.values() for n in group)}
REGIONS = {
    '03-01': [('涿鹿县', '报告列举的河北涿鹿解释'), ('怀来县', '报告所引怀戎解释的现代参考区'), ('延庆区', '报告列举的延庆解释')],
    '03-02': [('涿鹿县', '报告列举的涿鹿解释'), ('怀来县', '报告列举的怀来解释'), ('蔚县', '报告列举的蔚县解释')],
    '03-04': [('长子县', '报告列举的发鸠山长子解释'), ('高平市', '报告列举的发鸠山高平解释')],
    '04-04': [('临沂市', '报告列举的羽山山东解释'), ('连云港市', '报告列举的羽山江苏解释')],
    '04-05': [('临汾市', '报告转述尧都平阳的传统解释，非禅让发生点')],
    '05-03': [('怀远县', '报告列举的涂山怀远解释'), ('南岸区', '报告列举的涂山重庆解释'), ('绍兴市', '报告列举的涂山浙江解释')],
    '05-04': [('登封市', '报告所引嵩山／启母石解释的现代参考区')],
    '06-01': [('滑县', '报告转述有穷氏相关地点的滑县解释')],
    '06-02': [('寒亭区', '报告列举的寒国潍坊解释')],
    '06-03': [('济宁市', '报告列举的缗等地点的济宁解释')],
    '06-04': [('禹州市', '报告列举的夏台禹州解释')],
    '06-05': [('伊川县', '报告正文列举空桑伊川解释；纠正原文件坐标与文字不一致')],
    '07-01': [('和田地区', '报告转述的西王母之邦新疆解释'), ('青海省', '报告列举的青海解释'), ('甘肃省', '报告列举的甘肃解释')],
    '07-02': [('天山天池', '报告列举的瑶池天池解释'), ('青海湖', '报告列举的瑶池青海湖解释')],
    '07-03': [('昆仑山脉', '报告列举的昆仑山解释'), ('祁连山', '报告列举的祁连山解释')],
    '07-04': [('敦煌市', '报告列举的弇山敦煌解释')],
}
SOURCE_LINKS = {
    '女娲补天': 'https://ctext.org/huainanzi/lan-ming-xun/zh',
    '共工怒触不周山': 'https://ctext.org/huainanzi/tian-wen-xun/zh',
    '共工与颛顼争帝': 'https://ctext.org/huainanzi/tian-wen-xun/zh',
    '精卫填海': 'https://ctext.org/shan-hai-jing/bei-shan-jing/zh',
    '刑天舞干戚': 'https://ctext.org/shan-hai-jing/hai-wai-xi-jing/zh',
    '西王母（早期形态）': 'https://ctext.org/shan-hai-jing/xi-shan-jing/zh',
    '昆仑之丘': 'https://ctext.org/shan-hai-jing/xi-shan-jing/zh',
}
REFERENCE_QUERIES = {'天山天池': '天池 阜康市', '昆仑山脉': 'Kunlun Mountains'}


def read(path: Path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def write(path: Path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def fetch_json(url: str):
    req = urllib.request.Request(url, headers={'User-Agent': 'MythAtlasLocal/1.0 educational desktop cartography'})
    with urllib.request.urlopen(req, timeout=40) as response:
        return json.load(response)


def prepare_inputs(source: Path):
    RAW.mkdir(parents=True, exist_ok=True)
    for file in sorted(source.glob('*.geojson')):
        dest = RAW / file.name
        if not dest.exists():
            shutil.copy2(file, dest)
    for kind in ['land', 'rivers_lake_centerlines']:
        dest = RAW / f'ne_110m_{kind}.geojson'
        if not dest.exists():
            write(dest, fetch_json(f'https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_{kind}.geojson'))
    cache_path = RAW / 'modern-reference-places.json'
    cache = read(cache_path) if cache_path.exists() else {}
    for label in dict.fromkeys(label for regions in REGIONS.values() for label, _ in regions):
        if label in cache and cache[label].get('query') == REFERENCE_QUERIES.get(label, label):
            continue
        query = REFERENCE_QUERIES.get(label, label)
        url = 'https://nominatim.openstreetmap.org/search?' + urllib.parse.urlencode({'q': query, 'format': 'jsonv2', 'limit': 1, 'countrycodes': 'cn'})
        try:
            result = fetch_json(url)
            cache[label] = {'query': query, 'query_url': url, 'accessed_on': '2026-09-30', 'result': result[0] if result else None}
        except Exception as exc:
            print(f'No verified reference for {label}: {exc}', flush=True)
            continue
        write(cache_path, cache)
        print(f'Reference: {label}', flush=True)
        time.sleep(1.1)


def collection(features, note=''):
    return {'type': 'FeatureCollection', 'revision_id': REVISION, 'note': note, 'features': features}


def build():
    from shapely.geometry import box, mapping, shape

    originals = [f for i in range(1, 9) for file in RAW.glob(f'{i:02d}_*.geojson') for f in read(file)['features']]
    if len(originals) != 39:
        raise ValueError(f'Expected 39 preserved report records, got {len(originals)}')
    cache = read(RAW / 'modern-reference-places.json')
    artwork_file = ATLAS / 'artwork-manifest.json'
    reviewed_assets = {a['id']: a['status'] for a in read(artwork_file)['assets']} if artwork_file.exists() else {}
    sources, events, candidates, persons, audit = [], [], [], [], []
    for f in originals:
        p = f['properties']
        id_ = p['id']
        source_id = f'report-{id_}'
        name = '大羿射日' if id_ == '04-02' else p['name']
        sources.append({'id': source_id, 'title': p['source_text'], 'quote': p['source_quote'],
                        'commentary': p.get('commentary', ''), 'modern_source': p.get('modern_source', ''),
                        'url': SOURCE_LINKS.get(p['name']), 'verification_status': 'report_imported',
                        'note': '报告引文与现代学者归属须逐条对照版本；网络原文入口仅用于复核。'})
        event_candidates = []
        for n, (label, basis) in enumerate(REGIONS.get(id_, []), 1):
            entry = cache.get(label, {})
            modern = entry.get('result')
            cid = f'{id_}-candidate-{n}'
            geometry = {'type': 'Point', 'coordinates': [float(modern['lon']), float(modern['lat'])]} if modern else None
            cp = {'id': cid, 'stage_id': id_[:2], 'entity_id': id_, 'name': f'{name} · {label}', 'label': label,
                  'layer_role': 'modern_candidate', 'evidence_kind': 'report_hypothesis', 'precision': 'disputed',
                  'source_ids': [source_id], 'basis_note': basis + '。标记为现代参考区域的中心，不是古代事件发生点。',
                  'revision_id': REVISION, 'verification_status': 'modern_reference_verified' if modern else 'unlocated',
                  'historical_verification': 'pending', 'coordinate_source': entry.get('query_url'),
                  'osm_type': modern.get('osm_type') if modern else None, 'osm_id': modern.get('osm_id') if modern else None,
                  'modern_display_name': modern.get('display_name') if modern else None, 'reference_bbox': modern.get('boundingbox') if modern else None,
                  'analysis_eligible': False}
            candidates.append({'type': 'Feature', 'id': cid, 'geometry': geometry, 'properties': cp})
            event_candidates.append(cid)
        precision = 'disputed' if event_candidates else 'unlocatable'
        basis = '多种解释见候选层；事件本身无经核实的发生点。' if event_candidates else '原始报告的宽泛／示意位置不构成发生点依据；保留叙事条目，不补造坐标。'
        ep = {'id': id_, 'stage_id': id_[:2] if id_[:2] != '08' else None, 'entity_id': id_, 'name': name,
              'layer_role': 'spatial_reference' if id_.startswith('08') else 'event', 'evidence_kind': 'literary_record',
              'precision': precision, 'source_ids': [source_id], 'basis_note': basis, 'revision_id': REVISION,
              'person_ids': [NAMES[n] for n in PEOPLE.get(id_, [])], 'people': PEOPLE.get(id_, []), 'candidate_ids': event_candidates,
              'source_text': p['source_text'], 'source_quote': p['source_quote'], 'commentary': p.get('commentary', ''),
              'modern_identification': p.get('modern_identification', ''), 'modern_source': p.get('modern_source', ''),
              'dispute': p.get('dispute', ''), 'category': p.get('category', ''), 'tags': p.get('tags', []),
              'verification_status': 'report_imported', 'asset_id': f'illustration-{id_[:2]}' if not id_.startswith('08') else 'illustration-divine',
              'illustration_role': 'symbolic', 'analysis_eligible': False,
              'original_geometry': f['geometry'], 'original_modern_coordinates': p.get('modern_coordinates')}
        if id_ == '08-07':
            ep['basis_note'] += ' 《西山经》原文西王母居玉山；保留与昆仑不同的文本地点。'
        if id_ == '05-01':
            ep['basis_note'] += ' 治水涉及多条水系，现有材料不足以绘出活动区或复原古河道。'
        events.append({'type': 'Feature', 'id': id_, 'geometry': None, 'properties': ep})
        audit.append({'id': id_, 'name': name, 'decision': '事件几何置空；现代候选独立成层' if event_candidates else '只作叙事／神域对象',
                      'reason': basis, 'original_coordinate': p.get('modern_coordinates'), 'candidate_ids': event_candidates,
                      'visual_check': reviewed_assets.get('divine' if id_.startswith('08') else id_[:2], 'pending'),
                      'visual_review_scope': '人物、主题和关键意象对应；服饰建筑不作复原证据', 'source_status': 'report_imported'})
    for name, pid in NAMES.items():
        linked = [e for e in events if pid in e['properties']['person_ids']]
        persons.append({'id': pid, 'name': name, 'event_ids': [e['id'] for e in linked],
                        'stage_ids': sorted({e['properties']['stage_id'] for e in linked if e['properties']['stage_id']}),
                        'source_ids': [e['properties']['source_ids'][0] for e in linked], 'geometry': None})

    region = box(72, 17, 137, 55)
    for kind in ['land', 'rivers_lake_centerlines']:
        result = []
        for f in read(RAW / f'ne_110m_{kind}.geojson')['features']:
            geom = shape(f['geometry']).intersection(region)
            if geom.is_empty:
                continue
            result.append({'type': 'Feature', 'geometry': mapping(geom), 'properties': {'name': f['properties'].get('name'), 'layer_role': 'modern_geographic_reference'}})
        write(ATLAS / f'{"land" if kind == "land" else "rivers"}.geojson', collection(result, 'Natural Earth 1:110m 现代地理参照；海岸和河道不代表上古复原。'))

    # Connections express paired interpretations only; they are not reconstructed travel tracks.
    routes = []
    for pair, label in [(('昆仑山脉', '天山天池'), '昆仑山—天池候选连接'), (('祁连山', '青海湖'), '祁连山—青海湖候选连接')]:
        endpoints = []
        for region_name in pair:
            matches = [c for c in candidates if c['properties']['label'] == region_name and c['geometry']]
            endpoints.append(matches[0] if matches else None)
        if not all(endpoints):
            continue
        routes.append({'type': 'Feature', 'id': f'07-connection-{len(routes)+1}',
                       'geometry': {'type': 'LineString', 'coordinates': [e['geometry']['coordinates'] for e in endpoints]},
                       'properties': {'id': f'07-connection-{len(routes)+1}', 'stage_id': '07', 'entity_id': '07-03', 'name': label,
                                      'layer_role': 'narrative_connection', 'evidence_kind': 'cartographic_hypothesis', 'precision': 'disputed',
                                      'source_ids': ['report-07-03', 'report-07-02'], 'basis_note': '连接两种现代候选解释；直线不表示实际道路、方向顺序或行程。',
                                      'revision_id': REVISION, 'candidate_ids': [e['id'] for e in endpoints], 'analysis_eligible': False}})

    stages = []
    for i, title in enumerate(TITLES, 1):
        sid = f'{i:02d}'
        chapter = [e for e in events if e['properties']['stage_id'] == sid]
        stage_candidates = [c for c in candidates if c['properties']['stage_id'] == sid]
        write(ATLAS / f'{sid}-events.geojson', collection(chapter))
        write(ATLAS / f'{sid}-candidates.geojson', collection(stage_candidates))
        write(ATLAS / f'{sid}-routes.geojson', collection([r for r in routes if r['properties']['stage_id'] == sid]))
        write(ATLAS / f'{sid}-activities.geojson', collection([], '现有材料不足以确定部落／人物活动区；不以行政范围、缓冲区或凸包代替。'))
        stages.append({'id': sid, 'title': title, 'subtitle': SUBTITLES[i-1], 'event_ids': [e['id'] for e in chapter],
                       'export_map': f'output/atlas/maps/{sid}.png', 'illustration_source': f'frontend/artwork-source/atlas-illustrations/{sid}.png',
                       'layers': {role: f'/data/atlas/{sid}-{role}.geojson' for role in ['events', 'candidates', 'routes', 'activities']},
                       'source_ids': [e['properties']['source_ids'][0] for e in chapter], 'revision_id': REVISION})
    write(ATLAS / 'catalog.json', {'revision_id': REVISION, 'stages': stages, 'events': events, 'candidates': candidates, 'people': persons,
                                 'sources': sources, 'routes': routes, 'counts': {'narrative_events': 32, 'spatial_records': 7, 'all_records': 39},
                                 'geographic_reference': '现代地理骨架辅助阅读，不复原古代海岸线或河道。'})
    write(ATLAS / 'review.json', {'revision_id': REVISION, 'counts_verified': {'stages': [4, 5, 5, 5, 4, 5, 4], 'spatial': 7, 'total': 39},
          'report_corrections': ['原报告35条与实际39条不一致；七叙事阶段实际32条', '原报告35个事件+38个来源并不等于39',
          '示意WGS84坐标从实际事件几何移至original_geometry', '大羿与有穷氏后羿分开', '西王母早期文本居玉山，不能直接标作昆仑',
          '原文件06-05正文伊川解释与坐标不一致，现代参考改由地名查询确定'], 'records': audit,
          'input_hashes': {f.name: hashlib.sha256(f.read_bytes()).hexdigest() for f in RAW.glob('0*.geojson')}})
    print(f'Built {len(stages)} chapters, {len(events)} records, {len(candidates)} candidate interpretations, {len(routes)} schematic connections.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--fetch', action='store_true')
    parser.add_argument('--source', type=Path, help='Local source directory (required with --fetch)')
    args = parser.parse_args()
    if args.fetch:
        if args.source is None:
            parser.error('--source is required with --fetch')
        prepare_inputs(args.source)
    build()

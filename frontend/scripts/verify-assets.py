"""Read-only inventory, source pointer and published derivative validation."""
import argparse
import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path


def validate(root, inventory):
    errors = []
    rows = list(csv.DictReader(inventory.open(encoding='utf-8-sig'), delimiter='\t'))
    paths = {row['path'] for row in rows}
    if len(paths) != len(rows):
        errors.append('duplicate inventory paths')
    counts = {}
    for row in rows:
        path = root / row['path']
        if not path.is_file():
            errors.append(f'missing: {row["path"]}')
            continue
        raw = path.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        # Git's text checkout policy may change raw CRLF bytes, but never binary bytes.
        normalized = None
        if row.get('sha256_lf') not in ('', '-', None):
            normalized = raw.decode('utf8').replace('\r\n', '\n').replace('\r', '\n').encode('utf8')
        raw_ok = digest == row['sha256'] and len(raw) == int(row['bytes'])
        lf_ok = normalized is not None and hashlib.sha256(normalized).hexdigest() == row['sha256_lf'] and len(normalized) == int(row['bytes_lf'])
        if not (raw_ok or lf_ok):
            errors.append(f'changed bytes: {row["path"]}')
        for field in ['audit_status', 'audit_evidence', 'audit_unknowns', 'audit_scope']:
            if not row.get(field, '').strip():
                errors.append(f'unreviewed {field}: {row["path"]}')
        counts[row.get('audit_status')] = counts.get(row.get('audit_status'), 0) + 1
    asset_roots = ('frontend/public/', 'frontend/artwork-source/', 'data/reference-scans/', 'data/reference-maps/', 'docs/media/')
    for directory in asset_roots:
        for file in (root / directory).rglob('*'):
            path = file.relative_to(root).as_posix()
            if file.is_file() and path not in paths:
                errors.append(f'unlisted asset: {path}')
    for file in (root / 'frontend/src').rglob('*.json'):
        if file.relative_to(root).as_posix() not in paths:
            errors.append(f'unlisted metadata: {file.relative_to(root).as_posix()}')
    sources = {}
    def source_json(path):
        if path not in sources:
            sources[path] = json.loads((root / path).read_text(encoding='utf8'))
        return sources[path]
    pointers = set()
    for row in rows:
        for field in ['evidence', 'audit_evidence']:
            pointers.update(re.findall(r'(?:git:[0-9a-f]{7,40}:)?(?:frontend|data|docs)/[^\s;，；]+\.json#(?:/[^\s;，；]*)?', row.get(field, '')))
    for pointer in sorted(pointers):
        try:
            path, fragment = pointer.split('#', 1)
            if path.startswith('git:'):
                _, commit, path = path.split(':', 2)
                key = f'{commit}:{path}'
                if key not in sources:
                    sources[key] = json.loads(subprocess.check_output(['git', '-C', str(root), 'show', key]).decode('utf8'))
                value = sources[key]
            else:
                value = source_json(path)
            for part in fragment.lstrip('/').split('/') if fragment else []:
                part = part.replace('~1', '/').replace('~0', '~')
                value = value[int(part)] if isinstance(value, list) else value[part]
        except (ValueError, KeyError, IndexError, OSError, subprocess.CalledProcessError) as error:
            errors.append(f'invalid source pointer: {pointer}: {error}')
    edges = []
    def publish_path(path):
        return 'frontend/public/' + path.lstrip('/')
    for name in ['optimized-assets', 'preview-assets', 'refined-artwork']:
        for logical, info in source_json(f'frontend/src/{name}.json').items():
            if logical != 'bookplate' and not (root / publish_path(logical)).is_file() and not (name == 'refined-artwork' and info.get('full')):
                errors.append(f'missing logical asset: {logical}')
            variants = [info] if 'path' in info else info.values()
            for variant in variants:
                path = publish_path(variant['path'])
                if path not in paths or not (root / path).is_file():
                    errors.append(f'unregistered published variant: {path}')
                elif variant.get('bytes', variant.get('optimized_bytes')) != (root / path).stat().st_size:
                    errors.append(f'variant byte claim changed: {path}')
                if logical != 'bookplate':
                    edges.append((publish_path(logical), path))
    graph = {}
    for parent, child in edges:
        if parent != child:
            graph.setdefault(parent, set()).add(child)
    def visit(node, stack):
        if node in stack:
            errors.append(f'derivative cycle: {node}')
            return
        for child in graph.get(node, []):
            visit(child, stack | {node})
    for node in graph:
        visit(node, set())
    registry = source_json('data/character-artwork-registry.json')
    audit = registry.get('published_character_audit', {})
    assets = {item['published_asset']: item for item in audit.get('assets', [])}
    for path, item in assets.items():
        file = root / publish_path(path)
        if not file.is_file() or hashlib.sha256(file.read_bytes()).hexdigest() != item['sha256']:
            errors.append(f'role review asset changed: {path}')
    catalog = source_json('frontend/public/data/atlas/catalog.json')
    if {person['id'] for person in catalog['people']} != {person['person_id'] for person in audit.get('characters', [])}:
        errors.append('role review omits current catalogue people')
    def resolved(path):
        if not path.startswith('/'):
            path = '/data/atlas/myth-icons/' + path
        return source_json('frontend/src/refined-artwork.json').get(path, {}).get('full', {}).get('path') or source_json('frontend/src/optimized-assets.json').get(path, {}).get('path') or path
    def role_coverage(value):
        if isinstance(value, dict):
            for path in ([value['artwork']] if value.get('artwork') else []) + value.get('artworks', []):
                if resolved(path) not in assets:
                    errors.append(f'unreviewed current artwork: {path}')
            for child in value.values():
                role_coverage(child)
        elif isinstance(value, list):
            for child in value:
                role_coverage(child)
    world = source_json('frontend/public/data/myth-world.json')
    role_coverage(world)
    role_coverage(catalog['events'])
    for person in audit.get('characters', []):
        for usage in person['usages']:
            path = usage['published_asset']
            if path not in assets:
                errors.append(f'unreviewed role usage: {path}')
    for figure in audit.get('supporting_figures', []):
        if figure['entry_id'] not in assets.get(figure['published_asset'], {}).get('entry_ids', []):
            errors.append(f'unreviewed supporting figure: {figure["name"]}')
    world_audit = registry.get('world_character_artwork', {})
    entries = world_audit.get('entries', [])
    registered = {entry['entry_id']: entry for entry in entries}
    expected_groups = {
        'bestiary': world['beasts'],
        'deities': [entry for entry in world['text_entities'] if entry['kind'] == 'deity'],
        'domain_portraits': [entry for entry in world['domains']
                             if entry['id'] in {'domain-yushan', 'domain-zhangwei'}],
    }
    expected_ids = {entry['id'] for group in expected_groups.values() for entry in group}
    if registered.keys() != expected_ids or len(registered) != len(entries):
        errors.append('world role registry has missing, extra or duplicate entries')
    for group, records in expected_groups.items():
        for record in records:
            entry_id = record['id']
            entry = registered.get(entry_id, {})
            artwork = record.get('artwork')
            placeholder = record.get('appearance_unknown') or not artwork
            published = resolved(artwork) if not placeholder else None
            suppressed = resolved(artwork) if placeholder and artwork else None
            status = 'placeholder' if placeholder else 'configured_illustration'
            if (entry.get('group'), entry.get('name'), entry.get('status'),
                    entry.get('published_asset'), entry.get('suppressed_asset')) != (
                    group, record['name'], status, published, suppressed):
                errors.append(f'world role registry binding differs: {entry_id}')
            if published and entry_id not in assets.get(published, {}).get('entry_ids', []):
                errors.append(f'world role usage is missing from asset audit: {entry_id}')
    people_ids = {person['id'] for person in catalog['people']}
    for link in world_audit.get('relationships', []):
        if not set(link['entry_ids']) <= expected_ids or (
                'person_id' in link and link['person_id'] not in people_ids):
            errors.append(f'invalid role relationship: {link["entry_ids"]}')
        if link['type'] == 'shared_portrait':
            portraits = {registered.get(entry_id, {}).get('published_asset') for entry_id in link['entry_ids']}
            if len(portraits) != 1 or None in portraits:
                errors.append(f'role relationship no longer shares a portrait: {link["entry_ids"]}')
    return {'files': len(rows), 'source_pointers': len(pointers), 'published_edges': len(edges), 'reviewed_role_assets': len(assets), 'audit_status': counts, 'errors': errors}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--inventory', type=Path)
    args = parser.parse_args()
    report = validate(args.root, args.inventory or args.root / 'docs/assets-inventory.tsv')
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(bool(report['errors']))

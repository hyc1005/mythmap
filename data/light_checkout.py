"""Apply a source-aware sparse checkout without weakening verification scripts."""
import argparse
import json
import subprocess
from pathlib import Path, PurePosixPath

BASE_PATTERNS = ['/*', '!/frontend/artwork-source/**/*.png',
                 '!/frontend/artwork-source/**/*.webp', '!/data/reference-scans/**/*.jpg']


def patterns(root, profile):
    read = lambda path: json.loads((root / path).read_text(encoding='utf8'))
    registry = read('data/character-artwork-registry.json')
    required = {item['master_file'] for item in registry['works']}
    required.update(source['path'] for repair in registry.get('display_repairs', []) for source in repair['sources'])
    if profile in ('central-current', 'northern'):
        book = 'zhongshan' if profile == 'central-current' else 'beishan'
        required.update(item['local_path'] for item in read(f'data/reference-scans/{book}/sources.json'))
        manifests = ['entities-generation.json'] if book == 'zhongshan' else ['generation.json', 'entities-generation.json']
        for manifest in manifests:
            required.update(f'frontend/artwork-source/{book}/' + item['source_file']
                            for item in read(f'frontend/artwork-source/{book}/{manifest}')['assets'])
    if profile == 'narrative':
        required.add('frontend/artwork-source/archived/suiren-after-fire-v2-original.webp')
    required = sorted(path for path in required if path.startswith(('frontend/artwork-source/', 'data/reference-scans/')))
    for name in required:
        path = PurePosixPath(name)
        if path.is_absolute() or '..' in path.parts or '\\' in name or ':' in name:
            raise ValueError(f'Invalid source path: {name}')
    return BASE_PATTERNS + ['/' + name for name in required], required


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--profile', default='core', choices=['core', 'atlas', 'central-current', 'northern',
                        'narrative', 'western', 'southern-cards', 'southern-reader', 'stories'])
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    rules, required = patterns(args.root, args.profile)
    if args.dry_run:
        print(json.dumps({'profile': args.profile, 'patterns': rules, 'required_sources': required}, indent=2))
        return
    subprocess.run(['git', '-C', str(args.root), '-c', 'http.version=HTTP/1.1',
                    '-c', 'http.lowSpeedLimit=1024', '-c', 'http.lowSpeedTime=30',
                    'sparse-checkout', 'set', '--no-cone', '--stdin'],
                   input='\n'.join(rules) + '\n', text=True, check=True)
    for name in required:
        if not (args.root / name).is_file():
            raise ValueError(f'Required source was not hydrated: {name}')
    print(f'LIGHT {args.profile}: {len(required)} required source assets retained; all metadata and runtime assets included')


if __name__ == '__main__':
    main()

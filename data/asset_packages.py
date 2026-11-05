"""Package, verify and restore the project's original artwork and facsimiles."""
import argparse
import hashlib
import json
import subprocess
import urllib.request
import zipfile
from pathlib import Path, PurePosixPath

SOURCE_ROOTS = ('frontend/artwork-source/', 'data/reference-scans/')


def digest(path):
    result = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(4 * 1024 * 1024), b''):
            result.update(block)
    return result.hexdigest()


def content(path):
    value = path.read_bytes()
    return value.replace(b'\r\n', b'\n').replace(b'\r', b'\n') if path.suffix == '.json' else value


def destination(root, name):
    relative = PurePosixPath(name)
    if relative.is_absolute() or '..' in relative.parts or '\\' in name or ':' in name:
        raise ValueError(f'Invalid asset path: {name}')
    if not any(name.startswith(prefix) for prefix in SOURCE_ROOTS):
        raise ValueError(f'Asset outside source roots: {name}')
    target = (root / name).resolve()
    if not target.is_relative_to(root.resolve()):
        raise ValueError(f'Asset outside destination: {name}')
    return target


def pack(args):
    root = args.root.resolve()
    git = lambda *words: subprocess.check_output(['git', '-C', str(root), *words], encoding='utf8').strip()
    revision = git('rev-parse', args.source_commit or 'HEAD')
    if git('diff', '--name-only', revision, '--', *SOURCE_ROOTS):
        raise ValueError('Source assets differ from the selected source commit')
    paths = git('ls-files', '--', *SOURCE_ROOTS).splitlines()
    if not paths:
        raise ValueError('No tracked original assets found')
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    catalog = {'schema_version': 1, 'source_commit': revision,
               'builder_commit': git('rev-parse', 'HEAD'), 'release_tag': args.tag,
               'bundles': [], 'files': []}
    groups = {}
    for name in sorted(paths):
        path = destination(root, name)
        if not path.is_file():
            raise ValueError(f'Missing original; hydrate before packaging: {name}')
        parts = PurePosixPath(name).parts
        group = ('art-' if name.startswith(SOURCE_ROOTS[0]) else 'scan-') + parts[2]
        groups.setdefault(group, []).append(name)
    for group, names in groups.items():
        chunks, chunk, size = [], [], 0
        for name in names:
            amount = (root / name).stat().st_size
            if chunk and size + amount > args.max_mib * 1024 * 1024:
                chunks.append(chunk)
                chunk, size = [], 0
            chunk.append(name)
            size += amount
        if chunk:
            chunks.append(chunk)
        for number, members in enumerate(chunks, 1):
            bundle_name = f'mythmap-{group}-{number:02}.zip'
            archive = output / bundle_name
            if archive.exists():
                raise ValueError(f'Archive already exists: {archive}')
            with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=1) as package:
                for name in members:
                    value = content(root / name)
                    info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
                    info.compress_type = zipfile.ZIP_DEFLATED
                    info.external_attr = 0o100644 << 16
                    info.create_system = 3
                    package.writestr(info, value, compresslevel=1)
                    catalog['files'].append({'path': name, 'bytes': len(value),
                                             'sha256': hashlib.sha256(value).hexdigest(), 'bundle': bundle_name})
            catalog['bundles'].append({'name': bundle_name, 'group': group,
                                       'bytes': archive.stat().st_size, 'sha256': digest(archive),
                                       'members': len(members),
                                       'url': f'https://github.com/hyc1005/mythmap/releases/download/{args.tag}/{bundle_name}'})
    (output / 'asset-bundles.json').write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    for name in ['ASSETS.md', 'LICENSE']:
        (output / name).write_bytes((root / name).read_bytes())
    print(f'PACK {len(catalog["files"])} files in {len(catalog["bundles"])} bundles')


def selection(args):
    catalog = json.loads(args.catalog.read_text(encoding='utf8'))
    if catalog['schema_version'] != 1:
        raise ValueError('Unsupported asset catalog version')
    bundles = [item for item in catalog['bundles'] if not args.group or item['group'] in args.group]
    if not bundles or args.group and set(args.group) - {item['group'] for item in bundles}:
        raise ValueError('Unknown or empty asset group')
    names = {item['name'] for item in bundles}
    if len(names) != len(bundles) or any(Path(name).name != name or not name.endswith('.zip') or '\\' in name or ':' in name for name in names):
        raise ValueError('Invalid or duplicate bundle name')
    files = [item for item in catalog['files'] if item['bundle'] in names]
    if len({item['path'] for item in files}) != len(files):
        raise ValueError('Duplicate asset paths')
    for item in files:
        destination(args.root, item['path'])
    return bundles, files


def verify(args):
    bundles, files = selection(args)
    for bundle in bundles:
        path = args.archives / bundle['name']
        if path.stat().st_size != bundle['bytes'] or digest(path) != bundle['sha256']:
            raise ValueError(f'Bundle checksum mismatch: {path.name}')
        expected = {item['path']: item for item in files if item['bundle'] == path.name}
        if len(expected) != bundle['members']:
            raise ValueError(f'Catalog member count mismatch: {path.name}')
        with zipfile.ZipFile(path) as archive:
            names = archive.namelist()
            if len(names) != len(set(names)) or set(names) != set(expected):
                raise ValueError(f'Archive member list mismatch: {path.name}')
            for name in names:
                value = archive.read(name)
                if len(value) != expected[name]['bytes'] or hashlib.sha256(value).hexdigest() != expected[name]['sha256']:
                    raise ValueError(f'Asset checksum mismatch: {name}')
    print(f'VERIFY {len(files)} assets in {len(bundles)} bundles')
    return bundles, files


def restore(args):
    bundles, files = verify(args)
    missing = set()
    for item in files:
        target = destination(args.root, item['path'])
        if not target.exists():
            missing.add(item['path'])
        elif not target.is_file() or hashlib.sha256(content(target)).hexdigest() != item['sha256']:
            raise ValueError(f'Existing asset differs; refusing overwrite: {item["path"]}')
    for bundle in bundles:
        with zipfile.ZipFile(args.archives / bundle['name']) as archive:
            for name in archive.namelist():
                if name not in missing:
                    continue
                target = destination(args.root, name)
                target.parent.mkdir(parents=True, exist_ok=True)
                with target.open('xb') as stream:
                    stream.write(archive.read(name))
    print(f'RESTORE {len(missing)} missing assets; existing matching assets retained')


def check(args):
    _, files = selection(args)
    for item in files:
        value = content(destination(args.root, item['path']))
        if len(value) != item['bytes'] or hashlib.sha256(value).hexdigest() != item['sha256']:
            raise ValueError(f'Current source differs from distribution catalog: {item["path"]}')
    print(f'CHECK {len(files)} source files match the distribution catalog')


def download(args):
    bundles, _ = selection(args)
    args.archives.mkdir(parents=True, exist_ok=True)
    for bundle in bundles:
        target = args.archives / bundle['name']
        if target.exists():
            if target.stat().st_size == bundle['bytes'] and digest(target) == bundle['sha256']:
                continue
            raise ValueError(f'Existing download differs; retained for inspection: {target}')
        partial = target.with_suffix('.zip.download')
        if partial.exists():
            raise ValueError(f'Incomplete download retained for inspection: {partial}')
        expected_prefix = 'https://github.com/hyc1005/mythmap/releases/download/'
        if not bundle['url'].startswith(expected_prefix):
            raise ValueError('Download URL is outside this repository release channel')
        with urllib.request.urlopen(bundle['url'], timeout=90) as response, partial.open('xb') as stream:
            for block in iter(lambda: response.read(4 * 1024 * 1024), b''):
                stream.write(block)
        if partial.stat().st_size != bundle['bytes'] or digest(partial) != bundle['sha256']:
            raise ValueError(f'Download checksum mismatch; file retained: {partial}')
        partial.rename(target)
        print(f'DOWNLOAD {target.name}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    command = commands.add_parser('pack')
    command.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    command.add_argument('--output', type=Path, required=True)
    command.add_argument('--tag', required=True)
    command.add_argument('--source-commit')
    command.add_argument('--max-mib', type=int, default=180)
    for name in ['verify', 'restore', 'download', 'check']:
        command = commands.add_parser(name)
        command.add_argument('--catalog', type=Path, required=True)
        if name != 'check':
            command.add_argument('--archives', type=Path, required=True)
        command.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
        command.add_argument('--group', action='append')
    args = parser.parse_args()
    if args.command == 'pack' and (args.max_mib < 1 or not args.tag or any(c not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-' for c in args.tag)):
        parser.error('Use a positive bundle size and a simple release tag')
    globals()[args.command](args)


if __name__ == '__main__':
    main()

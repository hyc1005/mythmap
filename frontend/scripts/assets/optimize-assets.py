import json
import sys
from pathlib import Path

from PIL import Image

frontend = Path(__file__).resolve().parents[2]
public = frontend / 'public'
destination = public / 'data/atlas/optimized'
destination.mkdir(parents=True, exist_ok=True)
manifest = {}
sources = [path for path in (public / 'data/atlas/myth-icons').rglob('*')
           if path.suffix in {'.webp', '.png'} and 'animations' not in path.parts]
sources.append(public / 'data/atlas/myth-paper.webp')
for source in sources:
    if source.stat().st_size < 300_000:
        continue
    relative = source.relative_to(public / 'data/atlas')
    target = (destination / relative).with_suffix('.webp')
    target.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(source) as image:
        original_size = image.size
        image.thumbnail((1600, 1200), Image.Resampling.LANCZOS)
        if '--force' in sys.argv or not target.exists() or target.stat().st_mtime < source.stat().st_mtime:
            image.save(target, 'WEBP', quality=83, method=6, alpha_quality=100)
        manifest['/' + source.relative_to(public).as_posix()] = {
            'path': '/' + target.relative_to(public).as_posix(),
            'original_bytes': source.stat().st_size,
            'optimized_bytes': target.stat().st_size,
            'original_dimensions': original_size,
            'dimensions': image.size,
        }

source = frontend / 'artwork-source/brand/shanhai-mark-reference.png'
target = destination / 'shanhai-bookplate.webp'
with Image.open(source) as image:
    original_size = image.size
    image.thumbnail((384, 384), Image.Resampling.LANCZOS)
    image.save(target, 'WEBP', quality=88, method=6, alpha_quality=100)
    manifest['bookplate'] = {
        'path': '/data/atlas/optimized/shanhai-bookplate.webp',
        'original_bytes': source.stat().st_size,
        'optimized_bytes': target.stat().st_size,
        'original_dimensions': original_size,
        'dimensions': image.size,
    }
(frontend / 'src/optimized-assets.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
before = sum(item['original_bytes'] for item in manifest.values())
after = sum(item['optimized_bytes'] for item in manifest.values())
print(f'{len(manifest)} assets: {before:,} -> {after:,} bytes ({(1 - after / before):.1%} smaller); originals preserved')

previews = {}
for source in sources:
    if 'myth-icons' not in source.parts or 'scenes' in source.parts or 'terrain' in source.parts:
        continue
    original = '/' + source.relative_to(public).as_posix()
    previews[original] = {}
    for variant, width in [('card', 320), ('preview', 480)]:
        target = public / 'data/atlas/previews' / variant / source.relative_to(public / 'data/atlas/myth-icons').with_suffix('.webp')
        target.parent.mkdir(parents=True, exist_ok=True)
        with Image.open(source) as image:
            image.thumbnail((width, width), Image.Resampling.LANCZOS)
            image.save(target, 'WEBP', quality=82, method=6, alpha_quality=100)
            previews[original][variant] = {'path': '/' + target.relative_to(public).as_posix(),
                                           'bytes': target.stat().st_size, 'dimensions': image.size}
(frontend / 'src/preview-assets.json').write_text(json.dumps(previews, indent=2) + '\n', encoding='utf-8')

favicon = public / 'favicon.png'
preserved = frontend / 'artwork-source/brand/favicon-original.png'
if not preserved.exists():
    preserved.write_bytes(favicon.read_bytes())
with Image.open(preserved) as image:
    image.thumbnail((64, 64), Image.Resampling.LANCZOS)
    image.save(favicon, optimize=True)
print(f'{len(previews)} thumbnail pairs; favicon {favicon.stat().st_size} bytes; originals preserved')

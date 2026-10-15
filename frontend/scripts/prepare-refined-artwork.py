import json
from pathlib import Path

from PIL import Image

frontend = Path(__file__).resolve().parents[1]
sources = frontend / 'artwork-source/woodcut-refinement'
public = frontend / 'public'
destination = public / 'data/atlas/refined'
destination.mkdir(parents=True, exist_ok=True)
manifest = {}
for asset in json.loads((sources / 'generation.json').read_text(encoding='utf-8'))['assets']:
    variants = {'full': 1280, 'card': 320, 'preview': 480} if asset['name'].startswith('xiangliu-') else {'map': 128}
    manifest[asset['original']] = {}
    with Image.open(sources / (asset['name'] + '.png')) as source:
        assert source.mode == 'RGBA' and source.getchannel('A').getextrema()[0] == 0
        for variant, edge in variants.items():
            image = source.copy()
            image.thumbnail((round(edge * .88), round(edge * .88)), Image.Resampling.LANCZOS)
            canvas = Image.new('RGBA', (edge, edge), (0, 0, 0, 0))
            canvas.alpha_composite(image, ((edge - image.width) // 2, (edge - image.height) // 2))
            target = destination / (asset['name'] + '-' + variant + '.webp')
            canvas.save(target, 'WEBP', quality=88, method=6, alpha_quality=100)
            manifest[asset['original']][variant] = {'path': '/' + target.relative_to(public).as_posix(), 'bytes': target.stat().st_size, 'dimensions': [edge, edge]}
(frontend / 'src/refined-artwork.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
print('Prepared six transparent WebP assets:', sum(item['bytes'] for variants in manifest.values() for item in variants.values()), 'bytes')

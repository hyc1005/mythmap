"""Export the animation landscape runtime WebPs from the preserved transparent originals."""
import argparse
import json
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[3]
MANIFEST = ROOT / 'frontend/artwork-source/animation-landscapes/generation.json'


def build(check=False):
    manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    changed = False
    for asset in manifest['assets']:
        source = ROOT / asset['source']
        if not source.is_file():
            raise SystemExit(f'Missing source: {asset["source"]}')
        for variant in asset.get('variants', {}).values():
            target = ROOT / 'frontend/public' / variant['path'].lstrip('/')
            target.parent.mkdir(parents=True, exist_ok=True)
            with Image.open(source) as image:
                assert image.mode == 'RGBA' and image.getchannel('A').getextrema()[0] == 0, asset['source']
                width = min(variant['width'], image.width)
                height = round(image.height * width / image.width)
                resized = image.resize((width, height), Image.Resampling.LANCZOS)
            if check:
                if not target.is_file():
                    raise SystemExit(f'Missing runtime variant: {variant["path"]}')
                continue
            resized.save(target, 'WEBP', quality=variant.get('quality', 86), method=6, alpha_quality=100)
            dimensions = [target.stat().st_size, list(resized.size)]
            if variant.get('bytes') != dimensions[0] or variant.get('dimensions') != dimensions[1]:
                variant['bytes'] = dimensions[0]
                variant['dimensions'] = dimensions[1]
                changed = True
    if changed and not check:
        MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
    for asset in manifest['assets']:
        for variant in asset.get('variants', {}).values():
            print(f"{asset['name']}: {variant['path']} {variant.get('dimensions')} {variant.get('bytes')} bytes")
    print('Animation landscape runtime variants checked.' if check else 'Animation landscape runtime variants written.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Verify the recorded runtime files exist without rewriting them')
    build(parser.parse_args().check)

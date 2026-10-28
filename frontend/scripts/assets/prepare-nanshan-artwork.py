"""Export retained chapter illustrations with alpha and register runtime variants."""
import argparse
import json
from pathlib import Path
from PIL import Image

FRONTEND = Path(__file__).resolve().parents[2]
PUBLIC = FRONTEND / 'public'
parser = argparse.ArgumentParser()
parser.add_argument('--chapter', choices=['nanshan', 'xishan', 'beishan', 'dongshan', 'zhongshan'], default='nanshan')
chapter = parser.parse_args().chapter
SOURCE = FRONTEND / 'artwork-source' / chapter


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def write(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


optimized = read(FRONTEND / 'src/optimized-assets.json')
previews = read(FRONTEND / 'src/preview-assets.json')
refined = read(FRONTEND / 'src/refined-artwork.json')
artwork = read(PUBLIC / 'data/atlas/artwork-manifest.json')
generation = read(SOURCE / 'generation.json') if (SOURCE / 'generation.json').exists() else {'assets': []}
reader_manifest = SOURCE / 'reader-generation.json'
if reader_manifest.exists():
    generation['assets'] += read(reader_manifest)['assets']
entity_manifest = SOURCE / 'entities-generation.json'
if entity_manifest.exists():
    generation['assets'] += [asset for asset in read(entity_manifest)['assets'] if asset['status'] == 'reviewed']
destination = PUBLIC / 'data/atlas/myth-icons' / chapter
destination.mkdir(parents=True, exist_ok=True)
for asset in generation['assets']:
    if chapter in {'xishan', 'beishan', 'dongshan', 'zhongshan'} and asset.get('status') != 'reviewed':
        continue
    name = asset['name']
    source = SOURCE / asset.get('source_file', f'{name}-v1.png')
    original = Image.open(source)
    assert original.mode == 'RGBA' and original.getchannel('A').getextrema()[0] == 0, f'{name}: alpha required'
    variants = {}
    previous = next((item for item in artwork['assets'] if item.get('id') == f'{chapter}-{name}-v1'), None)
    sizes = [('full', 1280), ('card', 320), ('preview', 480), *([('map', 128)] if name == 'guanguan' else [])]
    fresh = previous and all((PUBLIC / previous['variants'][variant]['path'].lstrip('/')).exists() and (PUBLIC / previous['variants'][variant]['path'].lstrip('/')).stat().st_mtime >= source.stat().st_mtime for variant, edge in sizes)
    if fresh:
        variants = previous['variants']
    for variant, edge in [] if fresh else sizes:
        image = original.copy()
        image.thumbnail((edge, edge), Image.Resampling.LANCZOS)
        target = destination / f'{name}-v1{("-" + variant) if variant != "full" else ""}.webp'
        image.save(target, 'WEBP', quality=88, method=6, alpha_quality=100)
        variants[variant] = {'path': '/' + target.relative_to(PUBLIC).as_posix(), 'bytes': target.stat().st_size, 'dimensions': list(image.size)}
    base = variants['full']['path']
    optimized[base] = {'path': base, 'original_bytes': source.stat().st_size, 'optimized_bytes': variants['full']['bytes'],
                       'original_dimensions': list(original.size), 'dimensions': variants['full']['dimensions']}
    previews[base] = {key: variants[key] for key in ['card', 'preview']}
    if name == 'guanguan':
        refined[base] = {'map': variants['map']}
    id = f'{chapter}-{name}-v1'
    entry = {'id': id, 'tool': 'built-in image_gen', 'source_copy': source.relative_to(FRONTEND.parent).as_posix(),
             'destination': 'frontend/public' + base, 'initial_prompt': asset.get('initial_prompt', asset['prompt']),
             'reference_images': asset['reference_images'], 'status': f'reviewed_for_{chapter}_batch',
             'visual_review_note': asset['review_note'], 'variants': variants}
    if asset.get('revision_prompt'):
        entry['revision_prompt'] = asset['revision_prompt']
        entry['initial_reference_images'] = asset.get('initial_reference_images', [])
    artwork['assets'] = [item for item in artwork['assets'] if item.get('id') != id] + [entry]
    print(name, {key: value['bytes'] for key, value in variants.items()})
write(FRONTEND / 'src/optimized-assets.json', optimized)
write(FRONTEND / 'src/preview-assets.json', previews)
write(FRONTEND / 'src/refined-artwork.json', refined)
write(PUBLIC / 'data/atlas/artwork-manifest.json', artwork)

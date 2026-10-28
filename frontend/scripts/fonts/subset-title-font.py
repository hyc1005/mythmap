import argparse
import hashlib
import io
import json
import urllib.request
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.ttGlyphPen import TTGlyphPen

frontend = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser()
parser.add_argument('--source-font', type=Path)
args = parser.parse_args()
commit = '8b0a1d0f5983c89bc2b93f1b5fb55f9e252744b5'
source = f'https://raw.githubusercontent.com/google/fonts/{commit}/ofl/notoserifsc/'
characters = set(chr(code) for code in range(32, 127))


def collect(value, field=''):
    if isinstance(value, dict):
        for key, item in value.items():
            collect(item, key)
    elif isinstance(value, list):
        for item in value:
            collect(item, field)
    elif isinstance(value, str) and field in {'name', 'title', 'label'}:
        characters.update(value)
    elif isinstance(value, str):
        characters.update(c for c in value if 0x3400 <= ord(c) <= 0x4DBF or 0x20000 <= ord(c) <= 0x323AF)


for filename in ['myth-world.json', 'atlas/catalog.json', 'atlas/story-animations.json', 'atlas/kuafu-journey.json']:
    collect(json.loads((frontend / 'public/data' / filename).read_text(encoding='utf-8')))
characters.update(''.join(json.loads((frontend / 'src/locale-en.json').read_text(encoding='utf-8')).keys()))
font_bytes = args.source_font.read_bytes() if args.source_font else urllib.request.urlopen(source + 'NotoSerifSC%5Bwght%5D.ttf', timeout=60).read()
font = TTFont(io.BytesIO(font_bytes))
assert font['name'].getDebugName(1) == 'Noto Serif SC', 'Expected a licensed Noto Serif SC source'
print(f'Source: {font["name"].getDebugName(5)}; SHA256 {hashlib.sha256(font_bytes).hexdigest()}', flush=True)
instantiateVariableFont(font, {'wght': (400, 700)}, inplace=True)
supplements = [
    ('𤣎', '嬰', [('犭', (0.04, 0.30), None), ('嬰', (0.34, 0.97), None)]),
    ('𤛎', '敏', [('敏', (0.04, 0.96), (0.36, 0.84)), ('牛', (0.16, 0.86), (-0.06, 0.30))]),
]
for target, reference, components in supplements:
    if target not in characters or ord(target) in font.getBestCmap():
        continue
    glyphs = font.getGlyphSet(location={'wght': 400})
    pen = TTGlyphPen(glyphs)
    em = font['head'].unitsPerEm
    for character, (left, right), vertical in components:
        glyph = glyphs[font.getBestCmap()[ord(character)]]
        bounds = BoundsPen(glyphs)
        glyph.draw(bounds)
        x_min, y_min, x_max, y_max = bounds.bounds
        scale = (right - left) * em / (x_max - x_min)
        y_scale = (vertical[1] - vertical[0]) * em / (y_max - y_min) if vertical else 1
        y_offset = vertical[0] * em - y_min * y_scale if vertical else 0
        glyph.draw(TransformPen(pen, (scale, 0, 0, y_scale, left * em - x_min * scale, y_offset)))
    name = f'u{ord(target):X}.shanhai'
    font['glyf'][name] = pen.glyph()
    font['glyf'][name].recalcBounds(font['glyf'])
    font['hmtx'][name] = (em, font['glyf'][name].xMin)
    if 'vmtx' in font:
        font['vmtx'][name] = font['vmtx'][font.getBestCmap()[ord(reference)]]
    font.setGlyphOrder([*[g for g in font.getGlyphOrder() if g != name], name])
    for tag, maps in [('HVAR', ('AdvWidthMap', 'LsbMap', 'RsbMap')), ('VVAR', ('AdvHeightMap', 'TsbMap', 'BsbMap', 'VOrgMap'))]:
        if tag in font:
            for field in maps:
                mapping = getattr(font[tag].table, field, None)
                if mapping is not None:
                    mapping.mapping[name] = mapping.mapping[font.getBestCmap()[ord(reference)]]
    for table in font['cmap'].tables:
        if table.isUnicode() and table.format in (12, 13):
            table.cmap[ord(target)] = name
    print(f'Supplemented U+{ord(target):X} from verified components at weight 400', flush=True)
for glyph in font.getGlyphOrder():
    if glyph not in font['gvar'].variations:
        font['gvar'].variations[glyph] = []
options = subset.Options()
options.flavor = 'woff2'
options.name_IDs = ['*']
subsetter = subset.Subsetter(options=options)
subsetter.populate(unicodes={ord(character) for character in characters})
subsetter.subset(font)
font.flavor = 'woff2'
destination = frontend / 'public/fonts'
destination.mkdir(parents=True, exist_ok=True)
target = destination / 'shanhai-title.woff2'
font.save(target)
if not args.source_font:
    (destination / 'noto-serif-sc-LICENSE.txt').write_bytes(urllib.request.urlopen(source + 'OFL.txt', timeout=60).read())
assert (destination / 'noto-serif-sc-LICENSE.txt').is_file()
print(f'Title font: {len(characters)} requested characters, {target.stat().st_size:,} bytes; SIL OFL included')

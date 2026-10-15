import io
import json
import urllib.request
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

frontend = Path(__file__).resolve().parents[1]
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


for filename in ['myth-world.json', 'atlas/catalog.json', 'atlas/story-animations.json', 'atlas/kuafu-journey.json']:
    collect(json.loads((frontend / 'public/data' / filename).read_text(encoding='utf-8')))
characters.update(''.join(json.loads((frontend / 'src/locale-en.json').read_text(encoding='utf-8')).keys()))
font = TTFont(io.BytesIO(urllib.request.urlopen(source + 'NotoSerifSC%5Bwght%5D.ttf').read()))
instantiateVariableFont(font, {'wght': (400, 700)}, inplace=True)
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
(destination / 'noto-serif-sc-LICENSE.txt').write_bytes(urllib.request.urlopen(source + 'OFL.txt').read())
print(f'Title font: {len(characters)} requested characters, {target.stat().st_size:,} bytes; SIL OFL included')

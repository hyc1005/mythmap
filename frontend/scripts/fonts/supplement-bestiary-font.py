import argparse
import hashlib
import io
import json
import re
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import ProxyHandler, Request, build_opener

from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser()
parser.add_argument('--proxy')
args = parser.parse_args()
target = ROOT / 'public/fonts/shanhai-bestiary.woff2'
metadata = json.loads((ROOT / 'src/bestiary-metadata.json').read_text(encoding='utf-8'))
text = ''.join(item['display_name']['zh'] + item['qualifier']['zh'] for item in metadata.values())
for name in ['bestiary.js', 'components/Bestiary.jsx']:
    text += (ROOT / 'src' / name).read_text(encoding='utf-8')
covered = set()
for path in (ROOT / 'public/fonts').glob('*.woff2'):
    if path != target:
        with TTFont(path) as font:
            covered.update(font.getBestCmap())
characters = ''.join(sorted({c for c in text if (0x3400 <= ord(c) <= 0x9fff or 0x20000 <= ord(c) <= 0x323af) and ord(c) not in covered}))
assert characters, 'No additional bestiary glyphs required'


def fetch(url):
    opener = build_opener(ProxyHandler({'http': args.proxy, 'https': args.proxy})) if args.proxy else build_opener()
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'})
    with opener.open(request, timeout=30) as response:
        return response.read()


url = 'https://fonts.googleapis.com/css2?' + urlencode({'family': 'Noto Serif SC:wght@400..700', 'text': characters, 'display': 'swap'})
css = fetch(url).decode()
font_url = re.search(r'src: url\((https://fonts.gstatic.com/[^)]+)\)', css)[1]
data = fetch(font_url)
font = TTFont(io.BytesIO(data))
assert font.flavor == 'woff2'
assert font['name'].getDebugName(1).startswith('Noto Serif SC')
assert set(map(ord, characters)) <= set(font.getBestCmap())
axis = next(axis for axis in font['fvar'].axes if axis.axisTag == 'wght')
assert axis.minValue <= 400 and axis.maxValue >= 700
assert (ROOT / 'public/fonts/noto-serif-sc-LICENSE.txt').is_file()
target.write_bytes(data)
style_path = ROOT / 'src/styles/myth-world.css'
style = re.sub(r'@font-face\s*\{[^}]*shanhai-bestiary\.woff2[^}]*\}\s*', '', style_path.read_text(encoding='utf-8'))
rule = '@font-face { font-family: ShanhaiRare; font-style: normal; font-weight: 400 700; font-display: swap; src: url(/fonts/shanhai-bestiary.woff2) format("woff2"); unicode-range: ' + ', '.join('U+' + format(ord(c), 'X') for c in characters) + '; }\n'
style_path.write_text(rule + style, encoding='utf-8')
print(f'Bestiary Noto Serif SC 400–700: {len(characters)} glyphs, {len(data)} bytes, SHA256 {hashlib.sha256(data).hexdigest()}')
print('Characters:', characters)
print('Source:', font_url)
print('License: frontend/public/fonts/noto-serif-sc-LICENSE.txt')

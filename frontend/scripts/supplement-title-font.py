"""Retain licensed Noto title glyphs added by the Northern batches."""
import hashlib
import io
import re
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[1]
CHARACTERS = '單机華漨求䑏䟽何儵孟寓帶彭栢椐橐虢譙駝鰼䑕幽張杠極樗熏聮葵蔓薤訾雘韭鴳鵁鵺䐆㗸侯匠柘潘磁竦薨那韓題鮭鳲䰽䲃刚夕懐枳渾瀤獄窫鮨鴈'
url = 'https://fonts.googleapis.com/css2?' + urlencode({
    'family': 'Noto Serif SC:wght@400..700', 'text': CHARACTERS, 'display': 'swap'})
agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
css = urlopen(Request(url, headers={'User-Agent': agent}), timeout=30).read().decode()
font_url = re.search(r'src: url\((https://fonts.gstatic.com/[^)]+)\)', css).group(1)
data = urlopen(font_url, timeout=30).read()
font = TTFont(io.BytesIO(data))
assert font['name'].getDebugName(1).startswith('Noto Serif SC')
assert {ord(c) for c in CHARACTERS} <= set(font.getBestCmap()), sorted({ord(c) for c in CHARACTERS} - set(font.getBestCmap()))
axis = next(a for a in font['fvar'].axes if a.axisTag == 'wght')
assert axis.minValue <= 400 and axis.maxValue >= 700
assert (ROOT / 'public/fonts/noto-serif-sc-LICENSE.txt').is_file()
target = ROOT / 'public/fonts/shanhai-title-beishan.woff2'
assert font.flavor == 'woff2'
target.write_bytes(data)
print(f'Noto Serif SC 400–700: {CHARACTERS}; {len(data)} bytes; SHA256 {hashlib.sha256(data).hexdigest()}')
print('Source:', font_url)

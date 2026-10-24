"""Build the licensed five-glyph Northern supplement entirely in memory."""
import hashlib
import io
from pathlib import Path
from urllib.request import urlopen
from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://github.com/babelstone/babelstonehan-ufo/releases/download/v18.0.1/'
CHARACTERS = '𤟤𤠾𥬇𬋩𭥍'
license_text = urlopen(BASE + 'LICENSE', timeout=60).read().decode('utf-8')
assert 'Arphic' in license_text and '1999' in license_text
data = urlopen(BASE + 'BabelStoneHanExtra.ttf', timeout=60).read()
print('Downloaded upstream TTF in memory:', len(data), flush=True)
font = TTFont(io.BytesIO(data))
assert set(map(ord, CHARACTERS)) <= set(font.getBestCmap())
options = subset.Options()
options.layout_features = []
options.layout_closure = False
options.drop_tables += ['GSUB', 'GPOS', 'GDEF', 'BASE', 'JSTF']
options.name_IDs = ['*']
options.name_legacy = True
worker = subset.Subsetter(options=options)
worker.populate(unicodes=list(map(ord, CHARACTERS)))
worker.subset(font)
for record in font['name'].names:
    if record.nameID in {1, 3, 4, 6, 16}:
        value = 'AtlasNorthernExtB' if record.nameID == 6 else 'Atlas Northern ExtB'
        record.string = value.encode(record.getEncoding())
    elif record.nameID in {2, 17}:
        record.string = 'Regular'.encode(record.getEncoding())
font.flavor = 'woff2'
target = ROOT / 'public/fonts/atlas-northern-extb.woff2'
font.save(target)
assert set(map(ord, CHARACTERS)) <= set(TTFont(target).getBestCmap())
(ROOT / 'public/fonts/atlas-northern-extb-LICENSE.txt').write_text(
    'Atlas Northern ExtB: five-glyph subset, renamed by the Shan-hai Atlas project.\n'
    'Upstream: BabelStone Han Extra v18.0.1, ' + BASE + '\n'
    'Modified by subsetting and renaming; original copyright and license retained.\n\n'
    + license_text, encoding='utf-8')
print('ExtB:', CHARACTERS, target.stat().st_size, 'bytes; SHA256', hashlib.sha256(target.read_bytes()).hexdigest())
print('Upstream SHA256:', hashlib.sha256(data).hexdigest())

"""Build the licensed rare-character fallback without retaining a full font download."""
import io
import json
import zipfile
from pathlib import Path
from urllib.request import urlopen
from fontTools import subset
from fontTools.ttLib import TTFont

root = Path(__file__).resolve().parents[1] / 'public' / 'fonts'
url = 'https://www.babelstone.co.uk/Fonts/Download/BabelStoneHan-16.0.3.zip'
with urlopen(url, timeout=120) as response:
    archive = zipfile.ZipFile(io.BytesIO(response.read()))
font = TTFont(io.BytesIO(archive.read('BabelStoneHan.ttf')))
license_text = '\n\n'.join(dict.fromkeys(n.toUnicode() for n in font['name'].names if n.nameID in (0, 13, 14)))
assert 'Arphic' in license_text
options = subset.Options()
options.name_IDs = ['*']
subsetter = subset.Subsetter(options=options)
world_text = json.dumps(json.loads((root.parents[1] / 'public/data/myth-world.json').read_text(encoding='utf-8')), ensure_ascii=False)
characters = {ord(c) for c in world_text if 0x3400 <= ord(c) <= 0x4DBF or ord(c) >= 0x20000}
missing = characters - set(font.getBestCmap())
assert not missing, f'Unsupported rare characters: {[hex(c) for c in missing]}'
subsetter.populate(unicodes=characters)
subsetter.subset(font)
assert {0x2A2A8, 0x4A3C} <= set(font.getBestCmap())
names = {1: 'Shanhai Rare', 2: 'Regular', 3: 'ShanhaiRare-20261019', 4: 'Shanhai Rare', 6: 'ShanhaiRare', 16: 'Shanhai Rare', 17: 'Regular'}
for record in font['name'].names:
    if record.nameID in names:
        record.string = names[record.nameID].encode(record.getEncoding())
font.flavor = 'woff2'
font.save(root / 'shanhai-rare.woff2')
(root / 'ShanhaiRare-LICENSE.txt').write_text('Shanhai Rare: rare-character subset of BabelStone Han 16.0.3.\nModified by the Shanhai Atlas project, 2026-10-19; renamed and subset only.\nSource: ' + url + '\nPublisher: https://www.babelstone.co.uk/Fonts/Han.html\n\n' + license_text, encoding='utf-8')
print('Rare font:', (root / 'shanhai-rare.woff2').stat().st_size, 'bytes')

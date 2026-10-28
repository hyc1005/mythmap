"""Build the licensed seventeen-glyph Northern supplement entirely in memory."""
import hashlib
import io
import subprocess
from pathlib import Path
from urllib.request import urlopen
from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[2]
BASE = 'https://github.com/babelstone/babelstonehan-ufo/releases/download/v18.0.1/'
CHARACTERS = '𤟤𤠾𥬇𬋩𭥍𤓰𤞞𩣡𪄀𪃑𣵀𩹴𬐱𪄶𤍠𣸦𨹧'
license_text = urlopen(BASE + 'LICENSE', timeout=60).read().decode('utf-8')
assert 'Arphic' in license_text and '1999' in license_text
data = urlopen(BASE + 'BabelStoneHanExtra.ttf', timeout=60).read()
assert hashlib.sha256(data).hexdigest()=='cc8868109070c1813479dc2eb72fba508a1a6c33d807a485959e8f5dcd0e5724'
print('Downloaded upstream TTF in memory:', len(data), flush=True)
font = TTFont(io.BytesIO(data))
extra_characters=set(map(ord,CHARACTERS)) & set(font.getBestCmap())
options = subset.Options()
options.layout_features = []
options.layout_closure = False
options.drop_tables += ['GSUB', 'GPOS', 'GDEF', 'BASE', 'JSTF']
options.name_IDs = ['*']
options.name_legacy = True
worker = subset.Subsetter(options=options)
worker.populate(unicodes=extra_characters)
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
    'Atlas Northern ExtB: seventeen-glyph subset, renamed by the Shan-hai Atlas project.\n'
    'Upstream: BabelStone Han Extra v18.0.1, ' + BASE + '\n'
    'Modified by subsetting and renaming; original copyright and license retained.\n\n'
    + license_text, encoding='utf-8')
print('ExtB:', CHARACTERS, target.stat().st_size, 'bytes; SHA256', hashlib.sha256(target.read_bytes()).hexdigest())
print('Upstream SHA256:', hashlib.sha256(data).hexdigest())

# This edition character is absent from the BabelStone subset source.
HANAMIN = 'https://raw.githubusercontent.com/googlefonts/chinese/gh-pages/fonts/HanaMin/'
hana_license = urlopen(HANAMIN+'LICENSE.txt',timeout=60).read().decode('utf-8').replace('\r\n','\n').replace('\r','\n')
hana_license='\n'.join(line.rstrip() for line in hana_license.splitlines())+'\n'
assert 'Unlimited permission' in hana_license and 'Hanazono' in hana_license
hana_data=subprocess.check_output(['rtk','proxy','curl.exe','--fail','--location','--retry','2','--connect-timeout','15','--max-time','90','--silent',HANAMIN+'HanaMinB.ttf'])
assert hashlib.sha256(hana_data).hexdigest()=='829543436cdf7b4c6730e2af5806fa406f8ddf0d4b656e0cd49c58d4db1c8d3c'
hana=TTFont(io.BytesIO(hana_data))
assert ord('𨜰') in hana.getBestCmap()
hana_worker=subset.Subsetter(options=options)
hana_worker.populate(unicodes=[ord('𨜰')]);hana_worker.subset(hana)
for record in hana['name'].names:
    if record.nameID in {1,3,4,6,16}:
        value='AtlasNorthernTan' if record.nameID==6 else 'Atlas Northern Tan'
        record.string=value.encode(record.getEncoding())
hana.flavor='woff2'
hana_target=ROOT/'public/fonts/atlas-northern-tan.woff2'
hana.save(hana_target)
(ROOT/'public/fonts/atlas-northern-tan-LICENSE.txt').write_text(
    'Atlas Northern Tan: single-glyph subset for U+28730, renamed by the Shan-hai Atlas project.\n'
    'Source: '+HANAMIN+'HanaMinB.ttf\nModified by subsetting and renaming; original copyright and license retained.\n\n'+hana_license,encoding='utf-8',newline='\n')
print('Tan font:',hana_target.stat().st_size,'bytes; SHA256',hashlib.sha256(hana_target.read_bytes()).hexdigest())
print('HanaMinB upstream SHA256:',hashlib.sha256(hana_data).hexdigest())

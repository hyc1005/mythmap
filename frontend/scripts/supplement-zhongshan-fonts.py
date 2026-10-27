"""Bundle licensed font subsets for the implemented Central reader text."""
import argparse
import hashlib
import io
import json
import re
import subprocess
import zipfile
from pathlib import Path
from urllib.parse import urlencode
from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser()
parser.add_argument('--proxy')
args = parser.parse_args()


def fetch(url, timeout=60):
    cmd = ['curl.exe', '--ssl-revoke-best-effort', '--fail', '--location', '--connect-timeout', '25', '--max-time', str(timeout), '--silent', '--show-error', '--user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36']
    if args.proxy:
        cmd += ['--proxy', args.proxy]
    for attempt in range(4):
        result = subprocess.run([*cmd, url], capture_output=True)
        if result.returncode == 0:
            return result.stdout
    raise RuntimeError(result.stderr.decode(errors='replace'))


world = json.loads((ROOT / 'frontend/public/data/myth-world.json').read_text(encoding='utf-8'))
entries = [e for values in world.values() if isinstance(values, list) for e in values if isinstance(e, dict) and e.get('content_batch', '').startswith('zhongshan-')]
text = ''.join(str(e.get(k, '')) for e in entries for k in ['name', 'description', 'quote', 'commentary_quote', 'content_note', 'editorial_note', 'artwork_caption'])
bundled = set()
for path in (ROOT / 'frontend/public/fonts').glob('*.woff2'):
    if path.name not in {'shanhai-title-zhongshan.woff2', 'atlas-central-rare.woff2', 'atlas-central-exth.woff2'}:
        bundled.update(TTFont(path).getBestCmap())
missing = sorted({c for c in text if (0x3400 <= ord(c) <= 0x9fff or 0x20000 <= ord(c) <= 0x323af) and (ord(c) not in bundled or ord(c) > 0xffff)})
TITLE = ''.join(c for c in missing if ord(c) <= 0xffff)
RARE = ''.join(c for c in missing if 0xffff < ord(c) < 0x30000)
EXTENDED = ''.join(c for c in missing if ord(c) >= 0x30000)
assert TITLE and RARE
url = 'https://fonts.googleapis.com/css2?' + urlencode({'family': 'Noto Serif SC:wght@400..700', 'text': TITLE, 'display': 'swap'})
css = fetch(url).decode()
font_url = re.search(r'src: url\((https://fonts.gstatic.com/[^)]+)\)', css)[1]
data = fetch(font_url); font = TTFont(io.BytesIO(data))
if not set(map(ord, TITLE)) <= set(font.getBestCmap()):
    font_url = 'https://raw.githubusercontent.com/notofonts/noto-cjk/main/Serif/Variable/TTF/Subset/NotoSerifSC-VF.ttf'
    font = TTFont(io.BytesIO(fetch(font_url, timeout=300)))
    assert set(map(ord, TITLE)) <= set(font.getBestCmap()), ''.join(c for c in TITLE if ord(c) not in font.getBestCmap())
    title_options = subset.Options()
    title_worker = subset.Subsetter(options=title_options)
    title_worker.populate(unicodes=list(map(ord, TITLE))); title_worker.subset(font)
    font.flavor = 'woff2'; title_buffer = io.BytesIO(); font.save(title_buffer); data = title_buffer.getvalue()
assert any(a.axisTag == 'wght' and a.minValue <= 400 and a.maxValue >= 700 for a in font['fvar'].axes)
target = ROOT / 'frontend/public/fonts/shanhai-title-zhongshan.woff2'
target.write_bytes(data)
print('Central Noto subset', len(TITLE), len(data), flush=True)
source_url = 'https://raw.githubusercontent.com/googlefonts/chinese/gh-pages/fonts/HanaMin/HanaMinB.ttf'
source = fetch(source_url, timeout=300)
source_sha = hashlib.sha256(source).hexdigest()
assert len(source) == 30739236 and source_sha == '829543436cdf7b4c6730e2af5806fa406f8ddf0d4b656e0cd49c58d4db1c8d3c', (len(source), source_sha)
assert hashlib.sha1(b'blob ' + str(len(source)).encode() + b'\0' + source).hexdigest() == '81c4df21cdbd2570fa92ac55c04b02198c4bf692'
rare = TTFont(io.BytesIO(source)); assert set(map(ord, RARE)) <= set(rare.getBestCmap())
options = subset.Options(); options.layout_features = []; options.layout_closure = False
options.drop_tables += ['GSUB', 'GPOS', 'GDEF', 'BASE', 'JSTF']; options.name_IDs = ['*']; options.name_legacy = True
worker = subset.Subsetter(options=options); worker.populate(unicodes=list(map(ord, RARE))); worker.subset(rare)
for record in rare['name'].names:
    if record.nameID in {1, 3, 4, 6, 16}:
        value = 'AtlasCentralRare' if record.nameID == 6 else 'Atlas Central Rare'
        record.string = value.encode(record.getEncoding())
rare.flavor = 'woff2'; rare_target = ROOT / 'frontend/public/fonts/atlas-central-rare.woff2'; rare.save(rare_target)
license_text = (ROOT / 'frontend/public/fonts/atlas-eastern-rare-LICENSE.txt').read_text(encoding='utf-8').split('\n\n', 1)[1]
assert 'Unlimited permission' in license_text and 'Hanazono' in license_text
(ROOT / 'frontend/public/fonts/atlas-central-rare-LICENSE.txt').write_text('Atlas Central Rare: Central subset, renamed by the Shan-hai Atlas project.\nSource: ' + source_url + '\nModified by subsetting and renaming; original copyright and license retained.\n\n' + license_text, encoding='utf-8', newline='\n')
assert set(map(ord, RARE)) == set(TTFont(rare_target).getBestCmap())
extended_record = None
if EXTENDED:
    extended_url = 'https://www.babelstone.co.uk/Fonts/Download/BabelStoneHan-16.0.3.zip'
    archive_bytes = fetch(extended_url, timeout=300)
    archive = zipfile.ZipFile(io.BytesIO(archive_bytes))
    font_name = next(n for n in archive.namelist() if n.endswith('BabelStoneHan.ttf'))
    extended = TTFont(io.BytesIO(archive.read(font_name)))
    assert set(map(ord, EXTENDED)) <= set(extended.getBestCmap())
    license_url = 'https://ftp.gnu.org/non-gnu/chinese-fonts-truetype/LICENSE'
    license_text = fetch(license_url).decode('utf-8-sig')
    assert 'ARPHIC' in license_text.upper() and 'PUBLIC LICENSE' in license_text.upper()
    worker = subset.Subsetter(options=options); worker.populate(unicodes=list(map(ord, EXTENDED))); worker.subset(extended)
    for record in extended['name'].names:
        if record.nameID in {1, 3, 4, 6, 16}:
            value = 'AtlasCentralExtH' if record.nameID == 6 else 'Atlas Central ExtH'
            record.string = value.encode(record.getEncoding())
    extended.flavor = 'woff2'; extended_target = ROOT / 'frontend/public/fonts/atlas-central-exth.woff2'; extended.save(extended_target)
    extended_license = ROOT / 'frontend/public/fonts/atlas-central-exth-LICENSE.txt'
    extended_license.write_text('Atlas Central ExtH: subset and renamed from BabelStone Han 16.0.3.\nSource: ' + extended_url + '\nOriginal Arphic Public License and copyright retained.\n\n' + license_text, encoding='utf-8')
    extended_record = dict(family='Atlas Central ExtH', characters=EXTENDED, weights=[400], path=extended_target.relative_to(ROOT).as_posix(), license=extended_license.relative_to(ROOT).as_posix(), source_url=extended_url, upstream_sha256=hashlib.sha256(archive_bytes).hexdigest(), sha256=hashlib.sha256(extended_target.read_bytes()).hexdigest(), limits='独立授权与字体族；静态400字形，600沿用400，禁用伪粗。')
    bundled.update(extended.getBestCmap())
for name in ['exploration', 'myth-world']:
    path = ROOT / 'frontend/src/styles' / (name + '.css'); style = path.read_text(encoding='utf-8')
    family = "'Shanhai Title'" if name == 'exploration' else 'ShanhaiRare'
    header = "@font-face { font-family: 'Atlas Central Rare'; font-style: normal; font-weight: 400; font-display: swap; src: url(/fonts/atlas-central-rare.woff2) format(\"woff2\"); unicode-range: " + ', '.join('U+' + format(ord(c), 'X') for c in RARE) + '; }\n'
    header += '@font-face { font-family: ' + family + '; font-style: normal; font-weight: 400 700; font-display: swap; src: url(/fonts/shanhai-title-zhongshan.woff2) format("woff2"); unicode-range: ' + ', '.join('U+' + format(ord(c), 'X') for c in TITLE) + '; }\n'
    if EXTENDED:
        header = "@font-face { font-family: 'Atlas Central ExtH'; font-style: normal; font-weight: 400; font-display: swap; src: url(/fonts/atlas-central-exth.woff2) format(\"woff2\"); unicode-range: " + ', '.join('U+' + format(ord(c), 'X') for c in EXTENDED) + '; }\n' + header
    style = re.sub(r'@font-face\s*\{[^}]*?(?:atlas-central-rare|atlas-central-exth|shanhai-title-zhongshan)\.woff2[^}]*\}\s*', '', style)
    style = re.sub(r"@font-face\s*\{[^}]*font-family: 'Atlas Central Rare';[^}]*shanhai-rare\.woff2[^}]*\}\s*", '', style)
    if "font-family: 'Atlas Central Rare'," not in style:
        style = style.replace("font-family: 'Atlas Eastern Rare',", "font-family: 'Atlas Central Rare', 'Atlas Eastern Rare',")
    if EXTENDED and "font-family: 'Atlas Central ExtH'," not in style:
        style = style.replace("font-family: 'Atlas Central Rare',", "font-family: 'Atlas Central ExtH', 'Atlas Central Rare',")
    path.write_text(header + style, encoding='utf-8')
review_path = ROOT / 'data/zhongshan-edition-review.json'; review = json.loads(review_path.read_text(encoding='utf-8'))
review['font_supplements'] = [
    dict(family='Shanhai Title', source_family='Noto Serif SC', characters=TITLE, weights=[400, 700], path=target.relative_to(ROOT).as_posix(), license='frontend/public/fonts/noto-serif-sc-LICENSE.txt', source_url=font_url, sha256=hashlib.sha256(data).hexdigest()),
    dict(family='Atlas Central Rare', characters=RARE, weights=[400], path=rare_target.relative_to(ROOT).as_posix(), license='frontend/public/fonts/atlas-central-rare-LICENSE.txt', source_url=source_url, upstream_sha256=source_sha, upstream_git_blob='81c4df21cdbd2570fa92ac55c04b02198c4bf692', sha256=hashlib.sha256(rare_target.read_bytes()).hexdigest(), limits='独立字体族优先回退，静态400字形；600沿用400且禁用伪粗，不复制系统字体。')]
if extended_record:
    review['font_supplements'].append(extended_record)
bundled.update(font.getBestCmap()); bundled.update(TTFont(rare_target).getBestCmap())
preflight = review['font_preflight']; preflight.setdefault('initial_missing_stage_title_characters', preflight['missing_stage_title_characters'])
preflight['missing_stage_title_characters'] = ''.join(sorted({c for s in review['stage_plan'] for c in re.sub(r'⟦缺字图:([^⟧]+)⟧', r'\1', s['name']) if ord(c) not in bundled}))
preflight['missing_stage_title_count'] = len(preflight['missing_stage_title_characters'])
preflight['implemented_batch_missing_characters'] = ''.join(c for c in missing if ord(c) not in bundled)
assert not preflight['implemented_batch_missing_characters']
preflight.update(status='fully_covered' if not review['remaining_stages'] else 'current_batch_covered_future_pending', limits=f'已接入前{review["implemented_stages"]}阶段标题、实体、正文与郭注所需字已补；后续{review["remaining_stages"]}阶段完整内容仍需逐批预检。')
review_path.write_text(json.dumps(review, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('Central rare subset', len(RARE), 'characters', rare_target.stat().st_size, 'future title gaps', preflight['missing_stage_title_count'], flush=True)

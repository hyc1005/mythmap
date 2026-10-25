"""Build the two licensed opening-batch Eastern font subsets."""
import hashlib
import io
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from fontTools import subset
from fontTools.ttLib import TTFont

ROOT=Path(__file__).resolve().parents[1]
TITLE='㐨䎶䖪䖺䗤䚯亝亦似低借傳兒則勃占卡厚叩叫吟否呉呼咨圆堪妺姿尔弯從手拆拟捕損擅改斗旱旻昧曹植樕活涯添減湣漠激濼炭為犂犬犲狪猪獠琴瑟環番疗疫疾癰矿社祈科箴细羸胫腫膜臨蓋藟蚪蛙蝌蝠血裂見詨謂跨躯軨針针雅靈頰颗额餌鱅鱤鳍鳞鳴鸣鼻'
RARE='𣲵𧑤'
url='https://fonts.googleapis.com/css2?'+urlencode({'family':'Noto Serif SC:wght@400..700','text':TITLE,'display':'swap'})
agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
css=urlopen(Request(url,headers={'User-Agent':agent}),timeout=30).read().decode()
font_url=re.search(r'src: url\((https://fonts.gstatic.com/[^)]+)\)',css).group(1)
data=urlopen(font_url,timeout=30).read()
font=TTFont(io.BytesIO(data))
assert set(map(ord,TITLE))<=set(font.getBestCmap())
assert any(a.axisTag=='wght' and a.minValue<=400 and a.maxValue>=700 for a in font['fvar'].axes)
target=ROOT/'public/fonts/shanhai-title-dongshan.woff2'
target.write_bytes(data)
print('Eastern title font',len(TITLE),len(data),hashlib.sha256(data).hexdigest(),flush=True)
BASE='https://raw.githubusercontent.com/googlefonts/chinese/gh-pages/fonts/HanaMin/'
license_text=urlopen(BASE+'LICENSE.txt',timeout=60).read().decode('utf-8')
license_text='\n'.join(line.rstrip() for line in license_text.splitlines())+'\n'
assert 'Unlimited permission' in license_text and 'Hanazono' in license_text
source=subprocess.check_output(['rtk','proxy','curl.exe','--fail','--location','--retry','2','--connect-timeout','15','--max-time','90','--silent',BASE+'HanaMinB.ttf'])
assert hashlib.sha256(source).hexdigest()=='829543436cdf7b4c6730e2af5806fa406f8ddf0d4b656e0cd49c58d4db1c8d3c'
rare=TTFont(io.BytesIO(source))
assert set(map(ord,RARE))<=set(rare.getBestCmap())
options=subset.Options();options.layout_features=[];options.layout_closure=False
options.drop_tables+=['GSUB','GPOS','GDEF','BASE','JSTF'];options.name_IDs=['*'];options.name_legacy=True
worker=subset.Subsetter(options=options);worker.populate(unicodes=list(map(ord,RARE)));worker.subset(rare)
for record in rare['name'].names:
    if record.nameID in {1,3,4,6,16}:
        value='AtlasEasternRare' if record.nameID==6 else 'Atlas Eastern Rare'
        record.string=value.encode(record.getEncoding())
rare.flavor='woff2'
rare_target=ROOT/'public/fonts/atlas-eastern-rare.woff2';rare.save(rare_target)
(ROOT/'public/fonts/atlas-eastern-rare-LICENSE.txt').write_text(
    'Atlas Eastern Rare: Eastern subset, renamed by the Shan-hai Atlas project.\n'
    'Source: '+BASE+'HanaMinB.ttf\nModified by subsetting and renaming; original copyright and license retained.\n\n'+license_text,encoding='utf-8',newline='\n')
assert set(map(ord,RARE))==set(TTFont(rare_target).getBestCmap())
for name in ['exploration','myth-world']:
    p=ROOT/'src/styles'/f'{name}.css';s=p.read_text(encoding='utf-8')
    family="'Shanhai Title'" if name=='exploration' else 'ShanhaiRare'
    header="@font-face { font-family: 'Atlas Eastern Rare'; font-style: normal; font-weight: 400; font-display: swap; src: url(/fonts/atlas-eastern-rare.woff2) format(\"woff2\"); unicode-range: "+', '.join('U+'+format(ord(c),'X') for c in RARE)+"; }\n"
    header+="@font-face { font-family: "+family+"; font-style: normal; font-weight: 400 700; font-display: swap; src: url(/fonts/shanhai-title-dongshan.woff2) format(\"woff2\"); unicode-range: "+', '.join('U+'+format(ord(c),'X') for c in TITLE)+"; }\n"
    s=re.sub(r'@font-face\s*\{[^}]*?(?:atlas-eastern-rare|shanhai-title-dongshan)\.woff2[^}]*\}\s*','',s)
    s=header+s
    if "font-family: 'Atlas Eastern Rare'," not in s:s=s.replace("font-family: 'Atlas Northern Tan',","font-family: 'Atlas Eastern Rare', 'Atlas Northern Tan',")
    p.write_text(s,encoding='utf-8')
path=ROOT.parent/'data/dongshan-edition-review.json';review=json.loads(path.read_text(encoding='utf-8'))
review['font_supplements']=[
dict(family='Shanhai Title',source_family='Noto Serif SC',characters=TITLE,weights=[400,700],path='frontend/public/fonts/shanhai-title-dongshan.woff2',license='frontend/public/fonts/noto-serif-sc-LICENSE.txt',source_url=url,sha256=hashlib.sha256(data).hexdigest()),
dict(family='Atlas Eastern Rare',characters=RARE,weights=[400],path='frontend/public/fonts/atlas-eastern-rare.woff2',license='frontend/public/fonts/atlas-eastern-rare-LICENSE.txt',source_url=BASE+'HanaMinB.ttf',upstream_sha256=hashlib.sha256(source).hexdigest(),sha256=hashlib.sha256(rare_target.read_bytes()).hexdigest(),limits='独立字体族优先回退，静态400字形，600显示沿用400且禁用伪粗；不复制系统字体。')]
bundled=set()
for font_path in (ROOT/'public/fonts').glob('*.woff2'):bundled.update(TTFont(font_path).getBestCmap())
preflight=review['font_preflight']
preflight.setdefault('initial_missing_stage_title_characters',preflight['missing_stage_title_characters'])
preflight['missing_stage_title_characters']=''.join(sorted({c for stage in review['stage_plan'] for c in stage['name'] if ord(c) not in bundled}))
preflight['missing_stage_title_count']=len(preflight['missing_stage_title_characters'])
preflight['status']='current_batch_covered_future_pending'
review['font_preflight']['implemented_batch_missing_characters']=''
review['font_preflight']['limits']='前15阶段标题及所需字已补；后续36阶段的完整实体和注文仍需逐批预检。'
path.write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Eastern rare font',len(RARE),rare_target.stat().st_size,hashlib.sha256(rare_target.read_bytes()).hexdigest(),flush=True)

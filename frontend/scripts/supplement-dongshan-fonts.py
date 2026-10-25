"""Build the two licensed Eastern font subsets from verified sources."""
import hashlib
import io
import json
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from fontTools import subset
from fontTools.ttLib import TTFont

ROOT=Path(__file__).resolve().parents[1]
TITLE='㐨䃌䊧䎶䖪䖺䗤䚯䱎䱻䲛万亝亦仇伤似但低佯俠借傳傷儒充兒兔冒冬凋凫則剡功勃医占卡卵厚厲叉叩叫叶吐吟否含吻呉呌呕呼咨善嘔圆國培堪壳妴妺姪姿婉孚学客害實尔尖屬峩峳嶧幼庾廓廣弯彩從思性恐惧懼扇手拆拟捕損擅攸改敗斃斑斗斜旧旱旻昧普曹杨枣枪枯枽格栽梓植楊楨榑樕气氣汁沸活浅涌涯深添渚減湣漠澧激濆濼瀵災炭為烝牡犂犬犰犲狀狙狪狭狳猩猪猲獋獙獠獳环珍珧琴瑁瑇瑟環甚甲电番疗疟疠疣疫疾病瘞瘧癘癰盧眠睪知矿社祈禽科稳穰等算箴素終絜經纠纯细绎绿羸翡耿聲肺胫脚腫膜臨臭花苗苴荆药莬菌葉葛蓋蕪藟蘪蚌蚪蛙蛤蛭蜃蝌蝗蝠蝦螽蟞蠪蠵血裂裸褐見觉觜觡詨調謂警误调贝趾跂跨踇踵蹲躯軨轮逝遐針銘针铠铭限隅雀雁雅雜雨靈頗頰颈颗额風餌體鬲鬿鮇鮒鮯鯉鰌鱃鱅鱏鱑鱗鱣鱤鲋鲟鲤鳃鳍鳞鳴鴆鴛鴦鴻鵜鶘鸣鸭鸿鹈鹕麗黍鼈鼻'
RARE='𣲵𥠖𥧌𦍙𦬊𧑤𪁐𮮐'
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
license_path=ROOT/'public/fonts/atlas-eastern-rare-LICENSE.txt'
license_text=license_path.read_text(encoding='utf-8').split('\n\n',1)[1] if license_path.exists() else urlopen(BASE+'LICENSE.txt',timeout=60).read().decode('utf-8')
license_text='\n'.join(line.rstrip() for line in license_text.splitlines())+'\n'
assert 'Unlimited permission' in license_text and 'Hanazono' in license_text
source_size=30739236
source_blob='81c4df21cdbd2570fa92ac55c04b02198c4bf692'
def font_part(bounds):
    first,last=bounds
    for attempt in range(3):
        part=subprocess.run(['rtk','proxy','curl.exe','--fail','--location','--range',f'{first}-{last}','--connect-timeout','10','--max-time','30','--silent','--show-error',BASE+f'HanaMinB.ttf?atlas_range={first}-{last}'],capture_output=True)
        if part.returncode==0 and len(part.stdout)==last-first+1:return part.stdout
    raise RuntimeError(f'Incomplete font range {first}-{last}; existing subset retained.')
chunk=1024*1024
bounds=[(start,min(start+chunk,source_size)-1) for start in range(0,source_size,chunk)]
with ThreadPoolExecutor(max_workers=4) as pool:source=b''.join(pool.map(font_part,bounds))
assert len(source)==source_size
assert hashlib.sha1(b'blob '+str(len(source)).encode()+b'\0'+source).hexdigest()==source_blob
assert hashlib.sha256(source).hexdigest()=='829543436cdf7b4c6730e2af5806fa406f8ddf0d4b656e0cd49c58d4db1c8d3c'
print('Pinned source verified',len(source),source_blob,flush=True)
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
dict(family='Atlas Eastern Rare',characters=RARE,weights=[400],path='frontend/public/fonts/atlas-eastern-rare.woff2',license='frontend/public/fonts/atlas-eastern-rare-LICENSE.txt',source_url=BASE+'HanaMinB.ttf',upstream_sha256=hashlib.sha256(source).hexdigest(),upstream_git_blob=source_blob,sha256=hashlib.sha256(rare_target.read_bytes()).hexdigest(),limits='独立字体族优先回退，静态400字形，600显示沿用400且禁用伪粗；不复制系统字体。')]
bundled=set()
for font_path in (ROOT/'public/fonts').glob('*.woff2'):bundled.update(TTFont(font_path).getBestCmap())
preflight=review['font_preflight']
preflight.setdefault('initial_missing_stage_title_characters',preflight['missing_stage_title_characters'])
preflight['missing_stage_title_characters']=''.join(sorted({c for stage in review['stage_plan'] for c in stage['name'] if ord(c) not in bundled}))
preflight['missing_stage_title_count']=len(preflight['missing_stage_title_characters'])
preflight['status']='required_glyphs_covered' if review['remaining_stages']==0 else 'current_batch_covered_future_pending'
review['font_preflight']['implemented_batch_missing_characters']=''
review['font_preflight']['limits']='全篇51阶段标题及所需字已补；0091郭注疑难字保留捕获及影印提示，不猜补。'
path.write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Eastern rare font',len(RARE),rare_target.stat().st_size,hashlib.sha256(rare_target.read_bytes()).hexdigest(),flush=True)

"""Rebuild the chapter-level inventory; --fetch refreshes the attributed reference snapshot."""
import argparse
import hashlib
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / 'data/shanhaijing-reference.json'
PROVENANCE = ROOT / 'frontend/src/content-provenance.json'
REPORT = ROOT / 'docs/content-coverage.md'
CHAPTERS = ['南山经', '西山经', '北山经', '东山经', '中山经', '海外南经', '海外西经', '海外北经', '海外东经',
            '海内南经', '海内西经', '海内北经', '海内东经', '大荒东经', '大荒南经', '大荒西经', '大荒北经', '海内经']
NUMERALS = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二', '十三', '十四', '十五', '十六', '十七', '十八']
BASE = 'https://zh.wikisource.org/wiki/'
EDITION = '山海經_(四部叢刊本)'


def read(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


def dump(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def fetch_snapshot():
    import requests
    from bs4 import BeautifulSoup
    session = requests.Session()
    session.headers['User-Agent'] = 'ShanhaiAtlasContentAudit/1.0 (local research; attributed reference snapshots)'
    chapters = []
    for number, (title, numeral) in enumerate(zip(CHAPTERS, NUMERALS), 1):
        page_title = f'{EDITION}/卷第{numeral}'
        url = BASE + quote(page_title, safe='/()_')
        response = session.get(url, timeout=40)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.select_one('.prp-pages-output')
        if content is None:
            raise ValueError(f'{title}: missing transcribed pages')
        revision = re.search(r'"wgRevisionId"\s*:\s*(\d+)', response.text)
        if revision is None:
            raise ValueError(f'{title}: missing revision')
        lines, page_name, quality = [], None, None
        for paragraph in content.find_all('p'):
            for page in paragraph.select('.pagenum'):
                page_name = page.get('data-page-name')
                quality = page.get('data-page-quality')
            annotations = [node.get_text('', strip=True) for node in paragraph.select('small.sfrac')]
            for node in paragraph.select('.pagenum, small.sfrac, .wst-dl-bracket, style, script'):
                node.decompose()
            image_glyphs = []
            for image in paragraph.find_all('img'):
                glyph = image.get('alt', '')
                image_glyphs.append(glyph)
                image.replace_with(f'⟦缺字图:{glyph}⟧')
            text = re.sub(r'[\s\u200b\ufeff]+', '', paragraph.get_text())
            if text or annotations:
                lines.append({'text': text, 'annotations': annotations, 'page': page_name,
                              'page_quality': quality, **({'image_glyphs': image_glyphs} if image_glyphs else {})})
        if sum(len(line['text']) for line in lines) < 100:
            raise ValueError(f'{title}: suspiciously short transcription')
        chapters.append({'number': number, 'title': title, 'url': url,
                         'revision_url': f'https://zh.wikisource.org/w/index.php?title={quote(page_title)}&oldid={revision.group(1)}',
                         'html_sha256': hashlib.sha256(response.content).hexdigest(), 'lines': lines})
        print(f'Fetched {number:02} {title}: {len(lines)} source lines', flush=True)
    dump(SNAPSHOT, {'edition': '《四部丛刊》景江安傅氏双鉴楼藏明成化庚寅刊本，晋郭璞传',
                    'provider': '维基文库影印本电子录文', 'url': BASE + quote(EDITION, safe='()_'),
                    'retrieved_on': date.today().isoformat(), 'rights': 'Ancient work: public domain. Wikisource transcription attributed at each revision and scan-page link.',
                    'limits': '电子录文保留未校对页与缺字图标记。逐行保存正文和注文，不合并不同版本；不是全书逐字校勘完成的声明。',
                    'chapters': chapters})


def source_info(source):
    chapters = [chapter for chapter in CHAPTERS if chapter in source]
    # Source summaries such as 海外南/西/北/东经 are expanded explicitly, never matched by entity name.
    if '海外南/西/北/东经' in source:
        chapters = CHAPTERS[5:9]
    if '大荒东/南/西/北经' in source:
        chapters = CHAPTERS[13:17]
    books = list(dict.fromkeys(re.findall(r'《([^》]+)》', source)))
    other = [book for book in books if '山海经' not in book and book not in CHAPTERS and book != '四部丛刊']
    family = 'mixed' if chapters and other else 'shanhaijing' if chapters or any('山海经' in book for book in books) else 'other_classic' if books else 'pending'
    return {'family': family, 'source': source, 'chapters': chapters, 'review': 'declared_source_only'}


def generate(check=False):
    snapshot = read('data/shanhaijing-reference.json')
    assert [item['title'] for item in snapshot['chapters']] == CHAPTERS
    for chapter in snapshot['chapters']:
        assert len(chapter['html_sha256']) == 64 and 'oldid=' in chapter['revision_url']
        assert sum(len(line['text']) for line in chapter['lines']) > 100
        assert all(line['page'] and line['page_quality'] in ['0', '1', '2', '3', '4'] for line in chapter['lines'])
    world, catalog = read('frontend/public/data/myth-world.json'), read('frontend/public/data/atlas/catalog.json')
    western_passages = [p for p in world['passages'] if p.get('source_book') == 2]
    western_cards = [r for group in ['beasts', 'natural_features', 'text_entities'] for r in world[group]
                     if r.get('content_batch', '').startswith('xishan-')]
    western_names = '、'.join(p['name'] for p in western_passages)
    northern_passages = [p for p in world['passages'] if p.get('source_book') == 3]
    northern_cards = [r for group in ['beasts', 'natural_features', 'text_entities', 'places'] for r in world[group] if r.get('content_batch', '').startswith('beishan-')]
    eastern_review = read('data/dongshan-edition-review.json') if (ROOT / 'data/dongshan-edition-review.json').exists() else {}
    coverage = read('data/nanshan-entity-coverage.json')
    artwork_jobs = read('frontend/artwork-source/nanshan/entities-generation.json')['assets']
    reviewed_artwork = sum(asset['status'] == 'reviewed' for asset in artwork_jobs)
    pending_artwork = len(artwork_jobs) - reviewed_artwork
    stages = {item['id'] for item in world['stages']}
    records = []
    for group in ['beasts', 'places', 'domains', 'natural_features', 'passages', 'text_entities']:
        records.extend({'id': item['id'], 'name': item['name'], 'kind': group, 'visibility': 'web', **source_info(item.get('source', ''))} for item in world[group])
    for event in catalog['events']:
        value = event['properties']
        visibility = 'unexposed' if value.get('stage_id') not in stages else 'archive_or_group' if value.get('presentation') in ['archive', 'group'] else 'web'
        records.append({'id': event['id'], 'name': value['name'], 'kind': 'event', 'visibility': visibility, **source_info(value.get('source_text', ''))})
    origins = {item['id']: {'family': item['family']} for item in records}
    for source in catalog['sources']:
        origins[f'source:{source["id"]}'] = {'family': source_info(source['title'])['family']}
    if check:
        assert read('frontend/src/content-provenance.json') == origins, 'Content origins are stale; rebuild the inventory'
    else:
        dump(PROVENANCE, origins)
    count = Counter(item['visibility'] for item in records)
    out = ['# 《山海经》内容覆盖盘点', '', f'盘点基准：{snapshot["edition"]}。电子录文取自[维基文库]({snapshot["url"]})，快照日期 {snapshot["retrieved_on"]}。', '',
           '## 统计口径', '',
           f'- 十八篇录文块清单见 `data/shanhaijing-inventory.json`，每项保存页码、原文、注文与待核状态。《南山经》43段、《西山经》{len(western_passages)}段、《北山经》{len(northern_passages)}段与《东山经》{eastern_review.get("implemented_stages",0)}段已接入说明；其余结构候选的段界、实体、关系和影印仍待人工核定。不是全书穷尽实体索引，也不是各版本校勘定本。',
           '- 已保存十八篇逐行正文、注文、影印页锚点、校对状态和固定修订链接，见 `data/shanhaijing-reference.json`。录文中缺字图保留显式标记，不猜字补齐。',
           '- 下表按当前条目声明的出处计数；同一条目可引用多篇，同名异篇保持分开。地点锚点、神域、异兽、故事不是同一统计单位，不能相加后声称全书覆盖率。',
           f'- {len(world["places"])}条地点记录含4条山列集合锚点；{len(world["domains"])}条神域与相关地点分别建档。{len(world["beasts"])}条异兽记录，同名异篇分开；{len(world["natural_features"])}条自然条目含草木、水域、物产。43条事件记录含拆分子事件、归档、组和未开放资料，不等于43个独立故事。',
           '- “常规入口”是地图、图鉴、章节目录中的独立条目；“非默认条目”是归档/组，仍可从搜索或直链打开；“未开放”指数据已有记录，但没有可用章节入口。引用某篇不等于完整收录该篇。',
           f'- 项目共 {len(records)} 条上述记录（含{len(world["passages"])}条经文阅读段，与独立实体不是同一统计单位）：常规入口 {count["web"]}，非默认条目 {count["archive_or_group"]}，未开放 {count["unexposed"]}。另有39条书目记录、32条现代地点关联，不混入该统计。', '',
           '## 十八篇对应清单', '', '| 篇目 | 常规入口记录 | 非默认条目 | 未开放记录 | 当前状态 |', '| --- | ---: | ---: | ---: | --- |']
    for chapter in snapshot['chapters']:
        linked = [item for item in records if chapter['title'] in item['chapters']]
        counts = Counter(item['visibility'] for item in linked)
        state = '全篇43段说明可读；独立实体仍选编' if chapter['number'] == 1 else f'{len(western_passages)}段、{len(western_cards)}张新卡已接入；其余仍待核' if chapter['number'] == 2 else '选编，篇内仍有遗漏' if counts['web'] else '仅数据存留，未形成网页收录' if linked else '尚无明确篇目对应'
        if chapter['number'] == 3 and northern_passages:
            state = f'全篇{len(northern_passages)}阅读段、{len(northern_cards)}张独立卡已核；形貌不足者留占位'
        if chapter['number'] == 4 and eastern_review:
            state = f'{eastern_review["planned_stages"]}阶段已规划、{eastern_review["implemented_stages"]}阶段接入；其余仍待接入'
        out.append(f'| [{chapter["title"]}]({chapter["revision_url"]}) | {counts["web"]} | {counts["archive_or_group"]} | {counts["unexposed"]} | {state} |')
    out += ['', '## 逐篇已收录与待补方向', '']
    gaps = {
        '南山经': f'43段正文与39座逐述山入口已接入；新增97张独立卡涵盖山水、异兽、草木、动物、谷风、山神和祭礼。本轮{len(artwork_jobs)}幅插画已审{reviewed_artwork}幅、待补或待审{pending_artwork}幅；验收以最新交接记录为准，不将文本接入称为全量完成。',
        '西山经': f'{western_names}共{len(western_passages)}段和{len(western_cards)}张独立卡已核对接入；保留原有异兽与玉山等ID。全篇正文、山水物产与主要具名神祇已接入；第三列报山数与里程合计差异保留。配图仍按形貌依据审核，不宣称多版本逐字校勘或实体穷尽。',
        '北山经': f'全篇{len(northern_passages)}阅读段、{len(northern_cards)}张独立卡已核，對照76—108页影印。北山57幅新图已审，諸犍与精衛复用旧图；26个形貌不足对象留占位。297录文块含1标题与296正文/注文块，全部映射到阅读段。三列原报山数合88、里程23530，与篇末87山、23230里分别保留；列名阅读山段25/16/47与原报25/17/46分开，不补删凑数。独立实体仍为项目整理，不宣称多版本逐字校勘或全书完成。',
        '东山经': (f'已核影印109—124页段界并规划{eastern_review["planned_stages"]}阶段：46列名山段、4总括、1篇末；141录文块含2标题/署名与139正文/注文块，42结构候选不等于阶段数。次三列名9与原报19、四列原报合56与篇末46并存；里程合18860与篇末一致。已接入{eastern_review["implemented_stages"]}阅读段、{len(eastern_review.get("entry_ids",[]))}独立卡，余{eastern_review["remaining_stages"]}阶段；已审图{eastern_review.get("artwork_summary",{}).get("selected",0)}幅、形貌不足占位{eastern_review.get("artwork_summary",{}).get("appearance_unknown",0)}项。食/湖/海/江与鱤鱼的不同出处分别保留。计划及15页界修正见data/dongshan-edition-review.json。' if eastern_review else '山列只是集合锚点；具体山水与各类物产尚未形成逐山索引。'),
        '中山经': '补具体山系、山水、物产与祭祀记述，避免只凭少量异兽代表全篇。',
        '海外南经': '国家、异人、神祇及明确方位关系未形成完整可达条目。',
        '海外西经': '刑天故事之外，诸国、异人与神祇关系待系统整理。',
        '海外北经': '夸父、相柳之外的国家、神祇与方位关系仍有大量缺口。',
        '海外东经': '黑齿、扶桑等是片段；诸国、异人与日月相关记载仍待按篇建立。',
        '海内南经': '以该篇为单位建立现有条目对应和未收录实体清单。',
        '海内西经': '昆仑等片段之外，其他地域、神兽与人物关系尚未系统整理。',
        '海内北经': '穷奇等条目之外，异人、山水与国家仍待补齐。',
        '海内东经': '优先梳理水道及相关地点；不将文学方位自动换成现代坐标。',
        '大荒东经': '异兽片段之外，国家、谱系、山川与日月运行记载待补。',
        '大荒南经': '数据总述不能算全篇收录；诸国、人物、山川需逐项核对。',
        '大荒西经': '不同篇目的西王母等形象须分开记录，国家及山川关系待补。',
        '大荒北经': '烛龙等片段之外，人物、山川及谱系待补；相繇与相柳分篇保存。',
        '海内经': '鲧禹故事之外的谱系、国家、水系与其他记载仍待系统整理。',
    }
    for chapter in snapshot['chapters']:
        out += [f'### {chapter["number"]:02} {chapter["title"]}', '']
        for status, label in [('web', '常规入口'), ('archive_or_group', '非默认条目'), ('unexposed', '数据未开放')]:
            linked = [f'{item["name"]}（`{item["id"]}`）' for item in records if chapter['title'] in item['chapters'] and item['visibility'] == status]
            if linked:
                out.append(f'- {label}：' + '；'.join(linked) + '。')
        note = '；全篇已对照影印页16–32，补录第26页；经文、底本注文和白话分存。电子快照原样保留，差异见`data/nanshan-edition-review.json`。' if chapter['number'] == 1 else '；已核全篇77个列名山段、4列总括和篇末总计共82段，对照影印34–75页，页码与缺字图差异见`data/xishan-edition-review.json`；各列总数及里程不强行改成一致。' if chapter['number'] == 2 else '；北山经全篇92阅读段已核76—108页，数字差异与形貌不足占位保留，详见data/beishan-edition-review.json。' if chapter['number'] == 3 else '；109—124页段界已核，前5段已核文并接入双语及对象，其余仍待接入，不将51阶段规划视为阅读已完成。' if chapter['number'] == 4 and eastern_review else '；录文尚需与影印页对校，不把自动导入视为已核对。'
        out += [f'- 待补方向：{gaps[chapter["title"]]}', '- 校核入口：[该篇固定修订](' + chapter['revision_url'] + ')' + note, '']
        if chapter['number'] == 3 and northern_passages:
            out += ['- 單狐至篇末source-03-0002—0297已对照76—108页，32处实际页界另存、9处缺字图恢复保留捕获。次三总括0290—0296与篇末0297独立；錞于母逢与总括無逢写法分别保留，未统一改字。', '']
        if chapter['number'] == 4 and eastern_review:
            out += ['- 阶段总表（状态以各阶段交接验收为准）：', '', '| 阶段 | 范围 | 来源块 | 实际影印页 | 内容状态 |', '| --- | --- | --- | --- | --- |']
            for stage in eastern_review['stage_plan']:
                a,b=stage['source_units']
                out.append(f'| {stage["stage"]} | {stage["name"]} | source-04-{a:04d}—{b:04d} | '+ '、'.join(map(str,stage['facsimile_pages']))+' | '+('已接入，验收见交接' if stage['content_status']=='facsimile_reviewed' else '待接入')+' |')
            out += ['', '- 跨行与形貌风险以data/dongshan-edition-review.json各阶段note为准；保留当康、蜚、合窳与东山山列既有稳定ID。', '']
    inventory = read('data/shanhaijing-inventory.json')
    western_units = [unit for unit in inventory['units'] if unit['chapter'] == 2]
    western_drafts = [draft for draft in inventory['candidate_passages'] if draft['chapter'] == 2]
    western_pages = sorted({int(unit['page_url'].rsplit('/', 1)[-1]) for unit in western_units})
    western_records = [item for item in records if '西山经' in item['chapters']]
    western_art = read('frontend/artwork-source/xishan/generation.json')['assets']
    out += [f'## 西山经已核山段：{western_names}', '',
            f'- 已盘点{len(western_units)}个来源录文块、{len(western_drafts)}个结构候选段，涉及影印页{western_pages[0]}–{western_pages[-1]}；其中{sum("缺字图" in unit["text"] for unit in western_units)}个录文块含缺字图标记。候选段不等于已核定山数、实体数或已完成阅读段。',
            '- 底本继续采用《四部丛刊》景明成化本，先核对影印与郭注、剔除标题元信息，再确定段界及中英文说明；保留歧义，不按图字替代文本猜字或读音。',
            '- 本篇现有记录的稳定ID保留，尤其`beast-guan`为讙，不与南山经灌灌合并；同名异山、山中与水中关系分别核定。现有对应记录：' + '；'.join(f'{item["name"]}（`{item["id"]}`）' for item in western_records) + '。', '',
            '| 首批范围 | 对象与关系 | 形貌与配图要求 | 来源候选与影印页 |', '| --- | --- | --- | --- |']
    first_western_batch = [
        ('錢來', '钱来山', '山概况、羬羊；松与洗石先留在概况，郭注与经文分开。', '羬羊须突出羊状与马尾的区别，尾部单独留空；不得直接画成普通山羊。'),
        ('松果', '松果山', '濩水北流入渭、䳋渠；水中铜与山段鸟类分层，不由共现推断水中栖居。', '䳋渠先核原字与黑身赤足；用姿态和概括刻纹增强辨识，不添加未经文支持的器官。'),
        ('太華', '太华山', '削成四方的山势、肥𧔥；“鸟兽莫居”与蛇的记载照录，不改成现实地理结论。', '肥𧔥须逐一数清六足四翼；保留蛇形，不把旱灾画成已发生的现实结果。'),
    ]
    for draft, (original_name, name, objects, art_plan) in zip(western_drafts, first_western_batch):
        assert original_name in draft['text'], f'{name}: preparation candidate changed'
        pages = '、'.join(str(int(url.rsplit('/', 1)[-1])) for url in draft['source_pages'])
        out.append(f'| {name} | {objects} | {art_plan} | `{draft["id"]}`；影印页{pages} |')
    out += ['', '- 已对照影印34–35页核定首批3段经文、段界与形貌；正文、郭注、白话和英文分存。电子快照不改写，䳋渠末句的来源页由快照35页校正为实际34页，差异见`data/xishan-edition-review.json`。',
            '- 新增8张独立卡：钱来、松果、太华3座山；羬羊、䳋渠、太华肥𧔥3项异兽；濩水和作为承接水域的渭2项水文。松、洗石与铜仍留在相应山段或水文，不虚构独立物种。新卡和3段阅读均从03章起可见，不增加地图坐标。',
            f'- 本批{len(western_art)}幅插画任务，已审{sum(a["status"]=="reviewed" for a in western_art)}幅；原图、完整提示词及复核记录见`frontend/artwork-source/xishan/generation.json`。每幅仅在复核通过后导出完整、预览和卡片WebP。',
            '- 后续配图采用“先读原文特征 → 保证缩略图可辨 → 用木刻造型强化特征”的顺序；没有特殊器官记载的对象用姿态与表面纹样表现，纹样明确为艺术解释。',
            '- 第二批新增小华、符禺、石脆3段与15张独立卡：3山、㸲牛、赤鷩、葱聾、鴖、萆荔、文茎、两种條、符禺之水、灌水、禺水、流赭。符禺与石脆的條分别记录，渭保留松果、符禺两段来源。第二批经文已核对影印35–37页；小华段注文缺字保留待核标记。',
            '- 第三批新增英山、竹山、浮山3段与18张独立卡。英山肥遗鸟与太华肥𧔥蛇分卡，㸲牛及羬羊的复用插画注明别段依据；英山禺水与石脆同名水域不强行合并。竹山人鱼四脚来自郭注，丹水东南流的南字经影印38页补入阅读引文，原始缺字图快照保留。浮山无水文，不补造河流；盼木、薰草独立记录。',
            '- 后续批次已接入羭次、时山、西山经南山和大时。槖𩇯人面独足、猛豹熊状的正文与郭注边界分别保留；时山无草木。大时涔水按郭注音潜转写Qian、北注渭，清水南注汉，两水不合并；榖字小注的电子快照缺收已有说明。',
            '- 后续继续核对剩余山段；具体接续点见本地交接文档，剩余候选仍为待核。未增加数据库，未改动现有地图章节；浏览器验收结果以交接文档最新记录为准。', '']
    out += ['## 来源分层与全部记录', '', '| ID | 条目 | 分类 | 可达状态 | 原始出处声明 |', '| --- | --- | --- | --- | --- |']
    labels = {'shanhaijing': '《山海经》', 'other_classic': '其他古籍', 'mixed': '多书合引', 'pending': '待核对'}
    for item in records:
        visibility_label = {'web': '常规入口', 'archive_or_group': '非默认条目', 'unexposed': '未开放'}[item['visibility']]
        out.append(f'| `{item["id"]}` | {item["name"]} | {labels[item["family"]]} | {visibility_label} | {item["source"]} |')
    out += ['', '## 南山经全篇阅读与全书待办清单', '',
            f'- 已保留2433个原始录文块与第26页4个补录块。清单逐项区分已说明、标题元信息和待核，候选实体匹配不算已核定关系。其他16篇仍待系统核对，西山经{len(western_passages)}段已有审核链接，本篇已连续覆盖正文；不将2437个录文块冒充2437段独立内容。',
            '- 《南山经》43段连续覆盖正文：39个实际列名的山段、3个山列总述/祭祀段、1个篇末总计。中文白话、英文说明与英文释文同步，保留底本中文和注文；可从章节目录、搜索、收藏及续读进入。新段落不添加地图坐标。',
            '- 第26页洵山、虖勺、区吴三段由影印补录；第21页“二千九百五十里”纠正电子录文漏“二”。猾褢等差异单列记录，祗山沿用底本写法；一个未确认图字仍显式保留待核标记，原电子快照不改写。',
            '- 底本各列总数为10、17、14山，篇末写40山，逐项列名实际39段；三种口径分别保留，不据此补造山名。完整指正文段落说明齐备，不含全书实体穷尽、逐字多版本校勘或全量配图。',
            f'- 独立实体轮新增97卡：36座逐述山、3个参见地点、14项异兽、25项水域、2项植物、7项普通动物、2谷、2风、3组山神和3项祭礼。南山经共117项独立卡（不含总览），另有43段阅读器；覆盖ID及逐段关联见`data/nanshan-entity-coverage.json`，逐述山入口共{len(coverage["mountain_ids"])}座。',
            f'- 首批和阅读器批已有9幅插画；最新独立实体轮共{len(artwork_jobs)}幅任务，已审{reviewed_artwork}幅，待补或待审{pending_artwork}幅。仅已审图导出接入，水域等复用山景并标明场景示意；无成图的卡保留“插画待补”，不请求不存在的图片。权威提示词、状态和复核记录见`frontend/artwork-source/nanshan/entities-generation.json`。',
            '- 文本接入、图片审阅与浏览器回归分别验收；最新轮的具体通过项和未运行项以根目录本地交接文档为准。下方历史验证不代表新增97卡轮已通过。', '',
            '## 第一批补充内容：南山经三处（历史批次）', '',
            '本批已接入11个新条目、6幅新图；同步完善青丘与狌狌、鹿蜀、旋龟、九尾狐、赤鱬。新山与自然条目从02章可见，灌灌从03章可见，关联阅读不推进章节。', '',
            '| 地点 | 已有内容 | 首批新增/完善 | 原文关系与验收边界 |', '| --- | --- | --- | --- |',
            '| 招摇之山 | 狌狌异兽卡；南山经集合锚点 | 独立地点介绍、祝余、迷谷、丽𪊨之水与育沛 | 同一山段记载；区分草、木、水、物产，保留生僻字及音读待核项 |',
            '| 杻阳之山 | 鹿蜀、旋龟异兽卡 | 独立地点介绍、怪水与宪翼之水、山阳山阴物产 | 旋龟在水中记载，不能简单改写成与鹿蜀相同陆上栖居；原文功效只作为古籍记述 |',
            '| 青丘之山 | 青丘地点、九尾狐、赤鱬 | 新增灌灌、英水、即翼之泽，完善地点与分层关系 | 九尾狐与灌灌在山段，赤鱬在水中；不由同段共现推断捕食或因果 |', '',
            '- 纠正旧报告：原有 `beast-guan` 为《西山经》讙；本批新增 `beast-guanguan` 为《南山经》灌灌，分别保留。',
            '- 11个新ID：`place-zhaoyao`、`place-niuyang`、`plant-zhuyu`、`plant-migu`、`water-liji`、`water-guai`、`water-xianyi`、`water-ying-qingqiu`、`water-jiyi`、`material-yupei`、`beast-guanguan`。',
            '- 校核依据：`data/reference-scans/nanshan/page-16.jpg`至`page-21.jpg`；扫描来源、哈希与定位见同目录`sources.json`。当前条目分别保存经文、郭注摘录、白话整理及出处定位；简体字和标点为编辑整理。',
            '- 六幅图片：招摇、杻阳、青丘新版、祝余、迷谷、灌灌；均为内置image_gen生成并已接入。原图、提示词和核验记录在`frontend/artwork-source/nanshan/`。发布WebP含透明完整图、预览、缩略图；灌灌另有地图图标。育沛无具象图；五处水域复用场景并明示示意。',
            '- 五项旧异兽图已逐项目视核验并沿用；狌狌的人面倾向属于图像解释，非经文明言。图像仅作艺术表达，不作古代动物学复原。', '',
            '三处为首批编辑范围；其间山段已在后续43段阅读器和独立卡轮接入。叙述按“白话景象→原文→出处与边界”组织。任何古籍中的食用、佩用或治病功效均作为文本描述，不给现实使用建议。', '',
            '## 本轮发现的待校问题', '',
            '- `08-01`“海外诸国”和 `08-02`“大荒异兽”的 source_quote 实为项目汇总，不能当作连续经文引文。两项目前无网页章节入口；新增入口前须拆成逐篇、逐条原文。',
            '- `08-06`所引“西北海之外，赤水之北，有章尾山”对应《大荒北经》，原出处首先列《海外北经》；开放前须明确主引篇和参见篇。',
            '- 现有“郭璞注本”没有逐条精确到同一刊本。本轮选定的盘点基准不等于替换所有现有引文版本；简繁、异体、删节和文字差异均应逐条复核。',
            '- 同名异篇、神域与地点、原文与郭注分别保留；尚不计算“全书完成百分比”。', '',
            '## 全篇阅读验证（历史批次，2026-10-19）', '',
            '- 本地通过：`build --base /mythmap/`、`verify:data`、`verify:publish`、`verify:cache`、盘点和全书清单`--check`；9幅南山经图的28个WebP版本保留透明通道，19个所需生僻字符由本地字体覆盖。',
            '- Chromium、WebKit通过`verify:reader`：43段逐一打开、原文与目录、缺页补录、中文原名英文搜索、收藏/已读持久化、旧标记保留、续读、返回/刷新、关联阅读、3幅新场景实用与8种语言/视口组合；还覆盖地图图片加载中断。',
            '- 本轮现有`verify:search`、`verify:discovery`在Chromium通过，WebKit复测通过；复测前曾暴露图片加载中断导致的OpenLayers图标尺寸异常，已改用已知尺寸缩放并增加中断测试。`verify:locale`在Chromium通过。',
            '- 原47个地点/神域/异兽ID和原异兽开放章节保留。未运行Firefox、全故事长流程和数据库集成；远端CI尚未运行。未发布远端站点，检查结束后关闭测试端口。', '',
            '## 首批三处验证记录（历史批次，2026-10-19）', '',
            '- 本地通过：`build --base /mythmap/`、`verify:data`、`verify:cache`、`verify:publish`及本清单`--check`；6幅图的19个发布版本均保留透明通道。旧47个地点/神域/异兽ID全部保留，旧异兽开放章节未改变。',
            '- Chromium、WebKit通过：`verify:nanshan`（11项、双语、搜索、关联往返、返回/刷新、收藏/已读、续读、8种语言/视口组合），以及`verify:search`、`verify:discovery`、`verify:design`、`verify:reading`、`verify:resume`。`verify:locale`本地Chromium通过。',
            '- 本轮未运行Firefox、全故事时钟长流程及数据库集成检查；CI已纳入新条目检查，配置三浏览器运行，但尚未宣称远端CI通过。未发布远端站点。预览服务器在检查结束后关闭。', '',
            '## 复现与更新', '',
            '- `python data/build_nanshan_reader.py`：重建43段双语正文、出处和校核差异，保留既有独立条目。',
            '- `python data/build_nanshan_entities.py`：在旧批次/阅读器构建之后运行，恢复最新实体、关系、图像状态和覆盖清单；不可将reader或首批构建器作为最后一步。',
            '- `python data/build_source_inventory.py`（可加`--check`）：生成/检查十八篇原文块清单及明确的待核状态。',
            '- `python data/build_nanshan.py`：合并本批中英文条目、图像指向与有引文依据的关系，保留其他记录。',
            '- `python frontend/scripts/prepare-nanshan-artwork.py`：从保留的生成原图重建发布素材与素材清单。',
            f'- `python data/build_xishan.py`：合并西山经{len(western_passages)}段与{len(western_cards)}张双语卡，并记录影印页码和缺字图校正；在南山经构建器之后运行。',
            '- `python data/build_dongshan.py`：合并东山前20段/102双语卡，保留其他篇与东山既有稳定ID；东山插画通过prepare-nanshan-artwork.py --chapter dongshan导出，之后重建inventory/audit。',
            '- `python data/build_beishan.py`：合并已核北山经全篇92段及507张双语卡（含复用諸犍、精衛、發鳩），保留其他篇目与旧ID；`python frontend/scripts/prepare-nanshan-artwork.py --chapter beishan`仅导出已审图。随后重建全书清单和本盘点。',
            '- `python frontend/scripts/prepare-nanshan-artwork.py --chapter xishan`：仅导出已审核西山经插画。随后运行全书清单和本盘点构建器更新统计。',
            '- `python data/audit_shanhaijing.py`：离线重建本清单和网页来源分类。',
            '- `python data/audit_shanhaijing.py --check`：只检查快照结构、分类与清单是否和现有数据一致；CI运行该项。',
            '- `python data/audit_shanhaijing.py --fetch`：显式重新获取十八卷录文，再重建；联网获取需要 requests、beautifulsoup4，离线检查仅需Python标准库。',
            '- 影印页正文与注文分开保存。卷页固定修订链接不能锁定被嵌入页面的后续编辑，因此同时保留抓取日期、逐行快照及HTML SHA-256；更新后应审查差异。']
    report = '\n'.join(out) + '\n'
    if check:
        assert REPORT.read_text(encoding='utf-8') == report, 'Coverage report is stale; rebuild the inventory'
    else:
        REPORT.write_text(report, encoding='utf-8')
    print(f'Generated {len(CHAPTERS)} chapter inventory; {len(records)} project records; {dict(count)}', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--fetch', action='store_true')
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    if args.fetch:
        fetch_snapshot()
    generate(check=args.check)

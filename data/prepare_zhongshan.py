"""Rebuild the Central Mountains preparation plan without publishing reader content."""
import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / 'data/zhongshan-edition-review.json'
SNAPSHOT_SHA = '0df08619414c2ea7e068d5c91fb9a9bb155c56bfb766fa9b9985d084986097ce'
SLUGS = [
    'gancao lier quzhu conglong wo tuohu jinxing taiwei jianggu wulin niushou huo hegu yin gudeng',
    'huizhu fashi hao xian yang kunwu jian dusu manqu',
    'aoan qingyao gui yisu he',
    'luti fuzhu li jiwei bing baibian xionger mu huanju',
    'gouchuang shou xianzhu conglong tiaogu chao chenghou chaoge huai li shi liangyu guwei sheng yangxu',
    'pingfeng gaodi hui zhanzhu louzhuo baishi gu mi changshi mountain-194 tuo changzheng kuafu yanghua',
    'xiuyu guzhong guyao ku du fanggao da-241 banshi shaoshi taishi jiang yingliang fuxi shaoxing tai mo yi min dagui',
    'jing jingshan jiao nvji yizhu lun lugui guang qi tong mei dayao ling long heng shi ruo zhi yu huan renju shimei qingu',
    'nvfan min lai ju gaoliang she ge yuyang qi goumi fengyu yu xiong gui ge-mountain jiachao',
    'shouyang huwei fanhui yongshi fuzhou chu youyuan zhuo bing',
    'yiwang chaoge diqun shi qian feng-first tuchuang pi yaobi zhili zhidiao jinli yiku jigu ji gaoqian youxi cong yingzhen bi lema zhen ying hushou yinghou dashu bei yidi ni ya xuan heng feng-second yu-mountain xian zhang dazhi quwu shengxiong dagui zhongjiu lishi qiu chouyang ao fu yao ji-mountain',
    'pianyu yun gui bing fengbo fufu dongting bao jigong yao jiangfu zhenling yangdi chaisang rongyu',
]
NAMED = [15, 9, 5, 9, 15, 14, 19, 23, 16, 9, 48, 15]
REPORTED = [15, 9, 5, 9, 16, 14, 19, 23, 16, 9, 48, 15]
LI = [6670, 1670, 440, 1670, 2982, 790, 1184, 2890, 3500, 267, 3732, 2800]
NOTES = {
    2: '共水西注河；㔮为𤠢鼠状文题，郭注明言鼠形未详，不强定现代鼠种；医食功效仅作古述。',
    7: '櫔木方茎圆叶黄华而毛，实如揀；揀木音注跨8—9，9实在2页末，不并入渠猪山。',
    10: '豪鱼如鮪、赤喙尾赤羽；郭注鮪似鱣，羽字不自动推成鸟翼或鸭首。',
    13: '白垩黑青黄垩为颜色物产，不拆为四种生物。与次五同名葱聾山分开。',
    15: '涹山阳面多赤铜、阴面多铁；不合并其他同音山。',
    25: '鬼草缺字图可据4页读鬼；飞鱼本段如鲋，不并次三騩山豚状赤文飞鱼或其他篇飞鱼。',
    29: '霍山郭注列举多处同名地并明言非一，不绑定现代单一坐标；朏朏狸状白尾有鬣。',
    38: '底本十五山、六千六百七十里照录，不因里程异常自行纠正；历儿为冢，其余十三山祭礼照录。',
    54: '昆吾铜剑长注跨55—57，与蠪蚳彘状有角形貌分开；不混西山同名蠪蚳的人面羊角。',
    74: '青要武罗人面豹文小腰白齿、耳穿鐻；鴢鸟凫状青身朱目赤尾。鲧化注文另存，不把郭注比音添作器官。',
    90: '和山泰逢人状虎尾；郭注或作雀尾为异说，不能两种尾部同时叠加。',
    99: '鹿蹄甘水北注洛，泠石郭注未闻；水名、物产与异说分存。',
    104: '犀渠牛状苍身，𤢺如獳犬有鳞、毛如彘鬣；𤢺生鳞间注文跨107—108。滽滽水与次三同音水暂分出处，不凭同名判定现代水系。',
    111: '柄山滔雕水北注洛，其中多羬羊照录；不因水文叙述擅改为鱼种或合并其他篇羬羊。',
    122: '讙举为最后列名山；玄扈在本段是受水体，总括却称玄扈之山，分别保留，不补造第十列名山。',
    128: '首曰茍牀，郭注或作茍林，总括茍林；同段异名留存。',
    158: '次五列名15山而总括报16山，差1照录；尸水合天与祭礼注文跨161—162。',
    165: '平逢人状二首骄虫；蜂蜜之庐为古述，二首必核，雄鸡禳而勿杀不画杀祭。',
    187: '旋龟本段只给鸟首鳖尾与判木声，不从南山旋龟借赤黑色或现代种属。',
    194: '𫝊山保留底本文字；墦冢缺字图仅在阅读层校释，不改原快照。',
    210: '门水出河790里入雒与本段多水关系照录，不据现代水系消解矛盾。',
    227: '姑媱帝女女尸化䔄草；人神身份与植物分别建卡，不画无原文形貌的女神。',
    237: '文文如蜂、枝尾反舌；呼声不添加人面人手。',
    241: '三足龟据正文；郭注地方例另提六眼龟，不自动把六眼强加正文生物。',
    253: '少室与泰室分段；䱱鱼如𥂕蜼，郭注未详，不强套现代娃娃鱼。',
    287: '十六神豕身人面，苦山少室太室三冢人面三首；不可把三首与豕身自动并给所有神。',
    303: '𧕛围人面羊角虎爪，躯形未定；不混人身龙首计蒙或方面三足涉𧕦。',
    306: '鸟名及郭注有替换符；保留缺字待核，不拿现代鸟名或上一个白鷮强补。',
    318: '计蒙人身龙首，飘风暴雨为出入古述；无需雷电光环或多龙首。',
    321: '涉𧕦人身方面三足；三足逐数，不能画成普通双足人。',
    355: '正文女凡与总括女几异写分别保留；不并次八女几。',
    363: '崍山㹮形貌只在郭注，正文与注文来源分层；别名和现代熊猫对应不直接确定。',
    367: '怪蛇郭注钩蛇为例，不自动并入其他篇同名蛇；竊脂枭状赤身白首，不用郭注所疑现代青萑替换。',
    408: '次九总括女几、文山及醜之山与列名存在差异；不为总括提及名号补造路线山段。',
    420: '跂踵鸟枭状一足彘尾；东山跂踵是山名，两者不合并。',
    429: '首陽/首山异写及堵山、騩山祭礼引用照录；不向本列添加缺失山段。',
    434: '蛟形貌来自长郭注，四脚小首细颈白瘿等与正文来源分层。',
    448: '此豐山与509豐山同列重名分别建档；雍和蝯状赤目赤喙黄身，耕父仅记身份不编造独立神形。',
    453: '兎牀缺字图待阅读层校释，不与茍牀相混。',
    456: '瑶碧鴆为雉状食蜚，郭注明言不是食蛇鴆，不借旧鴆图。',
    478: '三足鳖枝尾与他篇旋龟、三足龟分开；三足和分枝尾分别核。',
    496: '狙如如鼣鼠白耳白喙，郭注鼠形未详，不强定现代种或借南山白耳鼠图。',
    503: '帝女之桑是木名与蚕事解释，不自动新造帝女形貌。',
    518: '大支多榖柞后又无草木，矛盾如实保留，不删改其一。',
    525: '梁渠狸状白首虎爪，与北山梁渠山、囂鸟分开，逐一注明出处。',
    537: '聞𧲂彘状黄身白头白尾，539异体替换符留待字形复核。',
    540: '次十一48列名与总括48相合；禾山、堵山、玉山是总括祭礼引用，不擅补路线。',
    545: '篇遇原字保留，郭注或作肩；不按通行本自动改字。',
    556: '于儿人身、身操两蛇照底本，不擅改为手操；数量两蛇必核，光为古述。',
    559: '洞庭长郭注563—575含多条纯注文，保留在洞庭段。郭璞辨帝之二女与尧女舜妃，不能把异说压成同一身份；怪神载蛇左右手操蛇与帝女分别录。575飘风接576复杂暴字缺字图雨仍属本段，不切给577𭧂山。',
    580: '蛫龟状白身赤首，御火为古述，不添加火焰器官。',
    596: '次十二十五山与列名相合，祭礼中的圭璧十五、五彩等数量分别录，不视为新山神数量。',
    603: '中山197山21371里、天下5370山64056里在同一收束段；604同块含两项总计，分别作实体引文，不强切捕获行。各列报数198与197差1，里程和28595与21371差7224，照录。',
    606: '禹曰及天地尺寸、出受水山、铜铁山、封禅国用是古宇宙地理与国用论述，不作实测现代数据或新路线山段。',
    614: '五臧五篇15503字为底本文本计数说明，不当作当前录文实际字数或五篇语义段数。',
}


def build(check=False):
    if TARGET.exists() and json.loads(TARGET.read_text(encoding='utf-8')).get('implemented_stages', 0):
        raise RuntimeError('Reader implementation exists; the preparation builder must not overwrite its progress.')
    raw = (ROOT / 'data/shanhaijing-reference.json').read_bytes()
    assert hashlib.sha256(raw).hexdigest() == SNAPSHOT_SHA
    chapter = json.loads(raw)['chapters'][4]
    lines = chapter['lines']
    assert len(lines) == 614
    scans = json.loads((ROOT / 'data/reference-scans/zhongshan/sources.json').read_text(encoding='utf-8'))
    assert [s['page'] for s in scans] == list(range(2, 71))
    for scan in scans:
        assert hashlib.sha256((ROOT / scan['local_path']).read_bytes()).hexdigest() == scan['sha256']
    starts, counts, range_number = [], Counter(), 0
    for number, line in enumerate(lines, 1):
        text = line['text']
        if text.startswith(('中次', '中山經薄山')):
            range_number += 1
        if text.startswith(('中次', '中山經薄山')) or re.match(r'^又?[東西南北]{1,2}[一二三四五六七八九十百千萬]+里曰', text):
            slug = SLUGS[range_number - 1].split()[counts[range_number]]
            counts[range_number] += 1
            starts.append((number, range_number, 'mountain', f'r{range_number:02}-{slug}', re.search(r'曰(.*?山)', text)[1]))
        elif text.startswith('凡'):
            starts.append((number, range_number, 'summary', f'r{range_number:02}-summary', f'次{range_number}总括与祭礼'))
    assert list(counts.values()) == NAMED
    starts += [(603, 13, 'closing_total', 'book-world-total', '中山及天下名山总计'), (606, 13, 'cosmography', 'yu-cosmography', '禹曰天地及国用'), (614, 13, 'colophon', 'five-books-colophon', '五臧五篇题计')]
    assert starts == sorted(starts) and len(starts) == 212
    offsets = [0]
    for line in lines:
        offsets.append(offsets[-1] + len(line['text']))
    corrections = {'source-05-0009': 2, 'source-05-0018': 3, 'source-05-0027': 4, 'source-05-0036': 5, 'source-05-0045': 6, 'source-05-0162': 19, 'source-05-0603': 68, 'source-05-0612': 69}
    stages = []
    for index, (first, group, kind, slug, name) in enumerate(starts):
        last = starts[index + 1][0] - 1 if index + 1 < len(starts) else len(lines)
        refs = lines[first - 1:last]
        ids = [f'source-05-{n:04d}' for n in range(first, last + 1)]
        captured = list(dict.fromkeys(int(l['page'].rsplit('/', 1)[-1]) for l in refs))
        pages = sorted({corrections.get(id, int(l['page'].rsplit('/', 1)[-1])) for id, l in zip(ids, refs)})
        stages.append(dict(stage=index + 1, slug=slug, name=name, range=group, kind=kind, source_units=[first, last], source_unit_ids=ids, source_span=[offsets[first - 1], offsets[last]], facsimile_pages=pages, captured_pages=captured, boundary_status='facsimile_boundary_reviewed' if index < 5 else 'captured_text_boundary_reviewed_facsimile_recheck_required', content_status='pending_bilingual_entity_review', browser_status='not_implemented', note=NOTES.get(first, '按本列独立整理正文、跨行郭注、水文方向与同名异篇；实体、形貌和关系仍待逐阶段影印复核。')))
    assert [id for s in stages for id in s['source_unit_ids']] == [f'source-05-{n:04d}' for n in range(2, 615)]
    assert len({s['slug'] for s in stages}) == len(stages)
    for a, b in zip(stages, stages[1:]):
        assert a['source_span'][1] == b['source_span'][0]
    issues = []
    for n, line in enumerate(lines, 1):
        if '⟦' in line['text'] or '�' in line['text'] + ''.join(line['annotations']):
            issues.append(dict(source_unit_id=f'source-05-{n:04d}', kind='missing_image_glyph' if '⟦' in line['text'] else 'replacement_character', captured_text=line['text'], captured_commentary=line['annotations'], status='preserved_pending_reading_layer_review'))
            if n in {26, 159, 611}:
                issues[-1].update(status='facsimile_reading_confirmed_pending_reading_layer', facsimile_reading={26: '鬼', 159: '冢', 611: '能'}[n])
    from fontTools.ttLib import TTFont
    cmap = set()
    for path in (ROOT / 'frontend/public/fonts').glob('*.woff2'):
        cmap.update(TTFont(path).getBestCmap())
    titles = ''.join(re.sub(r'⟦缺字图:([^⟧]+)⟧', r'\1', s['name']) for s in stages)
    missing = ''.join(sorted({ch for ch in titles if ord(ch) > 127 and ord(ch) not in cmap}))
    review = dict(chapter=5, edition='《山海經（四部叢刊本）》卷第五，郭氏傳', status='planned_not_implemented', scope='全篇录文段界规划，首五段影印段界核定；全部阶段仍待双语、实体关系、必要配图、字体及页面接入。', revision_url=chapter['revision_url'], snapshot_sha256=SNAPSHOT_SHA, scan_pages=list(range(2, 71)), scan_manifest='data/reference-scans/zhongshan/sources.json', heading_unit_ids=['source-05-0001'], source_unit_page_corrections=corrections, source_blocks=614, planned_content_blocks=613, commentary_only_unit_ids=[f'source-05-{n:04d}' for n, l in enumerate(lines, 1) if not l['text'] and l['annotations']], planned_stages=212, implemented_stages=0, remaining_stages=212, stage_counts=[n + 1 for n in NAMED] + [3], named_mountains=NAMED, reported_mountains=REPORTED, reported_li=LI, closing_total=dict(reported_mountains=197, reported_li=21371, named_mountain_sum=sum(NAMED), range_reported_mountain_sum=sum(REPORTED), mountain_difference=sum(REPORTED) - 197, range_li_sum=sum(LI), li_difference=sum(LI) - 21371, world_reported_mountains=5370, world_reported_li=64056, five_books_reported_characters=15503), glyph_issues=issues, first_batch=[s['slug'] for s in stages[:5]], next=dict(name=stages[0]['name'], source_units=stages[0]['source_units'], facsimile_pages=stages[0]['facsimile_pages'], status='pending_bilingual_entity_review'), stage_plan=stages, entry_ids=[], passages=[], artwork_summary=dict(selected=0, appearance_unknown=0), font_preflight=dict(status='future_content_pending', missing_stage_title_characters=missing, missing_stage_title_count=len(missing), limits='只预检规划标题；完整实体名、正文与注文仍须逐批预检。准备阶段不宣称字体或页面接入完成。'), limits='197列名山+12总括祭礼+3收束=212规划阶段，不等于200自动结构候选；仅首五段核定影印段界，其余逐阶段核页、释字与形貌。所有扫描保存并校验，不代表全部逐字校勘。快照原样保留，未生成或发布生物图，未增加网页阅读。')
    text = json.dumps(review, ensure_ascii=False, indent=2) + '\n'
    if check:
        assert TARGET.read_text(encoding='utf-8') == text, 'Central plan is stale'
    else:
        TARGET.write_text(text, encoding='utf-8')
    print(f'Central plan: {len(stages)} stages, {sum(NAMED)} named mountains, 69 scans; 0 published passages; {len(missing)} title glyphs pending')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    build(parser.parse_args().check)

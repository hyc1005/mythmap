"""Jiao and Nüji: limited anatomy and unit-specific transcription restoration."""
from zhongshan_next30 import R

ROWS = [
    R('r08-jiao', '驕山', 'Mount Jiao',
      '东北百五十里驕山，上玉下青䨼，多松柏桃枝鈎端。神𧕛圍人面羊角虎爪，常游睢漳之渊、出入有光；躯干与肢数未载，图仅人面羊角和虎爪的局部示意，不补虎身、人身或火焰。睢漳之渊单列，不强定与前雎水漳水的同一性。',
      'A hundred and fifty li northeast is Mount Jiao, with jade above and qinghu below, and song, bai, taozhi and gouduan plants. The god Tuowei dwells here, with a human face, goat horns and tiger claws, wandering in the Sui-Zhang pool and giving light when entering or leaving.',
      'The torso and limb count are not given. The illustration is a partial anatomy study only: a human face with goat horns and separately presented tiger paws. Age, horn curvature, two-paw layout and neutral base are artistic. The light claim adds no flames, and the pool is not forcibly merged with earlier river names.'),
    R('r08-nvji', '女几之山', 'Mount Nüji',
      '东北百二十里女几，上玉下黄金，多豹虎閭麋麖麂。麂似獐而大、偎毛豹脚原词保留，未明细节不强画像。白鷮郭注雉状长尾、走且鸣；翟只列名。308缺字据影印恢复鴆，仅阅读层改，郭注紫绿色長頭赤喙，雄運目雌隂諧照录，不据别本改成长颈或運日；食蝠蛇头为古注不画猎食。306实际35页末，后文续36页。',
      'A hundred and twenty li northeast is Mount Nüji, with jade above and gold below. It lists leopards, tigers, lümi, jing and ji beasts, white Jiao birds, Zhai birds and Zhen birds.',
      'Guo Pu describes white Jiao as pheasant-like with long tails, walking and calling. The damaged Zhen glyph in unit 308 is restored from the scan in the reading layer only. Its gloss gives purple-green coloring, a long head and red bill, with male Yunmu and female Yinxie names as captured. Long-head and Yunmu readings are not changed to other editions; the feeding claim is not illustrated. Unit 306 is on scan 35, followed by scan 36.')
]
LINKS = []
SHARES = []


def entities(E):
    LINKS.clear(); SHARES.clear(); out = []
    def add(s, k, key, name, en, q, eq, cn, note='', **extra):
        out.append(E(s, k, key, name, en, q, cn, eq, (eq+' '+note).strip(), **extra))
        return out[-1]['id']
    def product(s, key, name, en, q, eq, kind='material'):
        return add(s, kind, key, name, en, q, eq, '按本山物产原名与位置存录，不强定现代种属、成分或坐标。')
    def unknown(s, key, name, en, q, eq, cn, **extra):
        return add(s, 'animal', key, name, en, q, eq, cn, 'Independent form or terminology is insufficient; the placeholder is not a depiction.', unknown=True, **extra)
    s='r08-jiao'
    product(s,'jade-jiao8','玉（驕山）','Jade (Jiao)','其上多玉','Jade is abundant above.')
    product(s,'qinghu-jiao8','青䨼（驕山）','Qinghu (Jiao)','其下多青䨼','Qinghu is abundant below.')
    for key,n,en,q in [('song','松','Song trees','其木多松栢'),('bai','栢','Bai trees','其木多松栢'),('taozhi','桃枝','Taozhi','多桃枝鈎端'),('gouduan','鈎端','Gouduan','多桃枝鈎端')]:
        product(s,key+'-jiao8',n+'（驕山）',en+' (Jiao)',q,en+' occurs in the plant list.',kind='plant')
    pool=add(s,'water','sui-zhang-pool-jiao','睢漳之淵（驕山）','Sui-Zhang pool (Jiao)','恒遊于睢漳之淵','Tuowei habitually wanders in the Sui-Zhang pool.','睢漳之渊为神游处单列；不把睢字默改为前雎水或自动合并两条河。',commentary='淵水之府奥也',en_commentary='Guo Pu explains yuan as a deep water recess.')
    god=add(s,'deity','tuowei-jiao','𧕛圍（驕山）','Tuowei (Jiao)','神𧕛圍處之其狀如人面羊角虎爪恒遊于睢漳之淵出入有光','Tuowei dwells here, with a human face, goat horns and tiger claws, wandering in the pool and giving light on entering or leaving.','人面羊角虎爪有据，躯干与肢数未载；图仅头面羊角及分列虎爪局部，不作全身复原。双角、双爪布局、老年面容、短颈底座和爪纹为艺术解释；有光不画火。','The partial study does not assert a torso or limb count. Head age, two-horn/two-paw layout, short neck, display base, paw markings and colors are artistic.',commentary='𧕛音鼉魚之鼉',en_commentary='Guo Pu compares the first character’s pronunciation with tuo.')
    LINKS.append((pool,god))
    s='r08-nvji'
    product(s,'jade-nvji8','玉（女几）','Jade (Nüji)','其上多玉','Jade is abundant above.')
    product(s,'gold-nvji8','黃金（女几）','Gold (Nüji)','其下多黄金','Gold is abundant below.')
    for key,n,en,q in [('leopard','豹','Leopards','其獸多豹虎'),('tiger','虎','Tigers','其獸多豹虎'),('lvmi','閭麋','Lümi','多閭麋麖麂'),('jing','麖','Jing beasts','多閭麋麖麂')]:
        unknown(s,key+'-nvji8',n+'（女几）',en+' (Nüji)',q,en+' occurs in the beast list.','本段仅列名，閭麋词义分合保留；不借他山形体或强定现代物种。')
    unknown(s,'ji-nvji8','麂（女几）','Ji beasts (Nüji)','多閭麋麖麂','Ji occurs in the beast list.','郭注似獐而大、偎毛豹脚原词照录；毛与足的用词不足以稳妥补全形，不强画现代麂或把整身加豹斑。',commentary='麂似獐而大偎毛豹脚音几',en_commentary='Guo Pu compares ji with a larger zhang and records uncertain hair and leopard-foot wording, with ji pronunciation; these do not establish a modern species portrait.')
    add(s,'beast','whitejiao-nvji','白鷮（女几）','White Jiao birds (Nüji)','其鳥多白鷮','White Jiao birds are abundant.','白色据正文，雉状长尾、走且鸣据郭注；双足、喙足色、羽纹与行姿为艺术解释，不补凤冠火焰。','Pheasant-like form and long tail follow commentary; two ordinary bird legs, bill/feet coloring, feather arrangement and walking pose are artistic.',commentary='鷮似雉而長尾走且鳴音驕',en_commentary='Guo Pu compares Jiao with a pheasant, long-tailed, walking and calling, and supplies pronunciation.')
    unknown(s,'zhai-nvji8','翟（女几）','Zhai birds (Nüji)','多翟','Zhai birds are abundant.','本段翟仅列名，不将前白鷮或后鴆的形色与长尾移给翟。')
    add(s,'beast','zhen-nvji','鴆（女几）','Zhen birds (Nüji)','多鴆','Zhen birds are abundant.','308正文及郭注开头的缺字仅阅读层据影印恢复鴆；郭注大如鵰、紫绿色、長頭赤喙据本底本照录。图画紫绿鸟与赤喙，頭的比例、喙曲、羽纹、足尾及站姿为艺术解释；不强定现代种，食蝠蛇头不画猎食。運目、隂諧为注文名，不另造两种性别外形。','The scan restores Zhen only in the reading layer. Purple-green coloring, long head and red bill follow this edition; head proportions, bill curvature, ordinary wings/feet/tail and pose are artistic. Sex names add no invented sexual dimorphism.',commentary='鴆大如鵰紫綠色長頭赤喙食蝠蛇頭雄；名運目雌名隂諧也',en_commentary='The gloss continues across 308–309 and retains long head, the captured feeding wording, male Yunmu and female Yinxie. Other editions and dictionaries are not used to overwrite these readings.')
    return out

"""Merge reviewed Western Mountain passages and their independent entities."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BATCH = 'xishan-first-three'
SECOND_BATCH = 'xishan-second-three'
THIRD_BATCH = 'xishan-third-three'
FOURTH_BATCH = 'xishan-yuci'
FIFTH_BATCH = 'xishan-shishan'
SIXTH_BATCH = 'xishan-nanshan-west'
SEVENTH_BATCH = 'xishan-dashi'
EIGHTH_BATCH = 'xishan-bozhong'
NINTH_BATCH = 'xishan-tiandi'
TENTH_BATCH = 'xishan-gaotu'
ELEVENTH_BATCH = 'xishan-huangshan'
TWELFTH_BATCH = 'xishan-cuishan'
THIRTEENTH_BATCH = 'xishan-guishan'
SUMMARY_BATCH = 'xishan-range1-summary'
FOURTEENTH_BATCH = 'xishan-qianshan'
FIFTEENTH_BATCH = 'xishan-taimao'
SIXTEENTH_BATCH = 'xishan-shuli'
SEVENTEENTH_BATCH = 'xishan-gaoshan'
EIGHTEENTH_BATCH = 'xishan-nvchuang'
NINETEENTH_BATCH = 'xishan-longshou'
TWENTIETH_BATCH = 'xishan-lutai'
TWENTY_FIRST_BATCH = 'xishan-niaowei'
TWENTY_SECOND_BATCH = 'xishan-xiaoci'
TWENTY_THIRD_BATCH = 'xishan-daci'
RANGE2_FINISH_BATCHES = {'xishan-xunwu', 'xishan-quyang', 'xishan-zhongshou', 'xishan-huangren', 'xishan-zhonghuang', 'xishan-xihuang', 'xishan-laishan', 'xishan-range2-summary'}
SOURCE = '《山海经·西山经》（《四部丛刊》景明成化本，郭璞传）'
EN_SOURCE = 'Shanhaijing · Xishan Jing (Sibu Congkan facsimile; Guo Pu commentary)'
PAGE_CORRECTIONS = {'source-02-0009': 34, 'source-02-0018': 35, 'source-02-0027': 36,
                    'source-02-0036': 37, 'source-02-0045': 38, 'source-02-0054': 39, 'source-02-0063': 40,
                    'source-02-0072': 41, 'source-02-0081': 42, 'source-02-0090': 43, 'source-02-0099': 44, 'source-02-0108': 45, 'source-02-0117': 46, 'source-02-0126': 47, 'source-02-0135': 48, 'source-02-0144': 49, 'source-02-0153': 50, 'source-02-0162': 51, 'source-02-0171': 52, 'source-02-0180': 53, 'source-02-0189': 54, 'source-02-0198': 55, 'source-02-0207': 56, 'source-02-0216': 57}
SCENE_CAPTION = '场景示意 · 山形、配色和水流画法为艺术解释，不复原现代地理。'
EN_SCENE_CAPTION = 'Place scene · Landforms, colors and water are artistic interpretations, not a reconstruction of modern geography.'
ART_CAPTION = '原文形貌与木刻演绎 · 刻纹、配色和姿态为艺术解释。'
EN_ART_CAPTION = 'Textual form, woodcut interpretation · Carved patterns, colors and pose are artistic choices.'


def read(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


def write(path, value):
    (ROOT / path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


ROWS = [
    {
        'slug': 'qianlai', 'name': '钱来之山', 'en_name': 'Mount Qianlai', 'units': (3, 6),
        'description': '钱来山是《西山经》华山山列的起点。山上多松，山下多洗石；羬羊形状像羊，却拖着马一样的长尾。经文另记其脂的功效，郭注对洗石和“腊”分别作释，正文与注文在此分开阅读。',
        'en_description': 'Pines grow above washing stones at the opening mountain of the Hua range. Qianyang resembles a sheep with a horse’s tail. The text records a use for its fat, while the commentary explains the stones and the ailment separately.',
        'en_quote': 'The Western Mountains begin with the Hua range, whose first mountain is Qianlai. Pines are abundant above and washing stones below. A beast shaped like a sheep with a horse’s tail is called Qianyang. Its fat is said to treat cracked skin, as glossed in the commentary.',
        'subjects': ['钱来之山', '錢來之山', '松', '洗石', '羬羊'],
    },
    {
        'slug': 'songguo', 'name': '松果之山', 'en_name': 'Mount Songguo', 'units': (7, 9),
        'description': '钱来山向西四十五里，篇内次序来到松果山。濩水从这里流出，向北注入渭，水中多铜。随后写到䳋渠：形如山鸡，黑身赤足。鸟的记述接在水文之后，经文没有明说它生活在水中；其古籍功效字“𦢊”保留底本写法。',
        'en_description': 'Forty-five li west comes Songguo. The Huo River rises here and flows north into the Wei, with copper recorded in the water. The following bird, Tongqu, resembles a mountain pheasant with a black body and red feet; the wording does not explicitly make it aquatic.',
        'en_quote': 'Forty-five li west is Mount Songguo. The Huo River rises here and flows north into the Wei; copper is abundant in the water. There is a bird called Tongqu, shaped like a mountain pheasant, with a black body and red feet. It is said to treat the ailment written 𦢊, explained in the commentary as wrinkling or raised skin.',
        'subjects': ['松果之山', '濩水', '渭', '铜', '䳋渠', '𦢊'],
    },
    {
        'slug': 'taihua', 'name': '太华之山', 'en_name': 'Mount Taihua', 'units': (10, 14),
        'description': '再向西六十里是太华山，山势如削，四面方整。经文写其高五千仞、广十里，先称“鸟兽莫居”，接着记下一条名为肥𧔥的蛇，六足四翼，出现与大旱相连。这里并存保留这两层记述；郭注中的山名对应和仙人传说另列。',
        'en_description': 'Another sixty li west is Taihua, described as sheer and four-sided. After stating that birds and beasts do not dwell there, the text records Feiyi, a snake with six feet and four wings whose appearance is an omen of drought. Both statements are preserved.',
        'en_quote': 'Another sixty li west is Mount Taihua, sheer-cut and four-sided, five thousand ren high and ten li across. Birds and beasts do not dwell there. A snake called Feiyi has six feet and four wings; its appearance is said to herald a great drought throughout the land.',
        'subjects': ['太华之山', '太華之山', '肥𧔥', '六足', '四翼'],
    },
]

ROWS += [
    {
        'slug': 'xiaohua', 'name': '小华之山', 'en_name': 'Mount Xiaohua', 'units': (15, 21), 'batch': SECOND_BATCH,
        'description': '太华向西八十里是小华山。山中多荆𣏌与㸲牛，阴面有磬石，阳面有㻬琈之玉；赤鷩与萆荔接着出现。经文没有展开赤鷩的形貌，红腹、黄冠、绿头来自郭注。萆荔形如乌韭，既生石上，也缘木而生；功效作为古籍记述分存。',
        'en_description': 'Eighty li west of Taihua is Xiaohua, with shrubs, Zuoniu cattle, sounding stones and Tufu jade. Chibie and Bili follow. The bird’s red belly, yellow crown and green head come from the commentary; Bili resembles wujiu and grows on rocks and along trees.',
        'en_quote': 'Eighty li west is Mount Xiaohua. Its trees include jing and qi; its beasts include Zuoniu. Sounding stones occur on its shaded side and Tufu jade on its sunny side. Chibie birds are abundant and are said to ward off fire. Bili resembles wujiu, grows on rocks and also along trees, and is said to relieve heart pain when eaten.',
        'subjects': ['小华之山', '小華之山', '荆𣏌', '㸲牛', '磬石', '㻬琈之玉', '赤鷩', '萆荔'],
    },
    {
        'slug': 'fuyu', 'name': '符禺之山', 'en_name': 'Mount Fuyu', 'units': (22, 27), 'batch': SECOND_BATCH,
        'description': '再向西八十里，符禺山的阳面多铜，阴面多铁。文茎的果实如枣；名为條的草形如葵，红花、黄实，果实被比作婴儿舌。符禺水从山中流出，向北注渭。羊状赤鬣的葱聾与翠状赤喙的鴖，分别见于本山兽、鸟的记述。',
        'en_description': 'Fuyu lies another eighty li west, with copper and iron on opposing slopes. Wenjing bears jujube-like fruit. Its Tiao herb has kui-like form, red flowers and yellow tongue-shaped fruit. The Fuyu River flows north into the Wei. Conglong has a sheep-like form and red mane; Min resembles a cui bird with a red beak.',
        'en_quote': 'Eighty li west is Mount Fuyu, with copper on its sunny side and iron on its shaded side. Wenjing has fruit like jujubes and is said to relieve deafness. Tiao resembles kui, with red flowers and yellow fruit compared to an infant’s tongue; eating it is said to prevent confusion. The Fuyu River rises here and flows north into the Wei. Conglong resembles a sheep with a red mane. Min resembles a cui bird with a red beak and is said to ward off fire.',
        'subjects': ['符禺之山', '文茎', '文莖', '條', '符禺之水', '渭', '葱聾', '鴖'],
    },
    {
        'slug': 'shicui', 'name': '石脆之山', 'en_name': 'Mount Shicui', 'units': (28, 33), 'batch': SECOND_BATCH,
        'description': '符禺向西六十里是石脆山，多椶、柟。这里也有名为條的草，却形如韭，白花黑实，与符禺的同名草分开记录。阳面多㻬琈之玉，阴面多铜；灌水向北注入禺水，水文中记有流赭。郭注以“赤土”解释赭，经文另记涂牛马的功效。',
        'en_description': 'Sixty li west of Fuyu is Shicui, with zong and nan trees. Its Tiao herb resembles chives and has white flowers and black fruit, unlike the Fuyu plant of the same name. The Guan River flows north into the Yu; its water description records liuzhe, with zhe glossed as red earth.',
        'en_quote': 'Sixty li west is Mount Shicui, with zong and nan trees. Tiao resembles chives, with white flowers and black fruit, and is said to relieve scabies when eaten. Tufu jade occurs on the sunny side and copper on the shaded side. The Guan River rises here and flows north into the Yu. Liuzhe occurs in this water description; applying it to cattle and horses is said to keep them free of illness.',
        'subjects': ['石脆之山', '椶', '柟', '條', '㻬琈之玉', '灌水', '禺水', '流赭'],
    },
]

ROWS += [
    {
        'slug': 'ying', 'name': '英山', 'en_name': 'Mount Ying', 'units': (34, 40), 'batch': THIRD_BATCH,
        'description': '石脆向西七十里是英山，多杻、橿与箭、䉋，阴面多铁、阳面多赤金。禺水向北注入招水，水文中记有鳖状、羊声的䰷鱼；本卡不把羊声画成羊头。山段另列㸲牛、羬羊，又记黄身赤喙、鹑状的鸟肥遗，与太华山六足四翼的蛇分开。',
        'en_description': 'Seventy li west of Shicui is Ying, with trees, bamboos, iron and red metal. The Yu flows north into the Shao; its water account names turtle-shaped Bangyu with a sheep-like voice. Zuoniu and Qianyang are also listed. The quail-like, yellow-bodied, red-beaked Feiyi here is a bird, separate from Taihua’s snake.',
        'en_quote': 'Seventy li west is Mount Ying, with niu and jiang trees, iron on its shaded side and red metal on its sunny side. The Yu rises here and flows north into the Shao; Bangyu resemble turtles and sound like sheep. Arrow bamboos and mei bamboo grow on its sunny side. Zuoniu and Qianyang are abundant. A bird called Feiyi resembles a quail, with a yellow body and red beak; eating it is said to relieve li and kill parasites.',
        'subjects': ['英山', '杻', '橿', '禺水', '招水', '䰷魚', '䰷鱼', '箭䉋', '㸲牛', '羬羊', '肥遺', '肥遗'],
    },
    {
        'slug': 'zhushan', 'name': '竹山', 'en_name': 'Mount Zhu', 'units': (41, 49), 'batch': THIRD_BATCH,
        'description': '英山向西五十二里是竹山，多乔木、竹箭、铁与苍玉。黄雚形如樗、叶如麻，白花赤实。竹水向北注渭；丹水向东南注洛，随后水文记有水玉、人鱼。人鱼四脚的说明来自郭注，不作人身鱼尾。毫彘则像豚，白毛粗大如笄、末端黑；郭注的射物说法另列，不画成实际攻击。',
        'en_description': 'Fifty-two li west of Ying is Zhu, with tall trees, bamboo, iron and pale blue-green jade. Huangguan has hemp-like leaves, white flowers and red fruit. The Zhu flows north to the Wei; the Dan flows southeast to the Luo, followed by water minerals and Renyu. Four feet come from Renyu’s commentary. Haozhi is pig-like with thick white, black-tipped bristles.',
        'en_quote': 'Fifty-two li west is Mount Zhu, with tall trees and iron. Huangguan resembles chu, has hemp-like leaves, white flowers and red fruit; its appearance is compared to zhe. Bathing with it is said to relieve scabies and swelling. The Zhu River rises here and flows north into the Wei. Bamboo and pale blue-green jade occur on its sunny side. The Dan rises here and flows southeast into the Luo; water jade and Renyu follow in this water account. Haozhi resembles a pig with white hairs as thick as hairpins and black tips.',
        'subjects': ['竹山', '黄雚', '黃雚', '竹水', '渭', '丹水', '洛水', '水玉', '人魚', '人鱼', '毫彘'],
    },
    {
        'slug': 'fushan', 'name': '浮山', 'en_name': 'Mount Fu', 'units': (50, 53), 'batch': THIRD_BATCH,
        'description': '竹山向西百二十里是浮山，多盼木，原文记枳叶而无伤、木虫居之。薰草的麻叶、方茎、赤花、黑实各有明载；气味比作蘼芜，佩用功效只保留为古籍记述。浮山与前面的符禺山分别建卡，本段没有水源或河流记载，不补画水系。',
        'en_description': 'One hundred and twenty li west of Zhu is Fu, distinct from Fuyu. Panmu has leaves compared to zhi, does not injure, and houses wood insects. Xuncao has hemp-like leaves, square stems, red flowers and black fruit, with a scent compared to miwu. No river is described in this passage.',
        'en_quote': 'One hundred and twenty li west is Mount Fu, with much Panmu, whose leaves resemble zhi but do not injure; wood insects dwell in it. Xuncao has hemp-like leaves, square stems, red flowers and black fruit, and a scent like miwu. Wearing it is said to relieve li.',
        'subjects': ['浮山', '盼木', '木蟲', '薰草', '麻葉', '方莖', '赤華', '黑實', '蘼蕪'],
    },
]

ROWS += [{
    'slug': 'yuci', 'name': '羭次之山', 'en_name': 'Mount Yuci', 'units': (54, 60), 'batch': FOURTH_BATCH,
    'description': '浮山向西七十里是羭次山。漆水出山，向北注渭；山上多棫、橿，山下多竹箭，阴面多赤铜，阳面多嬰垣之玉。囂形如禺而长臂、善投；槖𩇯形如枭，人面独足，冬见夏蛰。郭注解释服用为着其毛羽，功效与异文另列。',
    'en_description': 'Seventy li west of Fu is Yuci. The Qi rises here and flows north into the Wei, among trees, bamboo, red copper and Yingyuan jade. Xiao is monkey-like with long arms and a skill for throwing. Tuofei is owl-like, with a human face and one foot, appearing in winter and dormant in summer. Wearing its feathers is explained separately in the commentary.',
    'en_quote': 'Seventy li west is Mount Yuci. The Qi rises here and flows north into the Wei. Yu and jiang trees grow above, with bamboo below; red copper occurs on the shaded side and Yingyuan jade on the sunny side. Xiao resembles a monkey, with long arms and skill at throwing. Tuofei resembles an owl, with a human face and one foot; it appears in winter and lies dormant in summer. Wearing it is said to remove fear of thunder.',
    'subjects': ['羭次之山', '漆水', '渭', '棫', '橿', '竹箭', '赤銅', '嬰垣之玉', '囂', '槖𩇯', '人面', '一足'],
}]

ROWS += [{
    'slug': 'shishan', 'name': '时山', 'en_name': 'Mount Shi', 'units': (61, 62), 'batch': FIFTH_BATCH,
    'description': '羭次向西百五十里是时山，经文明说无草木。逐水从山中流出，向北注渭，水中多水玉。郭注另记逐字或作遂；本卡保留底本逐字，不把异文当作另一条河流，也不将水玉确定为现代矿物。',
    'en_description': 'One hundred and fifty li west of Yuci is Shi, explicitly without grass or trees. The Zhu River rises here and flows north into the Wei, with much water jade. Guo Pu records sui as a variant of zhu. The source spelling is retained without making the variant a second river or identifying water jade as a modern mineral.',
    'en_quote': 'One hundred and fifty li west is Mount Shi, without grass or trees. The Zhu River rises here and flows north into the Wei; water jade is abundant in it.',
    'subjects': ['时山', '時山', '無草木', '逐水', '遂', '渭', '水玉'],
}]

ROWS += [{
    'slug': 'nanshan-west', 'name': '南山（西山经）', 'en_name': 'Mount Nan (Western Mountains)', 'units': (63, 65), 'batch': SIXTH_BATCH,
    'description': '时山向西百七十里是南山，属于《西山经》的山名，与《南山经》篇名分开。山上多丹粟，丹水出山向北注渭；兽多猛豹，鸟多尸鳩。熊状、小、短毛有光泽来自猛豹郭注；尸鳩的布谷类与鶘鸇比较异说并列，不强定现代物种。',
    'en_description': 'One hundred and seventy li west of Shi is Mount Nan in the Western Mountains, distinct from the Southern Mountains book. Dansu occurs above; the Dan rises here and flows north into the Wei. Mengbao and Shijiu are abundant. The small bear-like form and short glossy fur of Mengbao come from commentary. Shijiu has alternative comparisons, without a fixed modern species identification.',
    'en_quote': 'One hundred and seventy li west is Mount Nan, with much dansu above. The Dan River rises here and flows north into the Wei. Its beasts include many Mengbao, and its birds include many Shijiu.',
    'subjects': ['南山', '西山经南山', '丹粟', '丹水', '渭', '猛豹', '尸鳩', '尸鸠', '布谷', '鶘鸇'],
}]

ROWS += [{
    'slug': 'dashi', 'name': '大时之山', 'en_name': 'Mount Dashi', 'units': (66, 68), 'batch': SEVENTH_BATCH,
    'description': '南山向西百八十里是大时山，山上多榖、柞，山下多杻、橿，阴面多银，阳面多白玉。涔水向北注渭，清水向南注汉，分别保留两条水文关系。涔水郭注音潜，英文依此写Qian；榖作为木名保留，不写成粮食穀。',
    'en_description': 'One hundred and eighty li west of Nan is Dashi, with gu and zuo trees above, niu and jiang below, silver on its shaded side and white jade on its sunny side. The Qian flows north into the Wei, while the Qing flows south into the Han. These remain separate waters. Qian follows Guo Pu’s pronunciation gloss; gu is retained as a tree name, not grain.',
    'en_quote': 'One hundred and eighty li west is Mount Dashi, with gu and zuo above and niu and jiang below. Silver occurs on its shaded side and white jade on its sunny side. The Qian River rises here and flows north into the Wei. The Qing River rises here and flows south into the Han.',
    'subjects': ['大时之山', '大時之山', '榖', '柞', '杻', '橿', '銀', '白玉', '涔水', '音潜', '渭', '清水', '漢水', '汉水'],
}]

ROWS += [{
    'slug': 'bozhong', 'name': '嶓冡之山', 'en_name': 'Mount Bozhong', 'units': (69, 76), 'batch': EIGHTH_BATCH,
    'description': '大时向西三百二十里是嶓冡山。汉水出山向东南注沔，囂水另向北注汤水，两条水文分开；囂字缺字图经影印核定后只补入阅读引文。桃枝、鈎端及犀、兕、熊、羆分别列名，羆的熊状黄白色来自郭注。白翰、赤鷩分卡；蓇蓉叶如蕙、根如桔梗、黑花不实，食用记述另列。',
    'en_description': 'Three hundred and twenty li west of Dashi is Bozhong. The Han flows southeast into the Mian; the separate Xiao flows north into the Tang. An image glyph for Xiao was checked against the scan and restored only in the reading text. Named plants, beasts and birds retain separate sources. Pi’s bear-like yellow-and-white form comes from commentary. Gurong has hui-like leaves, a jiegeng-like root, black flowers and no fruit.',
    'en_quote': 'Three hundred and twenty li west is Mount Bozhong. The Han rises here and flows southeast into the Mian. The Xiao rises here and flows north into the Tang. Taozhi and Gouduan occur above. Its beasts include xi, si, bears and Pi; its birds include Baihan and Chibie. An herb called Gurong has leaves like hui, a root like jiegeng, black flowers and no fruit. Eating it is said to leave a person without children.',
    'subjects': ['嶓冡之山', '嶓冢', '漢水', '汉水', '沔', '囂水', '嚣水', '湯水', '汤水', '桃枝', '鈎端', '犀', '兕', '熊', '羆', '罴', '白翰', '赤鷩', '蓇蓉'],
}]

ROWS += [{
    'slug': 'tiandi', 'name': '天帝之山', 'en_name': 'Mount Tiandi', 'units': (77, 82), 'batch': NINTH_BATCH,
    'description': '嶓冡向西三百五十里是天帝山，上多㯶、柟，下多菅、蕙。谿邊形如狗，櫟鸟形如鹑、黑纹赤翁；郭注把翁解释为头下的毛，不改写成红色头冠。杜衡形如葵，气味如蘼芜；可以走马的两种解释分列在郭注中。山名不据此扩写成天帝居所或宫殿。',
    'en_description': 'Three hundred and fifty li west of Bozhong is Tiandi, with zong and nan above, and jian and hui below. Xibian is dog-shaped. The quail-like Li has black markings and a red feather tuft below the head, following the commentary on weng. Duheng resembles kui and smells like miwu. Two interpretations of its horse-related claim remain commentary; the mountain name does not establish a divine residence.',
    'en_quote': 'Three hundred and fifty li west is Mount Tiandi, with zong and nan above and jian and hui below. A dog-shaped beast is called Xibian; using its hide as a mat is said to protect against gu. A quail-shaped bird with black markings and red weng, glossed as feathers below the head, is called Li; eating it is said to relieve hemorrhoids. An herb shaped like kui and smelling like miwu is called Duheng. The text says it can help with horses, and that eating it relieves neck swellings; the horse claim has two commentary interpretations.',
    'subjects': ['天帝之山', '㯶', '柟', '菅', '蕙', '谿邊', '谿边', '溪边', '櫟', '栎', '黑文', '赤翁', '杜衡', '葵', '蘼蕪', '走馬'],
}]

ROWS += [{
    'slug': 'gaotu', 'name': '皐塗之山', 'en_name': 'Mount Gaotu', 'units': (83, 90), 'batch': TENTH_BATCH,
    'description': '天帝山向西南三百八十里是皐塗山。薔水向西注诸资，塗水向南注集获，两组水文分别阅读；薔的郭注音色，英文依此写Se。阳面丹粟、阴面银与黄金及山上桂木分别列名。白石礜与草無條各有毒鼠记述，不合为一种物。𤣎如鹿状、白尾、马足、人手、四角；郭注释前两脚似人手。數斯鸱状而人足，食用与异文另列。',
    'en_description': 'Three hundred and eighty li southwest of Tiandi is Gaotu. The Se flows west into Zhuzi, while the Tu flows south into Jihuo; these remain separate waters. Se follows Guo Pu’s pronunciation gloss. Dansu, silver, gold and gui trees are listed separately. The white stone Yu and herb Wutiao have separate mouse-poisoning claims. Yingru is deer-shaped with a white tail, horse feet, human hands and four horns; commentary assigns the hands to the front feet. Shusi is chi-shaped with human feet.',
    'en_quote': 'Three hundred and eighty li southwest is Mount Gaotu. The Se rises here and flows west into the Zhuzi; the Tu rises here and flows south into the Jihuo. Dansu occurs on its sunny side, silver and gold on its shaded side, and gui trees above. A white stone called Yu is said to poison mice. Wutiao resembles gaoyou, with kui-like leaves and red undersides, and is also said to poison mice. A deer-shaped beast with a white tail, horse feet, human hands and four horns is called Yingru. A chi-shaped bird with human feet is called Shusi. Eating it is said to relieve neck swellings; commentary records an alternative ailment character.',
    'subjects': ['皐塗之山', '皋涂', '薔水', '蔷水', '音色', '諸資', '诸资', '塗水', '涂水', '集獲', '集获', '丹粟', '銀', '黄金', '桂木', '礜', '槀苃', '無條', '无条', '赤背', '𤣎如', '白尾', '馬足', '人手', '四角', '數斯', '数斯', '人足'],
}]

ROWS += [{
    'slug': 'huangshan', 'name': '黄山（西山经）', 'en_name': 'Mount Huang (Western Mountains)', 'units': (91, 95), 'batch': ELEVENTH_BATCH,
    'description': '皐塗向西百八十里是黄山。经文无草木、多竹箭两句并存保留，不删其中一句来消解差异。盼水出山向西注赤水，郭注以眄释音，英文写Mian；随后记水中多玉，与南山经赤水分开。𤛎像牛，苍黑而大目，郭注音敏。鸚䳇像鸮，青羽、赤喙、人舌、能言；能字经影印核定后只修阅读引文，前后各两足趾来自郭注。郭注对汉代黄山地望说疑非此，不据此锁定现代地点。',
    'en_description': 'One hundred and eighty li west of Gaotu is Mount Huang. The text retains both no grass or trees and abundant bamboo without silently resolving the juxtaposition. The Mian (written Pan in the source, with Guo Pu’s pronunciation gloss) flows west into the Chi, followed by a record of jade in the water. Min is ox-shaped, blue-black and large-eyed; its pronunciation comes from commentary. Yingmu is owl-shaped with blue-green feathers, a red beak, a human tongue and speech. The image glyph for can was checked in the scan; two toes forward and two backward come from Guo Pu. His place comparison remains explicitly doubtful.',
    'en_quote': 'One hundred and eighty li west is Mount Huang, with no grass or trees but much bamboo. The Mian rises here and flows west into the Chi, with much jade in the water. A beast shaped like an ox, blue-black and large-eyed, is called Min. A bird shaped like an owl, with blue-green feathers, a red beak and a human tongue, can speak; it is called Yingmu.',
    'subjects': ['黄山', '黃山', '無草木', '竹箭', '盼水', '赤水', '玉', '𤛎', '音敏', '蒼黑', '大目', '鸚䳇', '鹦鹉', '青羽', '赤喙', '人舌', '能言', '脚指前後各兩', '疑非此'],
}]

ROWS += [{'slug': 'cuishan',
 'name': '翠山',
 'en_name': 'Mount Cui',
 'units': (96, 99),
 'batch': 'xishan-cuishan',
 'description': '黄山向西二百里是翠山。山上多㯶、枏，山下多竹箭；阳面多黄金、玉，阴面多旄牛、麢、麝，分别列卡。鸓像鹊，赤黑、四足，郭注音壘；本底本印作西首，另见《古今图书集成》引文两首，配图参照双首异文并明示区别，不暗改原文。可以禦火仅作古籍记述。末字火实际在影印44页末列，电子捕获45页保留。',
 'en_description': 'Two hundred li west of Huang lies Mount Cui. Zong and nan trees grow above, with zhujian '
                   'bamboo below; gold and jade occur on the sunny side, while maoniu, ling and musk deer '
                   'occur on the shaded side. Lei is magpie-shaped, red and black, with four feet. This '
                   'edition prints xi shou, while a quotation in the Gujin Tushu Jicheng reads two heads; '
                   'the illustration follows that variant explicitly. Its fire-averting claim is retained as '
                   'an ancient account. The final character fire is on scan page44 despite its captured '
                   'page45.',
 'en_quote': 'Two hundred li west lies Mount Cui, with zong and nan trees above and zhujian bamboo below. '
             'Its sunny side has gold and jade, and its shaded side maoniu, ling and musk deer. Its birds '
             'include Lei, magpie-shaped, red and black, with four feet; this edition prints xi shou where '
             'another quoted version reads two heads. It is said to avert fire.',
 'subjects': ['翠山',
              '㯶',
              '棕',
              '枏',
              '楠',
              '竹箭',
              '黄金',
              '玉',
              '旄牛',
              '麢',
              '羚',
              '麝',
              '鸓',
              '音壘',
              '西首',
              '兩首',
              '四足',
              '禦火']}]

ROWS += [{'slug': 'guishan',
 'name': '騩山',
 'en_name': 'Mount Gui',
 'units': (100, 102),
 'batch': 'xishan-guishan',
 'description': '翠山向西二百五十里是騩山，临西海；錞的郭注以堤埻说明。山无草木、多玉。淒水出山向西注海，水文后记采石、黄金，又记多丹粟，分别列卡而不外推矿产范围。郭注以有彩色之石释采石，其矿物举例保留为注文，不当作本山逐项确认矿种。山名释音电子录文有省缺，按原样保留并说明；不锁定现代山海地望。',
 'en_description': 'Two hundred and fifty li west of Cui lies Mount Gui beside the Western Sea; Guo Pu '
                   'explains chun with an embankment comparison. It has no grass or trees and much jade. The '
                   'Qi rises here and flows west into the sea, followed by colored stones, gold and dansu. '
                   'These remain separate records without extending their distribution. The commentary '
                   'explains colored stones with mineral examples, which do not establish each mineral here. '
                   'The captured name gloss is incomplete and retained explicitly, without a modern '
                   'location.',
 'en_quote': 'Two hundred and fifty li west is Mount Gui, bordering the Western Sea. It has no grass or '
             'trees and much jade. The Qi rises here and flows west into the sea, with many colored stones '
             'and gold; much dansu is also recorded.',
 'subjects': ['騩山', '音巍', '西海', '海', '錞', '堤埻', '無草木', '玉', '淒水', '凄水', '浽', '采石', '彩石', '黄金', '丹粟']}]

ROWS += [{'slug': 'range1-summary',
 'name': '西山首列总括与祭礼',
 'en_name': 'Western first range · Summary and rites',
 'units': (103, 111),
 'batch': 'xishan-range1-summary',
 'is_summary': True,
 'description': '本段总括钱来至騩山十九山、二千九百五十七里，不新增一座山。華山冢也及太牢祠礼、羭山所用燭与百日斋及百数玉器、其余十七山一羊之祠分别阅读。冢为神之所舍、太牢用牛羊豕、瑜为玉名等是郭注解释；不补神的形貌或实际祭祀场面。末句燭者百草之未灰白蒂采等純之按底本保留，不擅改白蒂或猜定断句。',
 'en_description': 'This summary gives nineteen mountains from Qianlai to Gui and a total of 2957 li; it does '
                   'not add another mountain. It distinguishes Hua’s zhong status and tailao offering, Yu’s '
                   'zhu rite with a hundred-day observance and counted jade offerings, and a single sheep '
                   'for the other seventeen mountains. Explanations of zhong, tailao and yu-jade belong to '
                   'Guo Pu’s commentary. No deity appearance or ritual scene is invented. The final '
                   'difficult wording on zhu, bai di and patterned borders is retained without silently '
                   'emending it.',
 'en_quote': 'The first Western range runs from Qianlai to Gui: nineteen mountains and 2957 li. Hua is its '
             'zhong; its rite uses tailao. The text then describes the Yu rite, zhu, a hundred-day '
             'observance, offerings counted in hundreds, yu-jade, wine, gui and bi jades. The other '
             'seventeen mountains receive one sheep each. The concluding wording on zhu, bai di and '
             'patterned borders is retained with the edition commentary rather than given a speculative '
             'fluent translation.',
 'subjects': ['西山首列',
              '总括',
              '十九山',
              '二千九百五十七里',
              '華山',
              '冢',
              '太牢',
              '羭山',
              '燭',
              '齋百日',
              '百犧',
              '百瑜',
              '百樽',
              '珪',
              '璧',
              '十七山',
              '毛牷',
              '白蒂',
              '純']}]

ROWS += [{
    'slug': 'qianshan', 'name': '鈐山', 'en_name': 'Mount Qian', 'units': (112, 113),
    'batch': FOURTEENTH_BATCH, 'range': 2,
    'description': '鈐山是西次二经的起点。经文只记山上多铜、山下多玉，树木多杻与橿，没有交代它与前一山列的方向或距离，也没有鸟兽、水系记述。杻、橿保留为两个古木名，不据名称补定现代树种、花果或叶形。山名读音与冷、塗异写另见郭注。',
    'en_description': 'Qian opens the second Western range. Copper is abundant above and jade below; its trees include niu and jiang. No direction or distance from the preceding range is given, and no animals or waterways are recorded here. The two old tree names do not establish modern species, flowers, fruit or leaf forms. Pronunciation and variant mountain names remain in the commentary.',
    'en_quote': 'The second Western range begins with Mount Qian. Copper is abundant above, jade below, and its trees include niu and jiang.',
    'subjects': ['鈐山', '西次二經', '西次二经', '铜', '銅', '玉', '杻', '橿'],
}]


ROWS += [{
    'slug': 'taimao', 'name': '㤗冐之山', 'en_name': 'Mount Taimao', 'units': (114, 116),
    'batch': FIFTEENTH_BATCH, 'range': 2,
    'description': '鈐山向西二百里是㤗冐之山，阳面多金，阴面多铁。浴水从山中流出，向东注于河，水中多藻玉与白蛇。藻玉的纹彩解释和白蛇为水蛇的说明出自郭注；山名保留㤗冐底本字形，或作秦不改入正文。本段没有山高、草木或现代坐标。',
    'en_description': 'Two hundred li west of Qian is Mount Taimao, with jin metal on its sunny side and iron on its shaded side. The Yu River rises here and flows east into the He; patterned jade and white snakes are recorded in the water. The jade gloss and identification of the snakes as water snakes belong to the commentary. Edition mountain characters and the Qin variant remain distinct; no height, vegetation or modern coordinates are supplied.',
    'en_quote': 'Two hundred li west is Mount Taimao. Jin metal is abundant on its sunny side and iron on its shaded side. The Yu River rises here and flows east into the He; its waters contain much zaoyu jade and many white snakes.',
    'subjects': ['㤗冐之山', '太冐', '太冒', '金', '鐡', '铁', '浴水', '河', '藻玉', '白蛇'],
}]


ROWS += [{
    'slug': 'shuli', 'name': '數歴之山', 'en_name': 'Mount Shuli', 'units': (117, 119), 'range': 2, 'batch': SIXTEENTH_BATCH,
    'description': '㤗冐山向西一百七十里是數歴山，山上多黄金，山下多银，树木多杻与橿，鸟多鸚䳇。楚水从这里流出，向南注渭，水中多珠。鸚䳇在本段只列名，不补入黄山段的青羽、赤喙、人舌等形貌；郭注所举蜀郡平泽青珠不移作本山珠的颜色。',
    'en_description': 'One hundred and seventy li west of Taimao is Shuli, with gold above, silver below, niu and jiang trees, and many Yingmu birds. The Chu River rises here and flows south into the Wei; pearls are recorded in the water. Yingmu is only named here, without importing Huang’s plumage, beak or tongue description. The commentary’s example of blue-green pearls elsewhere does not determine local pearl colors.',
    'en_quote': 'Another one hundred and seventy li west is Mount Shuli. Gold is abundant above and silver below. Its trees include niu and jiang, and its birds include many Yingmu. The Chu River rises here and flows south into the Wei; its waters contain many pearls.',
    'subjects': ['數歴之山', '数历山', '數歷山', '黄金', '銀', '银', '杻', '橿', '鸚䳇', '楚水', '渭', '珠'],
}]


ROWS += [{
    'slug': 'gaoshan', 'name': '髙山', 'en_name': 'Mount Gao', 'units': (120, 123), 'range': 2, 'batch': SEVENTEENTH_BATCH,
    'description': '數歴山向西一百五十里是髙山，山上多银，山下多青碧与雄黄，树木多㯶，草类多竹。涇水从这里流出，向东注渭，后接其中多磬石青碧。山下与水文中的青碧分别保存；郭注的玉类解释、山崩出雄黄旧例与涇水古地名另列，不补现代坐标或实际河道。',
    'en_description': 'One hundred and fifty li west of Shuli is Gao, with silver above, qingbi and xionghuang minerals below, zong trees and bamboo. The Jing River rises here and flows east into the Wei, followed by sounding stones and qingbi in the water account. Mountain-side and water-context qingbi remain separate. Jade glosses, a historical mineral example and the river’s old place names belong to commentary, without modern coordinates or a reconstructed course.',
    'en_quote': 'Another one hundred and fifty li west is Mount Gao. Silver is abundant above, and qingbi and xionghuang below. Its trees include many zong, and its grasses include much bamboo. The Jing River rises here and flows east into the Wei; the waters contain many sounding stones and qingbi.',
    'subjects': ['髙山', '高山', '銀', '银', '青碧', '雄黄', '㯶', '竹', '涇水', '泾水', '渭', '磬石'],
}]


ROWS += [{
    'slug': 'nvchuang', 'name': '女牀之山', 'en_name': 'Mount Nvchuang', 'units': (124, 127), 'range': 2, 'batch': EIGHTEENTH_BATCH,
    'description': '髙山向西南三百里是女牀山，阳面多赤铜，阴面多石𣵀，兽多虎、豹、犀、兕。有鸟形如翟，具五彩纹，名为鸞鳥；见则天下安宁是经文的瑞应记述。四兽在此只列名，不移入别山形貌；鸞鳥正文与郭注似鸡、旧瑞鸟故事分开，石𣵀也不直接鉴定为现代矿物。',
    'en_description': 'Three hundred li southwest of Gao is Nvchuang, with red copper on its sunny side and shi nie on its shaded side. Tigers, leopards, xi and si are named without separate forms. The Luan bird resembles a zhai and has five-colored markings; its appearance is described as an omen of peace. The main text remains distinct from the commentary’s chicken comparison and older auspicious-bird account, without a modern mineral or animal identification.',
    'en_quote': 'Three hundred li southwest is Mount Nvchuang. Red copper is abundant on its sunny side and shi nie on its shaded side. Its beasts include tigers, leopards, xi and si. A bird shaped like a zhai with five-colored markings is called Luan; its appearance is said to herald peace throughout the world.',
    'subjects': ['女牀之山', '女床山', '赤銅', '赤铜', '石𣵀', '虎', '豹', '犀', '兕', '鸞鳥', '鸾鸟', '翟', '五彩文'],
}]

ROWS += [{
    'slug': 'longshou', 'name': '龍首之山', 'en_name': 'Mount Longshou', 'units': (128, 129), 'range': 2, 'batch': NINETEENTH_BATCH,
    'description': '女牀山向西二百里是龍首山，阳面多黄金，阴面多鐡。苕水从这里流出，向东南注入涇水，水文后接其中多羙玉。此苕水与南山经同名水分别保存；涇水沿用髙山条目并保留东流注渭的原记述。山名不作为龙形生物的依据，不补现代坐标或完整河道。',
    'en_description': 'Two hundred li west of Nvchuang is Longshou, with gold on its sunny side and iron on its shaded side. The Tiao rises here and flows southeast into the Jing, followed by fine jade in the water account. This Tiao remains separate from its Southern Mountains namesake. The existing Jing record retains Gao’s eastward flow into the Wei. No dragon creature, modern coordinates or complete river course is inferred.',
    'en_quote': 'Another two hundred li west is Mount Longshou. Its sunny side has much gold and its shaded side much iron. The Tiao River rises here and flows southeast into the Jing; the waters contain much fine jade.',
    'subjects': ['龍首之山', '龙首山', '黄金', '鐡', '铁', '苕水', '涇水', '泾水', '羙玉', '美玉'],
}]

ROWS += [{
    'slug': 'lutai', 'name': '鹿臺之山', 'en_name': 'Mount Lutai', 'units': (130, 132), 'range': 2, 'batch': TWENTIETH_BATCH,
    'description': '龍首山向西二百里是鹿臺山，山上多白玉，山下多银，兽多㸲牛、羬羊、白豪。有鸟形如雄鸡而具人面，名鳬徯，其名自呌，见则有兵。前三兽在本段只列名，不借其他山段形貌；白豪的豪貆猪也与山名下今在上郡均属郭注。兵事记述作为古籍征兆保存，不补现代地点或事件。',
    'en_description': 'Two hundred li west of Longshou is Lutai, with white jade above and silver below. Its beasts include Zuoniu, Qianyang and Baihao, named here without forms borrowed from other passages. The Fuxi bird resembles a rooster with a human face, cries its own name, and is described as an omen of warfare. The Baihao gloss and old Shangjun location belong to commentary, without a modern location or event identification.',
    'en_quote': 'Another two hundred li west is Mount Lutai. White jade is abundant above and silver below. Its beasts include Zuoniu, Qianyang and Baihao. A bird shaped like a rooster with a human face is called Fuxi; its name comes from its own cry. Its appearance is said to herald warfare.',
    'subjects': ['鹿臺之山', '鹿台山', '白玉', '銀', '银', '㸲牛', '羬羊', '白豪', '鳬徯', '凫徯', '雄雞', '人面', '上郡'],
}]

ROWS += [{
    'slug': 'niaowei', 'name': '鳥危之山', 'en_name': 'Mount Niaowei', 'units': (133, 135), 'range': 2, 'batch': TWENTY_FIRST_BATCH,
    'description': '鹿臺山向西南二百里是鳥危山，阳面多磬石，阴面多檀、楮，其中多女牀。鳥危水出山向西注赤水，水文后接其中多丹粟。楮即榖木、女牀未詳分别属郭注，不将女牀解释为女牀山、生物或床具。赤水与黄山段共用西山经条目并保留各自出处，与南山同名水分别保存，不补现代河道。',
    'en_description': 'Two hundred li southwest of Lutai is Niaowei, with sounding stones on its sunny side and tan and chu trees on its shaded side. Nvchuang is also named, but its referent is left unexplained in the commentary. The Niaowei River rises here and flows west into the Chi, followed by dansu in the water account. The chu gloss is separate. The Western Chi retains Huang and Niaowei sources, separately from its Southern namesake, without a modern course.',
    'en_quote': 'Two hundred li southwest is Mount Niaowei. Its sunny side has many sounding stones and its shaded side many tan and chu trees. There is much nvchuang. The Niaowei River rises here and flows west into the Chi; the waters contain much dansu.',
    'subjects': ['鳥危之山', '鸟危山', '磬石', '檀', '楮', '榖木', '女牀', '女床', '鳥危之水', '鸟危水', '赤水', '丹粟'],
}]

ROWS += [{
    'slug': 'xiaoci', 'name': '小次之山', 'en_name': 'Mount Xiaoci', 'units': (136, 138), 'range': 2, 'batch': TWENTY_SECOND_BATCH,
    'description': '鳥危山向西四百里是小次山，山上多白玉，山下多赤铜。有兽形如猿，白首赤足，名朱厭，见则大兵。兵事征兆作为古籍记述保存；郭注另列见则有兵起焉、见则为兵两种异文，不替换正文或补造战争事件。没有记水文，也不补现代地望或朱厭额外器官。',
    'en_description': 'Four hundred li west of Niaowei is Xiaoci, with white jade above and red copper below. Zhuyan resembles an ape with a white head and red feet; its appearance is described as an omen of great warfare. Two alternative omen wordings remain separate in commentary rather than replacing the main text. No river, modern location, extra body parts or historical war is inferred.',
    'en_quote': 'Another four hundred li west is Mount Xiaoci. White jade is abundant above and red copper below. A beast shaped like an ape, with a white head and red feet, is called Zhuyan. Its appearance is said to herald great warfare.',
    'subjects': ['小次之山', '小次山', '白玉', '赤銅', '赤铜', '朱厭', '朱厌', '猨', '猿', '白首', '赤足', '大兵'],
}]

ROWS += [{
    'slug': 'daci', 'name': '大次之山', 'en_name': 'Mount Daci', 'units': (139, 140), 'range': 2, 'batch': TWENTY_THIRD_BATCH,
    'description': '小次山向西三百里是大次山，阳面多堊，阴面多碧，兽多㸲牛、麢羊。堊似土色甚白、音惡是郭注解释，分别保留，不将白色移给两兽。两兽在本段只列名，不借其他山的形貌或功效；碧不沿用髙山郭注作现代玉种鉴定，本段没有水文或现代坐标。',
    'en_description': 'Three hundred li west of Xiaoci is Daci, with e on its sunny side and bi on its shaded side. Its beasts include Zuoniu and Lingyang, named without separate forms. The soil-like, very white description and pronunciation of e belong to commentary, not the beasts. No other passage’s forms, uses or jade glosses are imported, and no river or modern location is supplied.',
    'en_quote': 'Another three hundred li west is Mount Daci. Its sunny side has much e and its shaded side much bi. Its beasts include Zuoniu and Lingyang.',
    'subjects': ['大次之山', '大次山', '堊', '垩', '碧', '㸲牛', '麢羊', '羚羊'],
}]

ROWS += [{'slug': 'xunwu',
  'name': '薰吳之山',
  'en_name': 'Mount Xunwu',
  'units': [141, 141],
  'range': 2,
  'batch': 'xishan-xunwu',
  'description': '大次山向西四百里是薰吳山，无草木，多金、玉。金与玉分别索引，正文没有说黄金，也没有兽类、水文或功效；不从吳字推导国域或人物。',
  'en_description': 'Four hundred li west of Daci is Xunwu, with no grass or trees and much jin and jade. Jin and '
                    'jade retain separate entries; the text does not specify gold, beasts, rivers or uses. No '
                    'country or person is inferred from the name.',
  'en_quote': 'Another four hundred li west is Mount Xunwu. It has no grass or trees and much jin and jade.',
  'subjects': ['薰吳之山', '薰吴山', '無草木', '金', '玉'],
  'content_note': '0141全见49页，0142另山。無草木与多金玉均保留；金不自动改黄金，无生物不加生物占位。',
  'en_content_note': 'Unit141 is on scan49;142 begins the next mountain. Both no vegetation and jin/jade remain. Jin '
                     'is not silently changed to gold; no creature is inferred.',
  'relations': [{'ids': ['place-xishan-daci', 'place-xishan-xunwu'],
                 'source': '《西山经》',
                 'quote': '又西四百里曰薰吳之山',
                 'labels': ['下一山 · 向西四百里', '上一山 · 大次山']}]}]

ROWS += [{'slug': 'quyang',
  'name': '𢇨陽之山',
  'en_name': 'Mount 𢇨yang',
  'units': [142, 144],
  'range': 2,
  'batch': 'xishan-quyang',
  'description': '薰吳山向西四百里是𢇨陽山，木多稷、柟、豫章，兽列犀、兕、虎、犳、㸲牛。稷与豫章的形貌来自郭注；五兽正文只列名。影印犳与捕获豹的差异明示，犳的音注不移给其他兽；山名音𭥍保留录文，不猜现代地名或音读。',
  'en_description': 'Four hundred li west of Xunwu is the mountain written 𢇨yang. Its trees include ji, nan and '
                    'yuzhang; its beasts include xi, si, tigers, zhuo and Zuoniu. Tree descriptions and the zhuo '
                    'pronunciation belong to commentary. The scan’s zhuo character differs from the captured leopard '
                    'character; forms of the five beasts and a modern place or unverified pronunciation are not '
                    'supplied.',
  'en_quote': 'Another four hundred li west is Mount 𢇨yang. Its trees include ji, nan and yuzhang; its beasts '
              'include xi, si, tigers, zhuo and Zuoniu.',
  'subjects': ['𢇨陽之山', '𢇨阳山', '稷', '柟', '豫章', '犀', '兕', '虎', '犳', '豹', '㸲牛', '音𭥍'],
  'content_note': '0142—0144全见49页，144捕获50页但牛与犳音注均在49页末列。正文影印犳而快照豹，仅阅读引文补犳，captured_text/快照不改。音𭥍原样保留，内部quyang标识不对现代音读背书。稷似松有剌細理音即与豫章后续郭注分别连读。',
  'en_content_note': 'Units142–144 are on scan49, including the final ox character and zhuo gloss despite144 being '
                     'captured as50. Only the reading quotation restores the scan’s zhuo character; captured text '
                     'and snapshot remain. The captured name-pronunciation glyph is retained without a speculative '
                     'reading; quyang is an internal identifier. Tree glosses are joined separately.',
  'text_replacements': {'犀兕虎豹㸲牛': '犀兕虎犳㸲牛'},
  'relations': [{'ids': ['place-xishan-xunwu', 'place-xishan-quyang'],
                 'source': '《西山经》',
                 'quote': '又西四百里曰𢇨陽之山',
                 'labels': ['下一山 · 向西四百里', '上一山 · 薰吳山']}]}]

ROWS += [{'slug': 'zhongshou',
  'name': '衆獸之山',
  'en_name': 'Mount Zhongshou',
  'units': [145, 146],
  'range': 2,
  'batch': 'xishan-zhongshou',
  'description': '𢇨陽山向西二百五十里是衆獸山，山上多㻬琈之玉，山下多檀、楮和黄金，兽多犀、兕。本段只列物产和兽名，没有㻬琈、檀楮或两兽的新形貌注，不因山名衆獸而补其他生物。',
  'en_description': 'Two hundred and fifty li west of 𢇨yang is Zhongshou, with tufu jade above, tan and chu trees '
                    'and gold below, and xi and si among its beasts. No forms or glosses are imported from '
                    'namesakes, and the mountain’s name does not establish additional creatures.',
  'en_quote': 'Another two hundred and fifty li west is Mount Zhongshou. Above is much tufu jade; below are many tan '
              'and chu trees and much gold. Its beasts include xi and si.',
  'subjects': ['衆獸之山', '众兽山', '㻬琈之玉', '檀', '楮', '黄金', '犀', '兕'],
  'content_note': '0145—0146均见50页，147皇人另段。山上与山下分列，犀兕仅列名；不移用小华㻬琈玉名注或鳥危楮注。',
  'en_content_note': 'Units145–146 are on scan50;147 begins Huangren. Upper and lower products remain distinct; xi '
                     'and si are only named. Xiaohua’s jade and Niaowei’s chu glosses are not imported.',
  'relations': [{'ids': ['place-xishan-quyang', 'place-xishan-zhongshou'],
                 'source': '《西山经》',
                 'quote': '又西二百五十里曰衆獸之山',
                 'labels': ['下一山 · 向西二百五十里', '上一山 · 𢇨陽山']}]}]

ROWS += [{'slug': 'huangren',
  'name': '皇人之山',
  'en_name': 'Mount Huangren',
  'units': [147, 149],
  'range': 2,
  'batch': 'xishan-huangren',
  'description': '衆獸山向西五百里是皇人山，山上多金、玉，山下记青雄黄。即雌黄也、或曰空青曽青之属为郭注，青雄黄连写不在此强定现代矿种或分词。皇水出山向西注赤水，水文后接丹粟；赤水沿用西山条目补本段出处，不扩展丹粟至全河。',
  'en_description': 'Five hundred li west of Zhongshou is Huangren, with jin and jade above and the continuous '
                    'mineral wording qing xionghuang below. The alternative mineral comparisons belong to '
                    'commentary, without a forced modern identification or segmentation. The Huang rises here and '
                    'flows west into the Chi, followed by dansu in the water account. The Western Chi keeps this '
                    'additional source without extending dansu to its entire course.',
  'en_quote': 'Another five hundred li west is Mount Huangren. Above are much jin and jade, and below qing '
              'xionghuang. The Huang River rises here and flows west into the Chi; the waters contain much dansu.',
  'subjects': ['皇人之山', '皇人山', '金', '玉', '青雄黄', '雌黄', '空青', '曽青', '皇水', '赤水', '丹粟'],
  'content_note': '0147—0149均见50页，青雄/黄跨147—148连读，丹粟跨148—149续。郭注即雌黄也或曰空青曽青之属存于矿物组，不移给皇水。保留连写分词歧义；山名不新增人物。赤水共享摘要、三出处及旧黄山配图复用范围需同步更新。',
  'en_content_note': 'Units147–149 are on scan50; mineral wording and dansu continue across lines. The mineral '
                     'comparisons are not a river gloss. Continuous wording retains its segmentation ambiguity; no '
                     'person is inferred from the mountain name. The shared Chi summary, three sources and reused '
                     'Huang scene remain explicit.',
  'relations': [{'ids': ['place-xishan-zhongshou', 'place-xishan-huangren'],
                 'source': '《西山经》',
                 'quote': '又西五百里曰皇人之山',
                 'labels': ['下一山 · 向西五百里', '上一山 · 衆獸山']},
                {'ids': ['place-xishan-huangren', 'water-xishan-chi-huangshan'],
                 'source': '《西山经》',
                 'quote': '皇水出焉西流注于赤水',
                 'labels': ['山段中的水文', '水文所在山段']},
                {'ids': ['water-xishan-huang-huangren', 'water-xishan-chi-huangshan'],
                 'source': '《西山经》',
                 'quote': '皇水出焉西流注于赤水',
                 'labels': ['向西流入', '来水 · 皇水']},
                {'ids': ['water-xishan-huang-huangren', 'material-xishan-dansu-huangren'],
                 'source': '《西山经》',
                 'quote': '皇水出焉西流注于赤水其中多丹粟',
                 'labels': ['同段水文中的物产', '水文上下文']}]}]

ROWS += [{'slug': 'zhonghuang',
  'name': '中皇之山',
  'en_name': 'Mount Zhonghuang',
  'units': [150, 151],
  'range': 2,
  'batch': 'xishan-zhonghuang',
  'description': '皇人山向西三百里是中皇山，山上多黄金，山下多蕙棠。蕙字据影印补入阅读引文，原始缺字图标记保留；彤棠之属也、或作羔是郭注，正文连写蕙棠不强分为两种确定草木。山名不补人物或宫殿。',
  'en_description': 'Three hundred li west of Huangren is Zhonghuang, with gold above and huitang below. The scan '
                    'restores hui only in the reading quotation; the captured image-glyph marker remains. The '
                    'tongtang comparison and alternative character belong to commentary, without forcing two '
                    'separate plant identifications or adding a person or palace.',
  'en_quote': 'Another three hundred li west is Mount Zhonghuang. Gold is abundant above and huitang below.',
  'subjects': ['中皇之山', '中皇山', '黄金', '蕙棠', '蕙', '彤棠', '羔'],
  'content_note': '0150—0151均见50页，151空正文郭注归蕙棠，152西皇另段。影印蕙字补阅读引文，captured_text和原快照仍存缺字图；彤棠之属也或作羔按录文保留，不猜现代植物。',
  'en_content_note': 'Units150–151 are on scan50; annotation-only151 belongs to huitang and152 starts Xihuang. The '
                     'reading quotation restores hui from the scan, while captured text and snapshot retain the '
                     'image marker. The captured gloss is not a modern plant identification.',
  'text_replacements': {'⟦缺字图:蕙⟧': '蕙'},
  'relations': [{'ids': ['place-xishan-huangren', 'place-xishan-zhonghuang'],
                 'source': '《西山经》',
                 'quote': '又西三百里曰中皇之山',
                 'labels': ['下一山 · 向西三百里', '上一山 · 皇人山']}]}]

ROWS += [{'slug': 'xihuang',
  'name': '西皇之山',
  'en_name': 'Mount Xihuang',
  'units': [152, 153],
  'range': 2,
  'batch': 'xishan-xihuang',
  'description': '中皇山向西三百五十里是西皇山，阳面多金，阴面多鐡，兽多麋、鹿、㸲牛。麋大如小牛、鹿属也是郭注，只作古籍比较，不补麋的其他形貌或移给鹿和㸲牛；金不擅改黄金。',
  'en_description': 'Three hundred and fifty li west of Zhonghuang is Xihuang, with jin on its sunny side and iron '
                    'on its shaded side. Its beasts include mi, deer and Zuoniu. The comparison of mi with a small '
                    'ox and its classification with deer belong only to commentary; no further forms are supplied or '
                    'transferred to the other beasts. Jin is not silently changed to gold.',
  'en_quote': 'Another three hundred and fifty li west is Mount Xihuang. Its sunny side has much jin and its shaded '
              'side much iron. Its beasts include mi, deer and Zuoniu.',
  'subjects': ['西皇之山', '西皇山', '金', '鐡', '铁', '麋', '鹿', '㸲牛'],
  'content_note': '0152—0153均见50页，153兽名及麋注不在捕获51页；154萊山另段。麋注只解释麋，麋鹿㸲牛分别索引，不据同属鹿固定现代物种。',
  'en_content_note': 'Units152–153 are on scan50, including the beasts and mi gloss despite153 being captured as51. '
                     'Unit154 begins Lai. The gloss belongs only to mi; the three beasts remain separately indexed '
                     'without modern species identification.',
  'relations': [{'ids': ['place-xishan-zhonghuang', 'place-xishan-xihuang'],
                 'source': '《西山经》',
                 'quote': '又西三百五十里曰西皇之山',
                 'labels': ['下一山 · 向西三百五十里', '上一山 · 中皇山']}]}]

ROWS += [{'slug': 'laishan',
  'name': '萊山',
  'en_name': 'Mount Lai',
  'units': [154, 155],
  'range': 2,
  'batch': 'xishan-laishan',
  'description': '西皇山向西三百五十里是萊山，木多檀、楮，鸟多羅羅，是食人。食人作为古籍记述保留；郭注称羅羅之鸟所未詳也，不补形貌或沿用其他鸟的身体。随后次二经总括与本山分段。',
  'en_description': 'Three hundred and fifty li west of Xihuang is Lai, with tan and chu trees and many Luoluo '
                    'birds, described as eating people. Commentary leaves the bird unexplained. No form is invented '
                    'or borrowed from another bird, and the following range summary remains a separate passage.',
  'en_quote': 'Another three hundred and fifty li west is Mount Lai. Its trees include tan and chu, and its birds '
              'include many Luoluo, which are said to eat people.',
  'subjects': ['萊山', '莱山', '檀', '楮', '羅羅', '罗罗', '食人'],
  'content_note': '0154—0155全见51页；0156起本列总括，不并入萊山。羅羅形貌未详，郭注所未詳也不改成不存在正文食人记述。',
  'en_content_note': 'Units154–155 are on scan51;156 begins the range summary. Luoluo has no supplied form; the '
                     'commentary’s uncertainty does not remove the main text’s people-eating statement.',
  'relations': [{'ids': ['place-xishan-xihuang', 'place-xishan-laishan'],
                 'source': '《西山经》',
                 'quote': '又西三百五十里曰萊山',
                 'labels': ['下一山 · 向西三百五十里', '上一山 · 西皇山']}]}]

ROWS += [{'slug': 'range2-summary',
  'name': '西次二经总括与祭礼',
  'en_name': 'Western second range · Summary and rites',
  'units': [156, 161],
  'range': 2,
  'batch': 'xishan-range2-summary',
  'description': '本段总括鈐山至萊山十七山、四千一百四十里，不新增山。十神人面马身；七神人面牛身、四足一臂、操杖而行，后接飞兽之神。少牢与白菅之席、十軰神一雄鷄鈐而不糈毛采分列。羊猪少牢、軰音背、鈐器名未詳及不糈解释属于郭注，不猜造神名、器形或祭祀实景。',
  'en_description': 'This summary gives seventeen mountains from Qian to Lai and 4140 li, without adding a mountain. '
                    'Ten deities have human faces and horse bodies; seven have human faces, ox bodies, four feet and '
                    'one arm, carrying a staff, followed by the flying-beast deity wording. Shaolao and white jian '
                    'seats remain separate from the ten-bei rite with a rooster, qian, no xu and mao cai. Offering '
                    'and uncertain-vessel glosses remain commentary without invented names, vessel forms or ritual '
                    'scenes.',
  'en_quote': 'The second Western range runs from Qian to Lai: seventeen mountains and 4140 li. Ten deities have '
              'human faces and horse bodies. Seven have human faces, ox bodies, four feet and one arm and carry a '
              'staff; the text then calls them flying-beast deities. The offerings include shaolao and white jian '
              'seats. The separate ten-bei rite records one rooster, qian without xu, and mao cai, with the '
              'difficult wording retained alongside commentary.',
  'subjects': ['西次二經',
               '西次二经',
               '总括',
               '十七山',
               '四千一百四十里',
               '人靣馬身',
               '人靣牛身',
               '四足一臂',
               '飛獸之神',
               '少牢',
               '白菅',
               '十軰',
               '雄鷄',
               '鈐',
               '不糈',
               '毛采'],
  'content_note': '0156—0161均核51页，总括独立成段不算第十八山；0162崇吾虽捕获52页但起句实在51，属于下一列。原文靣、軰、鈐、不糈毛采保留，不将鈐改作别字或猜祭器形状；两组神各作集体条目，不虚构17个专名。郭注保留录文，疑难断句不冒称定本。',
  'en_content_note': 'Units156–161 are on scan51. This is a summary, not an eighteenth mountain. Unit162 begins the '
                     'next range on scan51 despite its captured52 and remains outside this passage. Edition '
                     'characters and difficult offering wording stay unchanged. The two deity groups are collective '
                     'entries, not seventeen invented names; commentary and uncertain parsing are explicit.',
  'is_summary': True,
  'relations': [{'ids': ['passage-xishan-laishan', 'passage-xishan-range2-summary'],
                 'source': '《西山经》',
                 'quote': '凡西次二經之首自鈐山至于萊山凡十七山',
                 'labels': ['次二列总括与祭礼', '前一段 · 萊山']}]}]

ROWS += [{'slug': 'chongwu',
  'name': '崇吾之山',
  'en_name': 'Mount Chongwu',
  'units': [162, 168],
  'range': 3,
  'batch': 'xishan-chongwu',
  'description': '西次三经从崇吾山起，在河之南，向四方望见冡遂、䍃澤、帝之摶獸之丘与䗡淵。山中未命名的树有圆叶、白柎、赤花与黑理，果实如枳；经文另记宜子孙。舉父形如禺、文臂，底本豹虎二字保留；蠻蠻形如鳬，却一翼一目，相得才能飞，出现与天下大水相连。',
  'en_description': 'Chongwu opens the third Western range, south of the He, with four named landmarks in view. '
                    'An unnamed tree has round leaves, white fu, red flowers, dark markings and zhi-like fruit. '
                    'Jufu resembles a yu with patterned arms; the edition’s bao hu wording is retained. Manman '
                    'resembles a fu bird but has one wing and one eye and flies in pairs; its appearance is '
                    'linked to flooding.',
  'en_quote': 'The third Western range begins at Mount Chongwu, south of the He. It overlooks Zhongsui to the '
              'north, Yao Marsh to the south, the Emperor’s Tuan Beast Hill to the west and Yan Pool to the east. '
              'An unnamed tree has round leaves, white fu, red flowers, dark markings and fruit like zhi; eating '
              'it is said to favor descendants. Jufu resembles a yu with patterned arms and the wording bao hu, '
              'and is skilled at throwing. Manman resembles a fu bird, has one wing and one eye, and can fly when '
              'paired; its appearance is said to herald great floods throughout the land.',
  'subjects': ['崇吾', '河', '冡遂', '䍃之澤', '帝之摶獸之丘', '䗡淵', '舉父', '蠻蠻'],
  'content_note': '0162起句及冡遂郭注实在51页，捕获52页仅校正页码；0163—0168见52页，0169長沙另段。帝之摶獸之丘的摶据影印补入阅读引文，captured_text保留缺字图:搏标记；或作薄属此字，音遥属䍃澤，音於然反跨行属䗡淵。舉父正文豹虎照底本保留，不默改豹尾；或作夸父仅为郭注异名，不接逐日故事。白柎释义跨164—165，录文丈夫等疑字保留，不宣称郭注逐字无缺；蠻蠻青赤及鶼鶼来自郭注。',
  'en_content_note': 'Unit162 begins on scan51 although captured as52; units163–168 are on52 and169 begins '
                     'Changsha. The image-glyph marker labelled bo is restored as tuan in the reading quotation '
                     'from the scan, while captured text is unchanged. The bao hu wording for Jufu remains as '
                     'printed, without silently substituting a leopard tail or importing the sun-chasing Kuafu '
                     'story. The tree gloss spans units164–165 and retains uncertain captured wording; Manman '
                     'coloration and the Jianjian comparison belong to commentary.',
  'text_replacements': {'⟦缺字图:搏⟧': '摶'},
  'relations': [{'ids': ['place-xishan-chongwu', 'place-xishan-zhongsui-chongwu'],
                 'source': '《西山经》',
                 'quote': '北望冡遂',
                 'labels': ['北望所见', '方位参照 · 崇吾']},
                {'ids': ['place-xishan-chongwu', 'water-xishan-yaoze-chongwu'],
                 'source': '《西山经》',
                 'quote': '南望䍃之澤',
                 'labels': ['南望所见', '方位参照 · 崇吾']},
                {'ids': ['place-xishan-chongwu', 'place-xishan-tuan-shou-qiu-chongwu'],
                 'source': '《西山经》',
                 'quote': '西望帝之摶獸之丘',
                 'labels': ['西望所见', '方位参照 · 崇吾']},
                {'ids': ['place-xishan-chongwu', 'water-xishan-yanyuan-chongwu'],
                 'source': '《西山经》',
                 'quote': '東望䗡淵',
                 'labels': ['东望所见', '方位参照 · 崇吾']},
                {'ids': ['place-xishan-chongwu', 'water-xishan-he-taimao'],
                 'source': '《西山经》',
                 'quote': '崇吾之山在河之南',
                 'labels': ['位于其南', '方位参照 · 崇吾']}]}]

ROWS += [{'slug': 'changsha',
  'name': '長沙之山',
  'en_name': 'Mount Changsha',
  'units': [169, 170],
  'range': 3,
  'batch': 'xishan-changsha',
  'description': '崇吾山向西北三百里是長沙山。泚水从这里流出，向北注入泑水；郭注分别记泚音紫、泑又音黝及水色黑。经文随后写无草木、多青雄黄，保留底本连写，不以现代矿物名称或其他山段注文补释。',
  'en_description': 'Three hundred li northwest of Chongwu lies Changsha. The river written Ci, glossed as Zi, '
                    'rises here and flows north into the You. Commentary gives the receiving water an alternative '
                    'pronunciation and describes its dark color. The text also records no vegetation and abundant '
                    'qing xionghuang, retaining the edition’s unpunctuated wording without a modern mineral '
                    'identification.',
  'en_quote': 'Three hundred li northwest is Mount Changsha. The Zi River rises here and flows north into the '
              'You. There is no vegetation, and qing xionghuang is abundant.',
  'subjects': ['長沙之山', '长沙山', '泚水', '泑水', '青雄黄', '無草木'],
  'content_note': '0169—0170均核52页，泑与水跨单元连读。音紫属泚，烏交反又音黝水色黑也属泑水；黑色不移给泚水、山体或青雄黄。青雄黄保留连写，本段没有皇人山石青等释注。0171已起不周之山，实在52页但捕获53，留下一阶段校正，不吞入長沙段；不据山名套用现代长沙坐标。',
  'en_content_note': 'Units169–170 are on scan52; the receiving water’s name spans the captured units. The Zi '
                     'pronunciation belongs to Ci, while the alternate pronunciation and dark-water gloss belong '
                     'to You. Qing xionghuang retains the unpunctuated wording without importing Huangren’s '
                     'gloss. Unit171 begins Buzhou on scan52 despite capture as53 and is left for that stage. No '
                     'modern Changsha location is imposed.',
  'relations': [{'ids': ['place-xishan-chongwu', 'place-xishan-changsha'],
                 'source': '《西山经》',
                 'quote': '西北三百里曰長沙之山',
                 'labels': ['下一山 · 向西北三百里', '上一山 · 崇吾']},
                {'ids': ['water-xishan-ci-changsha', 'water-xishan-you-changsha'],
                 'source': '《西山经》',
                 'quote': '泚水出焉北流注于泑水',
                 'labels': ['向北流入', '来水 · 泚水']}]}]

ROWS += [{'slug': 'buzhou',
  'name': '不周之山',
  'en_name': 'Mount Buzhou',
  'units': [171, 177],
  'range': 3,
  'batch': 'xishan-buzhou',
  'description': '長沙向西北三百七十里是不周山。北望諸毗，临嶽崇，东望泑澤；河水潜行及其源渾渾泡泡的记述接在泑澤之后。这里另有未命名的嘉果，果如桃、叶如𬃷、黄花赤柎，食之不劳为古籍说法。山形有缺、不周风及河流地理解释均在郭注分列，不混入其他篇章的共工触山故事。',
  'en_description': 'Three hundred and seventy li northwest of Changsha is Buzhou. It overlooks Zhupi to the '
                    'north, faces Yuechong and overlooks You Marsh to the east. A statement about the He running '
                    'underground and its surging source follows. An unnamed fine fruit has peach-like fruit, '
                    'jujube-like leaves, yellow flowers and red fu; freedom from fatigue is an ancient eating '
                    'claim. The mountain-name and wind glosses and geographical explanations remain commentary.',
  'en_quote': 'Three hundred and seventy li northwest is Mount Buzhou. It overlooks Mount Zhupi to the north, '
              'faces Mount Yuechong and overlooks You Marsh to the east. The He runs underground here; its source '
              'surges with the sound hunhun paopao. A fine fruit grows here, with fruit like peaches, leaves like '
              'jujube, yellow flowers and red fu; eating it is said to prevent fatigue.',
  'subjects': ['不周之山', '諸毗之山', '嶽崇之山', '泑澤', '河水', '渾渾泡泡', '嘉果', '𬃷', '不周風'],
  'content_note': '0171山名起句及山形有缺郭注实在52页，捕获53页仅校正页码；0172—0177见53页，0178峚山另段。西北与不周風自此山出跨页合读为郭注，不作正文。0174—0175空正文仍保留河水长注，0176二音承接渾渾泡泡音注，不归嘉果。郭注快照泑減与影印泑澤有异，注栏保留捕获并明示差异，不宣称逐字无缺。𬃷字按底本保存。泑澤河水潜流记述不等同现代河道或与長沙泑水已证同一水域；嘉果的桃、𬃷仅作比拟，不据此命名。',
  'en_content_note': 'Unit171 begins on scan52 despite capture as53; units172–177 are on53 and178 begins Mi. The '
                     'northwest Buzhou-wind gloss crosses the scan boundary and remains commentary. '
                     'Annotation-only units174–175 retain the long river gloss; the two-pronunciations note in176 '
                     'completes the water-sound gloss, not the fruit. The captured You jian wording differs from '
                     'You ze in the scan and is retained with this notice. The edition’s jujube variant remains. '
                     'No modern river route or automatic identity with Changsha’s You River is inferred; peach '
                     'and jujube are comparisons, not the unnamed fruit’s name.',
  'relations': [{'ids': ['place-xishan-changsha', 'place-xishan-buzhou'],
                 'source': '《西山经》',
                 'quote': '又西北三百七十里曰不周之山',
                 'labels': ['下一山 · 向西北三百七十里', '上一山 · 長沙']},
                {'ids': ['place-xishan-buzhou', 'place-xishan-zhupi-buzhou'],
                 'source': '《西山经》',
                 'quote': '北望諸毗之山',
                 'labels': ['北望所见', '方位参照 · 不周']},
                {'ids': ['place-xishan-buzhou', 'place-xishan-yuechong-buzhou'],
                 'source': '《西山经》',
                 'quote': '臨彼嶽崇之山',
                 'labels': ['所临之山', '方位参照 · 不周']},
                {'ids': ['place-xishan-buzhou', 'water-xishan-youze-buzhou'],
                 'source': '《西山经》',
                 'quote': '東望泑澤',
                 'labels': ['东望所见', '方位参照 · 不周']},
                {'ids': ['place-xishan-buzhou', 'water-xishan-he-taimao'],
                 'source': '《西山经》',
                 'quote': '東望泑澤河水所潜也其源渾渾泡泡',
                 'labels': ['山段中的水文', '水文所在山段']},
                {'ids': ['water-xishan-youze-buzhou', 'water-xishan-he-taimao'],
                 'source': '《西山经》',
                 'quote': '泑澤河水所潜也',
                 'labels': ['河水所潜', '本段所述水域']}]}]

ROWS += [{'slug': 'mishan',
  'name': '峚山',
  'en_name': 'Mount Mi',
  'units': [178, 192],
  'range': 3,
  'batch': 'xishan-mishan',
  'description': '不周向西北四百二十里是峚山。丹木圆叶赤茎、黄花赤实，味如饴；丹水西注稷澤，水文中记白玉与玉膏。黄帝食飨玉膏、玉膏灌丹木及取玉榮投鍾山之阳的记述接续展开，𤣥玉、瑾瑜与天地鬼神另存出处。经文还写峚至鍾四百六十里，其间尽泽，多竒鳥、怪獸、竒魚；形貌未详，功效和神事均作为古籍记述。',
  'en_description': 'Four hundred and twenty li northwest of Buzhou is Mi. Danmu has round leaves, red stems, '
                    'yellow flowers, red fruit and a malt-sugar-like taste. The Dan flows west into Ji Marsh, '
                    'with white jade and jade paste in the water account. Huangdi’s consumption of the paste, its '
                    'use on the trees and his casting of jade blossom onto Zhong’s sunny side follow. The text '
                    'also records 460 li of wetlands between Mi and Zhong, with unnamed wondrous birds, strange '
                    'beasts and wondrous fish.',
  'en_quote': 'Four hundred and twenty li northwest is Mount Mi. Danmu has round leaves, red stems, yellow '
              'flowers and red fruit, tastes like malt sugar and is said to prevent hunger. The Dan River rises '
              'here and flows west into Ji Marsh, with white jade and surging jade paste. Huangdi consumes the '
              'paste, which produces xuan jade and waters the danmu; after five years its colors clear and '
              'flavors become fragrant. Huangdi takes Mi’s jade blossom and casts it onto Zhong’s sunny side. '
              'Jinyu jade is prized for its texture, luster and five colors. Heaven, earth, ghosts and spirits '
              'partake of it; gentlemen wear it to ward off ill fortune. Between Mi and Zhong are 460 li of '
              'wetlands with wondrous birds, strange beasts and wondrous fish.',
  'subjects': ['峚山', '丹木', '丹水', '稷澤', '白玉', '玉膏', '黄帝', '黃帝', '𤣥玉', '玉榮', '瑾瑜', '天地鬼神', '鍾山', '竒鳥', '怪獸', '竒魚'],
  'content_note': '0178—0192核53—55页，0180实53而捕获54、0189实54而捕获55，页码校正不改快照。0189鬼字缺字图据54页只补阅读引文；captured_text保留原标记。沸音与拂跨181—182，𤣥玉黑玉也跨182—183，玉榮与玉理/五色释注各跨行，分别归属；瑾瑜读音、說字及能/鬼等注文漏字保留捕获并明示，不宣称郭注逐字无缺。少室仙说/黄帝登龙/金刚石举例均属郭注，不作本山正文物产。0191峚至鍾460里与0193另山起句420里分别保留，不改距。鍾山条目合并本段投玉/460里与后续山段出处，两个里数分别保留。泽间三类异物只列名，无个体名或形貌。',
  'en_content_note': 'Units178–192 span scans53–55. Units180 and189 are actually on53 and54 rather than their '
                     'captured54 and55; the snapshot remains unchanged. Only the reading quotation restores the '
                     'gui image glyph from scan54. Pronunciation and jade glosses continue across units and are '
                     'assigned separately. Missing commentary characters remain in the capture with this notice; '
                     'no complete transcription is claimed. Immortality, dragon ascent and the diamond example '
                     'remain commentary. The 460-li statement is distinct from the next passage’s420-li opening. '
                     'The Zhong record retains this context alongside its own passage; the two distances stay separate. The '
                     'three kinds of wondrous creatures are unnamed collectives without specified forms.',
  'text_replacements': {'⟦缺字图:鬼⟧': '鬼'},
  'relations': [{'ids': ['place-xishan-buzhou', 'place-xishan-mishan'],
                 'source': '《西山经》',
                 'quote': '又西北四百二十里曰峚山',
                 'labels': ['下一山 · 向西北四百二十里', '上一山 · 不周']},
                {'ids': ['water-xishan-dan-mishan', 'water-xishan-jize-mishan'],
                 'source': '《西山经》',
                 'quote': '丹水出焉西流注于稷澤',
                 'labels': ['向西流入', '来水 · 峚山丹水']},
                {'ids': ['material-xishan-yugao-mishan', 'plant-xishan-danmu-mishan'],
                 'source': '《西山经》',
                 'quote': '玉膏所出以灌丹木',
                 'labels': ['灌溉对象', '灌溉所用']},
                {'ids': ['material-xishan-yugao-mishan', 'material-xishan-xuanyu-mishan'],
                 'source': '《西山经》',
                 'quote': '玉膏其源沸沸湯湯黄帝是食是饗是生𤣥玉',
                 'labels': ['所生之玉', '本段玉膏']},
                {'ids': ['deity-xishan-huangdi-mishan', 'material-xishan-yurong-mishan'],
                 'source': '《西山经》',
                 'quote': '黃帝乃取峚山之玉榮',
                 'labels': ['所取玉榮', '取玉者 · 黃帝']},
                {'ids': ['material-xishan-yurong-mishan', 'place-xishan-zhongshan'],
                 'source': '《西山经》',
                 'quote': '黃帝乃取峚山之玉榮而投之鍾山之陽',
                 'labels': ['投玉于山阳', '所投之玉']},
                {'ids': ['place-xishan-mishan', 'place-xishan-zhongshan'],
                 'source': '《西山经》',
                 'quote': '自峚山至于鍾山四百六十里其間盡澤也',
                 'labels': ['段末路程 · 至鍾山四百六十里', '段末路程 · 自峚山']},
                {'ids': ['water-xishan-dan-mishan', 'material-xishan-white-jade-mishan'],
                 'source': '《西山经》',
                 'quote': '丹水出焉西流注于稷澤其中多白玉',
                 'labels': ['同段水文中的物产', '水文上下文']},
                {'ids': ['water-xishan-dan-mishan', 'material-xishan-yugao-mishan'],
                 'source': '《西山经》',
                 'quote': '丹水出焉西流注于稷澤其中多白玉是有玉膏',
                 'labels': ['同段水文中的物产', '水文上下文']},
                {'ids': ['water-xishan-wetlands-mi-zhong', 'bird-xishan-birds-mi-zhong'],
                 'source': '《西山经》',
                 'quote': '其間盡澤也是多竒鳥怪獸竒魚皆異物焉',
                 'labels': ['泽间异物', '本段泽地']},
                {'ids': ['water-xishan-wetlands-mi-zhong', 'beast-xishan-beasts-mi-zhong'],
                 'source': '《西山经》',
                 'quote': '其間盡澤也是多竒鳥怪獸竒魚皆異物焉',
                 'labels': ['泽间异物', '本段泽地']},
                {'ids': ['water-xishan-wetlands-mi-zhong', 'beast-xishan-fish-mi-zhong'],
                 'source': '《西山经》',
                 'quote': '其間盡澤也是多竒鳥怪獸竒魚皆異物焉',
                 'labels': ['泽间异物', '本段泽地']}]}]

ROWS += [{'slug': 'zhongshan',
  'name': '鍾山',
  'en_name': 'Mount Zhong',
  'units': [193, 202],
  'range': 3,
  'batch': 'xishan-zhongshan',
  'description': '峚山向西北四百二十里是鍾山。皷人面龙身，与欽䲹杀葆江于崑崙之阳，帝随后行戮，记述接到鍾山东的𡺯崖。欽䲹化大鶚，皷化鵕鸟，两种鸟形与兵旱之兆分别记述；“帝”未明其名。末尾穆天子传及群兽记载属于郭注，空正文单元仍完整保留。',
  'en_description': 'Four hundred and twenty li northwest of Mi is Zhong. Gu has a human face and dragon body; '
                    'with Qinpi, Gu kills Baojiang on Kunlun’s sunny side. An unnamed emperor executes them, in '
                    'an account continuing to Yao Cliff east of Zhong. Qinpi becomes a great e bird and Gu a jun '
                    'bird, with separate forms and omens of warfare and drought. The final King Mu account and '
                    'its animals remain commentary, including annotation-only units.',
  'en_quote': 'Four hundred and twenty li northwest is Mount Zhong. Its child is called Gu, with a human face and '
              'dragon body. With Qinpi, Gu kills Baojiang on Kunlun’s sunny side. The emperor executes them; east '
              'of Zhong is Yao Cliff. Qinpi becomes a great e bird, like a diao, with black markings, a white '
              'head, red beak and tiger claws; its voice resembles a chenhu, and its appearance heralds war. Gu '
              'becomes a jun bird, like a chi, with red feet, a straight beak, yellow markings and white head; '
              'its voice resembles a hu, and its appearance brings drought to that settlement.',
  'subjects': ['鍾山', '皷', '欽䲹', '葆江', '崑崙之陽', '帝', '𡺯崖', '大鶚', '鵕鳥', '人靣龍身', '穆天子傳'],
  'content_note': '0193—0202核55—56页，0198实际55而捕获56，仅校页码不改快照；0199鸟形续56页，0201—0202无正文但有穆天子传长注，不丢弃。皷神名注跨193—194，丽山之子形貌只是郭注比拟，不移给皷；晨鵠郭注跨197—198，快照省說字，保留捕获并明示。欽䲹原身无形貌，化大鶚后形貌另卡；皷龙身/鵕鸟两形分卡且以变形关系相连。葆或作祖仅郭注，帝不改称黄帝或其他有名帝。鍾山稳定ID聚合峚/鍾双出处，460里与420里各归原句。穆王及赤豹白虎等不增作本段正文动物。',
  'en_content_note': 'Units193–202 span scans55–56; unit198 is on55 despite capture as56. Units201–202 contain '
                     'only the King Mu commentary and are retained. Gu’s name gloss and the chenhu gloss continue '
                     'across units. The Li Mountain comparison and a missing captured character remain commentary '
                     'issues. Qinpi’s original appearance is unspecified; each transformation is a separate '
                     'linked form. Bao’s variant is commentary and the emperor is not identified as Huangdi. '
                     'Zhong retains its stable ID and both Mi and Zhong sources, with 460 and 420 li kept separate. '
                     'King Mu’s animals are not added as main-text creatures.',
  'relations': [{'ids': ['place-xishan-mishan', 'place-xishan-zhongshan'],
                 'source': '《西山经》',
                 'quote': '又西北四百二十里曰鍾山',
                 'labels': ['下一山 · 向西北四百二十里', '上一山 · 峚山']},
                {'ids': ['deity-xishan-gu-zhongshan', 'bird-xishan-gu-jun-zhongshan'],
                 'source': '《西山经》',
                 'quote': '皷亦化為鵕鳥',
                 'labels': ['所化鸟形', '变形前 · 皷']},
                {'ids': ['deity-xishan-qinpi-zhongshan', 'bird-xishan-qinpi-e-zhongshan'],
                 'source': '《西山经》',
                 'quote': '欽䲹化為大鶚',
                 'labels': ['所化鸟形', '变形前 · 欽䲹']},
                {'ids': ['deity-xishan-gu-zhongshan', 'deity-xishan-qinpi-zhongshan'],
                 'source': '《西山经》',
                 'quote': '是與欽䲹殺葆江于崑崙之陽',
                 'labels': ['同段行事者 · 欽䲹', '同段行事者 · 皷']},
                {'ids': ['deity-xishan-qinpi-zhongshan', 'deity-xishan-baojiang-zhongshan'],
                 'source': '《西山经》',
                 'quote': '是與欽䲹殺葆江于崑崙之陽',
                 'labels': ['本段被杀者', '本段行事者']},
                {'ids': ['deity-xishan-baojiang-zhongshan', 'place-xishan-kunlun-yang-zhongshan'],
                 'source': '《西山经》',
                 'quote': '殺葆江于崑崙之陽',
                 'labels': ['事件所在 · 崑崙之陽', '本段被杀者']},
                {'ids': ['deity-xishan-di-zhongshan', 'place-xishan-yaoya-zhongshan'],
                 'source': '《西山经》',
                 'quote': '帝乃戮之鍾山之東曰𡺯崖',
                 'labels': ['行戮所及之地', '本段未具名之帝']}]}]

ROWS += [{'slug': 'taiqi',
  'name': '㤗噐之山',
  'en_name': 'Mount Taiqi',
  'units': [203, 207],
  'range': 3,
  'batch': 'xishan-taiqi',
  'description': '鍾山向西一百八十里是㤗噐山。𮗚水从这里流出，向西注于流沙，随后记多文鰩魚。文鰩魚如鲤，鱼身鸟翼，苍文白首赤喙，常行西海、游于东海、夜间飞行，音如鸞雞。酸甘、食之已狂与见则天下大穰均保留为古籍记述；两组郭注分别说明鸞雞和大穰。',
  'en_description': 'One hundred and eighty li west of Zhong is Taiqi. The Guan River rises here and flows west '
                    'into Liusha, followed by the Wenyao fish account. Wenyao resembles a carp, with a fish’s '
                    'body, bird wings, blue-green markings, white head and red beak. It frequents the Western '
                    'Sea, travels in the Eastern Sea and flies at night, with a voice like luanji. Its taste, '
                    'eating claim and harvest omen remain ancient textual accounts.',
  'en_quote': 'One hundred and eighty li west is Mount Taiqi. The Guan River rises here and flows west into '
              'Liusha. Wenyao fish are abundant: carp-like, with a fish’s body and bird wings, blue-green '
              'markings, white head and red beak. They frequent the Western Sea, travel in the Eastern Sea and '
              'fly at night, with a voice like luanji. Their taste is sour and sweet; eating them is said to '
              'relieve kuang, and their appearance to herald abundant harvests.',
  'subjects': ['㤗噐之山', '𮗚水', '流沙', '文鰩魚', '西海', '東海', '夜飛', '鸞雞', '大穰'],
  'content_note': '0203—0207正文及注文全部在56页；0207虽无正文仍承豐穰收熟也韓子曰穰嵗之秋，捕获57页仅校为56，不改快照。鸞雞注跨205—206，丰穰注跨206—207，两组分别连读；鸞雞仅为声音比拟且郭注名未詳，不另造本山鸟种。山名㤗噐与𮗚水保留底本字形；流沙只作注入地点，不定位现代沙漠或臆定为水体。西海复用西山经同名索引并留騩/㤗噐双出处，配图仅属騩山，不表示文鰩魚或其海上行迹；南山同名海域分开。两海不画实测航线，酸甘/已狂/大穰均非现代食疗或预测。',
  'en_content_note': 'Units203–207, including the final annotation-only unit, are all on scan56; unit207 was '
                     'captured as57 and is corrected without changing the snapshot. The luanji gloss spans205–206 '
                     'and the harvest gloss206–207. Luanji is only a voice comparison, not another bird assigned '
                     'to this mountain. Edition characters are retained. Liusha is the destination named in the '
                     'text, without a modern desert or definite water-body identity. The Western Sea index '
                     'retains separate Gui and Taiqi sources; the reused Gui scene does not depict Wenyao or its '
                     'sea travel. Namesakes in the Southern Mountains remain separate, with no modern route or '
                     'practical dietary prediction added.',
  'relations': [{'ids': ['place-xishan-zhongshan', 'place-xishan-taiqi'],
                 'source': '《西山经》',
                 'quote': '又西百八十里曰㤗噐之山',
                 'labels': ['下一山 · 向西百八十里', '上一山 · 鍾山']},
                {'ids': ['water-xishan-guan-taiqi', 'place-xishan-liusha'],
                 'source': '《西山经》',
                 'quote': '𮗚水出焉西流注于流沙',
                 'labels': ['向西注于', '来水 · 𮗚水']},
                {'ids': ['water-xishan-guan-taiqi', 'beast-xishan-wenyao-taiqi'],
                 'source': '《西山经》',
                 'quote': '𮗚水出焉西流注于流沙是多文鰩魚',
                 'labels': ['同段水文中的对象', '水文上下文']},
                {'ids': ['beast-xishan-wenyao-taiqi', 'water-xishan-westsea-guishan'],
                 'source': '《西山经》',
                 'quote': '常行西海',
                 'labels': ['常行之海', '本段文鰩魚']},
                {'ids': ['beast-xishan-wenyao-taiqi', 'water-xishan-eastsea-taiqi'],
                 'source': '《西山经》',
                 'quote': '遊於東海',
                 'labels': ['所游之海', '本段文鰩魚']}]}]

ROWS += [{'slug': 'huaijiang',
  'name': '槐江之山',
  'en_name': 'Mount Huaijiang',
  'units': [208, 222],
  'range': 3,
  'batch': 'xishan-huaijiang',
  'description': '㤗噐向西三百二十里是槐江山。丘時水北注泑水，水中多蠃母；山上、阳面、阴面的物产分别记述。神英招司帝之平圃，马身人面、虎文鸟翼。南望崑崙，西望后稷所潜的大澤，北望諸毗及槐鬼離侖、鷹鸇，东望四成怛山与有窮鬼。末尾另记清洛洛的滛水和牛状八足二首马尾天神，不能与英招混同。',
  'en_description': 'Three hundred and twenty li west of Taiqi is Huaijiang. The Qiushi flows north into the You, '
                    'with luomu in its waters; goods above and on opposing slopes are recorded separately. '
                    'Yingzhao oversees the emperor’s level garden, with a horse’s body, human face, tiger '
                    'markings and bird wings. Views extend to Kunlun, Houji’s Great Marsh, Zhupi and four-tiered '
                    'mountain in the eastern view. The closing water and an unnamed ox-like deity with eight feet, two heads and a '
                    'horse’s tail form a separate account.',
  'en_quote': 'Three hundred and twenty li west is Mount Huaijiang. The Qiushi River rises here and flows north '
              'into the You, containing many luomu. Above are qing xionghuang and hidden langgan, gold and jade; '
              'the sunny side has dansu and the shaded side the wording cai huangjin yin. This is the emperor’s '
              'level garden, overseen by Yingzhao, who has a horse’s body, human face, tiger markings and bird '
              'wings, circles the four seas and sounds like liu. To the south is luminous Kunlun; to the west the '
              'Great Marsh where Houji remains hidden, with jade and the yaomu zhi you ruo wording on its shaded '
              'side. To the north is Zhupi, inhabited by Huai-gui Lilun and ying and zhan birds. To the east is '
              'a four-tiered mountain in the eastern view, where Youqiong spirits dwell, each on a mountain side. There is clear '
              'flowing water and an ox-like heavenly deity with eight feet, two heads and a horse’s tail, '
              'sounding like bohuang; its appearance is an omen of warfare in that settlement.',
  'subjects': ['槐江',
               '丘時之水',
               '泑水',
               '蠃母',
               '英招',
               '帝之平圃',
               '崑崙',
               '大澤',
               '后稷',
               '榣木',
               '諸毗',
               '槐鬼離侖',
               '鷹',
               '鸇',
               '怛山',
               '有窮鬼',
               '滛水'],
  'text_replacements': {'⟦缺字图:鬼⟧': '鬼', '⟦缺字图:搏⟧': '摶', '⟦缺字图:滛⟧': '滛'},
  'content_note': '0208—0222核57—58页，0216实际57而捕获58，仅校页码不改快照。217/219鬼、220手旁專声摶及221滛据58页只补阅读层，捕获标记保留。青雄黃与采黄金銀不强断句，藏琅玕郭注/平圃注/英招榴音注/后稷长注/榣木注/鷹鸇注均跨行分属；后稷注省說、摶注省鬼及异体、滛音注省字等保留捕获并明示，不宣称郭注逐字无缺。怛山照录文不擅定现代恒山，滛水未明示专名，不据音遥定位现代河流。南望崑崙只先建上下文，下一崑崙主段尚未接入；泑水/諸毗复用篇内同名索引，保持各段出处，不合并不周泑澤。',
  'en_content_note': 'Units208–222 span scans57–58; unit216 is on57 despite capture as58. Four image-glyph '
                     'markers are restored only in the reading quotation, with the capture retained. Mineral '
                     'groupings and several cross-unit glosses stay separate; omissions in the Houji, '
                     'mountain-side and water glosses are explicitly noted rather than silently repaired. Dan is '
                     'retained as the edition name, not a modern Mount Heng. The flowing water is not assigned a '
                     'definite proper name or modern location. Kunlun’s southern view is documented here ahead of '
                     'its own passage. Namesake You and Zhupi references retain separate sources, without merging '
                     'You Marsh.',
  'relations': [{'ids': ['place-xishan-taiqi', 'place-xishan-huaijiang'],
                 'source': '《西山经》',
                 'quote': '又西三百二十里曰槐江之山',
                 'labels': ['下一山 · 向西三百二十里', '上一山 · 㤗噐']},
                {'ids': ['water-xishan-qiushi-huaijiang', 'water-xishan-you-changsha'],
                 'source': '《西山经》',
                 'quote': '丘時之水出焉而北流注于泑水',
                 'labels': ['向北流入', '来水 · 丘時水']},
                {'ids': ['water-xishan-qiushi-huaijiang', 'beast-xishan-luomu-huaijiang'],
                 'source': '《西山经》',
                 'quote': '丘時之水出焉而北流注于泑水其中多蠃母',
                 'labels': ['同段水文中的对象', '水文上下文']},
                {'ids': ['place-xishan-pingpu-huaijiang', 'deity-xishan-yingzhao-huaijiang'],
                 'source': '《西山经》',
                 'quote': '實惟帝之平圃神英招司之',
                 'labels': ['司掌之神', '所司之地']},
                {'ids': ['place-xishan-huaijiang', 'place-xishan-kunlun'],
                 'source': '《西山经》',
                 'quote': '南望崑崙其光熊熊其氣魂魂',
                 'labels': ['南望所见', '方位参照 · 槐江']},
                {'ids': ['place-xishan-huaijiang', 'water-xishan-daze-huaijiang'],
                 'source': '《西山经》',
                 'quote': '西望大澤后稷所潜也',
                 'labels': ['西望所见', '方位参照 · 槐江']},
                {'ids': ['water-xishan-daze-huaijiang', 'deity-xishan-houji-huaijiang'],
                 'source': '《西山经》',
                 'quote': '西望大澤后稷所潜也',
                 'labels': ['所潜之神', '本段所潜大澤']},
                {'ids': ['place-xishan-huaijiang', 'place-xishan-zhupi-buzhou'],
                 'source': '《西山经》',
                 'quote': '北望諸毗槐鬼離侖居之鷹鸇之所宅也',
                 'labels': ['北望所见', '方位参照 · 槐江']},
                {'ids': ['place-xishan-huaijiang', 'place-xishan-danshan-huaijiang'],
                 'source': '《西山经》',
                 'quote': '東望怛山四成',
                 'labels': ['东望所见', '方位参照 · 槐江']},
                {'ids': ['place-xishan-danshan-huaijiang', 'deity-xishan-youqiong-huaijiang'],
                 'source': '《西山经》',
                 'quote': '東望怛山四成有窮鬼居之各在一摶',
                 'labels': ['所居群鬼', '所居之山']},
                {'ids': ['place-xishan-zhupi-buzhou', 'deity-xishan-lilun-huaijiang'],
                 'source': '《西山经》',
                 'quote': '北望諸毗槐鬼離侖居之鷹鸇之所宅也',
                 'labels': ['本段所居对象', '所居諸毗']},
                {'ids': ['place-xishan-zhupi-buzhou', 'bird-xishan-ying-huaijiang'],
                 'source': '《西山经》',
                 'quote': '北望諸毗槐鬼離侖居之鷹鸇之所宅也',
                 'labels': ['本段所居对象', '所居諸毗']},
                {'ids': ['place-xishan-zhupi-buzhou', 'bird-xishan-zhan-huaijiang'],
                 'source': '《西山经》',
                 'quote': '北望諸毗槐鬼離侖居之鷹鸇之所宅也',
                 'labels': ['本段所居对象', '所居諸毗']},
                {'ids': ['water-xishan-daze-huaijiang', 'material-xishan-jade-daze-huaijiang'],
                 'source': '《西山经》',
                 'quote': '西望大澤后稷所潜也其中多玉其隂多榣木之有若',
                 'labels': ['同段水文中的对象', '水文上下文']},
                {'ids': ['water-xishan-daze-huaijiang', 'plant-xishan-yaomu-ruo-huaijiang'],
                 'source': '《西山经》',
                 'quote': '西望大澤后稷所潜也其中多玉其隂多榣木之有若',
                 'labels': ['同段水文中的对象', '水文上下文']}]}]

ENTITIES = [
    {
        'id': 'beast-xishan-qianyang', 'slug': 'qianlai', 'kind': '兽', 'group': 'beasts',
        'name': '羬羊', 'en_name': 'Qianyang', 'art': 'creature-qianyang',
        'quote': '有獸焉其狀如羊而馬尾名曰羬羊其脂可以已腊',
        'description': '羬羊像羊，却有一条马尾，这是经文最明确的形貌差异。郭注另以大月氐国的大羊作比较，不据此把它确定为现实物种。经文所载其脂功效仅作古籍内容呈现。',
        'en_description': 'Qianyang has a sheep-like form and a horse’s tail, its defining textual feature. Guo Pu compares it with large sheep of the Great Yuezhi; that comparison is kept as commentary, not a modern species identification.',
        'en_quote': 'A beast shaped like a sheep with a horse’s tail is called Qianyang. Its fat is said to treat cracked skin (the commentary’s gloss).',
        'commentary_quote': '今大月氐國有大羊如馿而馬尾爾雅云羊六尺為羬謂此羊也',
    },
    {
        'id': 'water-xishan-huo', 'slug': 'songguo', 'kind': 'water', 'group': 'natural_features',
        'name': '濩水', 'en_name': 'Huo River', 'art': 'scene-songguo',
        'quote': '濩水出焉北流注于渭其中多銅',
        'description': '濩水出于松果山，向北注入渭；“其中多铜”承接这段水文。此卡只说明经文明言的源出与流入关系，不补造现代河道，也不把随后出现的䳋渠当成水生鸟。',
        'en_description': 'The Huo rises at Songguo and flows north into the Wei. Copper is recorded in this water description. The entry preserves that textual connection without drawing a modern river course or treating the following bird as aquatic.',
        'en_quote': 'The Huo River rises here, flows north into the Wei, and has much copper in its waters.',
    },
    {
        'id': 'water-xishan-wei', 'slug': 'songguo', 'kind': 'water', 'group': 'natural_features',
        'name': '渭（松果山段）', 'en_name': 'Wei (Songguo passage)', 'art': 'scene-songguo',
        'quote': '濩水出焉北流注于渭',
        'description': '渭在松果山段作为濩水的汇入水域出现。该段没有交代渭的源头、全程或现代位置；关联松果山仅用于阅读上下文。',
        'en_description': 'The Wei appears as the receiving water of the Huo in the Songguo passage. This passage supplies neither its source nor its full course or modern position. Songguo provides reading context only.',
        'en_quote': 'The Huo River rises here and flows north into the Wei.',
    },
    {
        'id': 'beast-xishan-tongqu', 'slug': 'songguo', 'kind': '鸟', 'group': 'beasts',
        'name': '䳋渠', 'en_name': 'Tongqu', 'art': 'creature-tongqu',
        'quote': '有鳥焉其名曰䳋渠其狀如山雞黑身赤足可以已𦢊',
        'description': '䳋渠形似山鸡，黑色身体与红色足部构成鲜明对照。经文没有记载多首、多翼等器官；插画以刻纹和姿态加强神话感。底本保留“𦢊”字，郭注解释为皮肤皱起一类的表述，古籍功效不作现实建议。',
        'en_description': 'Tongqu resembles a mountain pheasant, with a black body and red feet. No additional heads or wings are specified, so carved motifs and pose carry the illustration’s mythic character. The source retains the rare ailment character 𦢊, glossed as wrinkling or raised skin.',
        'en_quote': 'A bird called Tongqu resembles a mountain pheasant, with a black body and red feet. It is said to treat 𦢊.',
        'commentary_quote': '䳋音彤弓之彤；謂皮皺起也音叵駮反',
    },
    {
        'id': 'beast-xishan-feiyi-taihua', 'slug': 'taihua', 'kind': '蛇', 'group': 'beasts',
        'name': '肥𧔥（太华山）', 'en_name': 'Feiyi (Taihua)', 'art': 'creature-feiyi',
        'quote': '有蛇焉名曰肥𧔥六足四翼見則天下大旱',
        'description': '太华山的肥𧔥是蛇形、六足、四翼的异物。经文把它的出现与天下大旱相连，这是一条灾异记述。郭注另提同名蛇的疑问，因此本卡限定在太华山段。英山另有名为肥遗的鸟，两者保留各自形貌与出处，不合并为同一异兽。',
        'en_description': 'The Feiyi of Taihua is a snake with six feet and four wings. Its appearance is associated with a great drought as an omen in the text. Guo Pu questions whether another snake of the same name is distinct. Ying also names a Feiyi bird; the entries retain their separate forms and sources.',
        'en_quote': 'A snake called Feiyi has six feet and four wings. Its appearance is said to herald a great drought throughout the land.',
        'commentary_quote': '湯時此蛇見於陽山下復有肥遺蛇疑是同名',
    },
]

ENTITIES += [
    {
        'id': 'animal-xishan-zuoniu', 'slug': 'xiaohua', 'kind': 'animal', 'group': 'text_entities',
        'name': '㸲牛（小华山）', 'en_name': 'Zuoniu (Xiaohua)', 'art': 'animal-zuoniu',
        'quote': '其獸多㸲牛',
        'description': '小华山段只说多㸲牛，没有记载额外器官或异兽情节。郭注以山牛作比较并记体量；本卡作为动物记载，形貌不等同于现代物种鉴定。',
        'en_description': 'The Xiaohua passage records many Zuoniu without unusual organs or a separate tale. Guo Pu compares them to mountain cattle and comments on their size. This is an animal record, not a modern species identification.',
        'en_quote': 'Its beasts include many Zuoniu.',
        'commentary_quote': '今華隂山中多山牛山羊肉皆千斤牛即此牛也音昨',
    },
    {
        'id': 'beast-xishan-chibie', 'slug': 'xiaohua', 'kind': '鸟', 'group': 'beasts',
        'name': '赤鷩', 'en_name': 'Chibie', 'art': 'bird-chibie',
        'quote': '鳥多赤鷩可以禦火',
        'description': '经文只记赤鷩多、可以御火，未展开器官形貌。郭注把它归入山鸡一类，写胸腹红、冠黄、头绿、尾中有赤毛。配图据此用色与木刻姿态表达；御火不画成实际发生的能力。',
        'en_description': 'The text names Chibie and says it can ward off fire without detailing its anatomy. The commentary describes a pheasant-type bird with a red breast and belly, yellow crown, green head and red feathers in its tail. Those commentary colors guide the illustration.',
        'en_quote': 'Chibie birds are abundant and are said to ward off fire.',
        'commentary_quote': '赤鷩山雞之属胷腹洞赤冠金皆黄頭緑尾中有赤毛彩鮮明',
    },
    {
        'id': 'plant-xishan-bili', 'slug': 'xiaohua', 'kind': 'plant', 'group': 'natural_features',
        'name': '萆荔', 'en_name': 'Bili', 'art': 'plant-bili',
        'quote': '其草有萆荔狀如烏韭而生於石上亦緣木而生食之已心痛',
        'description': '萆荔形如乌韭，生长位置有石上与缘木两种。郭注称其为香草，并补充乌韭在屋、墙上的称呼。这里不确定它对应今天的哪一种植物；插画保留贴石与缘木的生长方式，不补造花果。',
        'en_description': 'Bili resembles wujiu and grows on rocks as well as along trees. The commentary calls it an aromatic herb and discusses names for wujiu on roofs and walls. No modern species, flowers or fruit are inferred.',
        'en_quote': 'Bili resembles wujiu, grows on rocks and also along trees, and is said to relieve heart pain when eaten.',
        'commentary_quote': '萆荔香草也蔽戾兩音；烏韭在屋者曰昔邪在墻者曰垣衣',
    },
    {
        'id': 'plant-xishan-wenjing', 'slug': 'fuyu', 'kind': 'plant', 'group': 'natural_features',
        'name': '文茎', 'en_name': 'Wenjing', 'art': 'plant-wenjing',
        'quote': '其上有木焉名曰文莖其實如𬃷可以已聾',
        'description': '文茎是符禺山中的木，果实被比作枣。经文没有说明叶形、花色或树冠，因此插画的这些细节属于艺术解释。所载治聋功效作为古籍记述呈现。',
        'en_description': 'Wenjing is a tree at Fuyu with jujube-like fruit. Leaf shape, flowers and crown form are not specified, so unspecified visual details are artistic choices. The recorded use for deafness remains an ancient textual claim.',
        'en_quote': 'A tree called Wenjing bears fruit like jujubes and is said to relieve deafness.',
    },
    {
        'id': 'plant-xishan-tiao-fuyu', 'slug': 'fuyu', 'kind': 'plant', 'group': 'natural_features',
        'name': '條（符禺山）', 'en_name': 'Tiao (Fuyu)', 'art': 'plant-tiao-fuyu',
        'quote': '其草多條其狀如葵而赤花黄實如嬰兒舌食之使人不惑',
        'description': '符禺的條形如葵，红花、黄实，果实被比作婴儿舌。这里保留草的形态比喻，不画成人体部位，也不把它与石脆山白花黑实的同名草混为一张卡。',
        'en_description': 'The Fuyu Tiao resembles kui, with red flowers and yellow fruit compared to an infant’s tongue. The comparison describes fruit shape rather than human tissue. It is kept separate from Shicui’s white-flowered, black-fruited Tiao.',
        'en_quote': 'Tiao resembles kui, with red flowers and yellow fruit compared to an infant’s tongue. Eating it is said to prevent confusion.',
    },
    {
        'id': 'water-xishan-fuyu', 'slug': 'fuyu', 'kind': 'water', 'group': 'natural_features',
        'name': '符禺之水', 'en_name': 'Fuyu River', 'art': 'scene-fuyu',
        'quote': '符禺之水出焉而北流注于渭',
        'description': '符禺之水从符禺山流出，向北注入渭。它与濩水分别有明示的入渭关系，不据此补造两条水的汇流位置；其后所述葱聾、鴖也不被自动判为水生。',
        'en_description': 'The Fuyu River rises at Fuyu and flows north into the Wei. Its receiving-water relationship and that of the Huo are recorded separately; no modern confluence or aquatic habitat for the following creatures is inferred.',
        'en_quote': 'The Fuyu River rises here and flows north into the Wei.',
    },
    {
        'id': 'beast-xishan-conglong', 'slug': 'fuyu', 'kind': '兽', 'group': 'beasts',
        'name': '葱聾', 'en_name': 'Conglong', 'art': 'creature-conglong',
        'quote': '其獸多葱聾其狀如羊而赤鬛',
        'description': '葱聾像羊，区别在于赤色鬣毛。插画将颈背赤鬣与羊形身躯分开表现，使这处特征在缩略图中仍可辨；经文没有记载多角、多尾或翼。',
        'en_description': 'Conglong resembles a sheep with a red mane. The illustration separates the red mane from the sheep-like body so the defining feature remains readable at thumbnail size. Extra horns, tails and wings are not specified.',
        'en_quote': 'Conglong resembles a sheep with a red mane.',
    },
    {
        'id': 'beast-xishan-min', 'slug': 'fuyu', 'kind': '鸟', 'group': 'beasts',
        'name': '鴖', 'en_name': 'Min', 'art': 'bird-min',
        'quote': '其鳥多鴖其状如翠而赤喙可以禦火',
        'description': '鴖形如翠而有红喙。郭注说翠似燕、色绀，又解释御火为畜养辟火灾的古籍说法。配图突出红喙与绀色翼身，不借火焰、额外器官或现代鸟种鉴定来补足神话形象。',
        'en_description': 'Min resembles a cui bird and has a red beak. Guo Pu compares cui to a swallow and describes its dark-blue color. The text’s fire-averting claim is kept in the account; the image emphasizes the red beak and ink-blue form without flames or invented organs.',
        'en_quote': 'Min resembles a cui bird with a red beak and is said to ward off fire.',
        'commentary_quote': '音旻；翠似燕而紺色也；畜之辟火灾也',
    },
    {
        'id': 'plant-xishan-tiao-shicui', 'slug': 'shicui', 'kind': 'plant', 'group': 'natural_features',
        'name': '條（石脆山）', 'en_name': 'Tiao (Shicui)', 'art': 'plant-tiao-shicui',
        'quote': '其草多條其狀如韭而白華黑實食之已疥',
        'description': '石脆山的條形如韭，白花、黑实，与符禺的葵状红花黄实草不同。两处名称相同而形貌记载有别，分别保留原文、山段与插画，不强作同一植物。',
        'en_description': 'Shicui’s Tiao resembles chives, with white flowers and black fruit. Fuyu’s plant of the same name has a different form and colors. Their passages, artwork and identities remain separate.',
        'en_quote': 'Tiao resembles chives, has white flowers and black fruit, and is said to relieve scabies when eaten.',
    },
    {
        'id': 'water-xishan-guan', 'slug': 'shicui', 'kind': 'water', 'group': 'natural_features',
        'name': '灌水', 'en_name': 'Guan River', 'art': 'scene-shicui',
        'quote': '灌水出焉而北流注于禺水其中有流赭',
        'description': '灌水出于石脆山，向北注入禺水，随后水文中记有流赭。这里保留水域上下文，不进一步断定“其中”对应哪一段现代河道。',
        'en_description': 'The Guan rises at Shicui and flows north into the Yu. Liuzhe follows within this water description. The account is kept in context without identifying a specific modern river reach.',
        'en_quote': 'The Guan River rises here, flows north into the Yu, and liuzhe occurs in this water description.',
    },
    {
        'id': 'water-xishan-yu-shicui', 'slug': 'shicui', 'kind': 'water', 'group': 'natural_features',
        'name': '禺水（石脆山段）', 'en_name': 'Yu (Shicui passage)', 'art': 'scene-shicui',
        'quote': '灌水出焉而北流注于禺水',
        'description': '禺水在本段作为灌水的汇入水域出现。这段没有交代它的源头，因此关联石脆山只为说明阅读上下文；后续英山段的同名水域留待该段核对，不在本批自动合并。',
        'en_description': 'The Yu is the receiving water of the Guan in this passage, which does not identify the Yu’s source. Shicui provides reading context only. A water of the same name in the following Ying passage awaits its own review.',
        'en_quote': 'The Guan River rises here and flows north into the Yu.',
    },
    {
        'id': 'material-xishan-liuzhe', 'slug': 'shicui', 'kind': 'material', 'group': 'natural_features',
        'name': '流赭', 'en_name': 'Liuzhe', 'art': 'scene-shicui', 'relation_scope': 'water',
        'quote': '其中有流赭以𡍼牛馬無病',
        'description': '流赭见于灌水注禺水的水文之后，郭注以赤土解释“赭”。配图借用水边红褐土石作场景示意，不把它确定为某种现代矿物。涂牛马的功效保留为古籍记述。',
        'en_description': 'Liuzhe occurs after the Guan-to-Yu water description, with zhe glossed as red earth. Reddish stones in the shared scene are illustrative, not a modern mineral identification. Its use on cattle and horses remains a textual claim.',
        'en_quote': 'Liuzhe occurs here; applying it to cattle and horses is said to keep them free of illness.',
        'commentary_quote': '赭赤土',
    },
]


ENTITIES += [
    {
        'id': 'water-xishan-yu-ying', 'slug': 'ying', 'kind': 'water', 'group': 'natural_features',
        'name': '禺水（英山段）', 'en_name': 'Yu (Ying passage)', 'art': 'scene-ying',
        'quote': '禺水出焉北流注于招水',
        'description': '英山段明确记禺水从本山流出、向北注入招水。石脆段另有承接灌水的同名水域，本卡分别保留段落和上下文，不据同名推定现代水道或合并点位。',
        'en_description': 'The Ying passage explicitly gives this Yu a source at Ying and a northward flow into the Shao. Shicui separately names a Yu receiving the Guan. Their contexts remain distinct; a shared name does not establish a modern river course.',
        'en_quote': 'The Yu rises here and flows north into the Shao.',
    },
    {
        'id': 'water-xishan-zhao-ying', 'slug': 'ying', 'kind': 'water', 'group': 'natural_features',
        'name': '招水（英山段）', 'en_name': 'Shao (Ying passage)', 'art': 'scene-ying',
        'quote': '禺水出焉北流注于招水',
        'description': '招水在英山段作为禺水的汇入水域出现；郭注作音韶，因此英文采用Shao而保留中文招字。本段没有说明其源头、全程或现代位置，配图只提供英山阅读上下文。',
        'en_description': 'The Shao receives the Yu in the Ying passage. Guo Pu reads the character U+62DB as shao; its source spelling is retained. No source, full course or modern position is supplied. The shared Ying scene gives reading context only.',
        'commentary_quote': '音韶',
        'en_quote': 'The Yu rises here and flows north into the Shao.',
    },
    {
        'id': 'beast-xishan-bangyu-ying', 'slug': 'ying', 'kind': '鱼', 'group': 'beasts',
        'name': '䰷鱼', 'en_name': 'Bangyu', 'art': 'creature-bangyu', 'relation_scope': 'water',
        'quote': '其中多䰷魚其狀如鼈其音如羊',
        'description': '䰷鱼接在禺水注招水的水文中，形如鳖、声音像羊。羊声是声音比喻，不转写为羊头、羊角或羊毛；本卡也不进一步认定“其中”对应哪段现代河道。',
        'en_description': 'Bangyu follows the Yu-to-Shao water account. It resembles a turtle and sounds like a sheep. The sound comparison supplies no sheep-like anatomy, and no particular modern river reach is inferred.',
        'en_quote': 'Bangyu are abundant in this water account; they resemble turtles and sound like sheep.',
        'commentary_quote': '音同蚌蛤之蚌',
    },
    {
        'id': 'animal-xishan-zuoniu-ying', 'slug': 'ying', 'kind': 'animal', 'group': 'text_entities',
        'name': '㸲牛（英山段）', 'en_name': 'Zuoniu (Ying passage)', 'art': 'animal-zuoniu',
        'quote': '其獸多㸲牛羬羊',
        'description': '英山段只列㸲牛、羬羊，没有在这里重述形貌。㸲牛与小华山段分开保存出处；配图借用小华山卡的牛形艺术解释，不把别段郭注当作英山经文。',
        'en_description': 'Ying lists Zuoniu and Qianyang without repeating their form. This entry keeps the Ying source separate from Xiaohua. Its image reuses Xiaohua’s artistic cattle illustration; that passage’s commentary is not presented as Ying’s main text.',
        'en_quote': 'Its beasts include many Zuoniu and Qianyang.',
        'art_reference': ['复用小华山㸲牛示意图 · 英山本段仅列名，不重述形貌。', 'Reused Xiaohua Zuoniu illustration · Ying only lists the name and does not repeat its form.'],
    },
    {
        'id': 'beast-xishan-qianyang-ying', 'slug': 'ying', 'kind': '兽', 'group': 'beasts',
        'name': '羬羊（英山段）', 'en_name': 'Qianyang (Ying passage)', 'art': 'creature-qianyang',
        'quote': '其獸多㸲牛羬羊',
        'description': '英山经文只列羬羊之名。羊状马尾见于此前钱来山段，本卡保留英山的独立出处，并借用钱来山配图作参照，不把马尾描述补入英山引文。',
        'en_description': 'Ying only names Qianyang. The sheep-like form and horse’s tail occur in Qianlai’s earlier passage. The Ying source remains separate, with the Qianlai illustration reused as a reference rather than an addition to Ying’s quotation.',
        'en_quote': 'Its beasts include many Zuoniu and Qianyang.',
        'art_reference': ['复用钱来山羬羊示意图 · 羊状马尾出自钱来段，英山本段仅列名。', 'Reused Qianlai Qianyang illustration · Sheep form and horse tail come from Qianlai; Ying only names it.'],
    },
    {
        'id': 'beast-xishan-feiyi-ying', 'slug': 'ying', 'kind': '鸟', 'group': 'beasts',
        'name': '肥遗（英山鸟）', 'en_name': 'Feiyi (Ying bird)', 'art': 'bird-feiyi-ying',
        'quote': '有鳥焉其状如鶉黄身而赤喙其名曰肥遺食之已癘可以殺蟲',
        'description': '英山肥遗是鸟，形如鹑，黄身、赤喙。它与太华山六足四翼的肥𧔥蛇分别保留稳定ID、形貌和原文；不因名称相近而合成一种异兽。食用功效仅作为古籍记述。',
        'en_description': 'Ying’s Feiyi is a quail-like bird with a yellow body and red beak. It has its own stable ID, source and form, separate from the six-legged, four-winged snake of Taihua. The recorded uses remain ancient textual claims.',
        'en_quote': 'A bird called Feiyi resembles a quail, with a yellow body and red beak. Eating it is said to relieve li and kill parasites.',
        'commentary_quote': '癘疫病也；或曰惡創韓子曰癘人憐主',
    },
    {
        'id': 'plant-xishan-huangguan', 'slug': 'zhushan', 'kind': 'plant', 'group': 'natural_features',
        'name': '黄雚', 'en_name': 'Huangguan', 'art': 'plant-huangguan',
        'quote': '有草焉其名曰黄雚其状如樗其葉如麻白花而赤實其状如赭浴之已疥又可以已胕',
        'description': '黄雚在经文中归为草，形如樗、叶如麻，白花、赤实，后又比作赭；郭注以紫赤色解释。插画以草本构形、白花和深红果区分，不据此鉴定现代植物；浴用功效不作现实建议。',
        'en_description': 'Huangguan is an herb, compared to chu, with hemp-like leaves, white flowers and red fruit. The following zhe comparison is glossed as purplish red. These features guide an artistic herb rather than a modern species identification or treatment recommendation.',
        'en_quote': 'Huangguan resembles chu, has hemp-like leaves, white flowers and red fruit; its appearance is compared to zhe. Bathing with it is said to relieve scabies and swelling.',
        'commentary_quote': '紫赤色；治胕腫也音符',
    },
    {
        'id': 'water-xishan-zhu', 'slug': 'zhushan', 'kind': 'water', 'group': 'natural_features',
        'name': '竹水', 'en_name': 'Zhu River', 'art': 'scene-zhushan',
        'quote': '竹水出焉北流注于渭',
        'description': '竹水从竹山流出、向北注渭。本卡与同山的丹水分开：丹水向东南注洛，不把两条水合成同一河道。渭的多来源卡保留各自山段出处。',
        'en_description': 'The Zhu rises at Mount Zhu and flows north into the Wei. The same mountain’s Dan flows southeast into the Luo and remains a separate water. The Wei entry retains each contributing passage with its own source.',
        'en_quote': 'The Zhu River rises here and flows north into the Wei.',
    },
    {
        'id': 'water-xishan-dan-zhushan', 'slug': 'zhushan', 'kind': 'water', 'group': 'natural_features',
        'name': '丹水（竹山段）', 'en_name': 'Dan (Zhu passage)', 'art': 'scene-zhushan',
        'quote': '丹水出焉東南流注于洛水其中多水玉多人魚',
        'description': '竹山丹水向东南注洛。电子快照的“南”以缺字图保存，本卡在核对影印38页后补作南，原始快照不改写。随后水玉、人鱼保留水文上下文，不锁定现代河段，也不与南山经丹水合并。',
        'en_description': 'The Dan of Mount Zhu flows southeast into the Luo. The snapshot’s image-glyph placeholder for south was checked against scan page 38 and restored in the reading text; the captured snapshot remains intact. Water minerals and Renyu stay in their textual context, without a modern river identification or merger with the Southern Dan.',
        'en_quote': 'The Dan rises here and flows southeast into the Luo; water jade and Renyu follow in this water account.',
    },
    {
        'id': 'water-xishan-luo-zhushan', 'slug': 'zhushan', 'kind': 'water', 'group': 'natural_features',
        'name': '洛水（竹山段）', 'en_name': 'Luo (Zhu passage)', 'art': 'scene-zhushan',
        'quote': '丹水出焉東南流注于洛水',
        'description': '洛水在竹山段承接丹水，本段没有交代洛水的源头或完整河道。关联竹山仅为说明出处，配图不复原现实流域。',
        'en_description': 'The Luo receives the Dan in the Zhu passage, which gives neither the Luo’s source nor its full course. Mount Zhu is a source context, and the illustration does not reconstruct a modern basin.',
        'en_quote': 'The Dan rises here and flows southeast into the Luo.',
    },
    {
        'id': 'material-xishan-shuiyu-zhushan', 'slug': 'zhushan', 'kind': 'material', 'group': 'natural_features',
        'name': '水玉（竹山段）', 'en_name': 'Water jade (Zhu passage)', 'art': 'scene-zhushan', 'relation_scope': 'water',
        'quote': '其中多水玉多人魚',
        'description': '水玉接在丹水向东南注洛的水文之后。此处保留物产名和水域上下文，不单凭名称把它确定为现代矿物；场景中的浅色水边石只作示意。',
        'en_description': 'Water jade follows the Dan-to-Luo account. Its textual name and water context are retained without identifying a modern mineral. Pale stones in the shared scene are illustrative only.',
        'en_quote': 'Water jade and Renyu are abundant in this water account.',
    },
    {
        'id': 'beast-xishan-renyu-zhushan', 'slug': 'zhushan', 'kind': '鱼', 'group': 'beasts',
        'name': '人鱼（竹山段）', 'en_name': 'Renyu (Zhu passage)', 'art': 'creature-renyu-zhushan', 'relation_scope': 'water',
        'quote': '其中多水玉多人魚',
        'description': '竹山经文在水文中列人鱼，没有写人面、人身或鱼尾人形。郭注另说“如䱱鱼四脚”，配图据此采用四足水生形体；不把郭注混为正文，也不合并其他篇段的同名人鱼。',
        'en_description': 'The main text names Renyu in its water account without a human face or torso. Four feet and a comparison with ti fish come from Guo Pu’s separate commentary, guiding a four-limbed aquatic illustration rather than a mermaid or a merger with namesakes elsewhere.',
        'en_quote': 'Water jade and Renyu are abundant in this water account.',
        'commentary_quote': '如䱱魚四脚',
    },
    {
        'id': 'beast-xishan-haozhi-zhushan', 'slug': 'zhushan', 'kind': '兽', 'group': 'beasts',
        'name': '毫彘', 'en_name': 'Haozhi', 'art': 'creature-haozhi',
        'quote': '有獸焉其状如豚而白毛大如笄而黑端名曰毫彘',
        'description': '毫彘像豚，白毛粗大如笄、末端黑；“笄”是大小形状的比喻，不画成插在身上的人造簪针。郭注另有以背毫射物的说法，配图只呈现黑端白毫和豚形，不画攻击情节。',
        'en_description': 'Haozhi resembles a pig, with white hairs as thick as hairpins and black tips. Hairpins are a comparison, not manufactured objects attached to its body. The commentary’s shooting-bristle account remains separate; the image shows the bristles and pig-like form without an attack.',
        'en_quote': 'Haozhi resembles a pig with white hairs as thick as hairpins and black tips.',
        'commentary_quote': '笄簮属；狟猪也夾髀有麄豪長數尺以脊上毫射物亦自為牝牡狟或作假吳楚呼為鸞猪亦此𩔖也',
    },
    {
        'id': 'plant-xishan-panmu', 'slug': 'fushan', 'kind': 'plant', 'group': 'natural_features',
        'name': '盼木', 'en_name': 'Panmu', 'art': 'plant-panmu',
        'quote': '多盼木枳葉而無傷木蟲居之',
        'description': '盼木的叶被比作枳，原文又说无伤、木虫居之。插画用无尖刺的概括树形与小树洞示意，树叶、树冠和虫形细节均属艺术解释，不虚构独立虫种或未载花果。',
        'en_description': 'Panmu has leaves compared to zhi, does not injure, and houses wood insects. A generalized thornless tree and a small hollow illustrate the account; foliage, crown and generic insect details are artistic choices, not a named insect species or added flowers and fruit.',
        'en_quote': 'Panmu has leaves like zhi but does not injure; wood insects dwell in it.',
        'commentary_quote': '音羙目盻𠔃之眄；枳剌針也能傷人故名云；在樹之中',
    },
    {
        'id': 'plant-xishan-xuncao', 'slug': 'fushan', 'kind': 'plant', 'group': 'natural_features',
        'name': '薰草', 'en_name': 'Xuncao', 'art': 'plant-xuncao',
        'quote': '有草焉名曰薰草麻葉而方莖赤華而黑實臭如蘼蕪佩之可以已癘',
        'description': '薰草的麻叶、方茎、赤花、黑实都来自原文，气味被比作蘼芜。插画突出茎的棱面与花果色差，不把气味变成烟雾，也不描绘佩用治病；蘼芜只留作气味参照，不新增形貌未明的独立卡。',
        'en_description': 'Hemp-like leaves, square stems, red flowers and black fruit are stated in the text, with scent compared to miwu. Angular stems and contrasting flowers and fruit guide the image. No visible scent clouds or treatment scene is invented; miwu remains a scent comparison.',
        'en_quote': 'Xuncao has hemp-like leaves, square stems, red flowers and black fruit, and a scent like miwu. Wearing it is said to relieve li.',
        'commentary_quote': '音訓；蘼蕪香草易曰其臭如蘭眉無两音',
    },
]


ENTITIES += [
    {
        'id': 'water-xishan-qi-yuci', 'slug': 'yuci', 'kind': 'water', 'group': 'natural_features',
        'name': '漆水（羭次段）', 'en_name': 'Qi (Yuci passage)', 'art': 'scene-yuci',
        'quote': '漆水出焉北流注于渭',
        'description': '漆水从羭次山流出，向北注渭。郭注另提岐山的漆水，只作为注文保留，不据此为本卡添加现代坐标或完整河道。与其他山段的入渭水文分别关联出处。',
        'en_description': 'The Qi rises at Yuci and flows north into the Wei. Guo Pu mentions a Qi River at Qishan; this remains commentary, without assigning modern coordinates or a complete course. Its source passage stays distinct from other inflows into the Wei.',
        'en_quote': 'The Qi River rises here and flows north into the Wei.',
        'commentary_quote': '今漆水出岐山',
    },
    {
        'id': 'material-xishan-yingyuan-yuci', 'slug': 'yuci', 'kind': 'material', 'group': 'natural_features',
        'name': '嬰垣之玉', 'en_name': 'Yingyuan jade', 'art': 'scene-yuci',
        'quote': '其隂多赤銅其陽多嬰垣之玉',
        'description': '嬰垣之玉记在羭次山阳面。郭注列垣、短、根、埋等异文，并称传写谬错、未可得详；本卡保留底本名称与这一不确定性，不判定现代矿物。浅色石块仅作场景示意。',
        'en_description': 'Yingyuan jade occurs on Yuci’s sunny side. The commentary lists variant characters and says copying errors leave the name uncertain. The source spelling and uncertainty are preserved without a modern mineral identification; pale stones in the shared scene are illustrative.',
        'en_quote': 'Red copper occurs on its shaded side and Yingyuan jade on its sunny side.',
        'commentary_quote': '垣或作短或作根或作埋傳寫謬錯未可得詳',
    },
    {
        'id': 'beast-xishan-xiao-yuci', 'slug': 'yuci', 'kind': '兽', 'group': 'beasts',
        'name': '囂（羭次兽）', 'en_name': 'Xiao (Yuci beast)', 'art': 'creature-xiao-yuci',
        'quote': '有獸焉其狀如禺而長臂善投其名曰囂',
        'description': '囂形如禺，长臂、善投。郭注另以猕猴与投掷解释。配图突出两条长臂，手中小石仅为表现善投的艺术选择，不添加投掷目标、武器或攻击故事；与他篇同名字物分开。',
        'en_description': 'Xiao resembles a yu monkey, with long arms and skill at throwing. Guo Pu compares it to a macaque and glosses throwing. The illustration emphasizes two long arms; a small held stone is an artistic suggestion, without an invented target, weapon or attack story. Namesakes elsewhere remain separate.',
        'en_quote': 'A beast called Xiao resembles a monkey, with long arms and skill at throwing.',
        'commentary_quote': '亦在畏獸𦘕中似猕猴投擲也',
    },
    {
        'id': 'beast-xishan-tuofei-yuci', 'slug': 'yuci', 'kind': '鸟', 'group': 'beasts',
        'name': '槖𩇯', 'en_name': 'Tuofei', 'art': 'bird-tuofei-yuci',
        'quote': '有鳥焉其狀如梟人面而一足曰槖𩇯冬見夏蟄服之不畏雷',
        'description': '槖𩇯形如枭，却有人面、独足，冬见夏蛰。郭注释服为着其毛羽，并释雷为天雷、另记或作灾；不解作食鸟，不把古籍所记不畏雷画成实际防雷能力。颜色与羽纹为艺术演绎。',
        'en_description': 'Tuofei is owl-like, with a human face and exactly one foot, appearing in winter and dormant in summer. The commentary explains wearing its feathers, glosses thunder, and records a variant reading of calamity. This is neither an eating account nor evidence of real protection from lightning. Colors and feather patterns are artistic choices.',
        'en_quote': 'Tuofei resembles an owl, with a human face and one foot. It appears in winter and lies dormant in summer. Wearing it is said to remove fear of thunder.',
        'commentary_quote': '音肥；著其毛羽令人不畏天雷也或作灾',
    },
]


ENTITIES += [
    {
        'id': 'water-xishan-zhu-shishan', 'slug': 'shishan', 'kind': 'water', 'group': 'natural_features',
        'name': '逐水（时山段）', 'en_name': 'Zhu (Shi passage)', 'art': 'scene-shishan',
        'quote': '逐水出焉北流注于渭其中多水玉',
        'description': '逐水出自无草木的时山，向北注渭。郭注“或作遂”是逐字的异文，不另建一条遂水；英文Zhu与竹水读音转写相同，但两条水保持独立ID和出处，不合并河道。',
        'en_description': 'The Zhu rises at barren Mount Shi and flows north into the Wei. The commentary gives sui as a variant character, not another river. Its English romanization matches the Zhu of Mount Zhu, but the two retain separate IDs and sources without merging their courses.',
        'en_quote': 'The Zhu River rises here and flows north into the Wei; water jade is abundant in it.',
        'commentary_quote': '或作遂',
    },
    {
        'id': 'material-xishan-shuiyu-shishan', 'slug': 'shishan', 'kind': 'material', 'group': 'natural_features',
        'name': '水玉（时山段）', 'en_name': 'Water jade (Shi passage)', 'art': 'scene-shishan', 'relation_scope': 'water',
        'quote': '逐水出焉北流注于渭其中多水玉',
        'description': '时山水玉见于逐水向北注渭的水文记述，与竹山段同名物产分别保存出处。经文未在这里说明颜色、晶形或现代成分，配图的浅色水边石仅为示意，不当作矿物鉴定。',
        'en_description': 'Shi’s water jade occurs in the Zhu-to-Wei account, with a source separate from the namesake material at Mount Zhu. This passage gives no color, crystal form or modern composition. Pale streamside stones are an illustration, not a mineral identification.',
        'en_quote': 'The Zhu rises here and flows north into the Wei; water jade is abundant in it.',
    },
]


ENTITIES += [
    {
        'id': 'water-xishan-dan-nanshan', 'slug': 'nanshan-west', 'kind': 'water', 'group': 'natural_features',
        'name': '丹水（西山经南山段）', 'en_name': 'Dan (Western Mount Nan passage)', 'art': 'scene-nanshan-west',
        'quote': '丹水出焉北流注于渭',
        'description': '西山经南山的丹水向北注渭，与竹山东南注洛的丹水、南山经同名水域分别建卡。中文同名不据此合并河道；只记录本段的流向与出处，不补现代坐标。',
        'en_description': 'The Dan at Mount Nan in the Western Mountains flows north into the Wei. It remains separate from Mount Zhu’s Dan flowing southeast into the Luo, and from the Southern Mountains namesake. A shared name does not establish a single course or modern location.',
        'en_quote': 'The Dan River rises here and flows north into the Wei.',
    },
    {
        'id': 'material-xishan-dansu-nanshan', 'slug': 'nanshan-west', 'kind': 'material', 'group': 'natural_features',
        'name': '丹粟（西山经南山段）', 'en_name': 'Dansu (Western Mount Nan passage)', 'art': 'scene-nanshan-west',
        'quote': '南山上多丹粟',
        'description': '丹粟在经文中只记山上多有，本段没有详述成分或形貌。本卡保留原名，不直接鉴定现代矿物，也不把粟字画成种植的谷物田；山景中的朱砂色小点只是艺术示意。',
        'en_description': 'The passage records much dansu above without detailing composition or form. The textual name is retained without a modern mineral identification or interpreting su as cultivated grain. Small cinnabar-colored marks in the shared scene are illustrative only.',
        'en_quote': 'Much dansu occurs above on Mount Nan.',
    },
    {
        'id': 'beast-xishan-mengbao-nanshan', 'slug': 'nanshan-west', 'kind': '兽', 'group': 'beasts',
        'name': '猛豹（西山经南山段）', 'en_name': 'Mengbao (Western Mount Nan passage)', 'art': 'creature-mengbao-nan',
        'quote': '獸多猛豹',
        'description': '经文列猛豹之名，没有展开形貌。郭注另说似熊而小、毛浅有光泽，并记食蛇、铜铁及出蜀中；配图取小型熊状、短毛，不画成普通花豹，不演绎食金属或捕蛇故事。豹字另有作虎的异文。',
        'en_description': 'The main text names Mengbao without describing its form. Guo Pu describes a small bear-like animal with short glossy fur, and records eating snakes and metals and an origin in Shu. The image follows the commentary’s bear-like form without leopard spots or an invented feeding scene. A variant replaces bao with hu.',
        'en_quote': 'Its beasts include many Mengbao.',
        'commentary_quote': '猛豹似熊而小毛淺有光澤能食蛇食銅鐡出蜀中；豹或作虎',
        'art_reference': ['郭注形貌示意 · 熊状、小、短毛有光泽来自郭注；经文仅列名，配色与姿态为艺术解释。', 'Commentary-based form · Small bear-like shape and short glossy fur come from Guo Pu; the main text only names it. Colors and pose are artistic choices.'],
    },
    {
        'id': 'beast-xishan-shijiu-nanshan', 'slug': 'nanshan-west', 'kind': '鸟', 'group': 'beasts',
        'name': '尸鳩（西山经南山段）', 'en_name': 'Shijiu (Western Mount Nan passage)', 'art': 'bird-shijiu-nan',
        'quote': '鳥多尸鳩',
        'description': '经文只列尸鳩之名。郭注先比作布谷类，又记或曰鶘鸇，鳩字另有作丘的异文；配图采用布谷类的一种概括参照，颜色与羽纹是艺术选择，不据此确定唯一现代鸟种。',
        'en_description': 'The main text only names Shijiu. Guo Pu compares it to cuckoo-kind but also records an alternative, huzhan; qiu is a variant character for jiu. The image uses one generalized cuckoo-like comparison. Colors and feather patterns are artistic choices, not a unique modern species identification.',
        'en_quote': 'Its birds include many Shijiu.',
        'commentary_quote': '尸鳩布谷𩔖也或曰鶘鸇也鳩或作丘',
        'art_reference': ['郭注布谷类的一种艺术参照 · 鶘鸇异说并存，不作现代鸟种鉴定；配色羽纹为演绎。', 'One artistic reference to Guo Pu’s cuckoo-kind comparison · The alternative huzhan comparison remains; this is not a modern species identification. Colors and patterns are artistic choices.'],
    },
]


ENTITIES += [
    {
        'id': 'water-xishan-qian-dashi', 'slug': 'dashi', 'kind': 'water', 'group': 'natural_features',
        'name': '涔水（大时段）', 'en_name': 'Qian (Dashi passage)', 'art': 'scene-dashi',
        'quote': '涔水岀焉北流注于渭',
        'description': '涔水从大时山流出，向北注渭。郭注“音潜”是本卡英文Qian的依据，中文保留涔字。它与同山向南注汉的清水分开，不把两条水画作相通的河道；图中左右位置只是构图。',
        'en_description': 'The Qian rises at Dashi and flows north into the Wei. Its English name follows Guo Pu’s pronunciation gloss, while the Chinese source character is retained. It remains separate from the Qing flowing south into the Han. Left and right in the shared image are compositional choices, not compass directions.',
        'en_quote': 'The Qian River rises here and flows north into the Wei.',
        'commentary_quote': '音潜',
    },
    {
        'id': 'water-xishan-qing-dashi', 'slug': 'dashi', 'kind': 'water', 'group': 'natural_features',
        'name': '清水（大时段）', 'en_name': 'Qing (Dashi passage)', 'art': 'scene-dashi',
        'quote': '清水出焉南流注于漢水',
        'description': '清水从大时山流出、向南注汉，与北注渭的涔水分开。郭注另提河内、武县、黑山一处也出清水，保留其地名比较及电子录文，不据此把大时山或本卡清水锁定为现代坐标。',
        'en_description': 'The Qing rises at Dashi and flows south into the Han, separately from the north-flowing Qian. Guo Pu mentions another Qing at Heishan in the Henei and Wu County account. This comparison and the captured wording remain commentary, without fixing Dashi or its Qing to modern coordinates.',
        'en_quote': 'The Qing River rises here and flows south into the Han.',
        'commentary_quote': '今河内武縣縣北黑山亦出清水',
    },
    {
        'id': 'water-xishan-han-dashi', 'slug': 'dashi', 'kind': 'water', 'group': 'natural_features',
        'name': '汉水（大时段）', 'en_name': 'Han (Dashi passage)', 'art': 'scene-dashi',
        'quote': '清水出焉南流注于漢水',
        'description': '汉水在大时段中承接清水，本段没有展开汉水的源头或完整河道。关联大时山只说明出处；图中只示意山中出水，不把整条汉水、现代汇流点或渭汉相通画入场景。',
        'en_description': 'The Han receives the Qing in the Dashi passage, which does not describe the Han’s source or complete course. Dashi provides textual context. The illustration shows mountain waters, not the entire Han, a modern confluence, or a connection between the Wei and Han.',
        'en_quote': 'The Qing rises here and flows south into the Han.',
    },
    {
        'id': 'material-xishan-silver-dashi', 'slug': 'dashi', 'kind': 'material', 'group': 'natural_features',
        'name': '银（大时段）', 'en_name': 'Silver (Dashi passage)', 'art': 'scene-dashi',
        'quote': '隂多銀陽多白玉',
        'description': '银见于大时山阴面，白玉见于阳面。本卡保留物产名与原文方位，不补矿种、矿脉、开采或冶炼过程；场景里的灰色岩面小块仅作艺术示意，不画银锭或钱币。',
        'en_description': 'Silver occurs on Dashi’s shaded side, opposite the white jade on its sunny side. The material name and textual aspect are retained without an ore type, deposit, mine or smelting process. Small gray rock patches are illustrative, without silver bars or coins.',
        'en_quote': 'Silver occurs on its shaded side and white jade on its sunny side.',
    },
    {
        'id': 'material-xishan-white-jade-dashi', 'slug': 'dashi', 'kind': 'material', 'group': 'natural_features',
        'name': '白玉（大时段）', 'en_name': 'White jade (Dashi passage)', 'art': 'scene-dashi',
        'quote': '隂多銀陽多白玉',
        'description': '白玉记在大时山阳面，与本段阴面的银分别建卡。这里只保留古籍物产名，不据名称鉴定现代矿物；与其他山段的白玉、水玉或具名玉石保持各自出处，浅色山石只是配图示意。',
        'en_description': 'White jade occurs on Dashi’s sunny side, separate from silver on its shaded side. The textual material name does not establish a modern mineral identification. Namesake materials and named jades in other passages retain their own sources; pale rocks in the image are illustrative only.',
        'en_quote': 'Silver occurs on its shaded side and white jade on its sunny side.',
    },
]


ENTITIES += [
    {
        'id': 'water-xishan-mian-bozhong', 'slug': 'bozhong', 'kind': 'water', 'group': 'natural_features',
        'name': '沔（嶓冡段）', 'en_name': 'Mian (Bozhong passage)', 'art': 'scene-bozhong',
        'quote': '漢水出焉而東南流注于沔',
        'description': '沔在本段承接由嶓冡流出的汉水。郭注另有江夏、安陆与江即沔水的说明，保持为注文，不据此推定现代汇流点或把两名称删并。共享山景只示意山中出水，不复原沔的完整河道。',
        'en_description': 'The Mian receives the Han in this passage. Guo Pu’s account mentioning Jiangxia, Anlu and the Mian remains commentary, without fixing a modern confluence or deleting either textual name. The shared scene illustrates mountain waters, not the Mian’s full course.',
        'en_quote': 'The Han rises here and flows southeast into the Mian.',
        'commentary_quote': '至江夏安陸縣江即沔水',
    },
    {
        'id': 'water-xishan-xiao-bozhong', 'slug': 'bozhong', 'kind': 'water', 'group': 'natural_features',
        'name': '囂水（嶓冡段）', 'en_name': 'Xiao (Bozhong water)', 'art': 'scene-bozhong',
        'quote': '囂水出焉北流注于湯水',
        'description': '囂水从嶓冡流出，向北注汤水，与同段向东南注沔的汉水分开。囂在快照中为缺字图，影印41页核定后修复阅读引文，原快照不改；它也与羭次山同字兽名囂分开建卡。',
        'en_description': 'The Xiao rises at Bozhong and flows north into the Tang, separately from the Han-to-Mian account. Its image glyph was checked on scan page 41 and restored in the reading text while the snapshot remains unchanged. This water is also separate from the beast named Xiao at Yuci.',
        'en_quote': 'The Xiao rises here and flows north into the Tang.',
    },
    {
        'id': 'water-xishan-tang-bozhong', 'slug': 'bozhong', 'kind': 'water', 'group': 'natural_features',
        'name': '汤水（嶓冡段）', 'en_name': 'Tang (Bozhong passage)', 'art': 'scene-bozhong',
        'quote': '囂水出焉北流注于湯水',
        'description': '汤水在此承接向北流来的囂水。郭注“或作阳”作为异文保留，不另造一条阳水，不补汤水源头、温泉性质或现代河道；图中的水不画成沸水。',
        'en_description': 'The Tang receives the north-flowing Xiao. Guo Pu records yang as a variant character, not another river. No source, hot-spring property or modern course is added; the illustration does not show boiling water.',
        'en_quote': 'The Xiao rises here and flows north into the Tang.',
        'commentary_quote': '或作陽',
    },
    {
        'id': 'plant-xishan-taozhi-bozhong', 'slug': 'bozhong', 'kind': 'plant', 'group': 'natural_features',
        'name': '桃枝（嶓冡段）', 'en_name': 'Taozhi (Bozhong passage)', 'art': 'scene-bozhong',
        'quote': '其上多桃枝鈎端',
        'description': '桃枝与鈎端在山上并列，正文未在此展开形貌。保留名称与出处，不因桃字补画桃花、桃果或认作普通桃树；共享山景的植被仅为概括示意，不鉴定现代植物。',
        'en_description': 'Taozhi is listed beside Gouduan above the mountain without a description here. Its name and source are retained without adding peach flowers or fruit or identifying an ordinary peach tree. Vegetation in the shared scene is schematic, not a modern plant identification.',
        'en_quote': 'Taozhi and Gouduan are abundant above.',
    },
    {
        'id': 'plant-xishan-gouduan-bozhong', 'slug': 'bozhong', 'kind': 'plant', 'group': 'natural_features',
        'name': '鈎端（嶓冡段）', 'en_name': 'Gouduan (Bozhong passage)', 'art': 'scene-bozhong',
        'quote': '其上多桃枝鈎端',
        'description': '鈎端与桃枝并列，郭注另说鈎端桃枝属。保留这一比较，不按鈎字补出金属钩或棘刺；本卡复用概括山景，不把未载的花果、叶形当作原文事实。',
        'en_description': 'Gouduan is listed beside Taozhi, with the commentary placing it in Taozhi’s kind. This comparison does not justify adding metal hooks or thorns. The shared scene is schematic and does not establish unrecorded flowers, fruit or leaf shapes.',
        'en_quote': 'Taozhi and Gouduan are abundant above.',
        'commentary_quote': '鈎端桃枝属',
    },
    {
        'id': 'animal-xishan-xi-bozhong', 'slug': 'bozhong', 'kind': '兽', 'group': 'beasts',
        'name': '犀（嶓冡段）', 'en_name': 'Xi (Bozhong passage)', 'art': 'scene-bozhong',
        'quote': '獸多犀兕熊羆',
        'description': '犀在本段与兕、熊、羆并列，没有另写颜色、角数或形貌。保留嶓冡出处，与南山经同名条目分开；本卡使用统一留空剪影，不凭列名补造身体特征。',
        'en_description': 'Xi is listed with si, bears and Pi without colors, horn counts or morphology here. Its Bozhong source remains separate from the Southern Mountains namesake. The card uses the shared unknown-creature silhouette without inventing anatomy from the name.',
        'en_quote': 'Its beasts include xi, si, bears and Pi.',
    },
    {
        'id': 'animal-xishan-si-bozhong', 'slug': 'bozhong', 'kind': '兽', 'group': 'beasts',
        'name': '兕（嶓冡段）', 'en_name': 'Si (Bozhong passage)', 'art': 'scene-bozhong',
        'quote': '獸多犀兕熊羆',
        'description': '兕与犀分别列名，本段未述角数、颜色或现代物种。本卡保留独立名称与嶓冡出处，不把兕与犀合为一张，也不把别篇形貌移入本段引文；配图使用统一留空剪影。',
        'en_description': 'Si is named separately from xi without horn counts, colors or a modern species identification. Its name and Bozhong source remain distinct, without importing morphology from another passage. The illustration is the shared unknown-creature silhouette.',
        'en_quote': 'Its beasts include xi, si, bears and Pi.',
    },
    {
        'id': 'animal-xishan-bear-bozhong', 'slug': 'bozhong', 'kind': '兽', 'group': 'beasts',
        'name': '熊（嶓冡段）', 'en_name': 'Bear (Bozhong passage)', 'art': 'scene-bozhong',
        'quote': '獸多犀兕熊羆',
        'description': '熊与羆在正文中分别列名。郭注黄白色、猛憨、能拔树的说明属于羆，不转给熊；本卡只保留熊的本段出处，使用统一留空剪影，不补画毛色或行为。',
        'en_description': 'Bear and Pi are named separately. The commentary’s yellow-and-white coloring, strength and tree-uprooting account belong to Pi, not this bear entry. This card retains its source and uses the shared unknown-creature silhouette without added coat colors or behavior.',
        'en_quote': 'Its beasts include xi, si, bears and Pi.',
    },
    {
        'id': 'animal-xishan-pi-bozhong', 'slug': 'bozhong', 'kind': '兽', 'group': 'beasts',
        'name': '羆（嶓冡段）', 'en_name': 'Pi (Bozhong passage)', 'art': 'animal-pi-bozhong',
        'quote': '獸多犀兕熊羆',
        'description': '正文只列羆之名。郭注另说似熊而黄白色，猛憨、能拔树；配图据此采用黄白色熊状形体，色块分布与姿态为演绎，不鉴定现代物种，也不画拔树情节。',
        'en_description': 'The main text only names Pi. Guo Pu describes a bear-like animal with yellow-and-white coloring, strength and an ability to uproot trees. The image follows the commentary’s form and colors; their distribution and pose are artistic choices, without a modern species identification or uprooting scene.',
        'en_quote': 'Its beasts include xi, si, bears and Pi.',
        'commentary_quote': '羆似熊而黄白色猛憨能㧞樹',
        'art_reference': ['郭注形貌示意 · 熊状黄白色来自郭注，正文仅列名；色块分布与姿态为艺术解释。', 'Commentary-based form · Bear-like yellow-and-white coloring comes from Guo Pu; the main text only names Pi. Color distribution and pose are artistic choices.'],
    },
    {
        'id': 'bird-xishan-baihan-bozhong', 'slug': 'bozhong', 'kind': '鸟', 'group': 'beasts',
        'name': '白翰（嶓冡段）', 'en_name': 'Baihan (Bozhong passage)', 'art': 'bird-baihan-bozhong',
        'quote': '鳥多白翰赤鷩',
        'description': '白翰在正文中仅列名。郭注以白鵫、𪂂雉、白雉说明，配图采用概括白色雉形；不据这些古名鉴定唯一现代鸟种，喙足细节与姿态为艺术选择。',
        'en_description': 'The main text only names Baihan. Guo Pu compares it to white zhuo and pheasant names. A generalized white pheasant form follows that commentary without a unique modern species identification; beak and foot details and pose are artistic choices.',
        'en_quote': 'Its birds include many Baihan and Chibie.',
        'commentary_quote': '白翰白鵫也亦名𪂂雉又曰白雉',
        'art_reference': ['郭注白雉参照 · 正文仅列白翰之名，具体鸟形与姿态为艺术演绎，不作现代物种鉴定。', 'Guo Pu’s white-pheasant comparison · The main text only names Baihan. Specific form and pose are artistic, without a modern species identification.'],
    },
    {
        'id': 'bird-xishan-chibie-bozhong', 'slug': 'bozhong', 'kind': '鸟', 'group': 'beasts',
        'name': '赤鷩（嶓冡段）', 'en_name': 'Chibie (Bozhong passage)', 'art': 'bird-chibie',
        'quote': '鳥多白翰赤鷩',
        'description': '嶓冡正文只列赤鷩之名。本卡保留独立出处并复用小华赤鷩插画；红腹、黄冠、绿头出自小华郭注，不补进本段原文或移给白翰。',
        'en_description': 'Bozhong only names Chibie. Its source stays separate while reusing the Xiaohua illustration. Red belly, yellow crown and green head come from Xiaohua’s commentary, not this quotation or the Baihan entry.',
        'en_quote': 'Its birds include many Baihan and Chibie.',
        'art_reference': ['复用小华赤鷩示意图 · 红腹黄冠绿头来自小华郭注，本段仅列名。', 'Reused Xiaohua Chibie illustration · Red belly, yellow crown and green head come from Xiaohua’s commentary; this passage only names it.'],
    },
    {
        'id': 'plant-xishan-gurong-bozhong', 'slug': 'bozhong', 'kind': 'plant', 'group': 'natural_features',
        'name': '蓇蓉（嶓冡段）', 'en_name': 'Gurong (Bozhong passage)', 'art': 'plant-gurong-bozhong',
        'quote': '有草焉其葉如蕙其本如桔梗黑華而不實名曰蓇蓉食之使人無子',
        'description': '蓇蓉叶如蕙，本如桔梗；郭注释本为根，故图中显露概括粗根。黑花、不实来自正文，不把黑花画成果实或补种荚。形貌比较不等于现代植物鉴定；末句食用影响仅作古籍记述，不作现实食用建议。',
        'en_description': 'Gurong has hui-like leaves and a base compared to jiegeng; Guo Pu glosses the base as root. The image therefore exposes a generalized thick root. Black flowers and no fruit come from the main text: no black berries or seed pods are added. The comparisons do not identify a modern species; the final eating claim remains an ancient account.',
        'en_quote': 'Gurong has leaves like hui, a root like jiegeng, black flowers and no fruit. Eating it is said to leave a person without children.',
        'commentary_quote': '蕙香草蘭属也或以蕙為薰葉失之音惠；本根也；爾雅釋草曰榮而不實謂之蓇音骨',
    },
]
ENTITIES += [
    {
        'id': 'beast-xishan-xibian-tiandi', 'slug': 'tiandi', 'kind': '兽', 'group': 'beasts',
        'name': '谿邊（天帝山）', 'en_name': 'Xibian (Tiandi)', 'art': 'creature-xibian-tiandi',
        'quote': '有獸焉其状如狗名曰谿邊席其皮者不蠱',
        'description': '谿邊在经文中形如狗，未记多首、多尾、角翼或特殊毛色。插画用概括刻纹与姿态表现，不增加器官。谿、邊的或作谷、或作遺保留在郭注；席其皮者不蛊是古籍所载功效，不画剥皮、皮席或用蛊情节。',
        'en_description': 'Xibian is dog-shaped; the text specifies no extra heads, tails, horns, wings or coat colors. Carved motifs and pose provide the artistic treatment without added organs. Commentary preserves variant characters for its name. The claim about using its hide as a mat remains an ancient account, without an illustrated skinning, hide mat or gu scene.',
        'en_quote': 'A dog-shaped beast is called Xibian. Using its hide as a mat is said to protect against gu.',
        'commentary_quote': '或作谷；或作遺',
    },
    {
        'id': 'beast-xishan-li-tiandi', 'slug': 'tiandi', 'kind': '鸟', 'group': 'beasts',
        'name': '櫟（天帝山鸟）', 'en_name': 'Li (Tiandi bird)', 'art': 'bird-li-tiandi',
        'quote': '有鳥焉其状如鶉黑文而赤翁名曰櫟食之已痔',
        'description': '櫟是本段鸟名，形如鹑，黑纹、赤翁。郭注释翁为头下毛，读如汲瓮之瓮；配图把红色置于头下羽簇，不改成红冠、红头或整片红腹。櫟郭注音沙砾之砾，英文写Li，与木名区分；食用功效仅作古籍记述。',
        'en_description': 'Li is a quail-shaped bird with black markings and red weng. Guo Pu defines weng as feathers below the head and supplies its pronunciation. The image places red on a small feather tuft there, rather than on a crown, the whole head or belly. The name follows the commentary pronunciation Li and denotes a bird here. The eating claim remains an ancient account.',
        'en_quote': 'A quail-shaped bird with black markings and red weng is called Li. Eating it is said to relieve hemorrhoids. Guo Pu glosses weng as feathers below the head.',
        'commentary_quote': '翁頭下毛音汲甕之甕；音沙礫之礫',
        'art_reference': ['经文黑纹赤翁 · 头下红色羽簇据郭注释翁，其他配色、刻纹与姿态为艺术解释。', 'Black markings and red weng · The red feather tuft below the head follows Guo Pu; other colors, carved patterns and pose are artistic choices.'],
    },
    {
        'id': 'plant-xishan-duheng-tiandi', 'slug': 'tiandi', 'kind': 'plant', 'group': 'natural_features',
        'name': '杜衡（天帝山）', 'en_name': 'Duheng (Tiandi)', 'art': 'plant-duheng-tiandi',
        'quote': '有草焉其状如葵其臭如蘼蕪名曰杜衡可以走馬食之已癭',
        'description': '杜衡形如葵，气味如蘼芜；这里保留古名比较，不鉴定为某种现代植物，也不把臭误译为恶臭。可以走马的郭注一说佩带使人便马，一说马得之而健走，两说并列，不画人马功效场景。经文没有在此写花色、果实或根形，配图只用概括葵状叶草。',
        'en_description': 'Duheng resembles kui and smells like miwu; the ancient comparisons do not identify a modern species or imply a foul odor. Guo Pu offers two readings of its horse claim: carrying it helps a person handle horses, or horses obtaining it run well. Neither is illustrated as an event. Flower color, fruit and root form are unspecified here, so the image uses only a generalized kui-like leafy herb.',
        'en_quote': 'An herb shaped like kui and smelling like miwu is called Duheng. It is said to help with horses, and eating it to relieve neck swellings. The commentary offers carrying it to aid horsemanship or horses obtaining it to run well as alternative readings.',
        'commentary_quote': '香草也；帶之令人便馬或曰馬得之而徤走',
    },
]


ENTITIES += [
    {
        'id': 'water-xishan-se-gaotu', 'slug': 'gaotu', 'kind': 'water', 'group': 'natural_features',
        'name': '薔水（皐塗段）', 'en_name': 'Se (Gaotu passage)', 'art': 'scene-gaotu',
        'quote': '薔水出焉西流注于諸資之水',
        'description': '薔水出于皐塗，向西注诸资之水；郭注音色，保留或作蕢、又作富的异文，不另造两条河。英文依郭注写Se，不按蔷薇的读音写Qiang；与同段向南流的塗水分别建关系。',
        'en_description': 'The Se rises at Gaotu and flows west into Zhuzi. Its name follows Guo Pu’s pronunciation gloss; variant characters remain variants rather than additional rivers. It stays separate from the south-flowing Tu.',
        'en_quote': 'The Se rises here and flows west into the Zhuzi.',
        'commentary_quote': '音色或作蕢又作富',
    },
    {
        'id': 'water-xishan-zhuzi-gaotu', 'slug': 'gaotu', 'kind': 'water', 'group': 'natural_features',
        'name': '诸资之水（皐塗段）', 'en_name': 'Zhuzi (Gaotu passage)', 'art': 'scene-gaotu',
        'quote': '薔水出焉西流注于諸資之水',
        'description': '诸资之水在本段承接向西流来的薔水。经文没有在此交代诸资的源头、完整河道或现代位置；共享山景不把两条出山水流合接到同一承接水域。',
        'en_description': 'Zhuzi receives the west-flowing Se. Its source, full course and modern position are not given here; the shared scene does not join both mountain streams into one receiving water.',
        'en_quote': 'The Se rises here and flows west into the Zhuzi.',
    },
    {
        'id': 'water-xishan-tu-gaotu', 'slug': 'gaotu', 'kind': 'water', 'group': 'natural_features',
        'name': '塗水（皐塗段）', 'en_name': 'Tu (Gaotu passage)', 'art': 'scene-gaotu',
        'quote': '塗水出焉南流注于集獲之水',
        'description': '塗水从皐塗流出，向南注集获之水，与薔水向西注诸资的关系分开。只保留本段源出与流入方向，不补现代河道、汇流点或精确地图位置。',
        'en_description': 'The Tu rises at Gaotu and flows south into Jihuo, separately from the Se-to-Zhuzi account. Only the textual source and flow direction are retained, without a modern river course or confluence.',
        'en_quote': 'The Tu rises here and flows south into the Jihuo.',
    },
    {
        'id': 'water-xishan-jihuo-gaotu', 'slug': 'gaotu', 'kind': 'water', 'group': 'natural_features',
        'name': '集获之水（皐塗段）', 'en_name': 'Jihuo (Gaotu passage)', 'art': 'scene-gaotu',
        'quote': '塗水出焉南流注于集獲之水',
        'description': '集获之水承接由皐塗向南流来的塗水。本段没有给出其源头、全程或现代地望；不把集获与诸资合并为同一水域。',
        'en_description': 'Jihuo receives the south-flowing Tu. Its source, full course and modern location are unspecified, and it is not merged with Zhuzi.',
        'en_quote': 'The Tu rises here and flows south into the Jihuo.',
    },
    {
        'id': 'material-xishan-dansu-gaotu', 'slug': 'gaotu', 'kind': 'material', 'group': 'natural_features',
        'name': '丹粟（皐塗段）', 'en_name': 'Dansu (Gaotu passage)', 'art': 'scene-gaotu',
        'quote': '其陽多丹粟',
        'description': '丹粟见于皐塗阳面。保留原名与方位，不把粟字画成谷物田，也不鉴定现代矿物；与西山经南山段丹粟分别保留出处。山景少量朱色石纹仅作艺术示意。',
        'en_description': 'Dansu occurs on Gaotu’s sunny side. Its name and position are retained without turning su into a grain field or identifying a modern mineral. The Nan passage remains a separate source; red rock marks are schematic.',
        'en_quote': 'Dansu is abundant on its sunny side.',
    },
    {
        'id': 'material-xishan-silver-gaotu', 'slug': 'gaotu', 'kind': 'material', 'group': 'natural_features',
        'name': '银（皐塗段）', 'en_name': 'Silver (Gaotu passage)', 'art': 'scene-gaotu',
        'quote': '其隂多銀黄金',
        'description': '银与黄金并列于皐塗阴面。此卡保留独立名称与本段来源，不补采矿、冶炼或银锭，也不与大时山的银卡合并。',
        'en_description': 'Silver is listed beside gold on Gaotu’s shaded side. Its name and source remain distinct, without mines, smelting or ingots, and separate from Dashi’s silver entry.',
        'en_quote': 'Silver and gold are abundant on its shaded side.',
    },
    {
        'id': 'material-xishan-gold-gaotu', 'slug': 'gaotu', 'kind': 'material', 'group': 'natural_features',
        'name': '黄金（皐塗段）', 'en_name': 'Gold (Gaotu passage)', 'art': 'scene-gaotu',
        'quote': '其隂多銀黄金',
        'description': '黄金与银并列于皐塗阴面，分别建卡。本段未记矿体形态或采冶活动；配图用概括山石，不画金锭、金冠或宝藏。',
        'en_description': 'Gold is listed with silver on Gaotu’s shaded side and retains its own entry. No ore-body form or mining activity is described; the shared mountain scene adds no ingots, crown or treasure.',
        'en_quote': 'Silver and gold are abundant on its shaded side.',
    },
    {
        'id': 'plant-xishan-gui-gaotu', 'slug': 'gaotu', 'kind': 'plant', 'group': 'natural_features',
        'name': '桂木（皐塗段）', 'en_name': 'Gui trees (Gaotu passage)', 'art': 'scene-gaotu',
        'quote': '其上多桂木',
        'description': '桂木在本段只列山上多生，未写花色、果实或叶形。保留古名，不据桂字补画桂花、月宫或指定现代树种；共享山景林木仅为概括示意。',
        'en_description': 'Gui trees are listed above the mountain without flower color, fruit or leaf form. The ancient name does not establish modern osmanthus, a lunar palace or a specific modern species; scene vegetation is schematic.',
        'en_quote': 'Gui trees are abundant above.',
    },
    {
        'id': 'material-xishan-yu-gaotu', 'slug': 'gaotu', 'kind': 'material', 'group': 'natural_features',
        'name': '礜（皐塗段）', 'en_name': 'Yu stone (Gaotu passage)', 'art': 'scene-gaotu',
        'quote': '有白石焉其名曰礜可以毒鼠',
        'description': '礜在正文中是白石，所载毒鼠与郭注蚕食之而肥分别保留为古籍记述。郭注音豫，英文写Yu；不把它改成白玉或指定现代化学物质，也不把無條草的描述移给它。',
        'en_description': 'Yu is described as a white stone. Its mouse-poisoning claim and the commentary’s silkworm account remain ancient statements. The name follows Guo Pu’s pronunciation gloss, without identifying white jade or a modern chemical substance, or transferring Wutiao’s plant description to it.',
        'en_quote': 'A white stone called Yu is said to poison mice.',
        'commentary_quote': '今礜石殺鼠音豫蚕食之而肥',
    },
    {
        'id': 'plant-xishan-wutiao-gaotu', 'slug': 'gaotu', 'kind': 'plant', 'group': 'natural_features',
        'name': '無條（皐塗段）', 'en_name': 'Wutiao (Gaotu passage)', 'art': 'plant-wutiao-gaotu',
        'quote': '有草焉其状如槀苃其葉如葵而赤背名曰無條可以毒鼠',
        'description': '無條形如槀苃，叶如葵而叶背红。郭注以槀茇为香草，保留古名比较，不认定现代植物。配图翻出部分叶背突出红色，不补花果；毒鼠记述与白石礜分开，不画投毒或鼠类场景。',
        'en_description': 'Wutiao resembles gaoyou, with kui-like leaves and red undersides. The commentary compares gaoba to an aromatic herb, without a modern plant identification. Turned leaves reveal the red undersides; no flowers, fruit, poisoning event or mice are added, and the stone Yu remains distinct.',
        'en_quote': 'Wutiao resembles gaoyou, with kui-like leaves and red undersides, and is said to poison mice.',
        'commentary_quote': '槀茇香草',
    },
    {
        'id': 'beast-xishan-yingru-gaotu', 'slug': 'gaotu', 'kind': '兽', 'group': 'beasts',
        'name': '𤣎如（皐塗段）', 'en_name': 'Yingru (Gaotu passage)', 'art': 'creature-yingru-gaotu',
        'quote': '有獸焉其状如鹿而白尾馬足人手而四角名曰𤣎如',
        'description': '𤣎如鹿状，白尾、马足、人手、四角。郭注明确前两脚似人手，配图据此以前肢接人手、后肢接马蹄，仍是四肢；四角分别可数，不画成分叉鹿角，也不增添一双独立人臂。𤣎字和郭注嬰音保留，配色与姿态为艺术解释。',
        'en_description': 'Yingru is deer-shaped, with a white tail, horse feet, human hands and four horns. Guo Pu specifies that the front feet resemble hands; the image therefore has hand-ended forelimbs and horse-hoofed hindlimbs, still four limbs. Four separate horns replace branching antlers; no additional human arms are added. The source character and Ying pronunciation gloss are retained.',
        'en_quote': 'A deer-shaped beast with a white tail, horse feet, human hands and four horns is called Yingru.',
        'commentary_quote': '前两脚似人手；音猳𤣎之嬰',
        'art_reference': ['经文形貌与郭注分列 · 四角白尾据正文，前两脚似人手据郭注；配色与姿态为艺术解释。', 'Text and commentary distinguished · Four horns and a white tail follow the text; hand-like front feet follow Guo Pu. Colors and pose are artistic choices.'],
    },
    {
        'id': 'beast-xishan-shusi-gaotu', 'slug': 'gaotu', 'kind': '鸟', 'group': 'beasts',
        'name': '數斯（皐塗段）', 'en_name': 'Shusi (Gaotu passage)', 'art': 'bird-shusi-gaotu',
        'quote': '有鳥焉其状如鴟而人足名曰數斯食之已癭',
        'description': '數斯形如鸱而具人足，配图把两足的人形与鸟爪明确区别，不加人脸、人臂或额外肢体。正文食用记述写已癭，郭注或作癎，两字分别保留，不把注文异文直接改写进正文。',
        'en_description': 'Shusi is chi-shaped with human feet. The image distinguishes two human-like feet from bird talons without adding a human face, arms or extra limbs. The main text’s eating claim concerns neck swellings; Guo Pu records an alternative ailment character, retained separately rather than substituted into the quotation.',
        'en_quote': 'A chi-shaped bird with human feet is called Shusi. Eating it is said to relieve neck swellings.',
        'commentary_quote': '或作癎',
    },
]


ENTITIES += [
    {
        'id': 'plant-xishan-zhujian-huangshan', 'slug': 'huangshan', 'kind': 'plant', 'group': 'natural_features',
        'name': '竹箭（黄山段）', 'en_name': 'Zhujian bamboo (Huang passage)', 'art': 'scene-huangshan',
        'quote': '無草木多竹箭',
        'description': '黄山段说无草木，又说多竹箭，两句均保留。此卡按古名呈现竹类，不画成制成的箭矢、竹兵器或现代单一物种；山景只点出竹丛，不另添松林、花草。',
        'en_description': 'The passage says both no grass or trees and much zhujian bamboo. Both statements remain. The ancient bamboo name does not establish manufactured arrows, weapons or a unique modern species. The scene adds bamboo clumps without pine woodland, flowers or other herbs.',
        'en_quote': 'There is no grass or trees, but much zhujian bamboo.',
    },
    {
        'id': 'water-xishan-pan-huangshan', 'slug': 'huangshan', 'kind': 'water', 'group': 'natural_features',
        'name': '盼水（黄山段）', 'en_name': 'Mian (Huang passage)', 'art': 'scene-huangshan',
        'quote': '盼水出焉西流注于赤水',
        'description': '盼水出于黄山，向西注赤水。郭注用眄字说明读音，英文据此写Mian，中文保留盼字与本段出处；不与浮山盼木合并，也不补现代河道或精确坐标。',
        'en_description': 'The Mian rises at Huang and flows west into the Chi. Mian follows Guo Pu’s pronunciation gloss; the original Chinese character Pan and source remain unchanged. It is distinct from Fushan’s Panmu tree, without an added modern river course or location.',
        'en_quote': 'The Mian rises here and flows west into the Chi.',
        'commentary_quote': '音羙目眄𠔃之眄',
    },
    {
        'id': 'water-xishan-chi-huangshan', 'slug': 'huangshan', 'kind': 'water', 'group': 'natural_features',
        'name': '赤水（黄山段）', 'en_name': 'Chi (Huang passage)', 'art': 'scene-huangshan',
        'quote': '盼水出焉西流注于赤水',
        'description': '赤水在黄山段承接向西流来的盼水；本段未给出它的源头、全程或现代地望。与南山经柜山段赤水分别保存ID，不据同名或赤字拼接流域、补成红色河水。',
        'en_description': 'The Chi receives the west-flowing Mian, without a source, full course or modern location here. It retains an ID separate from the Southern Mountains Chi, and the name does not justify joining their basins or painting the river red.',
        'en_quote': 'The Mian rises here and flows west into the Chi.',
    },
    {
        'id': 'material-xishan-jade-huangshan', 'slug': 'huangshan', 'kind': 'material', 'group': 'natural_features',
        'name': '玉（黄山水文段）', 'en_name': 'Jade (Huang water passage)', 'art': 'scene-huangshan', 'relation_scope': 'water',
        'quote': '盼水出焉西流注于赤水其中多玉',
        'description': '其中多玉承接盼水至赤水的水文句，在此保留该范围，不扩写成整个赤水流域的矿产分布。经文只记玉，不改成大时白玉或竹山水玉，不鉴定现代矿物、晶体形态或开采方式。',
        'en_description': 'Much jade follows the Mian-to-Chi water account. That scope is retained without extending it to an entire basin’s mineral distribution. The text names jade, not Dashi’s white jade or Zhu’s water jade, and identifies no modern mineral, crystal form or extraction method.',
        'en_quote': 'The Mian rises here and flows west into the Chi, with much jade in the water.',
    },
    {
        'id': 'beast-xishan-min-huangshan', 'slug': 'huangshan', 'kind': '兽', 'group': 'beasts',
        'name': '𤛎（黄山段）', 'en_name': 'Min (Huang passage)', 'art': 'creature-min-huangshan',
        'quote': '有獸焉其状如牛而蒼黑大目其名曰𤛎',
        'description': '𤛎形如牛，苍黑、大目是本段明确特征，配图突出青黑形体和大眼，不添多首、额外角翼或功效情节。音敏郭注虽附在0094单元，影印中属于𤛎，不移给后面的鸚䳇；原字保留，不用敏字替换。',
        'en_description': 'Min is ox-shaped, blue-black and large-eyed. The image emphasizes those features without extra heads, horns, wings or an invented power. The pronunciation gloss belongs to Min even though it is attached to captured unit 94, rather than to the following bird. Its original character is retained.',
        'en_quote': 'An ox-shaped beast, blue-black and large-eyed, is called Min.',
        'commentary_quote': '音敏',
    },
    {
        'id': 'beast-xishan-yingmu-huangshan', 'slug': 'huangshan', 'kind': '鸟', 'group': 'beasts',
        'name': '鸚䳇（黄山段）', 'en_name': 'Yingmu (Huang passage)', 'art': 'bird-yingmu-huangshan',
        'quote': '有鳥焉其状如鴞青羽赤喙人舌能言名曰鸚䳇',
        'description': '鸚䳇形如鸮，青羽、赤喙、人舌、能言来自正文；能字缺字图已按影印核定，快照原样保留。郭注另说舌似小儿舌、足趾前后各两，并谈五色、纯赤白等比较，配图采用正文青羽赤喙，不混成所有异说的合体，也不锁定现代鹦鹉种类。',
        'en_description': 'Yingmu is owl-shaped, with blue-green feathers, a red beak, a human tongue and speech in the main text. The image glyph for can was checked in the scan without altering the snapshot. Guo Pu compares its tongue to a child’s and describes two toes forward and two backward, alongside other color comparisons. The image follows the main text’s colors without combining every alternative or identifying a modern parrot species.',
        'en_quote': 'An owl-shaped bird with blue-green feathers, a red beak and a human tongue can speak; it is called Yingmu.',
        'commentary_quote': '鸚䳇舌似小兒舌脚指前後各兩扶南徼外出五色者其亦有純赤白者大如鴈也',
        'art_reference': ['正文青羽赤喙人舌 · 前后各两足趾参照郭注；具体羽形、配色细节与姿态为艺术解释。', 'Main-text blue-green plumage, red beak and human tongue · Two toes forward and two backward follow commentary; feather details and pose are artistic choices.'],
    },
]


ENTITIES += [{'id': 'plant-xishan-zong-cuishan',
  'slug': 'cuishan',
  'kind': 'plant',
  'group': 'natural_features',
  'name': '㯶（翠山段）',
  'en_name': 'Zong (Cui passage)',
  'art': 'scene-cuishan',
  'quote': '其上多㯶枏',
  'description': '翠山山上多㯶；按底本保留㯶字，以棕类树木作概括示意，不据此锁定现代单一物种。与同句枏分别列卡。',
  'en_description': 'Zong occurs above on Cui. The edition’s character is retained, with a generalized '
                    'palm-like depiction rather than a fixed modern species. Nan remains a separate record.',
  'en_quote': 'Zong and nan trees are abundant above.'},
 {'id': 'plant-xishan-nan-cuishan',
  'slug': 'cuishan',
  'kind': 'plant',
  'group': 'natural_features',
  'name': '枏（翠山段）',
  'en_name': 'Nan (Cui passage)',
  'art': 'scene-cuishan',
  'quote': '其上多㯶枏',
  'description': '枏与㯶同见于翠山山上，分别列名；保留枏字，图中以阔叶树概括，不补花果、药效或精确树种。',
  'en_description': 'Nan occurs above beside zong. It is retained as a separate ancient tree name and '
                    'generalized broadleaf form, without added flowers, effects or exact species.',
  'en_quote': 'Zong and nan trees are abundant above.'},
 {'id': 'plant-xishan-zhujian-cuishan',
  'slug': 'cuishan',
  'kind': 'plant',
  'group': 'natural_features',
  'name': '竹箭（翠山段）',
  'en_name': 'Zhujian bamboo (Cui passage)',
  'art': 'scene-cuishan',
  'quote': '其下多竹箭',
  'description': '翠山山下多竹箭，按古名呈现竹丛而非制成的箭矢。与黄山竹箭各保留本段来源和ID。',
  'en_description': 'Zhujian bamboo occurs below on Cui, shown as bamboo rather than manufactured arrows. '
                    'Its record remains distinct from the Huang passage.',
  'en_quote': 'Zhujian bamboo is abundant below.'},
 {'id': 'material-xishan-gold-cuishan',
  'slug': 'cuishan',
  'kind': 'material',
  'group': 'natural_features',
  'name': '黄金（翠山段）',
  'en_name': 'Gold (Cui passage)',
  'art': 'scene-cuishan',
  'quote': '其陽多黄金玉',
  'description': '翠山阳面多黄金，与同句玉分卡；岩面点色仅为艺术解释，不添开采场景或现代矿床位置。',
  'en_description': 'Gold is recorded on Cui’s sunny side, separately from jade. Rock accents are artistic '
                    'choices, without mines or modern deposits.',
  'en_quote': 'Its sunny side has much gold and jade.'},
 {'id': 'material-xishan-jade-cuishan',
  'slug': 'cuishan',
  'kind': 'material',
  'group': 'natural_features',
  'name': '玉（翠山段）',
  'en_name': 'Jade (Cui passage)',
  'art': 'scene-cuishan',
  'quote': '其陽多黄金玉',
  'description': '翠山阳面多玉，不改成黄山水中玉或大时白玉；同名物产分别保存出处，不鉴定现代矿物。',
  'en_description': 'Jade is recorded on Cui’s sunny side, distinct from Huang’s water-context jade and '
                    'Dashi’s white jade; no modern mineral is identified.',
  'en_quote': 'Its sunny side has much gold and jade.'},
 {'id': 'animal-xishan-maoniu-cuishan',
  'slug': 'cuishan',
  'kind': '兽',
  'group': 'beasts',
  'name': '旄牛（翠山段）',
  'en_name': 'Maoniu (Cui passage)',
  'art': 'animal-maoniu-cuishan',
  'quote': '其隂多旄牛麢麝',
  'description': '翠山阴面多旄牛，与麢、麝分别列卡。配图用长毛牛形概括古名，不新增多首、怪角或功效，也不据此定位现代产地。',
  'en_description': 'Maoniu is recorded on the shaded side, separately from ling and musk deer. A '
                    'generalized long-haired bovine depicts the ancient name, without invented body parts or '
                    'a modern location.',
  'en_quote': 'Its shaded side has maoniu, ling and musk deer.'},
 {'id': 'animal-xishan-ling-cuishan',
  'slug': 'cuishan',
  'kind': '兽',
  'group': 'beasts',
  'name': '麢（翠山段）',
  'en_name': 'Ling (Cui passage)',
  'art': 'animal-ling-cuishan',
  'quote': '其隂多旄牛麢麝',
  'description': '麢见于翠山阴面。郭注以羊作比较，并说好在山崖间；保留底本字及注文，不据古名锁定现代羚类物种或补功效。',
  'en_description': 'Ling is recorded on the shaded side. Guo Pu compares it with a sheep and places it '
                    'among mountain cliffs. The ancient name is not fixed to a modern species.',
  'en_quote': 'Its shaded side has maoniu, ling and musk deer.',
  'commentary_quote': '麢似羊而大角細食好在山崖間'},
 {'id': 'animal-xishan-she-cuishan',
  'slug': 'cuishan',
  'kind': '兽',
  'group': 'beasts',
  'name': '麝（翠山段）',
  'en_name': 'She / musk deer (Cui passage)',
  'art': 'animal-she-cuishan',
  'quote': '其隂多旄牛麢麝',
  'description': '麝见于翠山阴面。郭注麝似獐而小与下一捕获单元有香连读，说明仍属麝，不把有香移作鸓特征；不另添药效或采香画面。',
  'en_description': 'She occurs on the shaded side. The commentary’s smaller-than-zhang comparison continues '
                    'with fragrant in the next captured unit. That gloss belongs to she, not Lei. No '
                    'medicinal claim or scent harvesting is added.',
  'en_quote': 'Its shaded side has maoniu, ling and musk deer.',
  'commentary_quote': '麝似獐而小有香'},
 {'id': 'bird-xishan-lei-cuishan',
  'slug': 'cuishan',
  'kind': '鸟',
  'group': 'beasts',
  'name': '鸓（翠山段）',
  'en_name': 'Lei (Cui passage)',
  'art': 'bird-lei-cuishan',
  'quote': '其鳥多鸓其状如鵲赤黑而西首四足可以禦火',
  'description': '鸓像鹊，赤黑、四足，郭注音壘。本底本及电子录文均作西首，不擅改为两首；配图双首参照《古今图书集成·禽虫典》第53卷引文两首四足，作为明示异文演绎。禦火不画成喷火或火焰能力。',
  'en_description': 'Lei is magpie-shaped, red and black, with four feet. This edition and its transcription '
                    'print xi shou, retained unchanged. The two-headed illustration explicitly follows the '
                    'two heads/four feet reading quoted in volume53 of the Gujin Tushu Jicheng, rather than '
                    'silently changing the base text. Averting fire is not shown as breathing flames.',
  'en_quote': 'Lei is magpie-shaped, red and black, with four feet; the base text prints xi shou, whereas '
              'the illustrated variant reads two heads. It is said to avert fire.',
  'commentary_quote': '音壘',
  'art_reference': ['双首参照异文 · 本底本作西首；参《古今图书集成·禽虫典》卷53两首四足。刻纹与姿态为艺术解释。',
                    'Two heads follow a quoted variant · This edition prints xi shou; see Gujin Tushu '
                    'Jicheng, Qinchong Dian53. Carving and pose are artistic choices.']}]


ENTITIES += [{'id': 'water-xishan-westsea-guishan',
  'slug': 'guishan',
  'kind': 'water',
  'group': 'natural_features',
  'name': '西海（騩山段）',
  'en_name': 'Western Sea (Gui passage)',
  'art': 'scene-guishan',
  'quote': '是錞于西海無草木多玉淒水出焉西流注于海',
  'description': '騩山临西海，后文又说淒水西流注于海。本卡按本段上下文呈现西海与海的两处称谓及承接关系，不补源头或海岸线，也不据此合并其他篇目的西海。',
  'en_description': 'Gui borders the Western Sea, and the Qi later flows west into the sea. This record '
                    'presents both names in their local context, without a modern coast or merging seas from '
                    'other chapters.',
  'en_quote': 'Gui borders the Western Sea; the Qi flows west into the sea.',
  'commentary_quote': '錞猶堤埻也音章閏反'},
 {'id': 'material-xishan-jade-guishan',
  'slug': 'guishan',
  'kind': 'material',
  'group': 'natural_features',
  'name': '玉（騩山段）',
  'en_name': 'Jade (Gui passage)',
  'art': 'scene-guishan',
  'quote': '無草木多玉',
  'description': '騩山无草木而多玉；这里是山的概况，不与随后水文中的采石、黄金混作同一句。经文只说玉，不补白玉、水玉或现代矿物鉴定。',
  'en_description': 'Gui has no vegetation and much jade. This is the mountain account, distinct from the '
                    'following water-context colored stones and gold. No jade color or modern mineral '
                    'identification is added.',
  'en_quote': 'There is no grass or trees, and much jade.'},
 {'id': 'water-xishan-qi-guishan',
  'slug': 'guishan',
  'kind': 'water',
  'group': 'natural_features',
  'name': '淒水（騩山段）',
  'en_name': 'Qi (Gui passage)',
  'art': 'scene-guishan',
  'quote': '淒水出焉西流注于海',
  'description': '淒水出騩山，向西流注海。或作浽是郭注所记异文，保留在本卡，不据异名虚构第二条河流；不添现代河道或精确坐标。',
  'en_description': 'The Qi rises at Gui and flows west into the sea. Guo Pu records Sui as a variant name; '
                    'it is retained here without inventing a second river or modern course.',
  'en_quote': 'The Qi rises here and flows west into the sea.',
  'commentary_quote': '或作浽'},
 {'id': 'material-xishan-caishi-guishan',
  'slug': 'guishan',
  'kind': 'material',
  'group': 'natural_features',
  'name': '采石（騩山水文段）',
  'en_name': 'Colored stones (Gui water passage)',
  'art': 'scene-guishan',
  'quote': '淒水出焉西流注于海其中多采石黄金',
  'description': '采石承接淒水入海后的其中句，郭注解释为有彩色的石，并举雌黄、空青、绿碧之属。这些是注文比较，不逐项另建本山已证实矿物；彩色岩点为艺术示意。',
  'en_description': 'Colored stones follow the Qi-to-sea water account. Guo Pu explains them as stones with '
                    'colors and gives mineral examples. Those commentary comparisons do not verify separate '
                    'mineral deposits here; colored rock accents are illustrative.',
  'en_quote': 'The Qi flows west into the sea; there are many colored stones and gold in that water context.',
  'commentary_quote': '采石石有采色者今雌黄空青緑碧之属',
  'relation_scope': 'water'},
 {'id': 'material-xishan-gold-guishan',
  'slug': 'guishan',
  'kind': 'material',
  'group': 'natural_features',
  'name': '黄金（騩山水文段）',
  'en_name': 'Gold (Gui water passage)',
  'art': 'scene-guishan',
  'quote': '淒水出焉西流注于海其中多采石黄金',
  'description': '黄金与采石同属其中文句，按该水文上下文呈现，不扩写为整个西海的矿产，也不添采矿、金锭或淘金场景。',
  'en_description': 'Gold appears beside colored stones in the local water-context sentence. It is not '
                    'extended to the whole Western Sea, and no mines, ingots or extraction scene are added.',
  'en_quote': 'The Qi flows west into the sea; there are many colored stones and gold in that water context.',
  'relation_scope': 'water'},
 {'id': 'material-xishan-dansu-guishan',
  'slug': 'guishan',
  'kind': 'material',
  'group': 'natural_features',
  'name': '丹粟（騩山段）',
  'en_name': 'Dansu (Gui passage)',
  'art': 'scene-guishan',
  'quote': '多丹粟',
  'description': '多丹粟位于采石、黄金记述之后，保留原句序；本段没有再次释义或给出精确分布。配图少量朱砂点色仅为示意，不把它画成谷物、认定现代矿种或扩张到整个海域。',
  'en_description': 'Much dansu follows the colored-stone and gold account, without another definition or '
                    'exact distribution. Sparse cinnabar accents are illustrative, without turning it into '
                    'grain or fixing a modern mineral or basin-wide deposit.',
  'en_quote': 'Much dansu is also recorded.'}]


ENTITIES += [{'id': 'rite-xishan-hua-range1',
  'slug': 'range1-summary',
  'kind': 'rite',
  'group': 'text_entities',
  'name': '华山冢与太牢祠礼',
  'en_name': 'Hua zhong and tailao rite',
  'quote': '華山冢也其祠之禮太牢',
  'description': '本段称華山为冢，并记祠礼用太牢。神之所舍也、牛羊豕为太牢是郭注解释，不另虚构神名、神像或现代祭礼流程。这里是首列总括卡，不是新增山卡。',
  'en_description': 'The summary calls Hua the zhong and prescribes tailao. The deity’s dwelling and the '
                    'cattle/sheep/pig explanation are commentary, without an invented deity image or modern '
                    'ritual procedure. This is a summary rite, not another mountain.',
  'en_quote': 'Hua is the zhong; its rite uses tailao.',
  'commentary_quote': '冢者神之所舍也；牛羊豕為太牢',
  'art': None},
 {'id': 'rite-xishan-yu-range1',
  'slug': 'range1-summary',
  'kind': 'rite',
  'group': 'text_entities',
  'name': '羭山燭礼与玉器',
  'en_name': 'Yu rite and jade offerings',
  'quote': '羭山神也祠之用燭齋百日以百犧瘞用百瑜湯其酒百樽嬰以百珪百璧',
  'description': '保留羭山神也祠之用燭的底本文字、百日斋与百数犧、瑜、酒、珪、璧。郭注对犧、瑜、湯或温、嬰等另释，数目不画成未经核定的实景。或作后的缺字不猜补，末句定义仍回到总括阅读，不补神的外貌。',
  'en_description': 'The text’s Yu phrase, zhu, hundred-day observance and offerings counted in hundreds are '
                    'retained. Commentary explains xi, yu-jade, warmed wine and ying separately. Missing '
                    'variant characters are not guessed, and no deity appearance or reconstructed ceremony '
                    'is added.',
  'en_quote': 'The text describes the Yu rite with zhu, a hundred-day observance, offerings counted in '
              'hundreds, yu-jade, wine, gui and bi jades.',
  'commentary_quote': '牲純色者為犧；瑜亦羙王名音〔录文缺字待核〕；或作温；温酒令𤍠；嬰謂陳之以環祭也或曰嬰即古𦉍字謂盂也徐州云穆天子傳曰黄金之嬰之属也',
  'art': None},
 {'id': 'rite-xishan-seventeen-range1',
  'slug': 'range1-summary',
  'kind': 'rite',
  'group': 'text_entities',
  'name': '其余十七山祠礼',
  'en_name': 'Rite for the other seventeen mountains',
  'quote': '其餘十七山之属皆毛牷用一羊祠之',
  'description': '首列其余十七山记毛牷、用一羊祠之。郭注释牷为牲体全具，并引左传说明；这里保留古籍记述，不把十七山各自新增为地理点位，也不将其合成另一座山。',
  'en_description': 'The remaining seventeen mountains are assigned one sheep each, with the offering term explained in commentary. Guo Pu '
                    'explains a complete sacrificial animal and quotes the Zuozhuan. The account does not '
                    'add seventeen mapped points or another mountain.',
  'en_quote': 'The other seventeen mountains each receive one sheep, with the offering described as complete in the commentary.',
  'commentary_quote': '牷謂牲体全具也左傳曰牷牲肥腯者也',
  'art': None}]



ENTITIES += [
    {
        'id': 'material-xishan-copper-qianshan', 'slug': 'qianshan', 'kind': 'material', 'group': 'natural_features',
        'name': '铜（鈐山段）', 'en_name': 'Copper (Qian passage)', 'art': None,
        'quote': '其上多銅',
        'description': '鈐山山上多铜，山下多玉分别保存。经文没有写矿脉形状、开采或器物，不据铜字补画矿井、铜锭，也不把这句移作河中矿产。',
        'en_description': 'Copper is recorded above on Mount Qian, separately from jade below. No vein shape, mining or manufactured object is described, and the statement is not assigned to a river.',
        'en_quote': 'Copper is abundant above.',
    },
    {
        'id': 'material-xishan-jade-qianshan', 'slug': 'qianshan', 'kind': 'material', 'group': 'natural_features',
        'name': '玉（鈐山段）', 'en_name': 'Jade (Qian passage)', 'art': None,
        'quote': '其下多玉',
        'description': '鈐山山下多玉。这里只记玉名与山下位置，没有颜色、形制或用途，不借用其他山段的玉器或特定玉种补足。',
        'en_description': 'Jade is abundant below Mount Qian. No color, worked shape or use is specified; jade objects and named varieties from other passages are not imported here.',
        'en_quote': 'Jade is abundant below.',
    },
    {
        'id': 'plant-xishan-niu-qianshan', 'slug': 'qianshan', 'kind': 'plant', 'group': 'natural_features',
        'name': '杻（鈐山段）', 'en_name': 'Niu tree (Qian passage)', 'art': None,
        'quote': '其木多杻橿',
        'description': '杻与橿并列为鈐山多有的树木。杻在本段没有独立形貌、花果或功效说明，保留古木名，不据现代同名植物画出确定形态。',
        'en_description': 'Niu and jiang are listed as abundant trees on Mount Qian. This passage gives no separate form, flowers, fruit or effect for niu; its old name does not identify a definite modern plant.',
        'en_quote': 'Its trees include niu and jiang in abundance.',
    },
    {
        'id': 'plant-xishan-jiang-qianshan', 'slug': 'qianshan', 'kind': 'plant', 'group': 'natural_features',
        'name': '橿（鈐山段）', 'en_name': 'Jiang tree (Qian passage)', 'art': None,
        'quote': '其木多杻橿',
        'description': '橿与杻分别保留为鈐山树木条目。经文没有写叶形、树皮、花果或用途，不将橿擅改为樟、疆或其他现代树名，也不移入别山段的郭注。',
        'en_description': 'Jiang is retained separately from niu as a tree of Mount Qian. No leaves, bark, flowers, fruit or use are described, and the edition character is not silently replaced with another tree name or supplemented from another passage.',
        'en_quote': 'Its trees include niu and jiang in abundance.',
    },
]


ENTITIES += [
    {
        'id': 'material-xishan-jin-taimao', 'slug': 'taimao', 'kind': 'material', 'group': 'natural_features',
        'name': '金（㤗冐段）', 'en_name': 'Jin metal (Taimao passage)', 'art': None,
        'quote': '其陽多金',
        'description': '㤗冐山阳面多金，原文金字保留，不改成黄金，也不画金锭、矿井或矿脉。阳面与阴面多铁分开记录，不补出现代地质成因。',
        'en_description': 'Jin is abundant on Taimao’s sunny side. The source term is retained rather than expanded into a specific modern mineral, ingots, mines or veins. The iron on the shaded side is recorded separately.',
        'en_quote': 'Jin metal is abundant on its sunny side.',
    },
    {
        'id': 'material-xishan-iron-taimao', 'slug': 'taimao', 'kind': 'material', 'group': 'natural_features',
        'name': '铁（㤗冐段）', 'en_name': 'Iron (Taimao passage)', 'art': None,
        'quote': '其隂多鐡',
        'description': '㤗冐山阴面多铁，阅读引文保留鐡字。经文没有写冶炼、器物或矿坑，不把铁移入后文浴水中的物产。',
        'en_description': 'Iron is recorded on Taimao’s shaded side. No smelting, object or mine is described, and this mountain-side statement is not moved into the river’s contents.',
        'en_quote': 'Iron is abundant on its shaded side.',
    },
    {
        'id': 'water-xishan-yu-taimao', 'slug': 'taimao', 'kind': 'water', 'group': 'natural_features',
        'name': '浴水（㤗冐段）', 'en_name': 'Yu River (Taimao passage)', 'art': None,
        'quote': '浴水出焉東流注于河其中多藻玉多白蛇',
        'description': '浴水出于㤗冐山，向东注于河，水中记有藻玉与白蛇。浴字保留，不因同音改成禺、玉或其他水名；这里只建立本段原文所记的流向，不绘出现代河道。',
        'en_description': 'The Yu River rises at Taimao and flows east into the He, with zaoyu jade and white snakes in the water. The edition’s Yu character is retained, without merging it with similarly named rivers or drawing a modern course.',
        'en_quote': 'The Yu River rises here and flows east into the He; its waters contain much zaoyu jade and many white snakes.',
    },
    {
        'id': 'water-xishan-he-taimao', 'slug': 'taimao', 'kind': 'water', 'group': 'natural_features',
        'name': '河（㤗冐段）', 'en_name': 'He (Taimao passage)', 'art': None,
        'quote': '浴水出焉東流注于河',
        'description': '河在本段作为浴水东流所注的承接水域出现。经文没有在这里写河的源头、边界、完整水道或现代汇流点，保留本段上下文卡，不合并其他篇章的同名水域。',
        'en_description': 'The He receives the east-flowing Yu in this passage. No source, boundary, full course or modern confluence is supplied here; this contextual record is not merged with namesakes elsewhere.',
        'en_quote': 'The Yu River rises here and flows east into the He.',
    },
    {
        'id': 'material-xishan-zaoyu-taimao', 'slug': 'taimao', 'kind': 'material', 'group': 'natural_features',
        'name': '藻玉（㤗冐段）', 'en_name': 'Zaoyu jade (Taimao passage)', 'art': None, 'relation_scope': 'water',
        'quote': '浴水出焉東流注于河其中多藻玉',
        'description': '藻玉接在浴水水文之后。郭注释为有符彩之玉，或作柬音練按录文分存；不把藻字画成水草，也不指定纹样、颜色、玉器形制或现代矿物名称。',
        'en_description': 'Zaoyu follows the Yu River account. The commentary describes patterned jade and retains a variant and pronunciation note. The name is not illustrated as algae, nor assigned a definite pattern, color, carved object or modern mineral.',
        'en_quote': 'The Yu River rises here and flows east into the He; its waters contain much zaoyu jade.',
        'commentary_quote': '藻玉玉有符彩者或作柬音練',
    },
    {
        'id': 'beast-xishan-white-snake-taimao', 'slug': 'taimao', 'kind': '蛇', 'group': 'beasts',
        'name': '白蛇（㤗冐段）', 'en_name': 'White snakes (Taimao passage)', 'art': None, 'relation_scope': 'water',
        'quote': '浴水出焉東流注于河其中多藻玉多白蛇',
        'description': '白蛇见于㤗冐山浴水的水中记述，郭注仅释水蛇。经文没有多首、足翼、角或额外能力，不与后世白蛇故事相连，也不鉴定现代蛇种。',
        'en_description': 'White snakes occur in the Yu River passage; the commentary only calls them water snakes. No extra heads, legs, wings, horns or powers are recorded, and neither a later White Snake story nor a modern species is imposed.',
        'en_quote': 'The Yu River rises here and flows east into the He; its waters contain much zaoyu jade and many white snakes.',
        'commentary_quote': '水蛇',
        'art_reference': ['统一留空形象 · 插画未生成，问号剪影不代表白蛇的原文形貌。', 'Shared placeholder · The illustration has not been made; this question-mark silhouette does not depict the textual white snakes.'],
    },
]


ENTITIES += [
    {'id': 'material-xishan-gold-shuli', 'slug': 'shuli', 'kind': 'material', 'group': 'natural_features', 'art': None,
     'name': '黄金（數歴段）', 'en_name': 'Gold (Shuli passage)', 'quote': '其上多黄金',
     'description': '數歴山上多黄金，原文明确作黄金，与前段㤗冐山的金字分别保留。没有矿脉、采矿、金锭或具体矿物形制的描述。',
     'en_description': 'Gold is recorded above on Shuli. The explicit gold wording remains distinct from the jin term in the Taimao passage; no vein, mining, ingot or specific mineral form is described.',
     'en_quote': 'Gold is abundant above.'},
    {'id': 'material-xishan-silver-shuli', 'slug': 'shuli', 'kind': 'material', 'group': 'natural_features', 'art': None,
     'name': '银（數歴段）', 'en_name': 'Silver (Shuli passage)', 'quote': '其下多銀',
     'description': '數歴山下多银，与山上黄金的位置分开。其下多在46页末，銀字续于47页，不因捕获页界把银改归下一座高山。',
     'en_description': 'Silver is recorded below Shuli, separately from gold above. The statement crosses scans46–47 and is not reassigned to the following Mount Gao because of the page break.',
     'en_quote': 'Silver is abundant below.'},
    {'id': 'plant-xishan-niu-shuli', 'slug': 'shuli', 'kind': 'plant', 'group': 'natural_features', 'art': None,
     'name': '杻（數歴段）', 'en_name': 'Niu tree (Shuli passage)', 'quote': '其木多杻橿',
     'description': '杻与橿是數歴山并列的树木，本段只记其多。保留本山独立出处，不把鈐山同名条目合并，也不补花果、叶形或现代物种鉴定。',
     'en_description': 'Niu and jiang are abundant trees at Shuli. This source remains distinct from Qian’s namesake entry, with no flowers, fruit, leaf form or modern species added.',
     'en_quote': 'Its trees include niu and jiang in abundance.'},
    {'id': 'plant-xishan-jiang-shuli', 'slug': 'shuli', 'kind': 'plant', 'group': 'natural_features', 'art': None,
     'name': '橿（數歴段）', 'en_name': 'Jiang tree (Shuli passage)', 'quote': '其木多杻橿',
     'description': '橿与杻分别存为數歴山树木条目。正文没有形貌或用途，不把橿改为樟，也不借用其他山段的草木特征补写。',
     'en_description': 'Jiang is retained separately from niu as a Shuli tree. No form or use is specified, and its edition character is not replaced with another tree name or supplemented from other passages.',
     'en_quote': 'Its trees include niu and jiang in abundance.'},
    {'id': 'beast-xishan-yingmu-shuli', 'slug': 'shuli', 'kind': '鸟', 'group': 'beasts', 'art': None, 'appearance_unknown': True,
     'name': '鸚䳇（數歴段）', 'en_name': 'Yingmu (Shuli passage)', 'quote': '其鳥多鸚䳇',
     'description': '數歴山多鸚䳇，原文在此仅列鸟名，没有重述形貌。保留本山独立出处，不把黄山的青羽、赤喙、人舌、能言或郭注趾数补入本段，也不直接认定为唯一现代鹦鹉种类。',
     'en_description': 'Yingmu birds are abundant at Shuli, but their appearance is not restated. This separate source does not import Huang’s blue-green plumage, red beak, human tongue, speech or commentary toe count, nor identify one modern parrot species.',
     'en_quote': 'Its birds include many Yingmu.',
     'art_reference': ['形貌未详 · 统一问号留空剪影，不借用黄山段插画表示本段已述形貌。', 'Appearance unspecified here · The shared question-mark placeholder does not import Huang’s illustrated form into this passage.']},
    {'id': 'water-xishan-chu-shuli', 'slug': 'shuli', 'kind': 'water', 'group': 'natural_features', 'art': None,
     'name': '楚水（數歴段）', 'en_name': 'Chu River (Shuli passage)', 'quote': '楚水出焉而南流注于渭其中多珠',
     'description': '楚水从數歴山流出，向南注渭，水中多珠。南流与首列多条水北注渭的记述分别保留，不机械统一为北流，也不绘出现代河道或精确汇流点。',
     'en_description': 'The Chu rises at Shuli and flows south into the Wei, with pearls in the water. This southward direction remains distinct from the first range’s northward inflows; no modern course or exact confluence is drawn.',
     'en_quote': 'The Chu River rises here and flows south into the Wei; its waters contain many pearls.'},
    {'id': 'material-xishan-pearl-shuli', 'slug': 'shuli', 'kind': 'material', 'group': 'natural_features', 'art': None, 'relation_scope': 'water',
     'name': '珠（數歴水文段）', 'en_name': 'Pearls (Shuli water passage)', 'quote': '楚水出焉而南流注于渭其中多珠',
     'description': '珠接在楚水南注渭的水文之后，保留其中的原文范围，不补采珠或佩用情节。郭注所举蜀郡平泽青珠及尸子引文另列，不据此把本段珠都画成青色或确定现代产地。',
     'en_description': 'Pearls follow the Chu-to-Wei water account, without added pearl harvesting or ornament use. The commentary’s example from the Shu region and Shizi quotation remain separate; they do not make all pearls here blue-green or identify a modern locality.',
     'en_quote': 'The Chu River rises here and flows south into the Wei; its waters contain many pearls.',
     'commentary_quote': '今蜀郡平澤出青珠尸子曰水員折者有珠'},
]


ENTITIES += [
    {'id': 'material-xishan-silver-gaoshan', 'slug': 'gaoshan', 'kind': 'material', 'group': 'natural_features', 'art': None,
     'name': '银（髙山段）', 'en_name': 'Silver (Gao passage)', 'quote': '其上多銀',
     'description': '髙山山上多银，与數歴山下多银的出处与位置分别保留。不补矿井、银锭或矿脉，也不把本句并入后面的水文物产。',
     'en_description': 'Silver is abundant above on Gao, distinct from the silver below Shuli. No mine, ingot or vein is added, and this statement is not transferred to the water account.',
     'en_quote': 'Silver is abundant above.'},
    {'id': 'material-xishan-qingbi-gaoshan', 'slug': 'gaoshan', 'kind': 'material', 'group': 'natural_features', 'art': None,
     'name': '青碧（髙山下）', 'en_name': 'Qingbi (below Mount Gao)', 'quote': '其下多青碧雄黄',
     'description': '青碧与雄黄并列于髙山下。郭注碧亦玉𩔗也跨两个录文单元续接，后举越嶲、会稽东山出碧；这些解释与经文分列，不由古名直接确定现代矿物或把注文产地定位成本山。水文末尾同名青碧另卡保存。',
     'en_description': 'Qingbi and xionghuang are listed below Gao. The commentary’s jade-class gloss continues across transcription units and cites other old localities; it does not identify a modern mineral or locate this mountain there. Water-context qingbi has a separate card.',
     'en_quote': 'Qingbi and xionghuang are abundant below.',
     'commentary_quote': '碧亦玉𩔗也今越嶲㑹稽縣東山出碧'},
    {'id': 'material-xishan-xionghuang-gaoshan', 'slug': 'gaoshan', 'kind': 'material', 'group': 'natural_features', 'art': None,
     'name': '雄黄（髙山段）', 'en_name': 'Xionghuang (Gao passage)', 'quote': '其下多青碧雄黄',
     'description': '雄黄记于髙山下，与青碧并列。郭注所举大兴三年高平郡界山崩出雄黄是另引旧例，不把它写成本山经文中发生的事件，不补开采或加工场景。',
     'en_description': 'Xionghuang occurs below Gao beside qingbi. The commentary’s historical landslide example belongs to a separate cited locality, not an event in this mountain’s main text. No mining or processing scene is added.',
     'en_quote': 'Qingbi and xionghuang are abundant below.',
     'commentary_quote': '𣈆大興三年髙平郡界有山崩其中出數千斤雄黄'},
    {'id': 'plant-xishan-zong-gaoshan', 'slug': 'gaoshan', 'kind': 'plant', 'group': 'natural_features', 'art': None,
     'name': '㯶（髙山段）', 'en_name': 'Zong tree (Gao passage)', 'quote': '其木多㯶',
     'description': '髙山树木多㯶，保留底本㯶字。这里没有描写叶形、花果或用途，不据现代棕类植物形态补成确定物种，也不与其他山段合并出处。',
     'en_description': 'Zong trees are abundant at Gao. The edition character is retained without supplying leaves, flowers, fruit, uses or a definite modern palm species, and the source is not merged with other mountain passages.',
     'en_quote': 'Its trees include many zong.'},
    {'id': 'plant-xishan-bamboo-gaoshan', 'slug': 'gaoshan', 'kind': 'plant', 'group': 'natural_features', 'art': None,
     'name': '竹（髙山段）', 'en_name': 'Bamboo (Gao passage)', 'quote': '其草多竹',
     'description': '竹列在髙山的草类记述中，原文只说多竹。保留原句次序，不补作竹箭、器物材料或确定现代竹种，也不借其他山段插画表示本段已写明竹形。',
     'en_description': 'Bamboo is listed among Gao’s grasses. This wording is retained without turning it into arrow bamboo, manufactured material or a particular modern species, or importing another passage’s illustrated form.',
     'en_quote': 'Its grasses include much bamboo.'},
    {'id': 'water-xishan-jing-gaoshan', 'slug': 'gaoshan', 'kind': 'water', 'group': 'natural_features', 'art': None,
     'name': '涇水（髙山段）', 'en_name': 'Jing River (Gao passage)', 'quote': '涇水出焉而東流注于渭其中多磬石青碧',
     'description': '涇水从髙山流出，向东注渭，后接其中多磬石青碧。涇字与郭注音經分别保留；注文记安定至京兆高陵的古水道，不据此补现代河道、坐标或精确汇流点。东流与楚水南流及首列七段北注分别阅读。',
     'en_description': 'The Jing rises at Gao and flows east into the Wei, followed by sounding stones and qingbi in the water account. The edition character and pronunciation gloss remain distinct. Old place names in the commentary do not establish a modern course, coordinates or exact confluence. This eastward flow remains separate from the Chu’s southward and seven first-range northward inflows.',
     'en_quote': 'The Jing River rises here and flows east into the Wei; the waters contain many sounding stones and qingbi.',
     'commentary_quote': '音經；今涇水出安定朝那縣西井頭山至京兆髙陵縣入渭也'},
    {'id': 'material-xishan-qingshi-gaoshan', 'slug': 'gaoshan', 'kind': 'material', 'group': 'natural_features', 'art': None, 'relation_scope': 'water',
     'name': '磬石（髙山水文段）', 'en_name': 'Sounding stones (Gao water passage)', 'quote': '涇水出焉而東流注于渭其中多磬石青碧',
     'description': '磬石接在涇水东注渭的水文中，郭注引书曰泗濵浮磬是也。保留石名与引用，不把它直接画成制好的磬乐器，也不据其中推定现代河段的完整矿产分布。',
     'en_description': 'Sounding stones follow the Jing-to-Wei account, with a quoted textual comparison in the commentary. The stone name is not turned into a finished chime instrument or a claim about a modern river reach’s mineral distribution.',
     'en_quote': 'The Jing River rises here and flows east into the Wei; the waters contain many sounding stones and qingbi.',
     'commentary_quote': '書曰泗濵浮磬是也'},
    {'id': 'material-xishan-qingbi-water-gaoshan', 'slug': 'gaoshan', 'kind': 'material', 'group': 'natural_features', 'art': None, 'relation_scope': 'water',
     'name': '青碧（髙山水文段）', 'en_name': 'Qingbi (Gao water passage)', 'quote': '涇水出焉而東流注于渭其中多磬石青碧',
     'description': '青碧在涇水东注渭之后再次出现，与磬石并列，另存水文上下文卡。它与山下青碧同名而原句范围不同，不把两处位置合成一个确定矿区，也不为水文末句新增独立郭注。',
     'en_description': 'Qingbi is named again after the Jing-to-Wei account, beside sounding stones. This water-context card remains separate from the same name below the mountain, without combining the locations into a definite mineral district or adding a separate gloss to the final wording.',
     'en_quote': 'The Jing River rises here and flows east into the Wei; the waters contain many sounding stones and qingbi.'},
]


ENTITIES += [
    {'id': 'material-xishan-red-copper-nvchuang', 'slug': 'nvchuang', 'kind': 'material', 'group': 'natural_features', 'art': None,
     'name': '赤铜（女牀段）', 'en_name': 'Red copper (Nvchuang passage)', 'quote': '其陽多赤銅',
     'description': '赤铜记于女牀山阳面，赤字是本段原文的一部分，与别山仅称铜的出处分开。不补铜锭、器物、矿井或现代纯度鉴定。',
     'en_description': 'Red copper occurs on Nvchuang’s sunny side. The red qualifier is retained separately from passages naming only copper, without adding ingots, objects, mines or a modern purity classification.',
     'en_quote': 'Red copper is abundant on its sunny side.'},
    {'id': 'material-xishan-shinie-nvchuang', 'slug': 'nvchuang', 'kind': 'material', 'group': 'natural_features', 'art': None,
     'name': '石𣵀（女牀段）', 'en_name': 'Shi nie (Nvchuang passage)', 'quote': '其隂多石𣵀',
     'description': '石𣵀记于女牀山阴面，保留底本𣵀字，不直接改成石涅或鉴定为某一现代矿物。郭注另列楚石、𣵀石、羽𣵀与本草经名称，这些古名不画成确定开采或加工场景。',
     'en_description': 'Shi nie occurs on Nvchuang’s shaded side. The edition character remains unchanged rather than identifying a specific modern mineral. Commentary names used in Chu, Qin and a materia medica remain old textual names, without a definite mining or processing scene.',
     'en_quote': 'Shi nie is abundant on its shaded side.',
     'commentary_quote': '即楚石也楚人名為𣵀石秦名為羽𣵀也本草經亦名曰石𣵀也'},
    {'id': 'animal-xishan-tiger-nvchuang', 'slug': 'nvchuang', 'kind': '兽', 'group': 'beasts', 'art': None, 'appearance_unknown': True,
     'name': '虎（女牀段）', 'en_name': 'Tigers (Nvchuang passage)', 'quote': '其獸多虎豹犀兕',
     'description': '虎与豹、犀、兕在女牀山并列。经文没有另写颜色、纹样、肢体或行为，保留本山独立出处，不把别篇虎身异兽的器官与能力移入。',
     'en_description': 'Tigers are listed beside leopards, xi and si at Nvchuang. No colors, markings, limbs or behavior are separately described, and forms or powers of tiger-bodied creatures elsewhere are not imported.',
     'en_quote': 'Its beasts include tigers, leopards, xi and si.'},
    {'id': 'animal-xishan-leopard-nvchuang', 'slug': 'nvchuang', 'kind': '兽', 'group': 'beasts', 'art': None, 'appearance_unknown': True,
     'name': '豹（女牀段）', 'en_name': 'Leopards (Nvchuang passage)', 'quote': '其獸多虎豹犀兕',
     'description': '豹在女牀山兽类中单独保留名称，没有形貌或功效记述。不把本段豹与其他篇章豹状而有角、多尾的异兽合成同一条目。',
     'en_description': 'Leopards are retained as a separate name among Nvchuang’s beasts without a form or effect description. They are not merged with leopard-shaped creatures having horns or multiple tails elsewhere.',
     'en_quote': 'Its beasts include tigers, leopards, xi and si.'},
    {'id': 'animal-xishan-xi-nvchuang', 'slug': 'nvchuang', 'kind': '兽', 'group': 'beasts', 'art': None, 'appearance_unknown': True,
     'name': '犀（女牀段）', 'en_name': 'Xi (Nvchuang passage)', 'quote': '其獸多虎豹犀兕',
     'description': '女牀山正文只列犀，与兕分别保存。这里没有角数、毛色、体态说明，不移用祷过山郭注或嶓冡同名条目的形貌解释，也不固定现代物种。',
     'en_description': 'Xi is only named at Nvchuang and remains separate from si. No horn count, coat color or build is given here, and commentary or forms from Daoguo and Bozhong are not transferred into this passage.',
     'en_quote': 'Its beasts include tigers, leopards, xi and si.'},
    {'id': 'animal-xishan-si-nvchuang', 'slug': 'nvchuang', 'kind': '兽', 'group': 'beasts', 'art': None, 'appearance_unknown': True,
     'name': '兕（女牀段）', 'en_name': 'Si (Nvchuang passage)', 'quote': '其獸多虎豹犀兕',
     'description': '兕与犀在女牀山分别列名。经文没有写一角、颜色或现代产地，不因其他山段的郭注或同名就补出本段身体结构。',
     'en_description': 'Si and xi are named separately at Nvchuang. No single horn, color or modern locality is stated, and a body structure is not supplied from namesakes or commentary in other passages.',
     'en_quote': 'Its beasts include tigers, leopards, xi and si.'},
    {'id': 'beast-xishan-luan-nvchuang', 'slug': 'nvchuang', 'kind': '鸟', 'group': 'beasts', 'art': None,
     'name': '鸞鳥（女牀段）', 'en_name': 'Luan bird (Nvchuang passage)', 'quote': '有鳥焉其状如翟而五彩文名曰鸞鳥見則天下安寧',
     'description': '鸞鳥的翟状、五彩文出自本段经文，见则天下安宁作为瑞应原说保留，不写成鸟主动施法。翟似雉而大、长尾及或作𪇱是郭注解释；旧注似鸡与周成王时献瑞鸟的故事分列，不并入正文形貌，也不与凤皇互换。',
     'en_description': 'The Luan’s zhai-like form and five-colored markings come from this passage. Peace is retained as a textual omen, not an active spell. The commentary’s large long-tailed pheasant comparison, alternative bird character, chicken comparison and older presentation story remain separate from the main form and are not exchanged with Fenghuang.',
     'en_quote': 'A bird shaped like a zhai with five-colored markings is called Luan; its appearance is said to herald peace throughout the world.',
     'commentary_quote': '翟似雉而大長尾或作𪇱𪇱鵰属也；舊鵉似鷄瑞鳥也周成王時西戎獻之',
     'content_note': '翟注在47页，鸞鳥及其旧注续48页。电子快照舊与鵉之间省字，郭注栏保留快照并明示，不宣称字字齐全。',
     'en_content_note': 'The zhai gloss is on scan47 and Luan with its older gloss continues on48. The captured annotation omits a character between jiu and luan; the panel retains the snapshot without claiming completeness.',
     'art_reference': ['统一留空形象 · 鸞鳥插画未生成，问号剪影不代表经文翟状五彩的形貌。', 'Shared placeholder · The Luan illustration has not been made; this question-mark silhouette does not depict its zhai-like, five-colored form.']},
]

ENTITIES += [{'id': 'material-xishan-gold-longshou',
  'slug': 'longshou',
  'kind': 'material',
  'group': 'natural_features',
  'art': None,
  'name': '黄金（龍首山阳面）',
  'en_name': 'Gold (sunny side of Longshou)',
  'quote': '其陽多黄金',
  'description': '黄金列在龍首山阳面，不与阴面的鐡合并。',
  'en_description': 'Gold is recorded on Longshou’s sunny side, separately from iron on its shaded side.',
  'en_quote': 'Its sunny side has much gold.'},
 {'id': 'material-xishan-iron-longshou',
  'slug': 'longshou',
  'kind': 'material',
  'group': 'natural_features',
  'art': None,
  'name': '鐡（龍首山阴面）',
  'en_name': 'Iron (shaded side of Longshou)',
  'quote': '其隂多鐡',
  'description': '鐡列在龍首山阴面，保留底本鐡字，不补矿床位置或开采记述。',
  'en_description': 'Iron is recorded on Longshou’s shaded side. The edition character is retained, without a mining '
                    'site or extraction account.',
  'en_quote': 'Its shaded side has much iron.'},
 {'id': 'water-xishan-tiao-longshou',
  'slug': 'longshou',
  'kind': 'water',
  'group': 'natural_features',
  'art': None,
  'name': '苕水（龍首山）',
  'en_name': 'Tiao River (Longshou)',
  'quote': '苕水出焉東南流注于涇水',
  'description': '苕水出自龍首山，向东南流注涇水，与南山经苕水分条。此句不直接写苕水注渭，不据涇水关系补造现代河网。',
  'en_description': 'The Tiao rises at Longshou and flows southeast into the Jing. It remains separate from the '
                    'Southern Mountains Tiao; the text does not directly record it entering the Wei or define a modern '
                    'river network.',
  'en_quote': 'The Tiao rises here and flows southeast into the Jing.'},
 {'id': 'material-xishan-fine-jade-longshou',
  'slug': 'longshou',
  'kind': 'material',
  'group': 'natural_features',
  'art': None,
  'name': '羙玉（龍首山水文）',
  'en_name': 'Fine jade (Longshou waters)',
  'quote': '其中多羙玉',
  'description': '其中多羙玉接在苕水东南注涇的水文之后，作为本段水文物产保存。保留羙字，不将物产扩展到整条涇水或鉴定现代玉种。',
  'en_description': 'Fine jade follows the Tiao-to-Jing statement and is retained as a product in this passage’s water '
                    'account. It is not extended to the entire Jing or identified as a modern jade variety.',
  'en_quote': 'The waters contain much fine jade.',
  'relation_scope': 'water'}]


ENTITIES += [
    {'id': 'material-xishan-white-jade-lutai', 'slug': 'lutai', 'kind': 'material', 'group': 'natural_features', 'art': None,
     'name': '白玉（鹿臺山上）', 'en_name': 'White jade (upper Lutai)', 'quote': '其上多白玉',
     'description': '白玉记在鹿臺山上，与山下的银分别保存，不据白色直接鉴定现代矿物品种或矿床。',
     'en_description': 'White jade is recorded above at Lutai, separately from silver below. Its color does not establish a modern mineral variety or deposit.',
     'en_quote': 'White jade is abundant above.'},
    {'id': 'material-xishan-silver-lutai', 'slug': 'lutai', 'kind': 'material', 'group': 'natural_features', 'art': None,
     'name': '銀（鹿臺山下）', 'en_name': 'Silver (lower Lutai)', 'quote': '其下多銀',
     'description': '銀在0130末其下多与0131首銀连读，属于鹿臺山下物产，不并入后面的兽类名称，也不补开采场景。',
     'en_description': 'Silver joins the end of unit130 to the start of131 and belongs below at Lutai. It is separate from the following beasts, without an extraction scene.',
     'en_quote': 'Silver is abundant below.'},
    {'id': 'animal-xishan-zuoniu-lutai', 'slug': 'lutai', 'kind': '兽', 'group': 'beasts', 'art': None, 'appearance_unknown': True,
     'name': '㸲牛（鹿臺段）', 'en_name': 'Zuoniu (Lutai passage)', 'quote': '其獸多㸲牛羬羊白豪',
     'description': '㸲牛在鹿臺山与羬羊、白豪并列，本段没有角数、毛色或体形记述。不从小华或英山的图像和注文移入外貌，保留本山独立出处。',
     'en_description': 'Zuoniu is named with Qianyang and Baihao at Lutai. No horns, color or body form are described here; imagery and commentary from Xiaohua or Ying are not imported.',
     'en_quote': 'Its beasts include Zuoniu, Qianyang and Baihao.'},
    {'id': 'beast-xishan-qianyang-lutai', 'slug': 'lutai', 'kind': '兽', 'group': 'beasts', 'art': None, 'appearance_unknown': True,
     'name': '羬羊（鹿臺段）', 'en_name': 'Qianyang (Lutai passage)', 'quote': '其獸多㸲牛羬羊白豪',
     'description': '羬羊在本段仅列名，没有重述羊形马尾或脂的功效。与钱来、英山的同名条目分开，不据同名将其他山段的身体特征和用途补入。',
     'en_description': 'Qianyang is only named here. A sheep-like form, horse’s tail and uses of its fat are not restated. This passage remains separate from the Qianlai and Ying entries.',
     'en_quote': 'Its beasts include Zuoniu, Qianyang and Baihao.'},
    {'id': 'animal-xishan-baihao-lutai', 'slug': 'lutai', 'kind': '兽', 'group': 'beasts', 'art': None, 'appearance_unknown': True,
     'name': '白豪（鹿臺段）', 'en_name': 'Baihao (Lutai passage)', 'quote': '其獸多㸲牛羬羊白豪', 'commentary_quote': '豪貆猪也',
     'description': '白豪列在鹿臺山兽类中，正文没有单独交代身体结构。豪貆猪也是郭注，分列保留，不直接固定成现代猪类、增添棘刺或凭名称补出毛色。',
     'en_description': 'Baihao is named among Lutai’s beasts without a separate body description. Guo Pu’s gloss, hao, huan zhu, remains commentary; it does not fix a modern pig species, spines or a coat color.',
     'en_quote': 'Its beasts include Zuoniu, Qianyang and Baihao.'},
    {'id': 'beast-xishan-fuxi-lutai', 'slug': 'lutai', 'kind': '鸟', 'group': 'beasts', 'art': None,
     'name': '鳬徯（鹿臺段）', 'en_name': 'Fuxi bird (Lutai passage)', 'quote': '有鳥焉其状如雄雞而人面名曰鳬徯其名自呌也見則有兵',
     'description': '鳬徯形如雄鸡而具人面，名字与其自呌相连。见则有兵是经文的兵事征兆记述；不新增手臂、兵器或人身，也不将其与伏羲人物混同。未生成专图时仅用统一留空形象。',
     'en_description': 'The Fuxi bird has a rooster-like form and a human face, and cries its own name. Warfare is recorded as an omen of its appearance. No arms, weapons or human torso are added, and it remains distinct from the figure Fu Xi. It currently uses the shared placeholder.',
     'en_quote': 'A bird shaped like a rooster with a human face is called Fuxi; its name comes from its own cry. Its appearance is said to herald warfare.'},
]


ENTITIES += [
    {'id': 'material-xishan-qingshi-niaowei', 'slug': 'niaowei', 'kind': 'material', 'group': 'natural_features', 'art': None,
     'name': '磬石（鳥危山阳面）', 'en_name': 'Sounding stones (sunny Niaowei)', 'quote': '其陽多磬石',
     'description': '磬石列在鳥危山阳面，与髙山水文中的磬石分别保留。本段不记开采、制器或现代矿物成分。',
     'en_description': 'Sounding stones occur on Niaowei’s sunny side, separately from those in Gao’s water account. No extraction, instrument-making or modern mineral composition is recorded here.',
     'en_quote': 'Its sunny side has many sounding stones.'},
    {'id': 'plant-xishan-tan-niaowei', 'slug': 'niaowei', 'kind': 'plant', 'group': 'natural_features', 'art': None,
     'name': '檀（鳥危山阴面）', 'en_name': 'Tan trees (shaded Niaowei)', 'quote': '其隂多檀楮',
     'description': '檀与楮列在鳥危山阴面，分条保存。此处没有颜色、花叶形态或用途，不借其他山段外貌，也不直接固定现代树种。',
     'en_description': 'Tan and chu are listed on Niaowei’s shaded side and retain separate entries. No color, flower, leaf form or use is supplied here, and no modern tree species is fixed.',
     'en_quote': 'Its shaded side has many tan and chu trees.'},
    {'id': 'plant-xishan-chu-niaowei', 'slug': 'niaowei', 'kind': 'plant', 'group': 'natural_features', 'art': None,
     'name': '楮（鳥危山阴面）', 'en_name': 'Chu trees (shaded Niaowei)', 'quote': '其隂多檀楮', 'commentary_quote': '楮即榖木',
     'description': '楮列在鳥危山阴面。郭注楮即榖木虽附在0134录文块，却解释0133的楮，不归女牀或水文；保留榖字，不补纸张制造等用途。',
     'en_description': 'Chu is recorded on Niaowei’s shaded side. The gloss chu is gu wood is captured in unit134 but explains chu in133, not nvchuang or the river. The edition character is retained without adding paper-making uses.',
     'en_quote': 'Its shaded side has many tan and chu trees.'},
    {'id': 'material-xishan-nvchuang-niaowei', 'slug': 'niaowei', 'kind': 'material', 'group': 'natural_features', 'art': None,
     'name': '女牀（鳥危段·所指未詳）', 'en_name': 'Nvchuang (Niaowei; referent unclear)', 'quote': '其中多女牀', 'commentary_quote': '未詳',
     'description': '女牀在鳥危段记其中多女牀，郭注未詳。本卡仅作为未定性的物产索引，不判为动物、草木、人物、地名或床具，也不与前文女牀山合并；图位留空。',
     'en_description': 'Nvchuang is named here, with the commentary unexplained. This is an index entry for an unclassified local item, without identifying an animal, plant, person, place or bed or merging it with Mount Nvchuang. Its image remains blank.',
     'en_quote': 'There is much nvchuang.',
     'content_note': 'kind=material仅沿用物产索引容器，不表示已确定其为矿物或器物；形貌与类别未详，不使用生物占位。',
     'en_content_note': 'The material container is an indexing category, not an identification as a mineral or manufactured object. Form and class are unclear; no creature placeholder is used.'},
    {'id': 'water-xishan-niaowei', 'slug': 'niaowei', 'kind': 'water', 'group': 'natural_features', 'art': None,
     'name': '鳥危之水', 'en_name': 'Niaowei River', 'quote': '鳥危之水出焉西流注于赤水',
     'description': '鳥危水从鳥危山流出，向西注赤水。此处只保留经文明示的出山与流入方向，不推定现代河道或将水画成赤色。',
     'en_description': 'The Niaowei rises at Mount Niaowei and flows west into the Chi. Only the stated source context and direction are retained, without a modern course or red-colored water.',
     'en_quote': 'The Niaowei River rises here and flows west into the Chi.'},
    {'id': 'material-xishan-dansu-niaowei', 'slug': 'niaowei', 'kind': 'material', 'group': 'natural_features', 'art': None, 'relation_scope': 'water',
     'name': '丹粟（鳥危段水文）', 'en_name': 'Dansu (Niaowei waters)', 'quote': '其中多丹粟',
     'description': '丹粟接在鳥危水西注赤水之后，属于本段水文物产。与南山、西山其他丹粟出处分别保存，不移入别山郭注的形色解释，也不扩展到整条赤水。',
     'en_description': 'Dansu follows the Niaowei-to-Chi account as a product of this passage’s waters. Other Southern and Western occurrences retain separate sources; no other passage’s gloss or entire-Chi distribution is imported.',
     'en_quote': 'The waters contain much dansu.'},
]


ENTITIES += [
    {'id': 'material-xishan-white-jade-xiaoci', 'slug': 'xiaoci', 'kind': 'material', 'group': 'natural_features', 'art': None,
     'name': '白玉（小次山上）', 'en_name': 'White jade (upper Xiaoci)', 'quote': '其上多白玉',
     'description': '白玉记在小次山上，与鹿臺等同名物产分别保存出处，不据颜色确定现代玉种、矿床或器物。',
     'en_description': 'White jade is recorded above at Xiaoci, retaining a source separate from Lutai and other occurrences. Its color does not establish a modern jade variety, deposit or object.',
     'en_quote': 'White jade is abundant above.'},
    {'id': 'material-xishan-red-copper-xiaoci', 'slug': 'xiaoci', 'kind': 'material', 'group': 'natural_features', 'art': None,
     'name': '赤銅（小次山下）', 'en_name': 'Red copper (lower Xiaoci)', 'quote': '其下多赤銅',
     'description': '赤铜列在小次山下，赤字与上下位置依本段保存，不移用女牀山阳面的物产位置，也不补开采、冶炼或现代纯度解释。',
     'en_description': 'Red copper is recorded below at Xiaoci. The color term and location remain specific to this passage, without importing Nvchuang’s sunny-side setting, mining, smelting or modern purity.',
     'en_quote': 'Red copper is abundant below.'},
    {'id': 'beast-xishan-zhuyan-xiaoci', 'slug': 'xiaoci', 'kind': '兽', 'group': 'beasts', 'art': None,
     'name': '朱厭（小次段）', 'en_name': 'Zhuyan (Xiaoci passage)', 'quote': '有獸焉其状如猨而白首赤足名曰朱厭見則大兵',
     'commentary_quote': '一作見則有兵起焉一作見則為兵',
     'description': '朱厭形如猿，白首赤足；赤足指足部，经文没有把全身写成红色。见则大兵及郭注两种兵事异文分别保存为古籍征兆，不加角、翅膀、武器或实际战争场景。专图未生成时使用统一留空形象，不将占位狐形当作朱厭形貌。',
     'en_description': 'Zhuyan resembles an ape with a white head and red feet; the text does not make its entire body red. Great warfare and two commentary variants remain ancient omen statements. No horns, wings, weapons or actual battle scene are added. The shared placeholder is not a depiction of Zhuyan.',
     'en_quote': 'A beast shaped like an ape, with a white head and red feet, is called Zhuyan. Its appearance is said to herald great warfare.',
     'content_note': '0137影印猨字与快照猿不同，仅阅读引文补作猨；0138空正文单元承接本兽郭注，仍纳入小次段来源；正文見則大兵不以异文替换，不将兵事征兆说成已验证预测。',
     'en_content_note': 'Scan49 has yuan (U+7328) while unit137 captures the variant U+733F; only the reading quotation is corrected. Annotation-only unit138 continues this beast’s commentary and remains in the passage sources. The main-text omen is not replaced by a variant or presented as a verified prediction.'},
]


ENTITIES += [
    {'id': 'material-xishan-e-daci', 'slug': 'daci', 'kind': 'material', 'group': 'natural_features', 'art': None,
     'name': '堊（大次山阳面）', 'en_name': 'E (sunny Daci)', 'quote': '其陽多堊', 'commentary_quote': '堊似土色甚白音惡',
     'description': '堊列在大次山阳面，郭注释似土、色甚白并注音惡。正文与解释分列，不直接鉴定现代白垩、颜料或矿床，也不把白色扩展到兽类。',
     'en_description': 'E occurs on Daci’s sunny side. Commentary calls it soil-like and very white and supplies its pronunciation. The text and gloss remain separate, without identifying modern chalk, pigment or a deposit or making the beasts white.',
     'en_quote': 'Its sunny side has much e.'},
    {'id': 'material-xishan-bi-daci', 'slug': 'daci', 'kind': 'material', 'group': 'natural_features', 'art': None,
     'name': '碧（大次山阴面）', 'en_name': 'Bi (shaded Daci)', 'quote': '其隂多碧',
     'description': '碧承接0139末其隂与0140首多碧，属于大次山阴面物产。本段没有另列碧的郭注，不移用髙山青碧注或指定现代矿物品种。',
     'en_description': 'Bi joins the end of139 to the start of140 and belongs to Daci’s shaded side. No separate bi commentary is supplied here; Gao’s qingbi gloss and modern mineral varieties are not imported.',
     'en_quote': 'Its shaded side has much bi.'},
    {'id': 'animal-xishan-zuoniu-daci', 'slug': 'daci', 'kind': '兽', 'group': 'beasts', 'art': None, 'appearance_unknown': True,
     'name': '㸲牛（大次段）', 'en_name': 'Zuoniu (Daci passage)', 'quote': '其獸多㸲牛麢羊',
     'description': '㸲牛与麢羊在大次山并列，经文没有角数、毛色、身体结构或行为。保留本山独立出处，不借小华、英山或鹿臺图像，也不移用堊郭注的白色。',
     'en_description': 'Zuoniu is named with Lingyang at Daci, without horns, coat color, body structure or behavior. This source remains separate from Xiaohua, Ying and Lutai imagery, and the white color in the e gloss is not transferred to it.',
     'en_quote': 'Its beasts include Zuoniu and Lingyang.'},
    {'id': 'animal-xishan-lingyang-daci', 'slug': 'daci', 'kind': '兽', 'group': 'beasts', 'art': None, 'appearance_unknown': True,
     'name': '麢羊（大次段）', 'en_name': 'Lingyang (Daci passage)', 'quote': '其獸多㸲牛麢羊',
     'description': '麢羊在大次段仅列名，保留麢字，不替换成别段羬羊或直接固定为现代羚羊物种。本段无角形、颜色和功效，不从翠山麢或其他羊形兽移入外貌。',
     'en_description': 'Lingyang is only named here. The edition character remains distinct from Qianyang, without fixing a modern antelope species or importing horns, color or uses from Cui’s ling or other sheep-like beasts.',
     'en_quote': 'Its beasts include Zuoniu and Lingyang.'},
]


ENTITIES += [{'id': 'material-xishan-jin-xunwu',
  'kind': 'material',
  'group': 'natural_features',
  'name': '金（薰吳段）',
  'en_name': 'Jin (Xunwu)',
  'art': None,
  'quote': '多金玉',
  'description': '金在薰吳段与玉并列，保留本段只称金的层次，不替换黄金或判定现代矿种。',
  'en_description': 'Jin is listed with jade here. Its wording is retained without substituting gold or fixing a '
                    'modern mineral.',
  'en_quote': 'There is much jin and jade.',
  'slug': 'xunwu'},
 {'id': 'material-xishan-jade-xunwu',
  'kind': 'material',
  'group': 'natural_features',
  'name': '玉（薰吳段）',
  'en_name': 'Jade (Xunwu)',
  'art': None,
  'quote': '多金玉',
  'description': '玉在无草木的薰吳山列为物产，本段没有颜色、质地或功效，不借其他山段玉名及郭注。',
  'en_description': 'Jade is a product at vegetation-free Xunwu, without a color, texture or use supplied here. '
                    'Other jade names and glosses are not imported.',
  'en_quote': 'There is much jin and jade.',
  'slug': 'xunwu'}]


ENTITIES += [{'id': 'plant-xishan-ji-quyang',
  'kind': 'plant',
  'group': 'natural_features',
  'name': '稷（𢇨陽段）',
  'en_name': 'Ji tree (𢇨yang)',
  'art': None,
  'quote': '其木多稷柟豫章',
  'description': '稷列本山树木。似松、有剌、细理与音即是跨行郭注，不把稷按常用字义画成谷物，也不固定现代松种。',
  'en_description': 'Ji is listed among trees. Pine-like form, prickles, fine grain and pronunciation are '
                    'commentary, not a grain crop or a fixed modern pine species.',
  'en_quote': 'Its trees include ji, nan and yuzhang.',
  'commentary_quote': '稷似松有剌細理音即',
  'slug': 'quyang'},
 {'id': 'plant-xishan-nan-quyang',
  'kind': 'plant',
  'group': 'natural_features',
  'name': '柟（𢇨陽段）',
  'en_name': 'Nan tree (𢇨yang)',
  'art': None,
  'quote': '其木多稷柟豫章',
  'description': '柟在本段只列名，不移用其他山木的颜色、叶形或功效，也不把前后郭注并到柟。',
  'en_description': 'Nan is only named here; neighboring tree glosses, colors, leaf forms and uses are not assigned '
                    'to it.',
  'en_quote': 'Its trees include ji, nan and yuzhang.',
  'slug': 'quyang'},
 {'id': 'plant-xishan-yuzhang-quyang',
  'kind': 'plant',
  'group': 'natural_features',
  'name': '豫章（𢇨陽段）',
  'en_name': 'Yuzhang (𢇨yang)',
  'art': None,
  'quote': '其木多稷柟豫章',
  'description': '豫章的大木、似楸叶、冬夏青及七年后可知来自郭注，正文仅列名。古籍识别记述分列，不套现代物种或用途。',
  'en_description': 'Large size, comparison with qiu leaves, green foliage across seasons and recognition after '
                    'seven years belong to commentary; the main text only names the tree. No modern species or use '
                    'is fixed.',
  'en_quote': 'Its trees include ji, nan and yuzhang.',
  'commentary_quote': '豫章大木似楸葉冬夏青生七年而後復可知也',
  'slug': 'quyang'},
 {'id': 'animal-xishan-xi-quyang',
  'kind': '兽',
  'group': 'beasts',
  'name': '犀（𢇨陽段）',
  'en_name': 'Xi (𢇨yang passage)',
  'art': None,
  'quote': '其獸多犀兕虎犳㸲牛',
  'description': '犀在𢇨陽段列名，正文未另写颜色、角数、身体结构或功效。保留本山独立出处，不借同名条目或其他篇章形貌；缺图仅用统一留空形象。',
  'en_description': 'Xi is named in this passage without a separate color, horn count, body structure or use. Its '
                    'source remains distinct; forms from namesakes or other passages are not imported. It uses the '
                    'shared placeholder.',
  'en_quote': 'Its beasts include xi, si, tigers, zhuo and Zuoniu.',
  'appearance_unknown': True,
  'slug': 'quyang'},
 {'id': 'animal-xishan-si-quyang',
  'kind': '兽',
  'group': 'beasts',
  'name': '兕（𢇨陽段）',
  'en_name': 'Si (𢇨yang passage)',
  'art': None,
  'quote': '其獸多犀兕虎犳㸲牛',
  'description': '兕在𢇨陽段列名，正文未另写颜色、角数、身体结构或功效。保留本山独立出处，不借同名条目或其他篇章形貌；缺图仅用统一留空形象。',
  'en_description': 'Si is named in this passage without a separate color, horn count, body structure or use. Its '
                    'source remains distinct; forms from namesakes or other passages are not imported. It uses the '
                    'shared placeholder.',
  'en_quote': 'Its beasts include xi, si, tigers, zhuo and Zuoniu.',
  'appearance_unknown': True,
  'slug': 'quyang'},
 {'id': 'animal-xishan-tiger-quyang',
  'kind': '兽',
  'group': 'beasts',
  'name': '虎（𢇨陽段）',
  'en_name': 'Tigers (𢇨yang passage)',
  'art': None,
  'quote': '其獸多犀兕虎犳㸲牛',
  'description': '虎在𢇨陽段列名，正文未另写颜色、角数、身体结构或功效。保留本山独立出处，不借同名条目或其他篇章形貌；缺图仅用统一留空形象。',
  'en_description': 'Tigers is named in this passage without a separate color, horn count, body structure or use. '
                    'Its source remains distinct; forms from namesakes or other passages are not imported. It uses '
                    'the shared placeholder.',
  'en_quote': 'Its beasts include xi, si, tigers, zhuo and Zuoniu.',
  'appearance_unknown': True,
  'slug': 'quyang'},
 {'id': 'animal-xishan-zhuo-quyang',
  'kind': '兽',
  'group': 'beasts',
  'name': '犳（𢇨陽段）',
  'en_name': 'Zhuo (𢇨yang passage)',
  'art': None,
  'quote': '其獸多犀兕虎犳㸲牛',
  'description': '犳在𢇨陽段列名，正文未另写颜色、角数、身体结构或功效。保留本山独立出处，不借同名条目或其他篇章形貌；缺图仅用统一留空形象。',
  'en_description': 'Zhuo is named in this passage without a separate color, horn count, body structure or use. Its '
                    'source remains distinct; forms from namesakes or other passages are not imported. It uses the '
                    'shared placeholder.',
  'en_quote': 'Its beasts include xi, si, tigers, zhuo and Zuoniu.',
  'appearance_unknown': True,
  'commentary_quote': '犳音之樂反',
  'content_note': '影印正文犳、快照豹，阅读引文补犳；音注只属犳，未借现代豹的形貌。',
  'en_content_note': 'The scan has zhuo where the snapshot captures leopard; only the reading quotation is '
                     'corrected. The pronunciation gloss belongs to zhuo and supplies no leopard form.',
  'slug': 'quyang'},
 {'id': 'animal-xishan-zuoniu-quyang',
  'kind': '兽',
  'group': 'beasts',
  'name': '㸲牛（𢇨陽段）',
  'en_name': 'Zuoniu (𢇨yang passage)',
  'art': None,
  'quote': '其獸多犀兕虎犳㸲牛',
  'description': '㸲牛在𢇨陽段列名，正文未另写颜色、角数、身体结构或功效。保留本山独立出处，不借同名条目或其他篇章形貌；缺图仅用统一留空形象。',
  'en_description': 'Zuoniu is named in this passage without a separate color, horn count, body structure or use. '
                    'Its source remains distinct; forms from namesakes or other passages are not imported. It uses '
                    'the shared placeholder.',
  'en_quote': 'Its beasts include xi, si, tigers, zhuo and Zuoniu.',
  'appearance_unknown': True,
  'slug': 'quyang'}]


ENTITIES += [{'id': 'material-xishan-tufu-zhongshou',
  'kind': 'material',
  'group': 'natural_features',
  'name': '㻬琈之玉（衆獸山上）',
  'en_name': 'Tufu jade (upper Zhongshou)',
  'art': None,
  'quote': '其上多㻬琈之玉',
  'description': '㻬琈之玉列在山上，本段没有另注颜色、纹样或功效；与别山同名玉分出处，不复制其郭注。',
  'en_description': 'Tufu jade occurs above, without a separate color, pattern or use here. Namesake jade entries '
                    'keep their own sources and glosses.',
  'en_quote': 'Above is much tufu jade.',
  'slug': 'zhongshou'},
 {'id': 'plant-xishan-tan-zhongshou',
  'kind': 'plant',
  'group': 'natural_features',
  'name': '檀（衆獸山下）',
  'en_name': 'Tan trees (lower Zhongshou)',
  'art': None,
  'quote': '其下多檀楮多黄金',
  'description': '檀、楮列山下，各自索引；本段无形貌与用途，不借其他山段郭注。',
  'en_description': 'Tan and chu occur below and have separate index entries, without forms, uses or borrowed '
                    'commentary.',
  'en_quote': 'Below are many tan and chu trees and much gold.',
  'slug': 'zhongshou'},
 {'id': 'plant-xishan-chu-zhongshou',
  'kind': 'plant',
  'group': 'natural_features',
  'name': '楮（衆獸山下）',
  'en_name': 'Chu trees (lower Zhongshou)',
  'art': None,
  'quote': '其下多檀楮多黄金',
  'description': '檀、楮列山下，各自索引；本段无形貌与用途，不借其他山段郭注。',
  'en_description': 'Tan and chu occur below and have separate index entries, without forms, uses or borrowed '
                    'commentary.',
  'en_quote': 'Below are many tan and chu trees and much gold.',
  'slug': 'zhongshou'},
 {'id': 'material-xishan-gold-zhongshou',
  'kind': 'material',
  'group': 'natural_features',
  'name': '黄金（衆獸山下）',
  'en_name': 'Gold (lower Zhongshou)',
  'art': None,
  'quote': '其下多檀楮多黄金',
  'description': '黄金记在衆獸山下，不移到山上㻬琈玉的位置，不补矿井或冶炼。',
  'en_description': 'Gold is recorded below, separately from upper tufu jade, without a mine or smelting scene.',
  'en_quote': 'Below are many tan and chu trees and much gold.',
  'slug': 'zhongshou'},
 {'id': 'animal-xishan-xi-zhongshou',
  'kind': '兽',
  'group': 'beasts',
  'name': '犀（衆獸段）',
  'en_name': 'Xi (Zhongshou passage)',
  'art': None,
  'quote': '其獸多犀兕',
  'description': '犀在衆獸段列名，正文未另写颜色、角数、身体结构或功效。保留本山独立出处，不借同名条目或其他篇章形貌；缺图仅用统一留空形象。',
  'en_description': 'Xi is named in this passage without a separate color, horn count, body structure or use. Its '
                    'source remains distinct; forms from namesakes or other passages are not imported. It uses the '
                    'shared placeholder.',
  'en_quote': 'Its beasts include xi and si.',
  'appearance_unknown': True,
  'slug': 'zhongshou'},
 {'id': 'animal-xishan-si-zhongshou',
  'kind': '兽',
  'group': 'beasts',
  'name': '兕（衆獸段）',
  'en_name': 'Si (Zhongshou passage)',
  'art': None,
  'quote': '其獸多犀兕',
  'description': '兕在衆獸段列名，正文未另写颜色、角数、身体结构或功效。保留本山独立出处，不借同名条目或其他篇章形貌；缺图仅用统一留空形象。',
  'en_description': 'Si is named in this passage without a separate color, horn count, body structure or use. Its '
                    'source remains distinct; forms from namesakes or other passages are not imported. It uses the '
                    'shared placeholder.',
  'en_quote': 'Its beasts include xi and si.',
  'appearance_unknown': True,
  'slug': 'zhongshou'}]


ENTITIES += [{'id': 'material-xishan-jin-huangren',
  'kind': 'material',
  'group': 'natural_features',
  'name': '金（皇人山上）',
  'en_name': 'Jin (upper Huangren)',
  'art': None,
  'quote': '其上多金玉',
  'description': '金在皇人山上与玉并列，本段只称金，不改黄金或套入采矿场景。',
  'en_description': 'Jin is listed above with jade, without changing it to gold or adding mining.',
  'en_quote': 'Above are much jin and jade.',
  'slug': 'huangren'},
 {'id': 'material-xishan-jade-huangren',
  'kind': 'material',
  'group': 'natural_features',
  'name': '玉（皇人山上）',
  'en_name': 'Jade (upper Huangren)',
  'art': None,
  'quote': '其上多金玉',
  'description': '玉列皇人山上，没有颜色、形态或功效描述，不借他山特定玉名。',
  'en_description': 'Jade is recorded above without a color, form, use or borrowed named variety.',
  'en_quote': 'Above are much jin and jade.',
  'slug': 'huangren'},
 {'id': 'material-xishan-qingxionghuang-huangren',
  'kind': 'material',
  'group': 'natural_features',
  'name': '青雄黄（皇人山下）',
  'en_name': 'Qing xionghuang (lower Huangren)',
  'art': None,
  'quote': '其下多青雄黄',
  'description': '青雄黄保留连续录文，郭注即雌黄也或曰空青曽青之属另列。此卡暂作整组矿物索引，不强定青与雄黄的分词、现代成分或药用。',
  'en_description': 'The continuous qing xionghuang wording and alternative commentary comparisons remain separate. '
                    'This entry indexes the mineral phrase without forcing segmentation, modern composition or '
                    'medicinal use.',
  'en_quote': 'Below is qing xionghuang.',
  'commentary_quote': '即雌黄也或曰空青曽青之属',
  'slug': 'huangren'},
 {'id': 'water-xishan-huang-huangren',
  'kind': 'water',
  'group': 'natural_features',
  'name': '皇水（皇人段）',
  'en_name': 'Huang River (Huangren)',
  'art': None,
  'quote': '皇水出焉西流注于赤水',
  'description': '皇水从皇人山流出，向西注赤水，不改成黄水或补现代河道。',
  'en_description': 'The Huang rises at Huangren and flows west into the Chi, without changing the Chinese river '
                    'name or supplying a modern course.',
  'en_quote': 'The Huang rises here and flows west into the Chi.',
  'slug': 'huangren'},
 {'id': 'material-xishan-dansu-huangren',
  'kind': 'material',
  'group': 'natural_features',
  'name': '丹粟（皇人段水文）',
  'en_name': 'Dansu (Huangren waters)',
  'art': None,
  'quote': '其中多丹粟',
  'description': '丹粟接在皇水西注赤水之后，保存本段水文上下文，不扩展到整个赤水或移用别山形色解释。',
  'en_description': 'Dansu follows the Huang-to-Chi statement, retaining its local water context without a whole-Chi '
                    'distribution or another passage’s form gloss.',
  'en_quote': 'The waters contain much dansu.',
  'relation_scope': 'water',
  'slug': 'huangren'}]


ENTITIES += [{'id': 'material-xishan-gold-zhonghuang',
  'kind': 'material',
  'group': 'natural_features',
  'name': '黄金（中皇山上）',
  'en_name': 'Gold (upper Zhonghuang)',
  'art': None,
  'quote': '其上多黄金',
  'description': '黄金记在中皇山上，与山下蕙棠分别保存，不补采矿活动或器物。',
  'en_description': 'Gold occurs above, separately from lower huitang, without mining or manufactured objects.',
  'en_quote': 'Gold is abundant above.',
  'slug': 'zhonghuang'},
 {'id': 'plant-xishan-huitang-zhonghuang',
  'kind': 'plant',
  'group': 'natural_features',
  'name': '蕙棠（中皇山下）',
  'en_name': 'Huitang (lower Zhonghuang)',
  'art': None,
  'quote': '其下多蕙棠',
  'description': '蕙棠连写保留，蕙按影印补读，郭注彤棠之属也或作羔分列。此处不强分两物，不套现代花叶形态或用途。',
  'en_description': 'Huitang remains continuous, with hui restored from the scan and its captured commentary '
                    'separate. No forced two-item split, modern foliage or use is added.',
  'en_quote': 'Huitang is abundant below.',
  'commentary_quote': '彤棠之属也或作羔',
  'slug': 'zhonghuang'}]


ENTITIES += [{'id': 'material-xishan-jin-xihuang',
  'kind': 'material',
  'group': 'natural_features',
  'name': '金（西皇山阳面）',
  'en_name': 'Jin (sunny Xihuang)',
  'art': None,
  'quote': '其陽多金',
  'description': '金在西皇山阳面，本段不称黄金，保留原字及位置。',
  'en_description': 'Jin is recorded on the sunny side; the passage does not specify gold.',
  'en_quote': 'Its sunny side has much jin.',
  'slug': 'xihuang'},
 {'id': 'material-xishan-iron-xihuang',
  'kind': 'material',
  'group': 'natural_features',
  'name': '鐡（西皇山阴面）',
  'en_name': 'Iron (shaded Xihuang)',
  'art': None,
  'quote': '其隂多鐡',
  'description': '鐡记西皇山阴面，保留底本字形，不补矿井或现代鉴定。',
  'en_description': 'Iron occurs on the shaded side, retaining the edition character without a mine or modern '
                    'identification.',
  'en_quote': 'Its shaded side has much iron.',
  'slug': 'xihuang'},
 {'id': 'animal-xishan-mi-xihuang',
  'kind': '兽',
  'group': 'beasts',
  'name': '麋（西皇段）',
  'en_name': 'Mi (Xihuang passage)',
  'art': None,
  'quote': '其獸多麋鹿㸲牛',
  'description': '麋在西皇段列名，郭注比较大如小牛并称鹿属。体量及类属解释分列，不补角形、毛色或现代物种；仍以统一留空图表示未有专图。',
  'en_description': 'Mi is named here; commentary compares its size with a small ox and classes it with deer. These '
                    'comparisons do not establish horns, coat color or a modern species. It still uses the shared '
                    'placeholder.',
  'en_quote': 'Its beasts include mi, deer and Zuoniu.',
  'appearance_unknown': True,
  'commentary_quote': '麋大如小牛鹿属也',
  'slug': 'xihuang'},
 {'id': 'animal-xishan-deer-xihuang',
  'kind': '兽',
  'group': 'beasts',
  'name': '鹿（西皇段）',
  'en_name': 'Deer (Xihuang passage)',
  'art': None,
  'quote': '其獸多麋鹿㸲牛',
  'description': '鹿在西皇段列名，正文未另写颜色、角数、身体结构或功效。保留本山独立出处，不借同名条目或其他篇章形貌；缺图仅用统一留空形象。',
  'en_description': 'Deer is named in this passage without a separate color, horn count, body structure or use. Its '
                    'source remains distinct; forms from namesakes or other passages are not imported. It uses the '
                    'shared placeholder.',
  'en_quote': 'Its beasts include mi, deer and Zuoniu.',
  'appearance_unknown': True,
  'slug': 'xihuang'},
 {'id': 'animal-xishan-zuoniu-xihuang',
  'kind': '兽',
  'group': 'beasts',
  'name': '㸲牛（西皇段）',
  'en_name': 'Zuoniu (Xihuang passage)',
  'art': None,
  'quote': '其獸多麋鹿㸲牛',
  'description': '㸲牛在西皇段列名，正文未另写颜色、角数、身体结构或功效。保留本山独立出处，不借同名条目或其他篇章形貌；缺图仅用统一留空形象。',
  'en_description': 'Zuoniu is named in this passage without a separate color, horn count, body structure or use. '
                    'Its source remains distinct; forms from namesakes or other passages are not imported. It uses '
                    'the shared placeholder.',
  'en_quote': 'Its beasts include mi, deer and Zuoniu.',
  'appearance_unknown': True,
  'slug': 'xihuang'}]


ENTITIES += [{'id': 'plant-xishan-tan-laishan',
  'kind': 'plant',
  'group': 'natural_features',
  'name': '檀（萊山段）',
  'en_name': 'Tan trees (Lai)',
  'art': None,
  'quote': '其木多檀楮',
  'description': '檀与楮在萊山并列，独立索引；本段没有形貌注，不借鳥危楮注或其他山树木用途。',
  'en_description': 'Tan and chu are named at Lai and separately indexed, without imported tree glosses or uses.',
  'en_quote': 'Its trees include tan and chu.',
  'slug': 'laishan'},
 {'id': 'plant-xishan-chu-laishan',
  'kind': 'plant',
  'group': 'natural_features',
  'name': '楮（萊山段）',
  'en_name': 'Chu trees (Lai)',
  'art': None,
  'quote': '其木多檀楮',
  'description': '檀与楮在萊山并列，独立索引；本段没有形貌注，不借鳥危楮注或其他山树木用途。',
  'en_description': 'Tan and chu are named at Lai and separately indexed, without imported tree glosses or uses.',
  'en_quote': 'Its trees include tan and chu.',
  'slug': 'laishan'},
 {'id': 'bird-xishan-luoluo-laishan',
  'kind': '鸟',
  'group': 'beasts',
  'name': '羅羅（萊山段）',
  'en_name': 'Luoluo (Lai passage)',
  'art': None,
  'quote': '其鳥多羅羅是食人',
  'description': '羅羅是萊山所记鸟名，经文说食人，郭注所未詳也。这里不补羽色、喙形、头数或其他怪鸟器官，食人只作古籍记述，图位统一占位。',
  'en_description': 'Luoluo is a bird named at Lai and said to eat people, while commentary leaves it unexplained. '
                    'No plumage, beak, head count or borrowed organs are supplied; the ancient statement remains '
                    'separate from the shared placeholder.',
  'en_quote': 'Its birds include many Luoluo, which are said to eat people.',
  'appearance_unknown': True,
  'commentary_quote': '羅羅之鳥所未詳也',
  'slug': 'laishan'}]


ENTITIES += [{'id': 'deity-xishan-horse-range2',
  'kind': 'deity',
  'group': 'text_entities',
  'name': '十神·人靣馬身（西次二经）',
  'en_name': 'Ten horse-bodied deities (second range)',
  'art': None,
  'quote': '其十神者皆人靣而馬身',
  'description': '十神为本列总括的集体记述，形貌只有人面马身，不新增十个神名或个体图像，不借后句牛身神的四足一臂。',
  'en_description': 'Ten deities form a collective summary entry with human faces and horse bodies. No ten '
                    'individual names or images are invented, and the following ox-bodied group’s limb description '
                    'is not transferred.',
  'en_quote': 'Ten deities have human faces and horse bodies.',
  'slug': 'range2-summary'},
 {'id': 'deity-xishan-ox-range2',
  'kind': 'deity',
  'group': 'text_entities',
  'name': '七神·人靣牛身（西次二经）',
  'en_name': 'Seven ox-bodied deities (second range)',
  'art': None,
  'quote': '其七神皆人靣牛身四足而一臂操杖以行是為飛獸之神',
  'description': '七神在总括中记人面牛身、四足一臂、操杖而行，后接飞兽之神。作为集体条目保留明确结构，不给另一组加同样器官，也不因飞字补翅膀。',
  'en_description': 'Seven deities are described with human faces, ox bodies, four feet, one arm and a staff, '
                    'followed by the flying-beast deity wording. The collective form stays explicit, without added '
                    'wings or transferring its limbs to the other group.',
  'en_quote': 'Seven deities have human faces, ox bodies, four feet and one arm and carry a staff; the text calls '
              'them flying-beast deities.',
  'slug': 'range2-summary'},
 {'id': 'rite-xishan-shaolao-range2',
  'kind': 'rite',
  'group': 'text_entities',
  'name': '少牢与白菅之席（西次二经）',
  'en_name': 'Shaolao and white jian seats',
  'art': None,
  'quote': '其祠之毛用少牢白菅為席',
  'description': '少牢和白菅为席是经文祭礼记述，羊猪为少牢是郭注。保留祭品与席材层次，不另立确定现代草种、祭器或实际操作流程。',
  'en_description': 'Shaolao and white jian seats belong to the ritual text; sheep and pigs explaining shaolao are '
                    'commentary. Offering and seat material remain distinct without a modern plant species, vessel '
                    'or practical procedure.',
  'en_quote': 'The offering uses shaolao, with white jian as seats.',
  'commentary_quote': '羊猪為少牢也',
  'slug': 'range2-summary'},
 {'id': 'rite-xishan-rooster-range2',
  'kind': 'rite',
  'group': 'text_entities',
  'name': '十軰神雄鷄之祠（西次二经）',
  'en_name': 'Rooster rite for the ten-bei deities',
  'art': None,
  'quote': '其十軰神者其祠之毛一雄鷄鈐而不糈毛采',
  'description': '十軰、一雄鷄、鈐而不糈与毛采依录文保存。軰音背、鈐所用祭噐名所未詳也及或作思訓祈、不糈祠不以米、言用雄色鷄也另列郭注；不猜定鈐器外观或擅改断句。',
  'en_description': 'Ten-bei, one rooster, qian without xu and mao cai retain the captured wording. Pronunciation, '
                    'the uncertain ritual vessel and alternative wording, the no-rice gloss and rooster-color gloss '
                    'remain commentary, without an invented vessel appearance or definitive parsing.',
  'en_quote': 'The ten-bei rite records one rooster, qian without xu, and mao cai.',
  'commentary_quote': '音背；鈐所用祭噐名所未詳也或作思訓祈不糈祠不以米；言用雄色鷄也',
  'slug': 'range2-summary'}]


ENTITIES += [{'id': 'place-xishan-zhongsui-chongwu',
  'slug': 'chongwu',
  'kind': 'place',
  'group': 'text_entities',
  'name': '冡遂（崇吾段）',
  'en_name': 'Zhongsui (Chongwu passage)',
  'quote': '北望冡遂',
  'description': '冡遂是崇吾山北望所见，郭注释山名。保留冡字，不给现代位置或把它列作本列下一座行程山。',
  'en_description': 'Zhongsui is seen to the north from Chongwu and is glossed as a mountain name. The edition '
                    'character is retained without a modern location or an extra route stage.',
  'en_quote': 'To the north it overlooks Zhongsui.',
  'art': None,
  'commentary_quote': '山名'},
 {'id': 'water-xishan-yaoze-chongwu',
  'slug': 'chongwu',
  'kind': 'water',
  'group': 'natural_features',
  'name': '䍃之澤（崇吾段）',
  'en_name': 'Yao Marsh (Chongwu passage)',
  'quote': '南望䍃之澤',
  'description': '䍃之澤是崇吾山南望所见，郭注音遥。这里只记方向，没有水源、出入水道或现代位置。',
  'en_description': 'Yao Marsh is seen to the south from Chongwu; its pronunciation is glossed as yao. No source, '
                    'inflow, outflow or modern position is given.',
  'en_quote': 'To the south it overlooks Yao Marsh.',
  'art': None,
  'commentary_quote': '音遥'},
 {'id': 'place-xishan-tuan-shou-qiu-chongwu',
  'slug': 'chongwu',
  'kind': 'place',
  'group': 'text_entities',
  'name': '帝之摶獸之丘（崇吾段）',
  'en_name': 'Emperor’s Tuan Beast Hill (Chongwu passage)',
  'quote': '西望帝之摶獸之丘',
  'description': '此丘是崇吾山西望所见，摶据影印补入，电子快照缺字图标签作搏；郭注或作薄。经文未指明帝的身份，也未描述此处兽的形貌，不另造一只神兽。',
  'en_description': 'This hill is seen to the west from Chongwu. Tuan restores the scanned glyph whose snapshot '
                    'marker is labelled bo; commentary gives bo as a variant. Neither the emperor’s identity nor '
                    'a beast’s form is specified.',
  'en_quote': 'To the west it overlooks the Emperor’s Tuan Beast Hill.',
  'art': None,
  'commentary_quote': '或作薄',
  'content_note': '阅读引文据影印补摶；捕获层缺字图:搏保留，异文不合并为确定兽种。',
  'en_content_note': 'Tuan is restored from the scan in the reading quotation only; the captured image-glyph '
                     'marker is retained, without identifying a definite beast species.'},
 {'id': 'water-xishan-yanyuan-chongwu',
  'slug': 'chongwu',
  'kind': 'water',
  'group': 'natural_features',
  'name': '䗡淵（崇吾段）',
  'en_name': 'Yan Pool (Chongwu passage)',
  'quote': '東望䗡淵',
  'description': '䗡淵是崇吾山东望所见，音於与然反跨单元合为音於然反，属淵名。没有出入水道或水中生物记载，不把随后树木写成水生。',
  'en_description': 'Yan Pool is seen to the east. Its pronunciation gloss continues across captured units. No '
                    'watercourse or aquatic creature is described, and the following tree is not made aquatic.',
  'en_quote': 'To the east it overlooks Yan Pool.',
  'art': None,
  'commentary_quote': '音於然反'},
 {'id': 'plant-xishan-unnamed-chongwu',
  'slug': 'chongwu',
  'kind': 'plant',
  'group': 'natural_features',
  'name': '未名木（崇吾段）',
  'en_name': 'Unnamed tree (Chongwu passage)',
  'quote': '有木焉員葉而白柎赤華而黒理其實如枳食之宜子孫',
  'description': '这棵树没有名字。正文记圆叶、白柎、赤花、黑理及枳状果实，宜子孙仅作古籍食用说法。白柎的子房、花下鄂等解释来自郭注，不以枳给树命名，也不作现代生育建议。',
  'en_description': 'The tree is unnamed. The text records round leaves, white fu, red flowers, dark markings and '
                    'zhi-like fruit. Favoring descendants is an ancient eating claim. Commentary offers '
                    'interpretations of fu; neither a modern species nor fertility advice is supplied.',
  'en_quote': 'An unnamed tree has round leaves, white fu, red flowers, dark markings and fruit like zhi; eating '
              'it is said to favor descendants.',
  'art': None,
  'commentary_quote': '今江東人呼草木子房為柎音府一曰柎花下鄂音丈夫字或作柎音符',
  'content_note': '白柎郭注跨0164—0165连读，丈夫等录文疑字按捕获保留，释义不并入正文。',
  'en_content_note': 'The fu gloss spans units164–165. Uncertain captured wording is retained, and its '
                     'interpretations remain separate from the main text.'},
 {'id': 'beast-xishan-jufu-chongwu',
  'slug': 'chongwu',
  'kind': '兽',
  'group': 'beasts',
  'name': '舉父（崇吾段）',
  'en_name': 'Jufu (Chongwu passage)',
  'quote': '有獸焉其状如禺而文臂豹虎而善投名曰舉父',
  'description': '舉父形如禺，臂有纹，善投。影印正文作豹虎，照底本保存并注明疑处，不默改豹尾。郭注或作夸父只作异名，不据此接入逐日、手杖化林或现代动物种类。',
  'en_description': 'Jufu resembles a yu, has patterned arms and is skilled at throwing. The scan’s bao hu '
                    'wording is retained as uncertain rather than silently changed to a leopard tail. Commentary '
                    'offers Kuafu as an alternative name; the sun-chasing story and modern species are not '
                    'imported.',
  'en_quote': 'A beast called Jufu resembles a yu, with patterned arms and the wording bao hu, and is skilled at '
              'throwing.',
  'art': None,
  'commentary_quote': '或作夸父',
  'content_note': '影印豹虎与捕获一致，保留疑读；不据常见通行文擅补豹尾。',
  'en_content_note': 'The scan and capture both read bao hu. The uncertain wording is retained without silently '
                     'substituting a leopard tail.',
  'art_reference': ['统一留空形象 · 舉父插画未生成，问号剪影不代表其形貌。',
                    'Shared placeholder · Jufu has not been illustrated; the question-mark silhouette does not '
                    'depict its form.']},
 {'id': 'bird-xishan-manman-chongwu',
  'slug': 'chongwu',
  'kind': '鸟',
  'group': 'beasts',
  'name': '蠻蠻（崇吾段）',
  'en_name': 'Manman (Chongwu passage)',
  'quote': '有鳥焉其状如鳬而一翼一目相得乃飛名曰蠻蠻見則天下大水',
  'description': '蠻蠻形如鳬，却只有一翼一目，须相得才能飞，见则天下大水为古籍灾异。青赤色、比翼鸟与尔雅鶼鶼的说明来自郭注，不混成正文，也不鉴定为现实鸟种。',
  'en_description': 'Manman resembles a fu bird but has one wing and one eye and can fly only when paired. '
                    'Flooding is an ancient omen. Blue-green and red coloration and the Jianjian comparison come '
                    'from commentary, without a modern species identification.',
  'en_quote': 'Manman resembles a fu bird, has one wing and one eye and flies when paired; its appearance is said '
              'to herald great floods.',
  'art': None,
  'commentary_quote': '比翼鳥也色青赤不比不能飛爾雅作鶼鶼鳥也',
  'art_reference': ['统一留空形象 · 蠻蠻插画未生成，问号剪影不代表其一翼一目形貌。',
                    'Shared placeholder · Manman has not been illustrated; the silhouette does not depict its '
                    'one-winged, one-eyed form.']}]


ENTITIES += [{'id': 'water-xishan-ci-changsha',
  'slug': 'changsha',
  'kind': 'water',
  'group': 'natural_features',
  'name': '泚水（長沙段）',
  'en_name': 'Zi River (Changsha passage)',
  'art': None,
  'quote': '泚水出焉北流注于泑水',
  'description': '泚水从長沙山流出，向北注入泑水。郭注音紫，英文依此用Zi，中文泚字与稳定ID保留；不与泑水混为一条水，也不把泑水的水色黑移来。',
  'en_description': 'The river written Ci rises at Changsha and flows north into the You. Its pronunciation is '
                    'glossed as Zi, used in English while the Chinese character and stable ID remain. It is '
                    'distinct from its receiving water and does not inherit the You’s dark-color gloss.',
  'en_quote': 'The Zi River rises here and flows north into the You.',
  'commentary_quote': '音紫'},
 {'id': 'water-xishan-you-changsha',
  'slug': 'changsha',
  'kind': 'water',
  'group': 'natural_features',
  'name': '泑水（長沙段）',
  'en_name': 'You River (Changsha passage)',
  'art': None,
  'quote': '泚水出焉北流注于泑水',
  'description': '泑水承接長沙山北流的泚水，泑在0169末、水续于0170首。郭注烏交反、又音黝及水色黑也只归此水；本段不写其源头或完整河道，不直接合并后段泑澤或同音水名。',
  'en_description': 'The You receives the north-flowing Zi from Changsha; its name spans units169–170. The '
                    'alternate pronunciation and dark-water gloss belong here. No source or complete course is '
                    'given, and later You Marsh or similarly pronounced waters are not automatically merged.',
  'en_quote': 'The Zi River flows north into the You.',
  'commentary_quote': '烏交反又音黝水色黑也'},
 {'id': 'material-xishan-qingxionghuang-changsha',
  'slug': 'changsha',
  'kind': 'material',
  'group': 'natural_features',
  'name': '青雄黄（長沙段）',
  'en_name': 'Qing xionghuang (Changsha passage)',
  'art': None,
  'quote': '無草木多青雄黄',
  'description': '長沙段在无草木之后记多青雄黄。连写形式保留，单设本山物产卡，不借皇人山郭注拆定石青与雄黄，不指定现代化学成分、颜色分区、器形或用途。',
  'en_description': 'Qing xionghuang follows the statement that there is no vegetation. This separate Changsha '
                    'record preserves the unpunctuated wording without importing Huangren’s commentary or fixing '
                    'a modern composition, color distribution, object form or use.',
  'en_quote': 'There is no vegetation, and qing xionghuang is abundant.'}]


ENTITIES += [{'id': 'place-xishan-zhupi-buzhou',
  'slug': 'buzhou',
  'kind': 'place',
  'group': 'text_entities',
  'name': '諸毗之山（不周段）',
  'en_name': 'Mount Zhupi (Buzhou passage)',
  'art': None,
  'quote': '北望諸毗之山',
  'description': '諸毗是不周山北望所见的山，正文只给名称与这一方位关系。它是本段附带地名，不额外计作行程主线山段，也不赋予现代坐标。',
  'en_description': 'Zhupi is the mountain seen north of Buzhou. Only its name and this viewing direction are '
                    'given. It is a landmark within this passage, not an additional route stage or a modern '
                    'mapped position.',
  'en_quote': 'To the north it overlooks Mount Zhupi.'},
 {'id': 'place-xishan-yuechong-buzhou',
  'slug': 'buzhou',
  'kind': 'place',
  'group': 'text_entities',
  'name': '嶽崇之山（不周段）',
  'en_name': 'Mount Yuechong (Buzhou passage)',
  'art': None,
  'quote': '臨彼嶽崇之山',
  'description': '嶽崇见于不周段临彼嶽崇之山一句，保留底本山名。临的关系与北望、东望分开，不另补一个未写明的方位，也不与崇吾合并。',
  'en_description': 'Yuechong appears in the statement that Buzhou faces that mountain. The edition’s name is '
                    'retained, separately from the northward and eastward views. No unstated direction is added, '
                    'and it is not merged with Chongwu.',
  'en_quote': 'It faces Mount Yuechong.'},
 {'id': 'water-xishan-youze-buzhou',
  'slug': 'buzhou',
  'kind': 'water',
  'group': 'natural_features',
  'name': '泑澤（不周段）',
  'en_name': 'You Marsh (Buzhou passage)',
  'art': None,
  'quote': '東望泑澤河水所潜也其源渾渾泡泡',
  'description': '泑澤是不周山东望所见，随后记河水所潜、其源渾渾泡泡。郭注另述崑崙、葱嶺、于闐、積石等地理解释与音注，保留为古籍注说，不画作现代河道；不因泑字直接合并長沙段泑水。',
  'en_description': 'You Marsh is seen east of Buzhou, followed by the He’s underground course and surging '
                    'source. Commentary supplies a separate geographical account and pronunciation glosses. These '
                    'remain ancient commentary rather than a modern river map, and the marsh is not automatically '
                    'merged with Changsha’s You River.',
  'en_quote': 'To the east it overlooks You Marsh, where the He runs underground; its source surges hunhun '
              'paopao.',
  'commentary_quote': '河南出崑崙潜行地下至葱嶺出于闐國復分流歧出合而東流注泑澤已復潜行南出于積石山而為中國河也名泑減即蒲澤一名蒲昌海廣三四百里其水停冬夏不增减去玉門𨵿三百餘里即河之重源所謂潜行也渾渾泡泡水濆湧之聲也衮咆二音',
  'content_note': '河水郭注连读0173—0176，含0174—0175两个空正文单元；二音释前面的衮咆音注，不释嘉果。捕获泑減与影印泑澤差异明示，原注栏未擅改。',
  'en_content_note': 'The river commentary spans units173–176, including two annotation-only units. The final '
                     'two-pronunciations note belongs to the water-sound gloss, not the fruit. Captured You jian '
                     'is retained with notice of the scan’s You ze.'},
 {'id': 'plant-xishan-jia-guo-buzhou',
  'slug': 'buzhou',
  'kind': 'plant',
  'group': 'natural_features',
  'name': '嘉果（不周段·未命名）',
  'en_name': 'Unnamed fine fruit (Buzhou passage)',
  'art': None,
  'quote': '爰有嘉果其實如桃其葉如𬃷黄華而赤柎食之不勞',
  'description': '本段嘉果未给专名，果实如桃、叶如𬃷、黄花赤柎。食之不劳仅是古籍功效记述，不作现实食用建议。桃与𬃷都是形貌比拟，不给它命名为桃、枣或丹木；不借崇吾白柎郭注作本段释义。',
  'en_description': 'This fine fruit has no specific name. Its fruit resembles peaches, its leaves jujube, with '
                    'yellow flowers and red fu. Preventing fatigue is an ancient eating claim. The comparisons do '
                    'not name it peach, jujube or danmu, and Chongwu’s fu commentary is not imported.',
  'en_quote': 'A fine fruit has peach-like fruit, jujube-like leaves, yellow flowers and red fu; eating it is '
              'said to prevent fatigue.',
  'content_note': '𬃷底本字形保留；0176二音属于前文水声郭注，本卡不收为果木音注，0177不勞续正文。',
  'en_content_note': 'The edition’s jujube variant is retained. Unit176’s two-pronunciations note belongs to the '
                     'preceding river gloss and is not assigned to this plant; unit177 completes the eating '
                     'claim.'}]


ENTITIES += [{'id': 'plant-xishan-danmu-mishan',
  'slug': 'mishan',
  'kind': 'plant',
  'group': 'natural_features',
  'name': '丹木（峚山段）',
  'en_name': 'Danmu (Mi passage)',
  'quote': '丹木員葉而赤莖黄華而赤實其味如飴食之不飢',
  'description': '丹木圆叶赤茎、黄花赤实，味如饴，食之不饥为古籍说法。后文还记玉膏灌木、五岁五色乃清及五味乃馨；不据丹字认定现代朱砂植物，不把正文效果作现实食用建议。',
  'en_description': 'Danmu has round leaves, red stems, yellow flowers, red fruit and a malt-sugar-like taste. '
                    'Preventing hunger, irrigation with jade paste and changes after five years are ancient '
                    'accounts, without a modern species or dietary recommendation.',
  'en_quote': 'Danmu has round leaves, red stems, yellow flowers and red fruit, tastes like malt sugar and is '
              'said to prevent hunger.',
  'art': None,
  'commentary_quote': '言光鮮也；言滋香也',
  'content_note': '两条郭注分别释后文五色乃清/五味乃馨，并非给丹木另取名字。',
  'en_content_note': 'The two glosses explain the later statements about clear colors and fragrant flavors, not '
                     'another tree name.'},
 {'id': 'water-xishan-dan-mishan',
  'slug': 'mishan',
  'kind': 'water',
  'group': 'natural_features',
  'name': '丹水（峚山段）',
  'en_name': 'Dan River (Mi passage)',
  'quote': '丹水出焉西流注于稷澤其中多白玉是有玉膏其源沸沸湯湯',
  'description': '丹水从峚山流出，向西注入稷澤，随后水文记白玉、玉膏及其涌出。西流保留，不借其他山的丹水改向或合卡，不补现代河道、矿脉与汇流点。',
  'en_description': 'The Dan rises at Mi and flows west into Ji Marsh, followed by white jade and surging jade '
                    'paste. The westward direction and separate source are retained without merging other Dan '
                    'rivers or drawing a modern course.',
  'en_quote': 'The Dan rises here and flows west into Ji Marsh, with white jade and surging jade paste.',
  'art': None},
 {'id': 'water-xishan-jize-mishan',
  'slug': 'mishan',
  'kind': 'water',
  'group': 'natural_features',
  'name': '稷澤（峚山段）',
  'en_name': 'Ji Marsh (Mi passage)',
  'quote': '丹水出焉西流注于稷澤',
  'description': '稷澤是峚山丹水西流所注的泽。后稷神所馮因名云属于郭注命名解释，正文不另述后稷形貌、出生或农耕事迹，不据此定位现代泽地。',
  'en_description': 'Ji Marsh receives Mi’s west-flowing Dan. The Houji naming explanation belongs to commentary, '
                    'without importing his appearance, birth or farming stories into the main text or identifying '
                    'a modern marsh.',
  'en_quote': 'The Dan flows west into Ji Marsh.',
  'art': None,
  'commentary_quote': '后稷神所馮因名云'},
 {'id': 'material-xishan-white-jade-mishan',
  'slug': 'mishan',
  'kind': 'material',
  'group': 'natural_features',
  'name': '白玉（峚山丹水）',
  'en_name': 'White jade (Mi Dan passage)',
  'quote': '丹水出焉西流注于稷澤其中多白玉',
  'description': '白玉见于丹水西注稷澤后的水中记述，与玉膏、𤣥玉、玉榮、瑾瑜分别存卡。不将郭注中的少室白玉膏或金刚石举例当成本段白玉的具体矿物鉴定。',
  'en_description': 'White jade occurs in the Dan water account, separately from jade paste, xuan jade, jade '
                    'blossom and jinyu. Commentary examples from another mountain and diamond are not a mineral '
                    'identification here.',
  'en_quote': 'The Dan flows west into Ji Marsh; its waters contain much white jade.',
  'art': None,
  'relation_scope': 'water'},
 {'id': 'material-xishan-yugao-mishan',
  'slug': 'mishan',
  'kind': 'material',
  'group': 'natural_features',
  'name': '玉膏（峚山段）',
  'en_name': 'Jade paste (Mi passage)',
  'quote': '其中多白玉是有玉膏其源沸沸湯湯黄帝是食是饗是生𤣥玉',
  'description': '玉膏接丹水白玉记述，源沸沸汤汤，黄帝食飨、生成𤣥玉及灌丹木见于正文。郭注引少室山一服即仙是另列注说，不把玉膏等同现代药物或确定化学物质。',
  'en_description': 'Jade paste follows white jade in the water account. Its surging source, Huangdi’s '
                    'consumption, production of xuan jade and irrigation of danmu belong to the main text. The '
                    'commentary’s immortality example remains separate, without a modern substance or medicine '
                    'identification.',
  'en_quote': 'There is jade paste with a surging source. Huangdi partakes of it, and it produces xuan jade.',
  'art': None,
  'commentary_quote': '玉膏涌出之貌也河圖王版曰少室山其上有白玉膏一服即仙矣亦此𩔖也沸音拂',
  'relation_scope': 'water'},
 {'id': 'material-xishan-xuanyu-mishan',
  'slug': 'mishan',
  'kind': 'material',
  'group': 'natural_features',
  'name': '𤣥玉（峚山段）',
  'en_name': 'Xuan jade (Mi passage)',
  'quote': '是生𤣥玉',
  'description': '𤣥玉是正文是生𤣥玉所记之玉，郭注言玉膏中又出黑玉也跨182—183连读。黑玉释义保留在郭注，不擅改底本𤣥字或指定现代矿物成分。',
  'en_description': 'Xuan jade is recorded as produced here. Its gloss, that black jade also emerges within the '
                    'paste, spans units182–183 and remains commentary. The edition character and lack of a modern '
                    'mineral identification are retained.',
  'en_quote': 'It produces xuan jade.',
  'art': None,
  'commentary_quote': '言玉膏中又出黑玉也'},
 {'id': 'material-xishan-yurong-mishan',
  'slug': 'mishan',
  'kind': 'material',
  'group': 'natural_features',
  'name': '玉榮（峚山段）',
  'en_name': 'Jade blossom (Mi passage)',
  'quote': '黃帝乃取峚山之玉榮而投之鍾山之陽',
  'description': '黄帝取峚山玉榮投鍾山之阳，郭注以玉华解释，并引其他文献、以为玉种。玉榮字形照底本，不将其改成植物花实或现代玉石种植方法。',
  'en_description': 'Huangdi takes Mi’s jade blossom and casts it onto Zhong’s sunny side. Commentary explains it '
                    'as jade flower and a jade seed, citing other texts. This does not turn it into botanical '
                    'flowers or a modern method for cultivating jade.',
  'en_quote': 'Huangdi takes Mi’s jade blossom and casts it onto Zhong’s sunny side.',
  'art': None,
  'commentary_quote': '謂玉華也離騷曰懐琬琰之華英又曰登崑崙𠔃食玉英汲冡書所謂苕華之玉；以為玉種'},
 {'id': 'material-xishan-jinyu-mishan',
  'slug': 'mishan',
  'kind': 'material',
  'group': 'natural_features',
  'name': '瑾瑜之玉（峚山段）',
  'en_name': 'Jinyu jade (Mi passage)',
  'quote': '瑾瑜之玉為良堅粟精密濁澤有而光五色發作以和柔剛',
  'description': '瑾瑜被称为良玉，正文记坚粟精密、濁澤有而光、五色发作与和柔刚。郭注分别解释玉理、润厚与符彩，不换成现代硬度、具体矿种；后续君子服之御不祥保留为古籍佩玉说法。',
  'en_description': 'Jinyu is praised for its texture, luster, five colors and balance of qualities. Commentary '
                    'explains the jade grain and rich luster separately. No modern hardness or mineral species is '
                    'supplied; warding off ill fortune remains an ancient wearing claim.',
  'en_quote': 'Jinyu jade is prized for its fine texture, rich luster, five colors and balance of qualities.',
  'art': None,
  'commentary_quote': '言最善也或作食覲两音；玉理也禮記曰瑱密似粟粟或作栗玉有粟文所謂榖璧也；濁謂潤厚；言符彩互映色王子靈符應曰赤如鷄冠黄如蒸栗白如割肪黑如醇漆玉之符彩也；言玉恊九徳也',
  'content_note': '郭注照捕获保留，瑾瑜读音及玉理前說字等有漏字，未猜补；金刚石只在后文郭注举例，不列成本段正文矿物。',
  'en_content_note': 'Captured glosses are retained with omissions in the pronunciation note and before the '
                     'jade-grain explanation. The later diamond example is commentary, not another main-text '
                     'mineral here.'},
 {'id': 'deity-xishan-huangdi-mishan',
  'slug': 'mishan',
  'kind': 'deity',
  'group': 'text_entities',
  'name': '黃帝（峚山段）',
  'en_name': 'Huangdi (Mi passage)',
  'quote': '黄帝是食是饗是生𤣥玉玉膏所出以灌丹木丹木五歲五色乃清五味乃馨黃帝乃取峚山之玉榮而投之鍾山之陽',
  'description': '本段黄帝食飨玉膏，并取峚山玉榮投鍾山之阳。正文黄帝/黃帝两种写法保留，未述其形貌；鼎湖登龙、龙蜕是郭注解释，不作正文事件或现代史实。',
  'en_description': 'Huangdi partakes of jade paste and casts Mi’s jade blossom onto Zhong’s sunny side. Both '
                    'edition spellings remain in the Chinese text, which gives no appearance. Dragon ascent at '
                    'Dinghu is commentary, not an added main-text event or modern historical fact.',
  'en_quote': 'Huangdi partakes of the jade paste and later casts Mi’s jade blossom onto Zhong’s sunny side.',
  'art': None,
  'commentary_quote': '所以得登龍於鼎湖而龍蛻也',
  'appearance_unknown': True},
 {'id': 'deity-xishan-heaven-earth-mishan',
  'slug': 'mishan',
  'kind': 'deity',
  'group': 'text_entities',
  'name': '天地鬼神（峚山段）',
  'en_name': 'Heaven, earth, ghosts and spirits (Mi passage)',
  'quote': '天地鬼神是食是饗',
  'description': '天地鬼神是食是飨接玉的品德记述之后，是一组未展开的称谓，正文没有逐个名称或形貌。鬼据54页补入阅读层，捕获缺字图不改；不据此新造多位神祇形象或具体祭法。',
  'en_description': 'This collective wording follows the jade account without individual names or appearances. '
                    'Gui is restored from scan54 only in the reading layer. No invented divine figures or '
                    'definite ritual procedure are supplied.',
  'en_quote': 'Heaven, earth, ghosts and spirits partake of it.',
  'art': None,
  'commentary_quote': '玉所以祈祭者言動天地感神',
  'appearance_unknown': True,
  'content_note': '郭注捕获省略影印能/鬼等字，保留捕获并明示，正文鬼字已核补，不宣称注文逐字无缺。',
  'en_content_note': 'The captured commentary omits characters visible in the scan and is retained with notice. '
                     'Restoring gui in the main text does not claim a complete commentary transcription.'},
 {'id': 'water-xishan-wetlands-mi-zhong',
  'slug': 'mishan',
  'kind': 'water',
  'group': 'natural_features',
  'name': '泽地（峚至鍾）',
  'en_name': 'Wetlands between Mi and Zhong',
  'quote': '自峚山至于鍾山四百六十里其間盡澤也是多竒鳥怪獸竒魚皆異物焉',
  'description': '峚至鍾四百六十里之间尽是泽地，多竒鳥、怪獸、竒魚。这里是路径间的整体环境记述，不是有专名的一处泽，也不把未详异物放到峚山山顶或画出实测边界。',
  'en_description': 'The 460 li between Mi and Zhong are described as wetlands containing three unnamed groups of '
                    'wondrous creatures. This is an intervening environment, not one named marsh, a summit '
                    'habitat or a measured boundary.',
  'en_quote': 'Between Mi and Zhong are 460 li of wetlands with wondrous birds, strange beasts and wondrous fish.',
  'art': None},
 {'id': 'bird-xishan-birds-mi-zhong',
  'slug': 'mishan',
  'kind': '鸟',
  'group': 'beasts',
  'name': '竒鳥（峚鍾泽间）',
  'en_name': 'Wondrous birds (Mi–Zhong wetlands)',
  'quote': '其間盡澤也是多竒鳥怪獸竒魚皆異物焉',
  'description': '竒鳥是峚至鍾泽间的集合称谓，只记多与皆异物，没有个体名、器官、颜色或能力。不借别山形貌，也不把集称当作已命名的新物种。',
  'en_description': 'Wondrous birds is a collective description in the wetlands between Mi and Zhong, with no '
                    'individual names, forms, colors or powers. It does not identify a new species or import '
                    'appearances from other passages.',
  'en_quote': 'The intervening wetlands contain wondrous birds, strange beasts and wondrous fish, all described '
              'as unusual beings.',
  'art': None,
  'appearance_unknown': True,
  'relation_scope': 'water'},
 {'id': 'beast-xishan-beasts-mi-zhong',
  'slug': 'mishan',
  'kind': '兽',
  'group': 'beasts',
  'name': '怪獸（峚鍾泽间）',
  'en_name': 'Strange beasts (Mi–Zhong wetlands)',
  'quote': '其間盡澤也是多竒鳥怪獸竒魚皆異物焉',
  'description': '怪獸是峚至鍾泽间的集合称谓，只记多与皆异物，没有个体名、器官、颜色或能力。不借别山形貌，也不把集称当作已命名的新物种。',
  'en_description': 'Strange beasts is a collective description in the wetlands between Mi and Zhong, with no '
                    'individual names, forms, colors or powers. It does not identify a new species or import '
                    'appearances from other passages.',
  'en_quote': 'The intervening wetlands contain wondrous birds, strange beasts and wondrous fish, all described '
              'as unusual beings.',
  'art': None,
  'appearance_unknown': True,
  'relation_scope': 'water'},
 {'id': 'beast-xishan-fish-mi-zhong',
  'slug': 'mishan',
  'kind': '鱼',
  'group': 'beasts',
  'name': '竒魚（峚鍾泽间）',
  'en_name': 'Wondrous fish (Mi–Zhong wetlands)',
  'quote': '其間盡澤也是多竒鳥怪獸竒魚皆異物焉',
  'description': '竒魚是峚至鍾泽间的集合称谓，只记多与皆异物，没有个体名、器官、颜色或能力。不借别山形貌，也不把集称当作已命名的新物种。',
  'en_description': 'Wondrous fish is a collective description in the wetlands between Mi and Zhong, with no '
                    'individual names, forms, colors or powers. It does not identify a new species or import '
                    'appearances from other passages.',
  'en_quote': 'The intervening wetlands contain wondrous birds, strange beasts and wondrous fish, all described '
              'as unusual beings.',
  'art': None,
  'appearance_unknown': True,
  'relation_scope': 'water'}]


ENTITIES += [{'id': 'deity-xishan-gu-zhongshan',
  'slug': 'zhongshan',
  'kind': 'deity',
  'group': 'text_entities',
  'name': '皷（鍾山龙身）',
  'en_name': 'Gu, dragon form (Zhong passage)',
  'quote': '其子曰皷其状如人靣而龍身',
  'description': '皷在鍾山段形如人面而龙身，郭注称神名。与欽䲹杀葆江及后续化鵕鸟另有关系；不把郭注丽山之子青羽人面马身比拟改成皷的正文形貌，不补足爪翼或衣饰。',
  'en_description': 'Gu has a human face and dragon body and is called a divine name in commentary. The killing '
                    'and later jun-bird transformation are linked separately. The commentary’s human-faced, '
                    'horse-bodied comparison is not Gu’s main-text form, and no limbs, wings or clothing are '
                    'invented.',
  'en_quote': 'Its child is called Gu, with a human face and dragon body.',
  'art': None,
  'commentary_quote': '此亦神名名之為鍾山之子耳其𩔗皆見㱕蔵啓筮；啓筮曰麗山之子青羽人靣馬身亦似此状也'},
 {'id': 'deity-xishan-qinpi-zhongshan',
  'slug': 'zhongshan',
  'kind': 'deity',
  'group': 'text_entities',
  'name': '欽䲹（鍾山原身）',
  'en_name': 'Qinpi, original form (Zhong passage)',
  'quote': '是與欽䲹殺葆江于崑崙之陽',
  'description': '欽䲹与皷杀葆江，原身没有形貌记述。郭注音邳归䲹，英文用Qinpi；后文大鶚是其变形后的形象，黑文、白首、赤喙、虎爪不倒填原身，也不定为现代人物或动物。',
  'en_description': 'Qinpi joins Gu in killing Baojiang, but the original form is not described. The '
                    'pronunciation gloss supports Qinpi. Black markings, white head, red beak and tiger claws '
                    'belong to the later transformed bird and are not imported into this original form.',
  'en_quote': 'With Qinpi, Gu kills Baojiang on Kunlun’s sunny side.',
  'art': None,
  'commentary_quote': '音邳',
  'appearance_unknown': True},
 {'id': 'deity-xishan-baojiang-zhongshan',
  'slug': 'zhongshan',
  'kind': 'deity',
  'group': 'text_entities',
  'name': '葆江（鍾山段）',
  'en_name': 'Baojiang (Zhong passage)',
  'quote': '殺葆江于崑崙之陽',
  'description': '葆江是皷与欽䲹在崑崙之阳所杀者，正文未写形貌或能力。郭注葆或作祖作为异文分存，不改正文名、不补身份谱系或复活情节。',
  'en_description': 'Baojiang is killed by Gu and Qinpi on Kunlun’s sunny side. No appearance or powers are '
                    'given. The commentary’s Zu variant remains separate, without changing the main name or '
                    'adding a genealogy or resurrection.',
  'en_quote': 'They kill Baojiang on Kunlun’s sunny side.',
  'art': None,
  'commentary_quote': '葆或作祖',
  'appearance_unknown': True},
 {'id': 'deity-xishan-di-zhongshan',
  'slug': 'zhongshan',
  'kind': 'deity',
  'group': 'text_entities',
  'name': '帝（鍾山段·未具名）',
  'en_name': 'Unnamed emperor (Zhong passage)',
  'quote': '帝乃戮之鍾山之東曰𡺯崖',
  'description': '帝在本段随后行戮，记述续至鍾山东的𡺯崖。正文未具帝名或形貌，不直接认作前段黄帝，也不借其他篇章身份补写。',
  'en_description': 'The emperor executes them in an account continuing to Yao Cliff east of Zhong. No name or '
                    'appearance is supplied. The figure is not automatically identified with Huangdi in the '
                    'preceding passage or with rulers elsewhere.',
  'en_quote': 'The emperor executes them; east of Zhong is Yao Cliff.',
  'art': None,
  'appearance_unknown': True},
 {'id': 'bird-xishan-qinpi-e-zhongshan',
  'slug': 'zhongshan',
  'kind': '鸟',
  'group': 'beasts',
  'name': '大鶚（欽䲹所化）',
  'en_name': 'Great e bird, transformed Qinpi',
  'quote': '欽䲹化為大鶚其状如鵰而黑文白首赤喙而虎𤓰其音如晨鵠見則有大兵',
  'description': '欽䲹所化大鶚形如鵰，黑文、白首、赤喙、虎爪，音如晨鵠；见则大兵为古籍灾异。𤓰底本字形保留，鶚鵰与晨鵠注释分列，不据比拟认定现代鹰种，也不反作欽䲹原身形貌。',
  'en_description': 'Qinpi’s transformed great e resembles a diao, with black markings, a white head, red beak '
                    'and tiger claws. Its chenhu-like voice and warfare omen are ancient descriptions. The '
                    'comparisons do not identify a modern eagle species or describe Qinpi’s original form.',
  'en_quote': 'Qinpi becomes a great e bird like a diao, with black markings, a white head, red beak and tiger '
              'claws. Its chenhu-like voice accompanies an omen of war.',
  'art': None,
  'commentary_quote': '鶚鵰属也音鄂；晨鵠鶚属猶云晨鳬耳𫟍曰緤吠犬比奉晨鳬也',
  'content_note': '晨鵠郭注跨0197—0198，𫟍前影印見說而捕获省字，注栏照捕获保留并明示，不移至鵕鸟。',
  'en_content_note': 'The chenhu gloss spans units197–198. The capture omits a character visible before the '
                     'edition’s yuan variant; the captured gloss is retained with notice and is not reassigned to '
                     'the jun bird.'},
 {'id': 'bird-xishan-gu-jun-zhongshan',
  'slug': 'zhongshan',
  'kind': '鸟',
  'group': 'beasts',
  'name': '鵕鳥（皷所化）',
  'en_name': 'Jun bird, transformed Gu',
  'quote': '皷亦化為鵕鳥其状如鴟赤足而直喙黄文而白首其音如鵠見即其邑大旱',
  'description': '皷所化鵕鸟形如鴟，赤足直喙、黄文白首，音如鵠；见则其邑大旱是本鸟灾异，范围与大鶚的大兵分别保留。其字续0199，不丢鴟形或把郭注穆王群兽写入本鸟形貌。',
  'en_description': 'Gu’s transformed jun resembles a chi, with red feet, a straight beak, yellow markings and '
                    'white head, and a hu-like voice. Its settlement-level drought omen remains separate from the '
                    'great e’s warfare omen. The King Mu commentary adds no features to this bird.',
  'en_quote': 'Gu becomes a jun bird like a chi, with red feet, a straight beak, yellow markings and white head. '
              'Its hu-like voice precedes drought in that settlement.',
  'art': None,
  'commentary_quote': '音俊'},
 {'id': 'place-xishan-kunlun-yang-zhongshan',
  'slug': 'zhongshan',
  'kind': 'place',
  'group': 'text_entities',
  'name': '崑崙之陽（鍾山段）',
  'en_name': 'Kunlun’s sunny side (Zhong passage)',
  'quote': '殺葆江于崑崙之陽',
  'description': '崑崙之阳是本段杀葆江的地点，只存这一方位与事件上下文。不将阳面化成现代精确点位，也不借此宣称后续崑崙山段已经完成。',
  'en_description': 'Kunlun’s sunny side is the location of Baojiang’s killing in this passage. This directional '
                    'event context is not a precise modern location or completion of the later Kunlun mountain '
                    'passage.',
  'en_quote': 'They kill Baojiang on Kunlun’s sunny side.',
  'art': None},
 {'id': 'place-xishan-yaoya-zhongshan',
  'slug': 'zhongshan',
  'kind': 'place',
  'group': 'text_entities',
  'name': '𡺯崖（鍾山之东）',
  'en_name': 'Yao Cliff (east of Zhong)',
  'quote': '帝乃戮之鍾山之東曰𡺯崖',
  'description': '𡺯崖见于帝乃戮之之后，正文记鍾山之东，郭注音遥。保留罕字与上下文，不另补山崖形状、现代坐标或未写出的刑罚方式。',
  'en_description': 'Yao Cliff follows the execution statement and is east of Zhong; commentary gives its '
                    'pronunciation. The edition character and context remain without an invented cliff shape, '
                    'modern coordinates or method of punishment.',
  'en_quote': 'The emperor executes them; east of Zhong is Yao Cliff.',
  'art': None,
  'commentary_quote': '音遥'}]


ENTITIES += [{'id': 'water-xishan-guan-taiqi',
  'slug': 'taiqi',
  'kind': 'water',
  'group': 'natural_features',
  'name': '𮗚水（㤗噐段）',
  'en_name': 'Guan River (Taiqi passage)',
  'art': None,
  'quote': '𮗚水出焉西流注于流沙',
  'description': '𮗚水从㤗噐山流出，向西注于流沙。保留𮗚字，不据异体或同音合并其他观水、灌水；本段没有现代河道、源点坐标或水速资料。',
  'en_description': 'The Guan rises at Taiqi and flows west into Liusha. The edition character is retained '
                    'without merging namesake Guan waters elsewhere or adding a modern course, source coordinates '
                    'or flow speed.',
  'en_quote': 'The Guan River rises here and flows west into Liusha.'},
 {'id': 'place-xishan-liusha',
  'slug': 'taiqi',
  'kind': 'place',
  'group': 'text_entities',
  'name': '流沙（㤗噐段）',
  'en_name': 'Liusha (Taiqi passage)',
  'art': None,
  'quote': '𮗚水出焉西流注于流沙',
  'description': '流沙是本段𮗚水西流所注的地点，流字在0203末、沙字续0204首。这里只保存正文称谓和承接关系，不指定现代沙漠边界、不补水体形制；后文同名流沙待核时再增加出处。',
  'en_description': 'Liusha is the destination of the west-flowing Guan. Its name spans units203–204. The record '
                    'retains the textual name and receiving relationship without a modern desert boundary or an '
                    'invented water-body form; later namesake references remain to be reviewed.',
  'en_quote': 'The Guan flows west into Liusha.'},
 {'id': 'beast-xishan-wenyao-taiqi',
  'slug': 'taiqi',
  'kind': '鱼',
  'group': 'beasts',
  'name': '文鰩魚（㤗噐段）',
  'en_name': 'Wenyao fish (Taiqi passage)',
  'art': None,
  'quote': '是多文鰩魚状如鯉魚魚身而鳥翼蒼文而白首赤喙常行西海遊於東海以夜飛其音如鸞雞其味酸甘食之已狂見則天下大穰',
  'description': '文鰩魚形如鲤，鱼身鸟翼，苍文、白首、赤喙，常行西海而游东海、夜飞，音如鸞雞。正文没有把它认作现代飞鱼或鰩类；鸞雞未详、欒异文与丰穰释义分别归郭注，古籍食用说法不扩为现代诊疗。',
  'en_description': 'Wenyao is carp-like, with a fish’s body and bird wings, blue-green markings, white head and '
                    'red beak. It frequents the Western Sea, travels in the Eastern Sea and flies at night, with '
                    'a luanji-like voice. No modern flying-fish or ray species is identified. Glosses and the '
                    'ancient eating claim remain separate from modern medical practice.',
  'en_quote': 'Wenyao fish are carp-like, with a fish’s body and bird wings, blue-green markings, white head and '
              'red beak. They frequent the Western Sea, travel in the Eastern Sea and fly at night, with a '
              'luanji-like voice. Their taste is sour and sweet; eating them is said to relieve kuang, and their '
              'appearance to herald abundant harvests.',
  'commentary_quote': '音遥；鸞雞鳥名未詳也或作欒；豐穰收熟也韓子曰穰嵗之秋',
  'relation_scope': 'water',
  'art_reference': ['统一留空形象 · 文鰩魚插画未生成，问号剪影不代表鱼身鸟翼的原文形貌。',
                    'Shared placeholder · Wenyao has not been illustrated; the silhouette does not depict its '
                    'fish body and bird wings.']},
 {'id': 'water-xishan-eastsea-taiqi',
  'slug': 'taiqi',
  'kind': 'water',
  'group': 'natural_features',
  'name': '東海（㤗噐段）',
  'en_name': 'Eastern Sea (Taiqi passage)',
  'art': None,
  'quote': '常行西海遊於東海以夜飛',
  'description': '東海是本段文鰩魚所游之海，与常行西海、夜飞并列保存。经文未给两海边界、往返时刻或实测路线；不直接合并南山经同名东海，也不把夜飞扩大为海中所有生物的行为。',
  'en_description': 'The Eastern Sea is where Wenyao travels, alongside its Western Sea activity and night '
                    'flight. No boundaries, travel schedule or measured route are given. The namesake Southern '
                    'sea stays separate, and the fish’s behavior is not assigned to all marine life.',
  'en_quote': 'Wenyao frequents the Western Sea, travels in the Eastern Sea and flies at night.'}]


ENTITIES += [{'id': 'water-xishan-qiushi-huaijiang',
  'slug': 'huaijiang',
  'kind': 'water',
  'group': 'natural_features',
  'name': '丘時之水（槐江段）',
  'en_name': 'Qiushi River (Huaijiang passage)',
  'quote': '丘時之水出焉而北流注于泑水其中多蠃母',
  'description': '丘時水自槐江出，向北注泑水，水中多蠃母。保留丘時底本名，不换成其他同音水名，不把后文山上矿物都移入水中。',
  'en_description': 'The Qiushi rises at Huaijiang and flows north into the You, with luomu in the water. Its '
                    'edition name and water context remain without importing the following mountain minerals.',
  'en_quote': 'The Qiushi rises here and flows north into the You, containing many luomu.',
  'art': None},
 {'id': 'beast-xishan-luomu-huaijiang',
  'slug': 'huaijiang',
  'kind': '水族',
  'group': 'beasts',
  'name': '蠃母（槐江水中）',
  'en_name': 'Luomu (Huaijiang waters)',
  'quote': '其中多蠃母',
  'description': '蠃母见于丘時水文，郭注即䗱螺也，正文未述器官、颜色或能力。作为水中生物集称保存，不借后文蠃母山名补成神祇，也不指定现代螺种。',
  'en_description': 'Luomu occurs in the river account and is glossed as a kind of luo. The main text supplies no '
                    'form, color or powers; this water creature is not turned into a deity from the later '
                    'namesake mountain.',
  'en_quote': 'Its waters contain many luomu.',
  'art': None,
  'commentary_quote': '即䗱螺也',
  'appearance_unknown': True,
  'relation_scope': 'water'},
 {'id': 'material-xishan-qingxionghuang-huaijiang',
  'slug': 'huaijiang',
  'kind': 'material',
  'group': 'natural_features',
  'name': '青雄黃（槐江山上）',
  'en_name': 'Qing xionghuang (above Huaijiang)',
  'quote': '其上多青雄黃',
  'description': '山上多青雄黃，连写保留。不借皇人山郭注拆定石青与雄黄，也不扩为现代矿物或开采记录。',
  'en_description': 'Qing xionghuang is abundant above. The unpunctuated grouping stays intact without importing '
                    'Huangren’s gloss or fixing a modern mineral or mining activity.',
  'en_quote': 'Qing xionghuang is abundant above.',
  'art': None},
 {'id': 'material-xishan-langgan-huaijiang',
  'slug': 'huaijiang',
  'kind': 'material',
  'group': 'natural_features',
  'name': '藏琅玕（槐江段）',
  'en_name': 'Hidden langgan (Huaijiang passage)',
  'quote': '多蔵琅玕黄金玉',
  'description': '琅玕见多藏琅玕黄金玉，郭注石似珠、藏犹隐及音注分存，不把珠状解释直接认定为某种现代宝石。',
  'en_description': 'Langgan occurs in the hidden-goods phrase. Commentary compares it to pearl-like stone and '
                    'explains hidden, without a modern gemstone identification.',
  'en_quote': 'Hidden langgan, gold and jade are abundant.',
  'art': None,
  'commentary_quote': '琅玕石似珠者蔵猶𨼆也郎干二音'},
 {'id': 'material-xishan-gold-above-huaijiang',
  'slug': 'huaijiang',
  'kind': 'material',
  'group': 'natural_features',
  'name': '黄金（槐江山上）',
  'en_name': 'Gold (above Huaijiang)',
  'quote': '多蔵琅玕黄金玉',
  'description': '黄金见于山上藏琅玕黄金玉一组，与阴面采黄金銀及大澤玉分别存出处，不造器物或现代采矿地点。',
  'en_description': 'Gold is retained in the upper hidden-goods group, separately from the shaded-side wording '
                    'and Great Marsh jade, without invented objects or mining sites.',
  'en_quote': 'Hidden langgan, gold and jade are abundant.',
  'art': None},
 {'id': 'material-xishan-jade-above-huaijiang',
  'slug': 'huaijiang',
  'kind': 'material',
  'group': 'natural_features',
  'name': '玉（槐江山上）',
  'en_name': 'Jade (above Huaijiang)',
  'quote': '多蔵琅玕黄金玉',
  'description': '玉见于山上藏琅玕黄金玉一组，与阴面采黄金銀及大澤玉分别存出处，不造器物或现代采矿地点。',
  'en_description': 'Jade is retained in the upper hidden-goods group, separately from the shaded-side wording '
                    'and Great Marsh jade, without invented objects or mining sites.',
  'en_quote': 'Hidden langgan, gold and jade are abundant.',
  'art': None},
 {'id': 'material-xishan-dansu-huaijiang',
  'slug': 'huaijiang',
  'kind': 'material',
  'group': 'natural_features',
  'name': '丹粟（槐江阳面）',
  'en_name': 'Dansu (sunny Huaijiang)',
  'quote': '其陽多丹粟',
  'description': '丹粟归槐江阳面，不移到丘時水或西望大澤，不借其他山的同名物产注释定成现代矿种。',
  'en_description': 'Dansu belongs to the sunny side, not the river or western marsh, and receives no imported '
                    'modern mineral identification.',
  'en_quote': 'Dansu is abundant on its sunny side.',
  'art': None},
 {'id': 'material-xishan-shaded-goods-huaijiang',
  'slug': 'huaijiang',
  'kind': 'material',
  'group': 'natural_features',
  'name': '采黄金銀（槐江阴面）',
  'en_name': 'Shaded-side goods (Huaijiang)',
  'quote': '其隂多采黄金銀',
  'description': '阴面多采黄金銀保留整组未断句记述。采不直接改作采矿动作，也不据此虚构矿坑或确定彩石种类。',
  'en_description': 'The shaded-side cai huangjin yin wording remains one unpunctuated group. Cai is not silently '
                    'turned into mining or a definite colored-stone species.',
  'en_quote': 'The shaded side has the wording cai huangjin yin.',
  'art': None},
 {'id': 'place-xishan-pingpu-huaijiang',
  'slug': 'huaijiang',
  'kind': 'place',
  'group': 'text_entities',
  'name': '帝之平圃（槐江段）',
  'en_name': 'Emperor’s level garden (Huaijiang)',
  'quote': '實惟帝之平圃神英招司之',
  'description': '帝之平圃由英招司掌；郭注𤣥圃及穆天子传引文另列，不给帝补具体名字，也不与崑崙下都自动合为同一地点。',
  'en_description': 'Yingzhao oversees the emperor’s level garden. The Xuanpu gloss and King Mu citation remain '
                    'commentary, without naming the emperor or automatically merging this garden with Kunlun’s '
                    'lower capital.',
  'en_quote': 'This is the emperor’s level garden, overseen by Yingzhao.',
  'art': None,
  'commentary_quote': '即𤣥圃也穆天子傳曰乃為銘迹於𤣥圃之上謂刋石紀功徳如秦皇漢武之為者也'},
 {'id': 'deity-xishan-yingzhao-huaijiang',
  'slug': 'huaijiang',
  'kind': 'deity',
  'group': 'text_entities',
  'name': '英招（槐江段）',
  'en_name': 'Yingzhao (Huaijiang passage)',
  'quote': '神英招司之其状馬身而人靣虎文而鳥翼徇于四海其音如榴',
  'description': '英招司平圃，马身人面、虎文鸟翼，徇四海，音如榴。人面不写成虎首，虎文不改虎身，未加经文之外的角与足翼。榴音注和异文跨213—214另列。',
  'en_description': 'Yingzhao oversees the garden, with a horse’s body, human face, tiger markings and bird '
                    'wings. It circles the four seas and sounds like liu. The face is not a tiger’s, and no extra '
                    'horns or limbs are added.',
  'en_quote': 'Yingzhao oversees it, with a horse’s body, human face, tiger markings and bird wings, circling the '
              'four seas and sounding like liu.',
  'art': None,
  'commentary_quote': '司主也；徇謂周行也；音留或作籕此所未詳也'},
 {'id': 'place-xishan-kunlun',
  'slug': 'huaijiang',
  'kind': 'place',
  'group': 'text_entities',
  'name': '崑崙（槐江南望）',
  'en_name': 'Kunlun (Huaijiang southern view)',
  'quote': '南望崑崙其光熊熊其氣魂魂',
  'description': '南望崑崙并记光熊熊、气魂魂；郭注释光气炎盛之貌。这里只存槐江眺望上下文，后续崑崙主段尚未完成，不加入现代位置。',
  'en_description': 'Kunlun is seen to the south with luminous light and vapor. The commentary explains the '
                    'appearance. This documents the view only, ahead of Kunlun’s own unfinished passage, without '
                    'a modern position.',
  'en_quote': 'To the south is Kunlun, with brilliant light and vapor.',
  'art': None,
  'commentary_quote': '皆光氣炎盛相焜燿之貌'},
 {'id': 'water-xishan-daze-huaijiang',
  'slug': 'huaijiang',
  'kind': 'water',
  'group': 'natural_features',
  'name': '大澤（槐江西望）',
  'en_name': 'Great Marsh (Huaijiang western view)',
  'quote': '西望大澤后稷所潜也其中多玉其隂多榣木之有若',
  'description': '西望大澤，后稷所潜，其中多玉、阴多榣木之有若。只是本段称谓，不把大澤当唯一现代湖名，不与稷澤或泑澤合并。',
  'en_description': 'The western Great Marsh is where Houji remains hidden, with jade and the shaded-side tree '
                    'wording. This contextual designation is not a unique modern lake or an automatic merger with '
                    'Ji or You Marsh.',
  'en_quote': 'To the west is the Great Marsh where Houji remains hidden, with jade and the shaded-side tree '
              'account.',
  'art': None},
 {'id': 'deity-xishan-houji-huaijiang',
  'slug': 'huaijiang',
  'kind': 'deity',
  'group': 'text_entities',
  'name': '后稷（槐江西望）',
  'en_name': 'Houji (Huaijiang western view)',
  'quote': '西望大澤后稷所潜也',
  'description': '后稷见于西望大澤所潜的正文，未写形貌。生而灵知、终化形为神及箕尾比拟来自郭注，不另补出生或农耕事迹。',
  'en_description': 'Houji appears in the marsh statement without an appearance. Spiritual knowledge, '
                    'transformation and the constellation comparison belong to commentary, not added birth or '
                    'farming episodes.',
  'en_quote': 'The Great Marsh is where Houji remains hidden.',
  'art': None,
  'commentary_quote': '后稷生而靈知及其終化形遯此澤而為之神亦猶傳𮪍箕尾也',
  'appearance_unknown': True},
 {'id': 'material-xishan-jade-daze-huaijiang',
  'slug': 'huaijiang',
  'kind': 'material',
  'group': 'natural_features',
  'name': '玉（槐江西望大澤）',
  'en_name': 'Jade (Huaijiang Great Marsh)',
  'quote': '西望大澤后稷所潜也其中多玉',
  'description': '玉归大澤其中多玉，不与槐江山上玉合卡，不擅加色泽或具体矿物。',
  'en_description': 'This jade belongs to the Great Marsh context, separately from jade above Huaijiang, without '
                    'an invented color or mineral identity.',
  'en_quote': 'The Great Marsh contains much jade.',
  'art': None,
  'relation_scope': 'water'},
 {'id': 'plant-xishan-yaomu-ruo-huaijiang',
  'slug': 'huaijiang',
  'kind': 'plant',
  'group': 'natural_features',
  'name': '榣木之有若（槐江西望）',
  'en_name': 'Yaomu and ruo wording (Huaijiang view)',
  'quote': '其隂多榣木之有若',
  'description': '榣木之有若归大澤阴面，保留未断句措辞。郭注大木/复生若木及引书跨216—217，不作现代树种鉴定，也不将正文改写成确定植物结构图。',
  'en_description': 'The yaomu zhi you ruo wording belongs to the marsh’s shaded side. The large-tree and ruo '
                    'explanations continue across units and remain commentary, without a modern species or '
                    'definite botanical reconstruction.',
  'en_quote': 'Its shaded side has abundant yaomu zhi you ruo.',
  'art': None,
  'commentary_quote': '榣木大木也言其上復生若木大木之竒靈者為若見尸子國語曰榣木不生花也',
  'relation_scope': 'water'},
 {'id': 'deity-xishan-lilun-huaijiang',
  'slug': 'huaijiang',
  'kind': 'deity',
  'group': 'text_entities',
  'name': '槐鬼離侖（槐江北望）',
  'en_name': 'Huai-gui Lilun (Huaijiang northern view)',
  'quote': '北望諸毗槐鬼離侖居之',
  'description': '槐鬼離侖居諸毗，郭注離侖其神名，正文没有形貌。槐字不拆成另一株槐树，鬼只据影印补阅读层，不借英招或牛状天神形貌。',
  'en_description': 'Huai-gui Lilun dwells at Zhupi; commentary calls Lilun a divine name. No appearance is '
                    'given, and Huai is not split into another tree or supplied with another deity’s features.',
  'en_quote': 'To the north is Zhupi, where Huai-gui Lilun dwells.',
  'art': None,
  'commentary_quote': '離侖其神名',
  'appearance_unknown': True},
 {'id': 'bird-xishan-ying-huaijiang',
  'slug': 'huaijiang',
  'kind': '鸟',
  'group': 'beasts',
  'name': '鷹（槐江北望）',
  'en_name': 'Ying birds (Huaijiang northern view)',
  'quote': '鷹鸇之所宅也',
  'description': '鷹见于諸毗所宅的鸟类记述，正文未展开形貌。鸇及鴟属等郭注另存，不据此指定现代物种或借其他篇章体色。',
  'en_description': 'Ying birds occurs in the Zhupi habitation statement without a main-text appearance. '
                    'Commentary comparisons do not identify a modern species or import colors from elsewhere.',
  'en_quote': 'Zhupi is inhabited by ying and zhan birds.',
  'art': None,
  'appearance_unknown': True},
 {'id': 'bird-xishan-zhan-huaijiang',
  'slug': 'huaijiang',
  'kind': '鸟',
  'group': 'beasts',
  'name': '鸇（槐江北望）',
  'en_name': 'Zhan birds (Huaijiang northern view)',
  'quote': '鷹鸇之所宅也',
  'description': '鸇见于諸毗所宅的鸟类记述，正文未展开形貌。鸇及鴟属等郭注另存，不据此指定现代物种或借其他篇章体色。',
  'en_description': 'Zhan birds occurs in the Zhupi habitation statement without a main-text appearance. '
                    'Commentary comparisons do not identify a modern species or import colors from elsewhere.',
  'en_quote': 'Zhupi is inhabited by ying and zhan birds.',
  'art': None,
  'appearance_unknown': True,
  'commentary_quote': '鸇亦鴟属也莊周曰鴟鴉甘鼠穆天子傳云鍾山上有白鳥青雕皆此族𩔗也'},
 {'id': 'place-xishan-danshan-huaijiang',
  'slug': 'huaijiang',
  'kind': 'place',
  'group': 'text_entities',
  'name': '怛山（槐江东望）',
  'en_name': 'Eastern-view mountain (edition name)',
  'quote': '東望怛山四成有窮鬼居之各在一摶',
  'description': '东望怛山四成，有窮鬼各居一摶；郭注成亦重、摶犹胁，均另列。怛字依底本保留，不改认现代恒山，不以四成增造四座主线山。',
  'en_description': 'The eastern-view mountain has four tiers and Youqiong spirits on its sides. Commentary explains '
                    'the tier and side terms. The edition name is not identified with modern Mount Heng or split '
                    'into four route mountains.',
  'en_quote': 'To the east is a four-tiered mountain in the eastern view, with Youqiong spirits dwelling on its sides.',
  'art': None,
  'commentary_quote': '成亦重也爾雅云𠕂成曰英也'},
 {'id': 'deity-xishan-youqiong-huaijiang',
  'slug': 'huaijiang',
  'kind': 'deity',
  'group': 'text_entities',
  'name': '有窮鬼（槐江东望）',
  'en_name': 'Youqiong spirits (Huaijiang eastern view)',
  'quote': '有窮鬼居之各在一摶',
  'description': '有窮鬼是怛山各在一摶的集体称谓，郭注称其总号。正文未给个体名或形貌，不拆成四位具名神，不补后羿等别篇人物。',
  'en_description': 'Youqiong spirits are a collective designation on the mountain’s sides; commentary calls it a '
                    'group name. No individual names or forms are given, and no unrelated figures are imported.',
  'en_quote': 'Youqiong spirits dwell there, each on a mountain side.',
  'art': None,
  'commentary_quote': '猶脅也言群各以𩔗聚處山四脅有窮其惣號耳一作',
  'appearance_unknown': True},
 {'id': 'water-xishan-flowing-huaijiang',
  'slug': 'huaijiang',
  'kind': 'water',
  'group': 'natural_features',
  'name': '滛水（槐江东望）',
  'en_name': 'Flowing water (Huaijiang eastern view)',
  'quote': '爰有滛水其清洛洛',
  'description': '爰有滛水、其清洛洛保留底本措辞。郭注水留下之貌也音遥也分存，未据此认定专有水名或现代河道。',
  'en_description': 'The edition’s water wording and its clarity are retained. The gloss describes flowing water '
                    'and gives a pronunciation; it does not establish a definite proper river name or modern '
                    'course.',
  'en_quote': 'There is flowing water, clear and sparkling.',
  'art': None,
  'commentary_quote': '水留下之貌也音遥也'},
 {'id': 'deity-xishan-ox-eight-huaijiang',
  'slug': 'huaijiang',
  'kind': 'deity',
  'group': 'text_entities',
  'name': '未名天神（槐江末段）',
  'en_name': 'Unnamed heavenly deity (Huaijiang closing account)',
  'quote': '有天神焉其状如牛而八足二首馬尾其音如勃皇見則其邑有兵',
  'description': '此天神未具名，牛状、八足二首马尾，音如勃皇，见则其邑有兵。勃皇未详属郭注；与英招分卡，不加虎文鸟翼或其他未述器官。',
  'en_description': 'This unnamed deity resembles an ox, with eight feet, two heads and a horse’s tail. Its '
                    'bohuang-like voice and warfare omen remain textual accounts. It is separate from Yingzhao '
                    'and gains no tiger markings or wings.',
  'en_quote': 'An unnamed heavenly deity resembles an ox, with eight feet, two heads and a horse’s tail, sounding '
              'like bohuang; its appearance is an omen of warfare in that settlement.',
  'art': None,
  'commentary_quote': '勃皇未詳'}]


from xishan_completion import extend, finish, REUSE

extend(ROWS, ENTITIES, PAGE_CORRECTIONS)


def build():
    snapshot = read('data/shanhaijing-reference.json')
    chapter = snapshot['chapters'][1]
    lines = chapter['lines']
    world, en = read('frontend/public/data/myth-world.json'), read('frontend/src/locale-content-en.json')
    manifest_path = ROOT / 'frontend/artwork-source/xishan/generation.json'
    jobs = {a['name']: a for a in read(manifest_path)['assets']} if manifest_path.exists() else {}
    jobs_by_entry = {a['entry_id']: a for a in jobs.values() if a.get('entry_id')}
    retained_art = {r['id']: r.get('artwork') for group in ['beasts', 'text_entities'] for r in world[group]}
    passages, records, relations = [], [], []

    def artwork(record, translation, name):
        job = jobs_by_entry.get(record['id'])
        if job:
            name = job['name']
        elif record['id'] in REUSE and retained_art.get(REUSE[record['id']]):
            record.update(artwork=retained_art[REUSE[record['id']]], artwork_caption=ART_CAPTION)
            translation['artwork_caption'] = EN_ART_CAPTION
            return
        if not name:
            record['artwork_pending'] = True
            return
        caption = SCENE_CAPTION if name.startswith('scene-') else ART_CAPTION
        translation['artwork_caption'] = EN_SCENE_CAPTION if name.startswith('scene-') else EN_ART_CAPTION
        job = jobs.get(name)
        if job and job['status'] == 'reviewed':
            assert (manifest_path.parent / job['source_file']).is_file(), name
            record.update(artwork=f'xishan/{name}-v1.webp', artwork_caption=caption)
        else:
            record.update(artwork_pending=True, planned_artwork=f'xishan/{name}-v1.webp')

    for order, row in enumerate(ROWS, 1):
        slug = row['slug']
        batch = row.get('batch', BATCH)
        first, last = row['units']
        refs = [(f'source-02-{i+1:04}', lines[i]) for i in range(first-1, last)]
        pages = sorted({PAGE_CORRECTIONS.get(id, int(line['page'].rsplit('/', 1)[-1])) for id, line in refs})
        urls = [f'https://zh.wikisource.org/wiki/Page:Sibu_Congkan0465-郭璞-山海經-2-1.djvu/{p}' for p in pages]
        passage_id, place_id = f'passage-xishan-{slug}', f'place-xishan-{slug}'
        captured = ''.join(line['text'] for _, line in refs)
        raw = captured.replace('⟦缺字图:南⟧', '南') if slug == 'zhushan' else captured
        for before, after in row.get('text_replacements', {}).items():
            raw = raw.replace(before, after)
        if slug == 'xiaoci':
            raw = raw.replace('如猿', '如猨')
        if slug == 'bozhong':
            raw = raw.replace('⟦缺字图:囂⟧', '囂')
        if slug == 'huangshan':
            raw = raw.replace('⟦缺字图:能⟧', '能')
        common = {
            'source': SOURCE, 'source_chapter': '《西山经》', 'source_book': 2, 'region': '西山经',
            'source_locator': '卷第二 · 影印页 ' + '、'.join(map(str, pages)),
            'source_pages': urls, 'url': urls[0], 'source_unit_ids': [id for id, _ in refs],
            'reveal_chapter': '03', 'content_batch': batch, 'review_status': 'facsimile_reviewed',
            'direction': '按《西山经》篇内次序与原文方位阅读；不换算现代坐标或实测里程。',
            'editorial_note': '经文据影印核对，保留底本异体字与未标点形式；白话和英文为项目整理。郭注分列，食用、治病、仙人与灾异均为古籍记述。',
        }
        translation = {
            'source': EN_SOURCE, 'source_chapter': 'Xishan Jing', 'region': 'Xishan Jing',
            'source_locator': 'Volume 2 · scan pages ' + ', '.join(map(str, pages)),
            'direction': 'Read the textual sequence and directions; these are not modern coordinates or measured distances.',
            'editorial_note': 'The Chinese transcription was compared with the scans; variant characters and unpunctuated form are retained. Explanations and English are editorial. Commentary is separate; uses, immortals and omens are ancient textual accounts.',
        }
        passage = {
            **common, 'id': passage_id, 'kind': 'passage', 'name': row['name'], 'range': row.get('range', 1), 'order': order,
            'description': row['description'], 'quote': raw, 'captured_text': captured,
            'commentary_quote': '\n'.join(f'〔影印页{PAGE_CORRECTIONS.get(id, int(line["page"].rsplit("/", 1)[-1]))}〕' + '；'.join(line['annotations']).replace('\ufffd', '〔录文缺字待核〕').replace('音；今漆水', '音〔录文缺字待核〕；今漆水') for id, line in refs if line['annotations']),
            'source_span': [sum(len(l['text']) for l in lines[:first-1]), sum(len(l['text']) for l in lines[:last])],
            'related_entry_ids': [] if row.get('is_summary') else [place_id], 'subjects': row['subjects'],
        }
        en[passage_id] = {**translation, 'name': row['en_name'], 'description': row['en_description'], 'quote': row['en_quote']}
        if row.get('content_note'):
            passage['content_note'] = row['content_note']
            en[passage_id]['content_note'] = row['en_content_note']
        if slug == 'daci':
            passage['content_note'] = '0139—0140均见49页，阴面其隂与多碧跨行连读；0141薰吳另段。堊郭注似土色甚白音惡只释堊，不归碧或两兽；麢羊与羬羊区分，㸲牛/麢羊只列名，不借别山形貌。'
            en[passage_id]['content_note'] = 'Units139–140 are on scan49; the shaded-side bi phrase continues across lines. Unit141 begins Xunwu. The soil-like white gloss and pronunciation belong only to e, not bi or the beasts. Lingyang remains distinct from Qianyang; neither beast inherits forms from other passages.'
        if slug == 'xiaoci':
            passage['content_note'] = '0136—0138核49页；0137影印猨、快照猿，阅读引文补作猨而captured_text及快照不改。0138只有朱厭郭注而无正文，不丢弃；0139大次另段。白玉归上、赤銅归下，朱厭猿状白首赤足与見則大兵正文保留，两种一作异文另列。此段无水文，不据山名或兵事补现代坐标与史实。'
            en[passage_id]['content_note'] = 'Units136–138 are on scan49. The scan has yuan (U+7328) where unit137 captures the variant U+733F; only the reading quotation is corrected, with captured text and snapshot retained. Unit138 contains only Zhuyan commentary and is retained. Unit139 begins Daci. White jade above, red copper below and Zhuyan’s form and omen remain main text; the two alternative wordings stay in commentary. No waterway, modern coordinates or historical event is added.'
        if slug == 'niaowei':
            passage['content_note'] = '0133—0135均见48页，0135其中多丹粟捕获49页但实际在48页末列，原快照保留；0136小次另段。0134所附楮即榖木解释前行楮，未詳释女牀，二注不可混同。女牀仅存未定性索引，不移入女牀山或任何生物形象。'
            en[passage_id]['content_note'] = 'Units133–135 are on scan48;135 was captured as49 but appears in the last column of48. The snapshot is retained and136 begins Xiaoci. The chu gloss in134 explains the preceding line, while unexplained belongs to nvchuang. The latter remains an unclassified index item, not Mount Nvchuang or a creature.'
        if slug == 'lutai':
            passage['content_note'] = '0130—0132均在影印48页，0130末其下多与0131首銀连读；0133鳥危另段。今在上郡属山名郭注，豪貆猪也只释白豪；鳬徯其名自呌也照底本保留，不擅改其鳴。㸲牛与羬羊只列名，不移入别山形貌或功效。'
            en[passage_id]['content_note'] = 'Units130–132 are on scan48; silver joins130 to131. Unit133 begins Niaowei. Shangjun is a mountain-name gloss, while the hao gloss belongs only to Baihao. The edition wording its name cries itself is retained, without silently changing the Chinese character. Name-only beasts do not inherit forms or uses from other passages.'
        if slug == 'longshou':
            passage['content_note'] = '0128—0129均见影印48页，128末苕与129首水连读；0130鹿臺另段。龍首、鐡、羙依底本保留；本段无郭注，不从山名推导生物。'
            en[passage_id]['content_note'] = 'Units128–129 are on scan48; Tiao at the end of128 joins water at the start of129. Unit130 begins Lutai. Edition forms remain unchanged; this passage has no captured commentary and its name does not establish a creature.'
        if slug == 'nvchuang':
            passage['content_note'] = '0124—0126实际见47页，126捕获48页但其状如翟至名曰及翟注仍在47页末；127鸞鳥续48页，128龙首另段。石𣵀郭注附在125单元但解释前句矿物，不归虎豹犀兕；旧注舊与鵉之间快照省字，保留录文并明示。不因女牀山名补神祇或床具。'
            en[passage_id]['content_note'] = 'Units124–126 are on scan47, despite126 being captured as48. Unit127 continues Luan on48;128 starts Longshou. The stone gloss attached to125 belongs to the preceding mineral, not the beasts. A character is omitted in the captured older Luan gloss; it is retained without claiming completeness. No deity or bed is inferred from the mountain name.'
        if slug == 'gaoshan':
            passage['content_note'] = '0120—0123均在影印47页，0124女牀另段。碧亦玉𩔗与也今越嶲㑹稽縣東山出碧跨120—121连读；今涇水出安定与朝那縣西井頭山至京兆髙陵縣入渭也跨122—123连读，分别归青碧与涇水郭注。山下青碧与水文青碧分别列卡；涇水东流不改北流，髙、㯶、涇、濵等底本字形保留。'
            en[passage_id]['content_note'] = 'Units120–123 are on scan47;124 begins Nvchuang. The jade-class gloss continues across120–121, and the Jing place-name gloss across122–123. These remain jade and river commentary respectively. Mountain-side and water-context qingbi have separate cards. The eastward flow and edition characters are retained.'
        if slug == 'shuli':
            passage['content_note'] = '0117起句至其下多实际在46页末，虽捕获47页；47页从銀续，0119止于多珠及郭注，0120高山另段。楚水南流明确，不改成北流；鸚䳇仅列名，不借黄山形貌。珠注今蜀郡平澤出青珠尸子曰水員折者有珠保留录文，不冒称多版本校勘定本。'
            en[passage_id]['content_note'] = 'Unit117 is at the end of scan46 despite being captured as47. Scan47 continues with silver; unit119 ends with pearls and commentary, while120 starts Gao. The Chu flows south; Yingmu is only named. The captured pearl commentary remains unchanged rather than claiming a critical edition.'
        if slug == 'taimao':
            passage['content_note'] = '本段0114—0116全见影印46页，止于白蛇；0117起數歴另段。㤗冐、鐡、浴按底本保留，山名或作秦、藻玉注或作柬音練、水蛇注均另列。河只作本段承接水域，不补现代坐标；白蛇配图未生成，仅用统一留空图。'
            en[passage_id]['content_note'] = 'Units114–116 are on scan46 and end with white snakes; unit117 begins the next mountain. Edition forms, mountain-name variants, the jade gloss and water-snake commentary remain separate. The He is a contextual receiving water, without modern coordinates. White snakes currently use only the shared placeholder.'
        if slug == 'qianshan':
            passage['content_note'] = '本段source-02-0112—0113均见影印46页，从西次二經之首起，止于杻橿；下一句西二百里属于太冐山，不并入本段。山名鈐及杻橿底本字形保留，音髠鉗之鉗或作冷又作塗按录文存于郭注；不以异写判定现代地名。'
            en[passage_id]['content_note'] = 'Units112–113 are on scan46, from the second-range heading through niu and jiang. The following two-hundred-li statement belongs to the next mountain. Edition characters and the captured pronunciation and variant-name gloss remain unchanged, without a modern location claim.'
        if slug == 'zhushan':
            passage['content_note'] = '影印38页核定缺字图为“南”；阅读引文补作东南流，captured_text及电子快照保留原始缺字图标记。郭注另排，不将注文中的射物情节画成经文事实。'
            en[passage_id]['content_note'] = 'The image glyph was checked as south on scan page 38. The reading quotation restores southeast; captured_text and the snapshot retain the original placeholder. Commentary remains separate.'
        artwork(passage, en[passage_id], None if row.get('is_summary') else 'scene-' + slug)
        if slug == 'bozhong':
            passage['content_note'] = '影印41页确认缺字图为囂，只修复阅读引文；captured_text与快照保留原标记。单元0072正文仍在41页，42页从多白翰续接。山名保留嶓冡字形，郭注嶓音波。白翰、羆的形貌注明来自郭注；犀兕熊等只列名，配图不补造其身体特征。'
            en[passage_id]['content_note'] = 'The image glyph was checked as Xiao on scan page 41 and restored only in the reading quotation. The captured text and snapshot retain the placeholder. Unit 72 remains on page 41; page 42 continues with Baihan. The source mountain spelling and Guo Pu’s pronunciation gloss are retained. Commentary-based forms and name-only entries remain distinguished.'
        if slug == 'dashi':
            passage['content_note'] = '涔水郭注音潜，英文采用Qian；左右分流只是配图构图，不是原文方位图。影印榖字下另有“榖構木”小注，电子快照未收；郭注栏保留快照，未宣称逐字无缺。清水郭注的重复县字也保留录文，不猜改现代地名。'
            en[passage_id]['content_note'] = 'Qian follows Guo Pu’s pronunciation gloss. The image’s left/right streams are compositional, not compass directions. A small gloss under gu is absent from the captured annotation; the commentary panel retains the snapshot rather than claiming completeness. Repeated county wording is retained without guessing a modern place.'
        if slug == 'tiandi':
            passage['content_note'] = '本段核对影印42—43页，0081单元实际仍在42页末，43页只续“之已癭”；原捕获页号保留。櫟鸟赤翁的头下羽毛来自郭注，杜衡走马的两说并列；㯶柟等底本字形保留，不据天帝山名补造神祇、宫殿或地理位置。'
            en[passage_id]['content_note'] = 'Checked against scan pages 42–43: unit 81 remains at the end of page 42, and page 43 continues only the final eating claim. Captured page numbers remain available. The bird’s red feather tuft and Duheng’s alternative horse readings are distinguished as commentary. No deity, palace or modern location is inferred from the mountain name.'
        if slug == 'gaotu':
            passage['content_note'] = '本段正文及末句食之已癭、或作癎郭注均见影印43页；0090捕获44页但核定43页，快照不改写。薔郭注音色、𤣎郭注嬰音保留；前两脚似人手是郭注解释，不新增独立人臂。'
            en[passage_id]['content_note'] = 'The entire passage, including its final eating claim and the alternative commentary character, appears on scan page 43. Unit 90 was captured as page 44 and is corrected to 43 without changing the snapshot. Pronunciation glosses for Se and Yingru are retained. The hand-like front feet follow commentary and do not add separate human arms.'
        if slug == 'huangshan':
            passage['content_note'] = '影印44页确认0094缺字图为能，只修阅读引文；captured_text与快照保留原标记。0094的音敏实际属前兽𤛎，0095空正文单元承接鸚䳇郭注。无草木、多竹箭并存保留；郭注疑非此不作为现代黄山定位依据。'
            en[passage_id]['content_note'] = 'Scan page 44 confirms the image glyph as can; only the reading quotation is restored. Captured text and snapshot retain the marker. The pronunciation note in unit 94 belongs to Min; annotation-only unit 95 continues Yingmu’s commentary. Both vegetation statements remain, and Guo Pu’s doubtful comparison establishes no modern location.'
        if slug == 'cuishan':
            passage['content_note'] = '本段全见影印44页，0099火字捕获45页而核定44页。底本西首原样保留；配图双首参照《古今图书集成·禽虫典》卷53鸓条两首四足引文，不改作底本字。0098有香承接麝注，音壘释鸓。异文来源：https://zh.wikisource.org/wiki/欽定古今圖書集成/博物彙編/禽蟲典/第053卷#鸓圖'
            en[passage_id]['content_note'] = 'The entire passage is on scan44; unit99 fire was captured as page45 and is corrected to44. Xi shou remains unchanged in the base quotation. Two heads in the illustration follow the explicit variant quoted under Lei in Gujin Tushu Jicheng, Qinchong Dian53. The fragrant gloss belongs to she; the pronunciation gloss belongs to Lei.'
        if slug == 'guishan':
            passage['content_note'] = '本段source-02-0100—0102，全见影印45页，止于多丹粟；随后首列总括与祭礼另段。山名音注影印可见隗囂之隗，电子快照省囂，注栏原样保留，不宣称逐字无缺。錞猶与堤埻也音章閏反跨单元连读。西海与后文海仅按本段上下文关联；采石郭注的矿物举例不等于本山逐项确认。'
            en[passage_id]['content_note'] = 'Units100–102 are entirely on scan45 and end with dansu. The following range summary and rites are separate. The captured name gloss omits a character visible in the scan; it is retained without claiming a complete transcription. The chun gloss continues across units. The two sea references remain local, and mineral examples in the commentary are not separately verified deposits.'
        if slug == 'yuci':
            passage['content_note'] = '本段跨影印39—40页；末尾空正文单元的“天雷也或作灾”属槖𩇯郭注。山名下音注的电子录文仅存“音”，未猜补其缺字；嬰垣的异文说明跨两个单元连读。'
            en[passage_id]['content_note'] = 'This passage spans scan pages 39–40. The final annotation-only unit continues Tuofei’s commentary. The captured pronunciation gloss under the mountain name is incomplete and is not guessed; the jade variant note continues across units.'
        if row.get('is_summary'):
            passage['is_summary'] = True
            if slug == 'range1-summary':
                passage['content_note'] = '首列十九山的总括，独立成阅读段，不计作第二十山。跨影印45—46页；108仅注文之属也，实际45页而非捕获46页。冢注电子录文省鬼，燭注或作后的异体与瑜注读音亦省字，缺项已明示；白蒂按底本保留，不擅改为白席。'
                en[passage_id]['content_note'] = 'This is the first range summary, not a twentieth mountain. It spans scans 45–46; annotation-only unit108 is on45 despite its captured46. The captured zhong gloss omits gui; incomplete variant and pronunciation glosses are also marked, and bai di is retained without emending it to bai xi.'
                passage['commentary_quote'] = passage['commentary_quote'].replace('或作；', '或作〔录文缺字待核〕；').replace('羙王名音；', '羙王名音〔录文缺字待核〕；')
        passages.append(passage)
        if not row.get('is_summary'):
            place = {
                **common, 'id': place_id, 'kind': 'place', 'name': row['name'], 'description': row['description'],
                'quote': raw, 'commentary_quote': passage['commentary_quote'], 'source_passage_ids': [passage_id],
                'related_entry_ids': [passage_id],
            }
            en[place_id] = {**translation, 'name': row['en_name'], 'description': row['en_description'], 'quote': row['en_quote']}
            artwork(place, en[place_id], 'scene-' + slug)
            if row.get('content_note') or slug in {'zhushan', 'tiandi', 'gaotu', 'huangshan', 'cuishan', 'guishan', 'qianshan', 'taimao', 'shuli', 'gaoshan', 'nvchuang', 'longshou', 'lutai', 'niaowei', 'xiaoci', 'daci'}:
                place['content_note'] = passage['content_note']
                en[place_id]['content_note'] = en[passage_id]['content_note']
            records.append(('text_entities', place))
        for entity in [e for e in ENTITIES if e['slug'] == slug]:
            assert entity['quote'] in raw, entity['id']
            record = {**common, **{k: entity[k] for k in ('id', 'kind', 'name', 'description', 'quote')},
                      'commentary_quote': entity.get('commentary_quote', ''),
                      'source_passage_ids': [passage_id], 'related_entry_ids': [passage_id],
                      'context_place_id': place_id}
            if row.get('is_summary'):
                record.pop('context_place_id', None)
            if entity.get('relation_scope'):
                record['relation_scope'] = entity['relation_scope']
            en[entity['id']] = {**translation, 'name': entity['en_name'], 'description': entity['en_description'], 'quote': entity['en_quote']}
            artwork(record, en[entity['id']], entity['art'])
            if entity.get('appearance_unknown') or (entity['group'] == 'beasts' and entity['art'] and entity['art'].startswith('scene-')):
                record['appearance_unknown'] = True
                record['artwork_caption'] = '形貌未详 · 灰白问号剪影为统一占位，不代表该生物的形态。'
                en[entity['id']]['artwork_caption'] = 'Appearance unspecified · The gray question-mark silhouette is a shared placeholder, not a depiction of this creature.'
            if entity.get('art_reference'):
                record['artwork_caption'], en[entity['id']]['artwork_caption'] = entity['art_reference']
            if entity.get('content_note'):
                record['content_note'] = entity['content_note']
                en[entity['id']]['content_note'] = entity['en_content_note']
            records.append((entity['group'], record))
            passage['related_entry_ids'].append(entity['id'])
            label = ['山段中的条目', '所属山段'] if entity['kind'] != 'water' else ['山段中的水文', '水文所在山段']
            if row.get('is_summary'):
                relations.append({'ids': [passage_id, entity['id']], 'source': '《西山经》', 'quote': entity['quote'], 'labels': ['总括中的神祇' if entity['kind'] == 'deity' else '总括中的祠礼', '所属总括']})
            else:
                relations.append({'ids': [place_id, entity['id']], 'source': '《西山经》', 'quote': entity['quote'], 'labels': label})

        relations.extend(row.get('relations', []))

    relations += [
        {'ids': ['place-xishan-qianlai', 'place-xishan-songguo'], 'source': '《西山经》', 'quote': '西四十五里曰松果之山', 'labels': ['下一山 · 向西四十五里', '上一山 · 钱来']},
        {'ids': ['place-xishan-songguo', 'place-xishan-taihua'], 'source': '《西山经》', 'quote': '又西六十里曰太華之山', 'labels': ['下一山 · 向西六十里', '上一山 · 松果']},
        {'ids': ['water-xishan-huo', 'water-xishan-wei'], 'source': '《西山经》', 'quote': '濩水出焉北流注于渭', 'labels': ['向北流入', '来水 · 濩水']},
        {'ids': ['place-xishan-taihua', 'place-xishan-xiaohua'], 'source': '《西山经》', 'quote': '又西八十里曰小華之山', 'labels': ['下一山 · 向西八十里', '上一山 · 太华']},
        {'ids': ['place-xishan-xiaohua', 'place-xishan-fuyu'], 'source': '《西山经》', 'quote': '又西八十里曰符禺之山', 'labels': ['下一山 · 向西八十里', '上一山 · 小华']},
        {'ids': ['place-xishan-fuyu', 'place-xishan-shicui'], 'source': '《西山经》', 'quote': '又西六十里曰石脆之山', 'labels': ['下一山 · 向西六十里', '上一山 · 符禺']},
        {'ids': ['water-xishan-fuyu', 'water-xishan-wei'], 'source': '《西山经》', 'quote': '符禺之水出焉而北流注于渭', 'labels': ['向北流入', '来水 · 符禺之水']},
        {'ids': ['water-xishan-guan', 'water-xishan-yu-shicui'], 'source': '《西山经》', 'quote': '灌水出焉而北流注于禺水', 'labels': ['向北流入', '来水 · 灌水']},
        {'ids': ['water-xishan-guan', 'material-xishan-liuzhe'], 'source': '《西山经》', 'quote': '灌水出焉而北流注于禺水其中有流赭', 'labels': ['水文所见', '本段水域']},
        {'ids': ['place-xishan-shicui', 'place-xishan-ying'], 'source': '《西山经》', 'quote': '又西七十里曰英山', 'labels': ['下一山 · 向西七十里', '上一山 · 石脆']},
        {'ids': ['place-xishan-ying', 'place-xishan-zhushan'], 'source': '《西山经》', 'quote': '又西五十二里曰竹山', 'labels': ['下一山 · 向西五十二里', '上一山 · 英山']},
        {'ids': ['place-xishan-zhushan', 'place-xishan-fushan'], 'source': '《西山经》', 'quote': '又西百二十里曰浮山', 'labels': ['下一山 · 向西百二十里', '上一山 · 竹山']},
        {'ids': ['water-xishan-yu-ying', 'water-xishan-zhao-ying'], 'source': '《西山经》', 'quote': '禺水出焉北流注于招水', 'labels': ['向北流入', '来水 · 英山禺水']},
        {'ids': ['water-xishan-yu-ying', 'beast-xishan-bangyu-ying'], 'source': '《西山经》', 'quote': '禺水出焉北流注于招水其中多䰷魚', 'labels': ['同段水文中的对象', '水文上下文']},
        {'ids': ['water-xishan-zhu', 'water-xishan-wei'], 'source': '《西山经》', 'quote': '竹水出焉北流注于渭', 'labels': ['向北流入', '来水 · 竹水']},
        {'ids': ['water-xishan-dan-zhushan', 'water-xishan-luo-zhushan'], 'source': '《西山经》', 'quote': '丹水出焉東南流注于洛水', 'labels': ['向东南流入', '来水 · 竹山丹水']},
        {'ids': ['water-xishan-dan-zhushan', 'beast-xishan-renyu-zhushan'], 'source': '《西山经》', 'quote': '丹水出焉東南流注于洛水其中多水玉多人魚', 'labels': ['同段水文中的对象', '水文上下文']},
        {'ids': ['water-xishan-dan-zhushan', 'material-xishan-shuiyu-zhushan'], 'source': '《西山经》', 'quote': '丹水出焉東南流注于洛水其中多水玉', 'labels': ['同段水文中的物产', '水文上下文']},
    ]
    wei = next(r for _, r in records if r['id'] == 'water-xishan-wei')
    fuyu = next(p for p in passages if p['id'] == 'passage-xishan-fuyu')
    wei.update(
        name='渭（西山经首列）',
        description='渭在松果与符禺两段分别作为濩水、符禺之水的汇入水域出现，两段都记向北流入。这里合并两条明示的承接关系，保留各自出处，不补造渭的源头、完整河道或两处汇流位置。',
        quote='濩水出焉北流注于渭；符禺之水出焉而北流注于渭',
        source_locator='卷第二 · 影印页 34、36',
        source_pages=list(dict.fromkeys([*wei['source_pages'], *fuyu['source_pages']])),
        source_unit_ids=list(dict.fromkeys([*wei['source_unit_ids'], *fuyu['source_unit_ids']])),
        source_passage_ids=[*wei['source_passage_ids'], fuyu['id']],
        context_place_ids=['place-xishan-songguo', 'place-xishan-fuyu'],
        related_entry_ids=[*wei['related_entry_ids'], fuyu['id']],
        content_note='引文分号分隔松果、符禺两段摘句，并非连续经文；配图复用松果山水场景。',
    )
    en[wei['id']].update(
        name='Wei (Western first range)',
        description='In the Songguo and Fuyu passages, the Wei receives the Huo and Fuyu rivers respectively, both flowing north. The two explicit receiving-water relationships are linked with separate sources; no source, complete course or modern confluence is inferred.',
        quote='The Huo River rises here and flows north into the Wei; the Fuyu River rises here and flows north into the Wei. These are excerpts from separate passages.',
        source_locator='Volume 2 · scan pages 34, 36',
        content_note='The Chinese semicolon separates excerpts from Songguo and Fuyu rather than a continuous quotation. The illustration reuses the Songguo water scene.',
    )
    fuyu['related_entry_ids'].append(wei['id'])
    zhushan = next(p for p in passages if p['id'] == 'passage-xishan-zhushan')
    wei.update(
        description='渭在松果、符禺、竹山三段分别承接濩水、符禺水、竹水，均记向北流入。三处摘句与出处分别保留，不补造渭的源头、完整河道或现代汇流点。',
        quote=wei['quote'] + '；竹水出焉北流注于渭',
        source_locator='卷第二 · 影印页 34、36、38',
        source_pages=list(dict.fromkeys([*wei['source_pages'], *zhushan['source_pages']])),
        source_unit_ids=list(dict.fromkeys([*wei['source_unit_ids'], *zhushan['source_unit_ids']])),
        source_passage_ids=[*wei['source_passage_ids'], zhushan['id']],
        context_place_ids=[*wei['context_place_ids'], 'place-xishan-zhushan'],
        related_entry_ids=[*wei['related_entry_ids'], zhushan['id']],
        content_note='分号分隔松果、符禺、竹山三段摘句，并非连续经文；配图继续复用松果场景。',
    )
    en[wei['id']].update(
        description='The Wei receives the Huo, Fuyu and Zhu in three separate passages, each recording a northward inflow. Their quotations and sources remain distinct; no source, complete course or modern confluence is inferred.',
        quote='The Huo rises and flows north into the Wei; the Fuyu rises and flows north into the Wei; the Zhu rises and flows north into the Wei. These are excerpts from three separate passages.',
        source_locator='Volume 2 · scan pages 34, 36, 38',
        content_note='Semicolons separate excerpts from Songguo, Fuyu and Zhu, rather than a continuous quotation. The illustration continues to reuse the Songguo scene.',
    )
    zhushan['related_entry_ids'].append(wei['id'])
    yuci = next(p for p in passages if p['id'] == 'passage-xishan-yuci')
    wei.update(
        description='渭在松果、符禺、竹山、羭次四段分别承接濩水、符禺水、竹水、漆水，均记向北流入。四处摘句与出处分别保留，不补造渭的源头、完整河道或现代汇流点。',
        quote=wei['quote'] + '；漆水出焉北流注于渭',
        source_locator='卷第二 · 影印页 34、36、38、39、40',
        source_pages=list(dict.fromkeys([*wei['source_pages'], *yuci['source_pages']])),
        source_unit_ids=list(dict.fromkeys([*wei['source_unit_ids'], *yuci['source_unit_ids']])),
        source_passage_ids=[*wei['source_passage_ids'], yuci['id']],
        context_place_ids=[*wei['context_place_ids'], 'place-xishan-yuci'],
        related_entry_ids=[*wei['related_entry_ids'], yuci['id']],
        content_note='分号分隔四个山段的摘句，并非连续经文；配图继续复用松果场景。',
    )
    en[wei['id']].update(
        description='The Wei receives the Huo, Fuyu, Zhu and Qi in four separate passages, each recording a northward inflow. Quotations and sources remain distinct; no source, complete course or modern confluence is inferred.',
        quote='The Huo rises and flows north into the Wei; the Fuyu rises and flows north into the Wei; the Zhu rises and flows north into the Wei; the Qi rises and flows north into the Wei. These are excerpts from four separate passages.',
        source_locator='Volume 2 · scan pages 34, 36, 38, 39, 40',
        content_note='Semicolons separate excerpts from four mountain passages. The illustration continues to reuse the Songguo scene.',
    )
    yuci['related_entry_ids'].append(wei['id'])
    shishan = next(p for p in passages if p['id'] == 'passage-xishan-shishan')
    wei.update(
        description='渭在松果、符禺、竹山、羭次、时山五段分别承接濩水、符禺水、竹水、漆水、逐水，均记向北流入。各段摘句与出处分别保留，不补造渭的源头、完整河道或现代汇流点。',
        quote=wei['quote'] + '；逐水出焉北流注于渭',
        source_unit_ids=list(dict.fromkeys([*wei['source_unit_ids'], *shishan['source_unit_ids']])),
        source_pages=list(dict.fromkeys([*wei['source_pages'], *shishan['source_pages']])),
        source_passage_ids=[*wei['source_passage_ids'], shishan['id']],
        context_place_ids=[*wei['context_place_ids'], 'place-xishan-shishan'],
        related_entry_ids=[*wei['related_entry_ids'], shishan['id']],
        content_note='分号分隔五个山段的摘句，并非连续经文；配图继续复用松果场景。',
    )
    en[wei['id']].update(
        description='The Wei receives the Huo, Fuyu, Zhu from Mount Zhu, Qi, and Zhu from Mount Shi in five separate passages, all recording northward inflows. Quotations and sources remain distinct; no source, complete course or modern confluence is inferred.',
        quote='The Huo rises and flows north into the Wei; the Fuyu rises and flows north into the Wei; the Zhu at Mount Zhu rises and flows north into the Wei; the Qi rises and flows north into the Wei; the Zhu at Mount Shi rises and flows north into the Wei. These are excerpts from five separate passages.',
        content_note='Semicolons separate excerpts from five mountain passages. The illustration continues to reuse the Songguo scene.',
    )
    shishan['related_entry_ids'].append(wei['id'])
    nan = next(p for p in passages if p['id'] == 'passage-xishan-nanshan-west')
    wei.update(
        description='渭在松果、符禺、竹山、羭次、时山、南山六段分别承接濩水、符禺水、竹水、漆水、逐水、南山丹水，均记向北流入。各段摘句与出处分别保留，不补造渭的源头、完整河道或现代汇流点。',
        quote=wei['quote'] + '；丹水出焉北流注于渭',
        source_locator='卷第二 · 影印页 34、36、38、39、40、41',
        source_unit_ids=list(dict.fromkeys([*wei['source_unit_ids'], *nan['source_unit_ids']])),
        source_pages=list(dict.fromkeys([*wei['source_pages'], *nan['source_pages']])),
        source_passage_ids=[*wei['source_passage_ids'], nan['id']],
        context_place_ids=[*wei['context_place_ids'], 'place-xishan-nanshan-west'],
        related_entry_ids=[*wei['related_entry_ids'], nan['id']],
        content_note='分号分隔六个山段的摘句，并非连续经文；配图继续复用松果场景。',
    )
    en[wei['id']].update(
        description='The Wei receives the Huo, Fuyu, Zhu from Mount Zhu, Qi, Zhu from Mount Shi, and Dan from Mount Nan in six separate passages, all recording northward inflows. Quotations and sources remain distinct; no source, complete course or modern confluence is inferred.',
        quote='The Huo rises and flows north into the Wei; the Fuyu rises and flows north into the Wei; the Zhu at Mount Zhu rises and flows north into the Wei; the Qi rises and flows north into the Wei; the Zhu at Mount Shi rises and flows north into the Wei; the Dan at Mount Nan rises and flows north into the Wei. These are excerpts from six separate passages.',
        source_locator='Volume 2 · scan pages 34, 36, 38, 39, 40, 41',
        content_note='Semicolons separate excerpts from six mountain passages. The illustration continues to reuse the Songguo scene.',
    )
    nan['related_entry_ids'].append(wei['id'])
    dashi = next(p for p in passages if p['id'] == 'passage-xishan-dashi')
    wei.update(
        description='渭在松果、符禺、竹山、羭次、时山、南山、大时七段分别承接濩水、符禺水、竹水、漆水、逐水、南山丹水、大时涔水，均记向北流入。各段摘句与出处分别保留，不补造渭的源头、完整河道或现代汇流点；大时清水南注汉另列。',
        quote=wei['quote'] + '；涔水岀焉北流注于渭',
        source_unit_ids=list(dict.fromkeys([*wei['source_unit_ids'], *dashi['source_unit_ids']])),
        source_pages=list(dict.fromkeys([*wei['source_pages'], *dashi['source_pages']])),
        source_passage_ids=[*wei['source_passage_ids'], dashi['id']],
        context_place_ids=[*wei['context_place_ids'], 'place-xishan-dashi'],
        related_entry_ids=[*wei['related_entry_ids'], dashi['id']],
        content_note='分号分隔七个山段的摘句，并非连续经文；配图继续复用松果场景。',
    )
    en[wei['id']].update(
        description='The Wei receives the Huo, Fuyu, Zhu from Mount Zhu, Qi, Zhu from Mount Shi, Dan from Mount Nan, and Qian from Dashi in seven separate passages, all recording northward inflows. Quotations and sources remain distinct; no source, complete course or modern confluence is inferred. Dashi’s Qing-to-Han account stays separate.',
        quote='The Huo rises and flows north into the Wei; the Fuyu rises and flows north into the Wei; the Zhu at Mount Zhu rises and flows north into the Wei; the Qi rises and flows north into the Wei; the Zhu at Mount Shi rises and flows north into the Wei; the Dan at Mount Nan rises and flows north into the Wei; the Qian at Dashi rises and flows north into the Wei. These are excerpts from seven separate passages.',
        content_note='Semicolons separate excerpts from seven mountain passages. The illustration continues to reuse the Songguo scene.',
    )
    dashi['related_entry_ids'].append(wei['id'])
    bozhong = next(p for p in passages if p['id'] == 'passage-xishan-bozhong')
    han = next(r for _, r in records if r['id'] == 'water-xishan-han-dashi')
    han.update(
        name='汉水（西山经首列）',
        description='汉水在大时段承接向南流来的清水，在嶓冡段则记从山中流出、向东南注沔。这里沿用既有稳定ID，分别保留两段引文和出处，不据同名推定现代河道或汇流点，也不把另向北流的囂水接成汉水支流。',
        quote=han['quote'] + '；漢水出焉而東南流注于沔',
        commentary_quote='〔嶓冡段郭注〕至江夏安陸縣江即沔水',
        source_locator='卷第二 · 影印页 41、42',
        source_pages=list(dict.fromkeys([*han['source_pages'], *bozhong['source_pages']])),
        source_unit_ids=list(dict.fromkeys([*han['source_unit_ids'], *bozhong['source_unit_ids']])),
        source_passage_ids=[*han['source_passage_ids'], bozhong['id']],
        context_place_ids=['place-xishan-dashi', 'place-xishan-bozhong'],
        related_entry_ids=[*han['related_entry_ids'], bozhong['id']],
        content_note='分号分隔大时与嶓冡两段摘句，并非连续经文；稳定ID保留dashi后缀，配图仍复用大时山景，不代指完整汉水。',
        artwork_caption='复用大时山景 · 示意出山水流，不复原汉水全程或现代汇流点。',
    )
    en[han['id']].update(
        name='Han (Western first range)',
        description='The Han receives the south-flowing Qing in the Dashi passage; the Bozhong passage records its source and southeastward flow into the Mian. The existing stable ID now retains both quotations and sources, without identifying a modern course or confluence or making the separate Xiao a branch of the Han.',
        quote='The Qing rises here and flows south into the Han; the Han rises at Bozhong and flows southeast into the Mian. These are excerpts from two separate passages.',
        source_locator='Volume 2 · scan pages 41, 42',
        content_note='The semicolon separates excerpts from Dashi and Bozhong rather than a continuous quotation. The stable ID retains its dashi suffix and the reused Dashi scene does not depict the complete Han.',
        artwork_caption='Reused Dashi scene · Schematic mountain waters, not the full Han or a modern confluence.',
    )
    bozhong['related_entry_ids'].append(han['id'])
    relations += [
        {'ids': ['place-xishan-xiaoci', 'place-xishan-daci'], 'source': '《西山经》', 'quote': '又西三百里曰大次之山', 'labels': ['下一山 · 向西三百里', '上一山 · 小次山']},
        {'ids': ['place-xishan-niaowei', 'place-xishan-xiaoci'], 'source': '《西山经》', 'quote': '又西四百里曰小次之山', 'labels': ['下一山 · 向西四百里', '上一山 · 鳥危山']},
        {'ids': ['place-xishan-lutai', 'place-xishan-niaowei'], 'source': '《西山经》', 'quote': '西南二百里曰鳥危之山', 'labels': ['下一山 · 向西南二百里', '上一山 · 鹿臺山']},
        {'ids': ['place-xishan-niaowei', 'water-xishan-chi-huangshan'], 'source': '《西山经》', 'quote': '鳥危之水出焉西流注于赤水', 'labels': ['山段中的水文', '水文所在山段']},
        {'ids': ['water-xishan-niaowei', 'water-xishan-chi-huangshan'], 'source': '《西山经》', 'quote': '鳥危之水出焉西流注于赤水', 'labels': ['向西流入', '来水 · 鳥危水']},
        {'ids': ['water-xishan-niaowei', 'material-xishan-dansu-niaowei'], 'source': '《西山经》', 'quote': '鳥危之水出焉西流注于赤水其中多丹粟', 'labels': ['同段水文中的物产', '水文上下文']},
        {'ids': ['place-xishan-longshou', 'place-xishan-lutai'], 'source': '《西山经》', 'quote': '又西二百里曰鹿臺之山', 'labels': ['下一山 · 向西二百里', '上一山 · 龍首山']},
        {'ids': ['place-xishan-nvchuang', 'place-xishan-longshou'], 'source': '《西山经》', 'quote': '又西二百里曰龍首之山', 'labels': ['下一山 · 向西二百里', '上一山 · 女牀山']},
        {'ids': ['place-xishan-longshou', 'water-xishan-jing-gaoshan'], 'source': '《西山经》', 'quote': '苕水出焉東南流注于涇水', 'labels': ['山段中的水文', '水文所在山段']},
        {'ids': ['water-xishan-tiao-longshou', 'water-xishan-jing-gaoshan'], 'source': '《西山经》', 'quote': '苕水出焉東南流注于涇水', 'labels': ['向东南流入', '来水 · 龍首山苕水']},
        {'ids': ['water-xishan-tiao-longshou', 'material-xishan-fine-jade-longshou'], 'source': '《西山经》', 'quote': '苕水出焉東南流注于涇水其中多羙玉', 'labels': ['同段水文中的物产', '水文上下文']},
        {'ids': ['place-xishan-fushan', 'place-xishan-yuci'], 'source': '《西山经》', 'quote': '又西七十里曰羭次之山', 'labels': ['下一山 · 向西七十里', '上一山 · 浮山']},
        {'ids': ['water-xishan-qi-yuci', 'water-xishan-wei'], 'source': '《西山经》', 'quote': '漆水出焉北流注于渭', 'labels': ['向北流入', '来水 · 漆水']},
        {'ids': ['place-xishan-yuci', 'place-xishan-shishan'], 'source': '《西山经》', 'quote': '又西百五十里曰時山', 'labels': ['下一山 · 向西百五十里', '上一山 · 羭次']},
        {'ids': ['water-xishan-zhu-shishan', 'water-xishan-wei'], 'source': '《西山经》', 'quote': '逐水出焉北流注于渭', 'labels': ['向北流入', '来水 · 时山逐水']},
        {'ids': ['water-xishan-zhu-shishan', 'material-xishan-shuiyu-shishan'], 'source': '《西山经》', 'quote': '逐水出焉北流注于渭其中多水玉', 'labels': ['同段水文中的物产', '水文上下文']},
        {'ids': ['place-xishan-shishan', 'place-xishan-nanshan-west'], 'source': '《西山经》', 'quote': '又西百七十里曰南山', 'labels': ['下一山 · 向西百七十里', '上一山 · 时山']},
        {'ids': ['water-xishan-dan-nanshan', 'water-xishan-wei'], 'source': '《西山经》', 'quote': '丹水出焉北流注于渭', 'labels': ['向北流入', '来水 · 南山丹水']},
        {'ids': ['place-xishan-nanshan-west', 'place-xishan-dashi'], 'source': '《西山经》', 'quote': '又西百八十里曰大時之山', 'labels': ['下一山 · 向西百八十里', '上一山 · 南山（西山经）']},
        {'ids': ['water-xishan-qian-dashi', 'water-xishan-wei'], 'source': '《西山经》', 'quote': '涔水岀焉北流注于渭', 'labels': ['向北流入', '来水 · 大时涔水']},
        {'ids': ['water-xishan-qing-dashi', 'water-xishan-han-dashi'], 'source': '《西山经》', 'quote': '清水出焉南流注于漢水', 'labels': ['向南流入', '来水 · 大时清水']},
        {'ids': ['place-xishan-dashi', 'place-xishan-bozhong'], 'source': '《西山经》', 'quote': '又西三百二十里曰嶓冡之山', 'labels': ['下一山 · 向西三百二十里', '上一山 · 大时']},
        {'ids': ['place-xishan-bozhong', 'water-xishan-han-dashi'], 'source': '《西山经》', 'quote': '漢水出焉而東南流注于沔', 'labels': ['山段中的水文', '水文所在山段']},
        {'ids': ['water-xishan-han-dashi', 'water-xishan-mian-bozhong'], 'source': '《西山经》', 'quote': '漢水出焉而東南流注于沔', 'labels': ['向东南流入', '来水 · 嶓冡汉水']},
        {'ids': ['water-xishan-xiao-bozhong', 'water-xishan-tang-bozhong'], 'source': '《西山经》', 'quote': '囂水出焉北流注于湯水', 'labels': ['向北流入', '来水 · 嶓冡囂水']},
        {'ids': ['place-xishan-bozhong', 'place-xishan-tiandi'], 'source': '《西山经》', 'quote': '又西三百五十里曰天帝之山', 'labels': ['下一山 · 向西三百五十里', '上一山 · 嶓冡']},
        {'ids': ['place-xishan-tiandi', 'place-xishan-gaotu'], 'source': '《西山经》', 'quote': '西南三百八十里曰皐塗之山', 'labels': ['下一山 · 向西南三百八十里', '上一山 · 天帝']},
        {'ids': ['water-xishan-se-gaotu', 'water-xishan-zhuzi-gaotu'], 'source': '《西山经》', 'quote': '薔水出焉西流注于諸資之水', 'labels': ['向西流入', '来水 · 薔水']},
        {'ids': ['water-xishan-tu-gaotu', 'water-xishan-jihuo-gaotu'], 'source': '《西山经》', 'quote': '塗水出焉南流注于集獲之水', 'labels': ['向南流入', '来水 · 塗水']},
        {'ids': ['place-xishan-gaoshan', 'place-xishan-nvchuang'], 'source': '《西山经》', 'quote': '西南三百里曰女牀之山', 'labels': ['下一山 · 向西南三百里', '上一山 · 髙山']},
        {'ids': ['place-xishan-shuli', 'place-xishan-gaoshan'], 'source': '《西山经》', 'quote': '又西百五十里曰髙山', 'labels': ['下一山 · 向西百五十里', '上一山 · 數歴山']},
        {'ids': ['water-xishan-jing-gaoshan', 'water-xishan-wei'], 'source': '《西山经》', 'quote': '涇水出焉而東流注于渭', 'labels': ['向东流入', '来水 · 髙山涇水']},
        {'ids': ['water-xishan-jing-gaoshan', 'material-xishan-qingshi-gaoshan'], 'source': '《西山经》', 'quote': '涇水出焉而東流注于渭其中多磬石青碧', 'labels': ['同段水文中的物产', '水文上下文']},
        {'ids': ['water-xishan-jing-gaoshan', 'material-xishan-qingbi-water-gaoshan'], 'source': '《西山经》', 'quote': '涇水出焉而東流注于渭其中多磬石青碧', 'labels': ['同段水文中的物产', '水文上下文']},
        {'ids': ['place-xishan-taimao', 'place-xishan-shuli'], 'source': '《西山经》', 'quote': '又西一百七十里曰數歴之山', 'labels': ['下一山 · 向西一百七十里', '上一山 · 㤗冐山']},
        {'ids': ['water-xishan-chu-shuli', 'water-xishan-wei'], 'source': '《西山经》', 'quote': '楚水出焉而南流注于渭', 'labels': ['向南流入', '来水 · 數歴山楚水']},
        {'ids': ['water-xishan-chu-shuli', 'material-xishan-pearl-shuli'], 'source': '《西山经》', 'quote': '楚水出焉而南流注于渭其中多珠', 'labels': ['同段水文中的物产', '水文上下文']},
        {'ids': ['place-xishan-qianshan', 'place-xishan-taimao'], 'source': '《西山经》', 'quote': '西二百里曰㤗冐之山', 'labels': ['下一山 · 向西二百里', '上一山 · 鈐山']},
        {'ids': ['water-xishan-yu-taimao', 'water-xishan-he-taimao'], 'source': '《西山经》', 'quote': '浴水出焉東流注于河', 'labels': ['向东流入', '来水 · 㤗冐山浴水']},
        {'ids': ['water-xishan-yu-taimao', 'material-xishan-zaoyu-taimao'], 'source': '《西山经》', 'quote': '浴水出焉東流注于河其中多藻玉', 'labels': ['同段水文中的物产', '水文上下文']},
        {'ids': ['water-xishan-yu-taimao', 'beast-xishan-white-snake-taimao'], 'source': '《西山经》', 'quote': '浴水出焉東流注于河其中多藻玉多白蛇', 'labels': ['水段所见', '本段水域']},
        {'ids': ['passage-xishan-range1-summary', 'passage-xishan-qianshan'], 'source': '《西山经》', 'quote': '西次二經之首曰鈐山', 'labels': ['下一山列 · 鈐山', '前一山列总括']},
        {'ids': ['passage-xishan-guishan', 'passage-xishan-range1-summary'], 'source': '《西山经》', 'quote': '凡西經之首自錢來之山至于騩山凡十九山', 'labels': ['首列总括与祠礼', '前一段 · 騩山']},
        {'ids': ['place-xishan-cuishan', 'place-xishan-guishan'], 'source': '《西山经》', 'quote': '又西二百五十里曰騩山', 'labels': ['下一山 · 向西二百五十里', '上一山 · 翠山']},
        {'ids': ['water-xishan-qi-guishan', 'water-xishan-westsea-guishan'], 'source': '《西山经》', 'quote': '淒水出焉西流注于海', 'labels': ['向西流入', '来水 · 騩山淒水']},
        {'ids': ['water-xishan-qi-guishan', 'material-xishan-caishi-guishan'], 'source': '《西山经》', 'quote': '淒水出焉西流注于海其中多采石黄金', 'labels': ['同段水文中的物产', '水文上下文']},
        {'ids': ['water-xishan-qi-guishan', 'material-xishan-gold-guishan'], 'source': '《西山经》', 'quote': '淒水出焉西流注于海其中多采石黄金', 'labels': ['同段水文中的物产', '水文上下文']},
        {'ids': ['place-xishan-huangshan', 'place-xishan-cuishan'], 'source': '《西山经》', 'quote': '又西二百里曰翠山', 'labels': ['下一山 · 向西二百里', '上一山 · 黄山']},
        {'ids': ['place-xishan-gaotu', 'place-xishan-huangshan'], 'source': '《西山经》', 'quote': '又西百八十里曰黄山', 'labels': ['下一山 · 向西百八十里', '上一山 · 皐塗']},
        {'ids': ['water-xishan-pan-huangshan', 'water-xishan-chi-huangshan'], 'source': '《西山经》', 'quote': '盼水出焉西流注于赤水', 'labels': ['向西流入', '来水 · 黄山盼水']},
        {'ids': ['water-xishan-pan-huangshan', 'material-xishan-jade-huangshan'], 'source': '《西山经》', 'quote': '盼水出焉西流注于赤水其中多玉', 'labels': ['同段水文中的物产', '水文上下文']},
    ]
    shuli = next(p for p in passages if p['id'] == 'passage-xishan-shuli')
    wei.update(
        name='渭（西山经）',
        description='渭在首列松果、符禺、竹山、羭次、时山、南山、大时七段承接北流来水；西次二经數歴段另记楚水南流注渭。八处摘句与出处分别保留，南北方向不混同，不补渭的源头、完整河道或现代汇流点。',
        quote=wei['quote'] + '；楚水出焉而南流注于渭',
        source_locator='卷第二 · 影印页 34、36、38、39、40、41、46、47',
        source_pages=list(dict.fromkeys([*wei['source_pages'], *shuli['source_pages']])),
        source_unit_ids=list(dict.fromkeys([*wei['source_unit_ids'], *shuli['source_unit_ids']])),
        source_passage_ids=[*wei['source_passage_ids'], shuli['id']],
        context_place_ids=[*wei['context_place_ids'], 'place-xishan-shuli'],
        related_entry_ids=[*wei['related_entry_ids'], shuli['id']],
        content_note='分号分隔八个山段摘句，并非连续经文；首列七段北注与數歴楚水南注分别保留。配图复用松果场景，不表示渭的完整形态或现代地理。',
    )
    en[wei['id']].update(
        name='Wei (Western Mountains)',
        description='Seven first-range passages record northward inflows to the Wei; the second-range Shuli passage separately records the Chu flowing south into it. The eight excerpts and sources remain distinct. No source, complete course or modern confluence is inferred.',
        quote=en[wei['id']]['quote'] + ' The Chu rises and flows south into the Wei, in the separate Shuli passage.',
        source_locator='Volume 2 · scan pages 34, 36, 38, 39, 40, 41, 46, 47',
        content_note='Semicolons separate eight passage excerpts. Seven northward inflows and Shuli’s southward Chu remain distinct. The reused Songguo scene does not depict the Wei’s complete form or modern geography.',
    )
    shuli['related_entry_ids'].append(wei['id'])
    gaoshan = next(p for p in passages if p['id'] == 'passage-xishan-gaoshan')
    wei.update(
        description='渭在首列松果、符禺、竹山、羭次、时山、南山、大时七段承接北流来水；西次二经另记數歴楚水南流、髙山涇水东流注渭。九处摘句与出处分别保留，七北一南一东不混同，不补渭的源头、完整河道或现代汇流点。',
        quote=wei['quote'] + '；涇水出焉而東流注于渭',
        source_pages=list(dict.fromkeys([*wei['source_pages'], *gaoshan['source_pages']])),
        source_unit_ids=list(dict.fromkeys([*wei['source_unit_ids'], *gaoshan['source_unit_ids']])),
        source_passage_ids=[*wei['source_passage_ids'], gaoshan['id']],
        context_place_ids=[*wei['context_place_ids'], 'place-xishan-gaoshan'],
        related_entry_ids=[*wei['related_entry_ids'], gaoshan['id']],
        content_note='分号分隔九个山段摘句，并非连续经文；首列七段北注、數歴楚水南注、髙山涇水东注分别保留。配图复用松果场景，不表示渭的完整形态或现代地理。',
    )
    en[wei['id']].update(
        description='Seven first-range passages record northward inflows to the Wei. In the second range, Shuli separately records the Chu flowing south, and Gao the Jing flowing east into it. The nine excerpts and sources remain distinct; no source, complete course or modern confluence is inferred.',
        quote=en[wei['id']]['quote'] + ' The Jing rises and flows east into the Wei in the separate Gao passage.',
        content_note='Semicolons separate nine passage excerpts. Seven northward inflows, Shuli’s southward Chu and Gao’s eastward Jing remain distinct. The reused Songguo scene does not depict the Wei’s complete form or modern geography.',
    )
    gaoshan['related_entry_ids'].append(wei['id'])
    longshou = next(p for p in passages if p['id'] == 'passage-xishan-longshou')
    jing = next(r for _, r in records if r['id'] == 'water-xishan-jing-gaoshan')
    jing.update(
        name='涇水（西山经次二列）',
        description='髙山段记涇水出山、东流注渭，水文后接多磬石青碧；龍首段记苕水东南流来注涇。两段摘句与物产语境分别保留，不把龍首水文羙玉扩展到全部涇水。音經及古水道郭注仅来自髙山段，不补现代河道、坐标或汇流点。',
        quote=jing['quote'] + '；苕水出焉東南流注于涇水',
        source_locator='卷第二 · 影印页 47、48',
        source_pages=list(dict.fromkeys([*jing['source_pages'], *longshou['source_pages']])),
        source_unit_ids=[*jing['source_unit_ids'], *longshou['source_unit_ids']],
        source_passage_ids=[*jing['source_passage_ids'], longshou['id']],
        context_place_ids=['place-xishan-gaoshan', 'place-xishan-longshou'],
        related_entry_ids=[*jing['related_entry_ids'], longshou['id']],
        content_note='分号分隔髙山与龍首两段摘句，并非连续经文；保留gaoshan稳定ID。郭注只属髙山段；苕水东南注涇与涇水东注渭分别保存，龍首并未直接记苕水注渭。',
    )
    en[jing['id']].update(
        name='Jing (Western second range)',
        description='At Gao, the Jing rises and flows east into the Wei, followed by sounding stones and qingbi in that water account. At Longshou, it receives the southeast-flowing Tiao. The excerpts and products retain their separate contexts; Longshou’s fine jade is not assigned to the entire Jing. The pronunciation and ancient-course commentary belong only to Gao, without a modern course or confluence.',
        quote=en[jing['id']]['quote'] + ' In the separate Longshou passage, the Tiao rises and flows southeast into the Jing.',
        source_locator='Volume 2 · scan pages 47, 48',
        content_note='The semicolon separates Gao and Longshou excerpts. The gaoshan stable ID remains. Commentary belongs only to Gao. Tiao-to-Jing and Jing-to-Wei directions stay separate; Longshou does not directly record the Tiao entering the Wei.',
    )
    longshou['related_entry_ids'].append(jing['id'])
    niaowei = next(p for p in passages if p['id'] == 'passage-xishan-niaowei')
    chi = next(r for _, r in records if r['id'] == 'water-xishan-chi-huangshan')
    chi.update(
        name='赤水（西山经）',
        description='赤水在黄山段承接向西流来的盼水，在鳥危段承接向西流来的鳥危水。两段摘句与出处分开保存；鳥危水文中的丹粟不扩展到整条赤水。与南山经柜山段赤水分别保存，不据同名拼接现代流域、源头或汇流点，也不据赤字补成红色河水。',
        quote=chi['quote'] + '；鳥危之水出焉西流注于赤水',
        source_locator='卷第二 · 影印页 44、48',
        source_pages=list(dict.fromkeys([*chi['source_pages'], *niaowei['source_pages']])),
        source_unit_ids=[*chi['source_unit_ids'], *niaowei['source_unit_ids']],
        source_passage_ids=[*chi['source_passage_ids'], niaowei['id']],
        context_place_ids=['place-xishan-huangshan', 'place-xishan-niaowei'],
        related_entry_ids=[*chi['related_entry_ids'], niaowei['id']],
        content_note='分号分隔黄山与鳥危两段摘句，并非连续经文。沿用huangshan稳定ID，配图仍仅复用黄山山景，不代表鳥危山景或完整赤水。',
        artwork_caption='复用黄山场景 · 不代指鳥危山景、完整赤水或现代河道。',
    )
    en[chi['id']].update(
        name='Chi (Western Mountains)',
        description='The Chi receives the west-flowing Mian in Huang and the west-flowing Niaowei in its own mountain passage. The excerpts and sources remain separate; Niaowei’s dansu is not assigned to the entire Chi. The Southern Chi retains a separate record, without joining modern basins, sources or confluences or coloring the water red.',
        quote=en[chi['id']]['quote'] + ' In the separate Niaowei passage, the Niaowei River rises and flows west into the Chi.',
        source_locator='Volume 2 · scan pages 44, 48',
        content_note='The semicolon separates Huang and Niaowei excerpts. The huangshan stable ID and reused Huang scene remain; the image does not depict Niaowei or the full Chi.',
        artwork_caption='Reused Huang scene · Not Niaowei, the full Chi or a modern river course.',
    )
    niaowei['related_entry_ids'].append(chi['id'])
    if any(p['id'] == 'passage-xishan-huangren' for p in passages):
        huangren = next(p for p in passages if p['id'] == 'passage-xishan-huangren')
        chi.update(
            description='赤水在黄山段承接西流盼水、鳥危段承接西流鳥危水、皇人段承接西流皇水。三段摘句与出处各自保存，後两段水文丹粟不扩展至全河。与南山柜山赤水分开，不据同名拼接现代流域或把河水补成红色。',
            quote=chi['quote'] + '；皇水出焉西流注于赤水',
            source_locator='卷第二 · 影印页 44、48、50',
            source_pages=list(dict.fromkeys([*chi['source_pages'], *huangren['source_pages']])),
            source_unit_ids=[*chi['source_unit_ids'], *huangren['source_unit_ids']],
            source_passage_ids=[*chi['source_passage_ids'], huangren['id']],
            context_place_ids=[*chi['context_place_ids'], 'place-xishan-huangren'],
            related_entry_ids=[*chi['related_entry_ids'], huangren['id']],
            content_note='分号分隔黄山、鳥危、皇人三段摘句，并非连续经文；huangshan稳定ID与黄山旧图保留，不代指其余山段、完整赤水或现代地理。',
            artwork_caption='复用黄山场景 · 不代指鳥危、皇人、完整赤水或现代河道。',
        )
        en[chi['id']].update(
            description='The Chi receives the west-flowing Mian at Huang, Niaowei at its mountain, and Huang at Huangren. The three excerpts and sources remain distinct. Dansu in the latter two water accounts is not assigned to the whole river. The Southern Chi remains separate, without a joined modern basin or red water.',
            quote=en[chi['id']]['quote'] + ' In the separate Huangren passage, the Huang rises and flows west into the Chi.',
            source_locator='Volume 2 · scan pages 44, 48, 50',
            content_note='Semicolons separate Huang, Niaowei and Huangren excerpts. The stable ID and reused Huang scene remain; the image does not depict the other mountains, the full Chi or modern geography.',
            artwork_caption='Reused Huang scene · Not Niaowei, Huangren, the full Chi or a modern river course.',
        )
        huangren['related_entry_ids'].append(chi['id'])
    he = next(r for _, r in records if r['id'] == 'water-xishan-he-taimao')
    chongwu = next(p for p in passages if p['id'] == 'passage-xishan-chongwu')
    he.update(name='河（西山经）', description='河在㤗冐段承接东流的浴水，在崇吾段作为山在其南的方位参照。两段分别保存出处；不据此拼出河的完整河道、现代汇流点或崇吾坐标。', quote='浴水出焉東流注于河；崇吾之山在河之南', source_locator='卷第二 · 影印页 46、51、52', source_pages=list(dict.fromkeys([*he['source_pages'], *chongwu['source_pages']])), source_unit_ids=list(dict.fromkeys([*he['source_unit_ids'], *chongwu['source_unit_ids']])), source_passage_ids=[*he['source_passage_ids'], chongwu['id']], context_place_ids=['place-xishan-taimao','place-xishan-chongwu'], related_entry_ids=[*he['related_entry_ids'],chongwu['id']], content_note='分号分开㤗冐与崇吾摘句，并非连续经文；两种关系不等于同一段流向。')
    en[he['id']].update(name='He (Western Mountains)', description='The He receives the east-flowing Yu in the Taimao passage and is a directional reference north of Chongwu in the third range. Both contexts retain separate sources; no complete river course, modern confluence or Chongwu coordinates are inferred.', quote='The Yu rises and flows east into the He; in a separate passage, Chongwu stands south of the He.', source_locator='Volume 2 · scan pages 46, 51, 52', content_note='The semicolon separates excerpts from Taimao and Chongwu rather than continuous text or a single flow statement.')
    chongwu['related_entry_ids'].append(he['id'])
    buzhou = next(p for p in passages if p['id'] == 'passage-xishan-buzhou')
    he.update(description='河在㤗冐段承接浴水，在崇吾段作山在其南的方位参照，在不周段记泑澤河水潜流及其源渾渾泡泡。三段各存出处，郭注地理解释不当现代河道，不据此复原完整流域或汇流点。', quote=he['quote']+'；東望泑澤河水所潜也其源渾渾泡泡', source_locator='卷第二 · 影印页 46、51、52、53', source_pages=list(dict.fromkeys([*he['source_pages'],*buzhou['source_pages']])), source_unit_ids=list(dict.fromkeys([*he['source_unit_ids'],*buzhou['source_unit_ids']])), source_passage_ids=[*he['source_passage_ids'],buzhou['id']], context_place_ids=[*he['context_place_ids'],'place-xishan-buzhou'], related_entry_ids=[*he['related_entry_ids'],buzhou['id']], content_note='分号分开㤗冐/崇吾/不周三段摘句，不是连续经文或单一流向。郭注长释见不周阅读及泑澤卡，地名对应保留为古籍注说。')
    en[he['id']].update(description='The He receives the Yu at Taimao, lies north of Chongwu, and is described as running underground at You Marsh with a surging source in the Buzhou passage. All three retain separate sources; the commentary’s geography is not a modern river course or a reconstructed basin.', quote='The Yu flows east into the He; separately, Chongwu stands south of the He; in the Buzhou passage, You Marsh is seen to the east, where the He runs underground and its source surges.', source_locator='Volume 2 · scan pages 46, 51, 52, 53', content_note='Semicolons separate Taimao, Chongwu and Buzhou excerpts rather than a continuous text or one flow direction. The long commentary remains on the Buzhou and You Marsh records as an ancient explanation.')
    buzhou['related_entry_ids'].append(he['id'])
    zhong = next(r for _, r in records if r['id'] == 'place-xishan-zhongshan')
    mi = next(p for p in passages if p['id'] == 'passage-xishan-mishan')
    zhong_passage = next(p for p in passages if p['id'] == 'passage-xishan-zhongshan')
    zhong.update(description=zhong['description']+' 峚段另记黄帝投玉于鍾山之阳、峚至鍾460里泽地；与本山起句420里分存。', quote='黃帝乃取峚山之玉榮而投之鍾山之陽；自峚山至于鍾山四百六十里其間盡澤也；'+zhong['quote'], source_locator='卷第二 · 影印页 53、54、55、56', source_pages=list(dict.fromkeys([*mi['source_pages'],*zhong['source_pages']])), source_unit_ids=list(dict.fromkeys([*mi['source_unit_ids'],*zhong['source_unit_ids']])), source_passage_ids=[mi['id'],zhong_passage['id']], related_entry_ids=[*zhong['related_entry_ids'],mi['id']], context_place_ids=['place-xishan-mishan','place-xishan-zhongshan'], content_note=zhong['content_note']+' 稳定ID复用峚段先建条目；分号分开峚段两摘句与鍾山正文，不是连续经文。')
    en[zhong['id']].update(description=en[zhong['id']]['description']+' The separate Mi passage records Huangdi’s jade casting and 460 li of wetlands to Zhong; the 420-li opening remains distinct.', quote='In the separate Mi passage, Huangdi casts jade blossom onto Zhong’s sunny side, and 460 li of wetlands lie between Mi and Zhong. '+en[zhong['id']]['quote'], source_locator='Volume 2 · scan pages 53, 54, 55, 56', content_note=en[zhong['id']]['content_note']+' The stable Zhong ID retains both sources. Semicolons separate two Mi excerpts from Zhong’s own text, not a continuous quotation.')
    mi['related_entry_ids'].append(zhong['id'])
    westsea = next(r for _, r in records if r['id'] == 'water-xishan-westsea-guishan')
    taiqi = next(p for p in passages if p['id'] == 'passage-xishan-taiqi')
    westsea.update(name='西海（西山经）', description='西海在騩山段为临山/淒水所注的海，在㤗噐段为文鰩魚常行之海。按篇内同名保留两处上下文与出处，不据此认定现代同一海域、海岸线或鱼的实测迁徙路线；南山同名分开。', quote=westsea['quote']+'；常行西海遊於東海以夜飛', source_locator='卷第二 · 影印页 45、56', source_pages=list(dict.fromkeys([*westsea['source_pages'],*taiqi['source_pages']])), source_unit_ids=list(dict.fromkeys([*westsea['source_unit_ids'],*taiqi['source_unit_ids']])), source_passage_ids=[*westsea['source_passage_ids'],taiqi['id']], context_place_ids=['place-xishan-guishan','place-xishan-taiqi'], related_entry_ids=[*westsea['related_entry_ids'],taiqi['id']], content_note='分号分隔騩山与㤗噐两段摘句，不是连续经文。现图仅复用騩山场景，不描绘文鰩魚、两海全貌或飞行路线；原騩山郭注只释其錞字。', artwork_caption='复用騩山场景 · 不代指文鰩魚或两海行迹。')
    en[westsea['id']].update(name='Western Sea (Western Mountains)', description='The Western Sea is beside Gui and receives the Qi in its passage; in Taiqi it is frequented by Wenyao. This namesake index retains separate contexts, without identifying a modern single sea, coastline or measured migration. The Southern namesake remains separate.', quote=en[westsea['id']]['quote']+' In the separate Taiqi passage, Wenyao frequents the Western Sea, travels in the Eastern Sea and flies at night.', source_locator='Volume 2 · scan pages 45, 56', content_note='The semicolon separates Gui and Taiqi excerpts. The image reuses only Gui’s scene, not Wenyao, both seas or a flight route; Gui’s commentary gloss belongs to that passage alone.', artwork_caption='Reused Gui scene · Not Wenyao or its travel between the seas.')
    taiqi['related_entry_ids'].append(westsea['id'])
    huaijiang = next(p for p in passages if p['id'] == 'passage-xishan-huaijiang')
    you = next(r for _, r in records if r['id'] == 'water-xishan-you-changsha')
    you.update(name='泑水（西山经）', description='泑水在長沙段承泚水北流，在槐江段承丘時水北流；两处同名索引分别保留出处，不据此合并不周泑澤或复原现代水系。原水色黑郭注仅存長沙出处。', quote=you['quote']+'；丘時之水出焉而北流注于泑水', source_locator='卷第二 · 影印页 52、57、58', source_pages=list(dict.fromkeys([*you['source_pages'],*huaijiang['source_pages']])), source_unit_ids=list(dict.fromkeys([*you['source_unit_ids'],*huaijiang['source_unit_ids']])), source_passage_ids=[*you['source_passage_ids'],huaijiang['id']], context_place_ids=['place-xishan-changsha','place-xishan-huaijiang'], related_entry_ids=[*you['related_entry_ids'],huaijiang['id']], content_note='分号分隔長沙/槐江摘句，不是连续经文；長沙水色黑郭注不移作丘時水颜色或全流域描述。')
    en[you['id']].update(name='You River (Western Mountains)', description='The You receives the north-flowing Zi in Changsha and Qiushi in Huaijiang. This namesake index retains both sources without merging You Marsh or reconstructing a modern network. The dark-water gloss remains tied to Changsha.', quote='The Zi flows north into the You; separately, the Qiushi rises and flows north into the You.', source_locator='Volume 2 · scan pages 52, 57, 58', content_note='The semicolon separates Changsha and Huaijiang excerpts. Changsha’s dark-water gloss is not reassigned to Qiushi or an entire basin.')
    huaijiang['related_entry_ids'].append(you['id'])
    zhupi = next(r for _, r in records if r['id'] == 'place-xishan-zhupi-buzhou')
    zhupi.update(name='諸毗之山（西山经）', description='諸毗在不周与槐江两段均为北望所见；槐江段另记槐鬼離侖及鷹鸇所宅。两处上下文分存，不增加现代坐标或新的主线山段。', quote=zhupi['quote']+'；北望諸毗槐鬼離侖居之鷹鸇之所宅也', source_locator='卷第二 · 影印页 52、53、57、58', source_pages=list(dict.fromkeys([*zhupi['source_pages'],*huaijiang['source_pages']])), source_unit_ids=list(dict.fromkeys([*zhupi['source_unit_ids'],*huaijiang['source_unit_ids']])), source_passage_ids=[*zhupi['source_passage_ids'],huaijiang['id']], context_place_ids=['place-xishan-buzhou','place-xishan-huaijiang'], related_entry_ids=[*zhupi['related_entry_ids'],huaijiang['id']], content_note='分号分隔不周/槐江两段摘句，不是连续经文；新增居民只归槐江出处。')
    en[zhupi['id']].update(name='Mount Zhupi (Western Mountains)', description='Zhupi is seen to the north in both Buzhou and Huaijiang. The latter adds Huai-gui Lilun and ying and zhan birds as residents. Both contexts remain separate, without modern coordinates or an extra route stage.', quote='Buzhou overlooks Mount Zhupi to the north; separately, Huaijiang looks north to Zhupi, inhabited by Huai-gui Lilun and ying and zhan birds.', source_locator='Volume 2 · scan pages 52, 53, 57, 58', content_note='The semicolon separates Buzhou and Huaijiang excerpts; the added residents belong to Huaijiang’s source only.')
    huaijiang['related_entry_ids'].append(zhupi['id'])
    finish(passages, records, en, relations)
    for group in ['passages', 'text_entities', 'beasts', 'natural_features']:
        additions = passages if group == 'passages' else [r for g, r in records if g == group]
        addition_ids = {r['id'] for r in additions}
        batches = {r['content_batch'] for r in additions}
        world[group] = [r for r in world[group] if r['id'] not in addition_ids and r.get('content_batch') not in batches] + additions
    world['revision'] = 'myth-world-2026-10-24-xishan-complete-v1'
    write('frontend/public/data/myth-world.json', world)
    write('frontend/src/locale-content-en.json', en)
    write('frontend/src/xishan-relations.json', relations)
    edition_review = {
        'scope': '西山经全篇：首列19山、次二17山、次三22列名山、次四19山，4列总括和篇末总计，共82阅读段；第三列报23山、实际列名22山，里程分列合17521而篇末17517，保留差异。',
        'snapshot_sha256': hashlib.sha256((ROOT / 'data/shanhaijing-reference.json').read_bytes()).hexdigest(),
        'revision_url': chapter['revision_url'], 'scan_pages': list(range(34, 76)),
        'source_unit_page_corrections': PAGE_CORRECTIONS,
        'corrections': [{'source_unit_id': 'source-02-0216', 'captured_page': 58, 'reviewed_page': 57, 'basis': '57页末列已有其中多玉其隂多榣木之有若及注首，58页首续注。'},{'source_unit_id': 'source-02-0207', 'captured_page': 57, 'reviewed_page': 56, 'basis': '56页左列注尾也韓子曰穰嵗之秋承206丰穰注，207虽空正文仍归㤗噐。'},{'source_unit_id': 'source-02-0198', 'captured_page': 56, 'reviewed_page': 55, 'basis': '55页末列已有見則有大兵皷亦化為鵕鳥其，56页首续状如鴟。'},{'source_unit_id': 'source-02-0180', 'captured_page': 54, 'reviewed_page': 53, 'basis': '53页末列已有流注于稷澤其中多白玉是有玉膏其源。'}, {'source_unit_id': 'source-02-0189', 'captured_page': 55, 'reviewed_page': 54, 'basis': '54页末列已有天地鬼神是食是饗君子，55页起服之。'},{'source_unit_id': 'source-02-0171', 'captured_page': 53, 'reviewed_page': 52, 'basis': '52页末列已起不周山，山名郭注跨至53页首西北不周風。'},{'source_unit_id': 'source-02-0162', 'captured_page': 52, 'reviewed_page': 51, 'basis': '51页末列已起崇吾并记北望冡遂，52页首续南望。'},{'source_unit_id': 'source-02-0144', 'captured_page': 50, 'reviewed_page': 49, 'basis': '49页末列牛及犳音注承接𢇨陽段，50页起衆獸。'},
                        {'source_unit_id': 'source-02-0153', 'captured_page': 51, 'reviewed_page': 50, 'basis': '50页最末列为西皇兽类及麋注；51页起萊山。'},
                        {'source_unit_id': 'source-02-0137', 'captured_text': '其状如猿', 'reviewed_text': '其状如猨', 'basis': '49页朱厭形貌字为猨；阅读引文按影印补作猨，captured_text与原快照保留猿。'},
                        {'source_unit_id': 'source-02-0135', 'captured_page': 49, 'reviewed_page': 48, 'basis': '48页最末列其中多丹粟接鳥危水西注赤水；49页起小次山，快照不改写。'},
                        {'source_unit_id': 'source-02-0126', 'captured_page': 48, 'reviewed_page': 47, 'basis': '47页末为有鳥焉其状如翟而五彩文名曰及翟注，48页从鸞鳥续；原捕获页号保留。'},
                        {'source_unit_id': 'source-02-0117', 'captured_page': 47, 'reviewed_page': 46, 'basis': '數歴山起句至其下多位于46页末，47页从銀字续接；原捕获页号保留。'},
                        {'source_unit_id': 'source-02-0108', 'captured_page': 46, 'reviewed_page': 45, 'basis': '45页末列之属也承接嬰注；46页从其餘十七山起，快照不改。'},
                        {'source_unit_id': 'source-02-0099', 'captured_page': 45, 'reviewed_page': 44, 'basis': '影印44页最末列为火；45页从騩山起，电子快照不改。'},
                        {'source_unit_id': 'source-02-0090', 'captured_page': 44, 'reviewed_page': 43,
                         'basis': '影印43页末列可见食之已癭及或作癎郭注；44页录文起于黄山，原快照不改写。'},
                        {'source_unit_id': 'source-02-0081', 'captured_page': 43, 'reviewed_page': 42,
                         'basis': '影印42页末列可见蘼蕪名曰杜衡可以走馬食及郭注，43页仅续之已癭。原快照不改写。'},
                        {'source_unit_id': 'source-02-0072', 'captured_page': 42, 'reviewed_page': 41,
                         'basis': '影印41页末列可见端獸多犀兕熊羆鳥，42页从多白翰续接。'},
                        {'source_unit_id': 'source-02-0009', 'captured_page': 35, 'reviewed_page': 34,
                         'basis': '影印第34页左列可见“如山雞黑身赤足可以已𦢊”；第35页起首为太華山。原快照不改写。'},
                        {'source_unit_id': 'source-02-0018', 'captured_page': 36, 'reviewed_page': 35,
                         'basis': '“鳥多赤鷩”与首段郭注位于影印35页左列；郭注“作鼈”续行位于36页。'},
                        {'source_unit_id': 'source-02-0027', 'captured_page': 37, 'reviewed_page': 36,
                         'basis': '“翠而赤喙可以禦火”与对应郭注位于影印36页左列；37页正文起于石脆山。'},
                         {'source_unit_id': 'source-02-0063', 'captured_page': 41, 'reviewed_page': 40,
                          'basis': '影印40页末列可见“又西百七十里曰南山上多丹粟丹水出焉北”，41页续“流注于渭獸多猛豹”。'},
                         {'source_unit_id': 'source-02-0036', 'captured_page': 38, 'reviewed_page': 37,
                         'basis': '影印37页左列末行可见“北流注于招水其中多䰷魚其狀如”，38页首续“鼈其音如羊”。'},
                         {'source_unit_id': 'source-02-0054', 'captured_page': 40, 'reviewed_page': 39,
                          'basis': '影印39页末列可见“又西七十里曰羭次之山漆水出焉”，40页续“北流注于渭”。'},
                         {'source_unit_id': 'source-02-0045', 'captured_page': 39, 'reviewed_page': 38,
                         'basis': '影印38页左列可见“竹箭多蒼玉丹水出焉東南流注”，39页首续“于洛水”。'}],
        'text_corrections': [{'source_unit_id': 'source-02-0217', 'captured': '⟦缺字图:鬼⟧', 'reviewed': '鬼', 'basis': '58页核鬼字，只补阅读层。'}, {'source_unit_id': 'source-02-0219', 'captured': '⟦缺字图:鬼⟧', 'reviewed': '鬼', 'basis': '58页核鬼字，只补阅读层。'}, {'source_unit_id': 'source-02-0220', 'captured': '⟦缺字图:搏⟧', 'reviewed': '摶', 'basis': '58页手旁專声字，只补阅读层，原标签保留。'}, {'source_unit_id': 'source-02-0221', 'captured': '⟦缺字图:滛⟧', 'reviewed': '滛', 'basis': '58页核滛字，只补阅读层。'},{'source_unit_id': 'source-02-0189', 'captured': '⟦缺字图:鬼⟧', 'reviewed': '鬼', 'basis': '54页末列核鬼字，仅阅读引文补录，捕获层保留标记。'},{'source_unit_id': 'source-02-0163', 'captured': '⟦缺字图:搏⟧', 'reviewed': '摶', 'basis': '52页手旁專声字据影印补阅读引文，捕获缺字标记保留。'},{'source_unit_id': 'source-02-0143', 'captured': '犀兕虎豹㸲', 'reviewed': '犀兕虎犳㸲', 'basis': '49页正文为犳且末列附犳音之樂反；仅阅读引文补犳，captured_text和快照保留豹。'},
                             {'source_unit_id': 'source-02-0150', 'captured': '⟦缺字图:蕙⟧棠', 'reviewed': '蕙棠', 'basis': '50页可辨蕙棠；仅阅读引文恢复蕙，captured_text与快照保留缺字图。'},
                             {'source_unit_id': 'source-02-0094', 'captured': '人舌⟦缺字图:能⟧言', 'reviewed': '人舌能言',
                              'basis': '影印44页可辨能字，只修阅读引文，captured_text及快照保留缺字图。'},
                             {'source_unit_id': 'source-02-0070', 'captured': '沔⟦缺字图:囂⟧', 'reviewed': '沔囂',
                              'basis': '影印41页确认此字为囂，是下一条囂水之名；只修复阅读引文，captured_text与快照保留缺字图。'},
                             {'source_unit_id': 'source-02-0045', 'captured': '東⟦缺字图:南⟧流注', 'reviewed': '東南流注',
                              'basis': '影印38页左列确认缺字图为南；只修正阅读引文，原始快照与captured_text保留。'}],
        'reading_notes': [{'entry_id': 'passage-xishan-guishan', 'source_unit_id': 'source-02-0100', 'basis': '影印45页山名音注有隗囂之隗，快照省囂；注栏保留快照并明示省缺，不冒称注文逐字完整。'},
                          {'entry_id': 'bird-xishan-lei-cuishan', 'source_unit_id': 'source-02-0098', 'basis': '底本作西首，保留；双首配图参《古今图书集成·禽虫典》卷53鸓条两首四足引文，显式注明异文。', 'comparison_url': 'https://zh.wikisource.org/wiki/欽定古今圖書集成/博物彙編/禽蟲典/第053卷#鸓圖'},
                          {'entry_id': 'animal-xishan-she-cuishan', 'source_unit_id': 'source-02-0098', 'basis': '有香承接0097麝似獐而小，不移给鸓；音壘属鸓。'},
                          {'entry_id': 'beast-xishan-min-huangshan', 'source_unit_id': 'source-02-0094',
                           'basis': '影印44页音敏小注位于𤛎名后、鸚䳇正文前；虽附0094快照单元，释音属于前兽，不转给鸟名。'},
                          {'entry_id': 'water-xishan-qian-dashi', 'source_unit_id': 'source-02-0067',
                           'basis': '影印41页郭注音潜；英文采用Qian，中文涔字与岀字形保留。'},
                          {'entry_id': 'passage-xishan-dashi', 'source_unit_id': 'source-02-0066',
                           'basis': '影印榖字下另见榖構木小注，电子快照未收；注栏保留快照并用content_note说明，不猜补或宣称郭注逐字无缺。'},
                          {'entry_id': 'water-xishan-zhao-ying', 'source_unit_id': 'source-02-0036',
                           'basis': '郭注音韶；英文采用Shao，中文保留底本招字，稳定ID不变。'}],
        'heading_unit_ids': ['source-02-0001', 'source-02-0002'],
        'limits': '首列十九山段及总括、西次二经十七山段及总括、西次三经崇吾、長沙、不周、峚、鍾、㤗噐、槐江段的段界、页码已对照34—58页影印；注文保留电子录文并分列，不是多版本逐字校勘定本。䳋、𦢊、𧔥等保留所据底本字形。source-02-0017注文中的替代字符在阅读卡显示为显式待核标记，不猜补。竹山南字缺字图仅在阅读引文补录；source-02-0048注文快照未含影印能字，郭注不宣称逐字无缺。羭次山名下的音注快照仅存音字，未猜补；末尾无正文的单元60仍归本段。',
        'unresolved_commentary': [{'source_unit_id': 'source-02-0017', 'captured': '㻬琈玉名所未詳也\ufffd浮两音', 'display_marker': '〔录文缺字待核〕'},
                                  {'source_unit_id': 'source-02-0054', 'captured': '音', 'display_marker': '音〔录文缺字待核〕'}],
        'passages': [{'id': p['id'], 'source_unit_ids': p['source_unit_ids'], 'source_span': p['source_span'], 'status': p['review_status']} for p in passages],
        'entry_ids': [r['id'] for _, r in records],
    }
    edition_review['limits'] = '西山经全篇正文段界、形貌和流向已对照34—75页影印；经文、捕获快照、郭注和编辑说明分存。不是多版本逐字校勘定本，电子注文的未确认缺字与异文保留并明示。第三列报23山而实际列名22、各列里程合17521与篇末17517的差异保留，不补山或改数。'
    edition_review['corrections'][:0] = [{'source_unit_id': f'source-02-{n:04}', 'captured_page': 59+(n-225)//9, 'reviewed_page': 58+(n-225)//9, 'basis': '逐页核影印末列和次页首列；此单元实在前页，捕获快照页码不改。'} for n in range(225, 370, 9)]
    edition_review['text_corrections'].append({'source_unit_id':'source-02-0343', 'captured':'⟦缺字图:⿰氵𭝠--𣾰⟧', 'reviewed':'𣾰', 'basis':'72页水旁异体只补阅读层，保留原缺字图标签，不定现代树种或古读。'})
    write('data/xishan-edition-review.json', edition_review)
    print(f'Built {len(passages)} reviewed Western passages and {len(records)} independent entries')


if __name__ == '__main__':
    build()

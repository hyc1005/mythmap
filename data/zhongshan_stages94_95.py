"""Eighth-range opening: separate main text, commentary and uncertain forms."""
from zhongshan_next30 import R

ROWS = [
    R('r08-jing', '景山', 'Mount Jing (eighth-range opening)',
      '中次八荆山首景山，上多金玉、杼檀。雎水东南注江，多丹粟、文鱼；文鱼郭注仅有斑，不借其他篇文鳐形。地名音注与古郡县说分别存，不换算现代坐标。',
      'The eighth range begins at Mount Jing, with gold and jade above and zhu and tan trees. Ju water rises here and flows southeast into the Jiang, with dansu and patterned fish.',
      'Guo Pu only adds markings for the fish. Its independent body form remains unspecified, without borrowing Wenyao anatomy from another book. Historical place-name and pronunciation glosses remain textual.'),
    R('r08-jingshan', '荆山', 'Mount Jingshan (northeast of Jing)',
      '景山东北百里荆山，阴铁阳赤金；犛牛郭注旄牛属黑色，虎豹只列名。松柏竹橘櫾分别录，櫾似橘而大皮厚味酸据注。漳水东南注雎，多黄金鮫鱼；鮫注跨300—301，皮珠文、长尾及毒为古述，不强定现代鲨或鳐。閭麋原词保留及似鹿而大注，不强拆物种。297实际在34页末。',
      'A hundred li northeast is Mount Jingshan, with iron on its shaded side and red metal on its sunny side. It has li cattle, tigers and leopards, song and bai trees, bamboo, ju and you. Zhang water rises here and flows southeast into Ju water, with gold and Jiao fish; the text also lists lümi.',
      'Guo Pu describes li cattle as black mao-cattle kind and you as larger than ju, with thick peel and a sour taste. The Jiao gloss spans 300–301, describing patterned tough skin, a long tail and an ancient venom claim, without settling modern shark or ray identity. Lümi and its larger-than-deer comparison retain uncertain word division. Unit 297 is on scan 34, followed by scan 35.')
]
LINKS = []
SHARES = []


def entities(E):
    LINKS.clear(); SHARES.clear(); out = []
    def add(s, k, key, name, en, q, eq, cn, note='', **extra):
        out.append(E(s, k, key, name, en, q, cn, eq, (eq + ' ' + note).strip(), **extra))
        return out[-1]['id']
    def product(s, key, name, en, q, eq, kind='material', **extra):
        return add(s, kind, key, name, en, q, eq, '依本段物产及原文位置存录，不强定现代种属、矿物成分或坐标。', **extra)
    def unknown(s, key, name, en, q, eq, cn, kind='animal', **extra):
        return add(s, kind, key, name, en, q, eq, cn, 'Insufficient independent form evidence; the placeholder is not a depiction.', unknown=True, **extra)
    s = 'r08-jing'
    product(s, 'gold-jing8', '金（景山）', 'Gold (Jing)', '其上多金玉', 'Gold is abundant above.')
    product(s, 'jade-jing8', '玉（景山）', 'Jade (Jing)', '其上多金玉', 'Jade is abundant above.')
    product(s, 'zhu-jing8', '杼（景山）', 'Zhu trees (Jing)', '其木多杼', 'Zhu trees are abundant.', kind='plant', commentary='杼音椽柱之柱', en_commentary='Guo Pu supplies the zhu pronunciation comparison.')
    product(s, 'tan-jing8', '檀（景山）', 'Tan trees (Jing)', '其木多杼檀', 'Tan trees are abundant.', kind='plant')
    ju = add(s, 'water', 'ju-range8', '雎水（中次八文本索引）', 'Ju water (eighth-range textual index)', '雎水出焉東南流注于江', 'Ju water rises here and flows southeast into the Jiang.', '景山出水、东南注江；与后文漳水入雎分存，历史睢/沮字形只作郭注，不强定现代河道。', commentary='雎音癰疽之疽；今睢水出新城魏昌縣東南發阿山東南至南郡枝江縣入江也', en_commentary='Guo Pu gives pronunciation and a historical river route, retaining the captured spelling.')
    jiang = add(s, 'water', 'jiang-range8', '江（中次八受水文本索引）', 'Jiang (eighth-range recipient index)', '東南流注于江', 'Ju water flows southeast into the Jiang.', '本段受水体江单列，不以文学方位换算现代定位。')
    LINKS.append((ju, jiang))
    product(s, 'dansu-jing8', '丹粟（雎水）', 'Dansu (Ju water)', '其中多丹粟', 'Dansu is abundant in this water account.')
    wen = unknown(s, 'wenfish-jing8', '文魚（景山雎水）', 'Patterned fish (Jing, Ju water)', '多文魚', 'Patterned fish are abundant.', '郭注仅有斑，无独立全身形貌；不与异篇文鳐合并，不据名字补飞翼或足。', kind='beast', commentary='有斑', en_commentary='Guo Pu only says that there are markings.', water=True)
    LINKS.append((ju, wen))
    s = 'r08-jingshan'
    product(s, 'iron-jingshan8', '鐵（荆山阴）', 'Iron (Jingshan shaded side)', '其隂多鐵', 'Iron is abundant on the shaded side.')
    product(s, 'red-metal-jingshan8', '赤金（荆山阳）', 'Red metal (Jingshan sunny side)', '其陽多赤金', 'Red metal is abundant on the sunny side.')
    add(s, 'beast', 'li-cattle-jingshan8', '犛牛（荆山）', 'Li cattle (Jingshan)', '其中多犛牛', 'Li cattle are abundant.', '郭注旄牛属、黑色为形色依据；图取黑色长毛牛形，双角四蹄、尾、比例及姿态为艺术解释，不强定现代犛牛亚种。', 'The black mao-cattle comparison follows commentary. Horn curvature, hooves, tail details, proportions and pose are artistic, without a modern subspecies claim.', commentary='旄牛属也黑色出西南徼外也音狸一音來', en_commentary='Guo Pu describes black mao-cattle kind and supplies historical distribution and pronunciation glosses.')
    unknown(s, 'tiger-jingshan8', '虎（荆山）', 'Tigers (Jingshan)', '多虎豹', 'Tigers are abundant.', '本段仅列虎名，无独立细部；不借他篇怪兽形体。')
    unknown(s, 'leopard-jingshan8', '豹（荆山）', 'Leopards (Jingshan)', '多虎豹', 'Leopards are abundant.', '本段仅列豹名，无独立细部；不借他篇怪兽形体。')
    for key, name, en, q in [('song', '松', 'Song trees', '其木多松栢'), ('bai', '栢', 'Bai trees', '其木多松栢'), ('bamboo', '竹', 'Bamboo', '其草多竹'), ('ju', '橘', 'Ju trees', '多橘櫾')]:
        product(s, key+'-jingshan8', name+'（荆山）', en+' (Jingshan)', q, en+' are abundant.', kind='plant')
    product(s, 'you-jingshan8', '櫾（荆山）', 'You (Jingshan)', '多橘櫾', 'You is abundant.', kind='plant', commentary='櫾似橘而大也皮厚味酸', en_commentary='Guo Pu compares you with larger ju, with thick peel and sour taste.')
    zhang = add(s, 'water', 'zhang-jingshan8', '漳水（荆山）', 'Zhang water (Jingshan)', '漳水出焉而東南流注于雎', 'Zhang water rises here and flows southeast into Ju water.', '出荆山东南注雎，郭注古县与沮水写法分存；不以近音字合并现代水系。', commentary='出荆山至南郡當陽縣入沮水', en_commentary='Guo Pu records a historical route with the Ju recipient written differently.')
    SHARES.append((ju, s, '漳水出焉而東南流注于雎', 'Zhang water flows southeast into Ju water.'))
    LINKS.append((zhang, ju))
    product(s, 'gold-zhang8', '黃金（漳水）', 'Gold (Zhang water)', '其中多黃金', 'Gold is abundant in this water account.')
    jiao = unknown(s, 'jiao-zhang8', '鮫魚（漳水）', 'Jiao fish (Zhang water)', '多鮫魚', 'Jiao fish are abundant.', '郭注鮫鮒魚類跨300—301，皮珠文坚、尾三四尺、末有毒及皮用途照录；全形仍不足，不强套现代鲨鱼或鳐鱼。', kind='beast', commentary='鮫鮒；魚𩔖也皮有珠文而堅尾長三四尺末有毒螫人皮可飾刀劒口錯治材角今臨海郡亦有之音交', en_commentary='The gloss spans 300–301: a fish-kind comparison, tough patterned skin, a tail of three to four chi, an ancient venom claim and historical skin uses. These do not establish a modern shark or ray.', water=True)
    LINKS.append((zhang, jiao))
    unknown(s, 'lvmi-jingshan8', '閭麋（荆山原词）', 'Lümi (Jingshan, captured term)', '其獸多閭麋', 'The text lists lümi among the beasts.', '原词閭麋与郭注似鹿而大分存，词义及分合暂不强定，不擅拆两个独立物种或补鹿角。', commentary='似鹿而大也', en_commentary='Guo Pu compares the form with a larger deer; uncertain word division is retained.')
    return out

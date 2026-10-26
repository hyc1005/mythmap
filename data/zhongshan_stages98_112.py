"""Eighth-range stages 98–112, with scan corrections and local form evidence."""
from zhongshan_next30 import R

ROWS = [
    R('r08-yizhu', '冝諸之山', 'Mount Yizhu',
      '东北二百里冝諸，上多金玉，下多青䨼。洈水南注漳，水中白玉单列；郭注所述古郡县与入江路线另存，不覆盖正文南注漳，也不按现代地图定位。',
      'Two hundred li northeast is Mount Yizhu, with gold and jade above and qinghu below. Wei water rises here and flows south into the Zhang; white jade is abundant in it.',
      'The Wei pronunciation and historical route to the Jiang are commentary, kept distinct from the main-text southward flow into the Zhang. White jade belongs to the water account, not an additional mountain-top deposit.'),
    R('r08-lun', '綸山', 'Mount Lun',
      '东北三百五十里綸山，多梓柟桃枝柤栗橘櫾，兽列閭麈麢㚟。柤似棃而酢濇为郭注；㚟似菟而鹿脚青色，图依兔状鹿足青色，四足分蹄、长耳比例及姿态为解释。音勑略反跨314—315连读，两块均在36页，其他兽仅名留空。',
      'Three hundred and fifty li northeast is Mount Lun, with zi, nan, taozhi, zha, li, ju and you trees, and animals named lüchen, ling and chuo.',
      'Guo Pu compares zha with a sour, astringent pear-like fruit. Chuo resembles a hare with deer feet and blue-green coloring. Four cloven-hoofed legs, ear proportions and pose are artistic. The pronunciation gloss continues across units 314–315, both on scan 36. The other animal names supply no independent detailed form.'),
    R('r08-lugui', '陸䣀之山', 'Mount Lugui',
      '东北二百里陸䣀，上多㻬琈玉，下多堊，木多杻橿。䣀读音按郭注跪告之跪记录，不并陆吾神或其他近字山。㻬琈之玉跨316—317，仍属上部物产。',
      'Two hundred li northeast is Mount Lugui, with tufu jade above, e below, and niu and jiang trees.',
      'The jade name continues across units 316–317. The mountain-name pronunciation follows the commentary comparison with gui; no modern mineral or place identification is imposed.'),
    R('r08-guang', '光山', 'Mount Guang',
      '东百三十里光山，上多碧，下多木。计蒙人身龙首，常游漳渊，出入必有飘风暴雨；人身与龙首为图像依据，衣装、双臂双腿、龙角须、配色与姿态为艺术解释，不画蛇身、翼或虎爪。漳渊单列，不强并漳水或睢漳之渊。',
      'A hundred and thirty li east is Mount Guang, with bi above and many trees below. Jimeng dwells here, with a human body and a dragon head, habitually wandering in the Zhang pool; its entering and leaving bring whirling wind and torrential rain.',
      'Human body and dragon head are explicit. Clothing, two human arms and legs, dragon horn and whisker design, colors and pose are artistic. The illustration adds no serpent body, wings or tiger paws. The pool and ancient weather claim remain separate from modern geography.'),
    R('r08-qi', '岐山', 'Mount Qi',
      '东百五十里岐山，阳赤金、阴白珉，上金玉、下青䨼，多樗。白珉似玉石郭注跨321—322连读。神涉𧕦人身方面三足；三条人腿须可数，面形、衣装、手臂与配色为艺术解释，不并计蒙或𧕛围，不加龙首羊角虎爪。',
      'A hundred and fifty li east is Mount Qi, with red metal on its sunny side, white min on its shaded side, gold and jade above, qinghu below, and chu trees. Shetuo dwells here with a human body, a square face and three feet.',
      'The min gloss, comparing it with jade-like stone, continues across units 321–322. The deity illustration makes three human legs and feet separately countable. Arm count, clothing, facial proportions, colors and pose are artistic; the variant name character remains commentary.'),
    R('r08-tong', '銅山', 'Mount Tong',
      '东百三十里銅山，上多金银铁，木列榖柞柤栗橘櫾，豹仅列名不补形。324实际37页末，325续38页；山名有铜不等于正文另列铜矿，不借綸山柤注覆盖本地植物。',
      'A hundred and thirty li east is Mount Tong, with gold, silver and iron above; gu, zuo, zha, li, ju and you trees; and leopards.',
      'Unit 324 begins on scan 37 and the account continues on 38. The mountain name adds no separately stated copper deposit. Leopards are only named, and the earlier Lun gloss is not silently transferred here.'),
    R('r08-mei', '羙山', 'Mount Mei',
      '东北一百里羙山，兽列兕牛、閭麈、豕鹿，上多金、下青䨼。保留閭麈分合疑点；本段动物无独立细部，不借他篇犀角、牛形或鹿角强画像。羙字依本底本保留。',
      'A hundred li northeast is Mount Mei. It lists si, cattle, lüchen, pigs and deer, with gold above and qinghu below.',
      'The captured Mei character and uncertain lüchen word division are retained. The animal list does not provide independent detailed forms, so no horns or other anatomy are borrowed from another passage.'),
    R('r08-dayao', '大堯之山', 'Mount Dayao',
      '东北百里大堯，多松栢梓桑机，草多竹，兽多豹虎麢㚟。本段㚟仅列名，不把綸山郭注默作本地正文；四项动物均留占位。',
      'A hundred li northeast is Mount Dayao, with song, bai, zi, mulberry and ji trees, bamboo in the grass list, and leopards, tigers, ling and chuo beasts.',
      'These animal names supply no local independent form description. In particular, Lun commentary is not silently inserted into this main text or used to assert that the two Chuo accounts have identical anatomy.'),
    R('r08-ling', '靈山', 'Mount Ling',
      '东北三百里靈山，上多金玉、下青䨼，木多桃李梅杏。梅注似杏而酢按捕获原词分存，不据现代植物分类合并梅与杏，也不将郭注变成本山独立新物种。',
      'Three hundred li northeast is Mount Ling, with gold and jade above, qinghu below, and tao, li, mei and xing trees.',
      'The captured gloss compares mei with sour xing-like fruit. Comparison and product accounts remain separate; no modern botanical identity or additional local species is inferred.'),
    R('r08-long', '龍山', 'Mount Long',
      '东北七十里龍山，上多寓木与碧，下多赤锡，草列桃枝鈎端。郭注寓木为寄生、一名宛童并引尔雅，不借龙名补龙兽。332—333均38页，原捕获333为39页另存。',
      'Seventy li northeast is Mount Long, with yumu and bi above, red tin below, and taozhi and gouduan in the grass list.',
      'Guo Pu glosses yumu as parasitic growth, also called Wantong, citing Erya. No host, leaf or fruit form is supplied. Units 332–333 are both on scan 38; the dragon mountain name adds no dragon creature.'),
    R('r08-heng', '衡山', 'Mount Heng',
      '东南五十里衡山，上多寓木榖柞及黄堊白堊。334捕获寓不，据39页木字仅阅读层恢复为寓木；不作全书不字替换。榖与柞各列，堊颜色分存，不强定现代矿物或现代衡山。',
      'Fifty li southeast is Mount Heng, with yumu, gu and zuo trees above, and yellow and white e.',
      'The captured bu in the yumu term is restored to mu from scan 39 in unit 334 only, while original text is preserved. The two e colors remain separate and no modern mountain identification is imposed.'),
    R('r08-shi', '石山', 'Mount Shi (eighth range)',
      '东南七十里石山，上多金、下多青䨼，多寓木。寓木二字跨335—336连读，不因分行拆词；不并其他篇同名石山，不借龍山郭注新增外形。',
      'Seventy li southeast is Mount Shi, with gold above, qinghu below and abundant yumu.',
      'The yumu name continues across units 335–336. This eighth-range account stays separate from other mountains named Shi, without borrowing a host or plant anatomy.'),
    R('r08-ruo', '若山', 'Mount Ruo',
      '南百二十里若山，上多㻬琈玉，又多赭、邽石、寓木与柘。赭为赤土、邽石未详分属不同郭注；若或作前为山名异说，不新增前山阶段，邽石不强定现代矿物。',
      'A hundred and twenty li south is Mount Ruo, with tufu jade above, ochre, Gui stone, yumu and zhe trees.',
      'Guo Pu glosses ochre as red earth and explicitly leaves Gui stone unidentified. Qian is a variant mountain name, not another stage. The mineral and plant accounts remain distinct.'),
    R('r08-zhi', '彘山', 'Mount Zhi',
      '东南一百二十里彘山，多羙石与柘。羙石仅泛称美石，不凭空拆成玉或矿种；山名彘不是本段有猪的物产依据。',
      'A hundred and twenty li southeast is Mount Zhi, with fine stones and zhe trees.',
      'Fine stone is a general product term, not a specified jade or mineral. The pig character in the mountain name supplies no local animal record.'),
    R('r08-yu', '玉山', 'Mount Yu (eighth range)',
      '东南一百五十里玉山，上多金玉、下多碧铁，木多栢。郭注一作楢为栢字异文，单独记录，不把栢楢都算本山实生木；同名玉山不跨篇强合。',
      'A hundred and fifty li southeast is Mount Yu, with gold and jade above, bi and iron below, and bai trees.',
      'You is a commentary variant for the tree name, not a second tree asserted to grow here. This same-name mountain remains an eighth-range textual account, without a cross-book geographic merger.')
]
LINKS = []
SHARES = []


def entities(E):
    LINKS.clear(); SHARES.clear(); out = []
    def add(s, kind, key, name, en, q, eq, cn, note='', **extra):
        suffix = s.removeprefix('r08-') + '8'
        out.append(E(s, kind, key+'-'+suffix, name, en, q, cn, eq, (eq+' '+note).strip(), **extra))
        return out[-1]['id']
    def product(s, key, name, en, q, eq, kind='material', **extra):
        stage_name = next(r['name'] for r in ROWS if r['slug'] == s)
        stage_en = next(r['en_name'] for r in ROWS if r['slug'] == s)
        return add(s, kind, key, name+'（'+stage_name+'）', en+' ('+stage_en+')', q, eq,
                   '按本段原名与方位分别存录；不强定现代种属、成分或坐标。', **extra)
    def products(s, specs, kind='material'):
        for key, name, en, q, eq in specs:
            product(s, key, name, en, q, eq, kind)
    def unknown(s, key, name, en, q):
        return add(s, 'animal', key, name, en, q, en+' occurs in this passage.',
                   '本段仅列名，未给独立细部；词义分合保留，不借他山形貌或现代物种强配图。',
                   'Insufficient independent local form evidence; uncertain word division is retained and the placeholder is not a depiction.', unknown=True)

    s='r08-yizhu'
    products(s, [('gold','金','Gold','其上多金玉','Gold is abundant above.'),
                 ('jade','玉','Jade','其上多金玉','Jade is abundant above.'),
                 ('qinghu','青䨼','Qinghu','其下多青䨼','Qinghu is abundant below.')])
    wei=add(s,'water','wei','洈水（冝諸）','Wei water (Yizhu)','洈水出焉而南流注于漳',
            'Wei water rises here and flows south into the Zhang.',
            '正文南注漳；郭注古路线入江另存，不据古地名坐标化或改写受水体。',
            commentary='音詭；今洈水出南郡東洈山至華容縣入江也',
            en_commentary='Guo Pu supplies gui pronunciation and a historical route from Dongwei mountain to the Jiang via Huarong; this does not overwrite the main-text Zhang recipient.')
    white=product(s,'white-jade','白玉（洈水）','White jade in Wei water','其中多白玉','White jade is abundant in the water account.')
    SHARES.append(('water-zhongshan-zhang-jingshan8',s,'洈水出焉而南流注于漳','Wei water flows south into the Zhang.'))
    LINKS.extend([(wei,'water-zhongshan-zhang-jingshan8'),(wei,white)])
    s='r08-lun'
    products(s,[('zi','梓','Zi trees','其木多梓柟','Zi trees are abundant.'),
                ('nan','柟','Nan trees','其木多梓柟','Nan trees are abundant.'),
                ('taozhi','桃枝','Taozhi','多桃枝','Taozhi is abundant.'),
                ('li','栗','Li trees','多柤栗橘櫾','Li trees are abundant.'),
                ('ju','橘','Ju trees','多柤栗橘櫾','Ju trees are abundant.'),
                ('you','櫾','You trees','多柤栗橘櫾','You trees are abundant.')], 'plant')
    product(s,'zha','柤','Zha trees','多柤栗橘櫾','Zha is abundant.','plant',
            commentary='柤似棃而酢濇',en_commentary='Guo Pu compares zha with a sour, astringent pear-like fruit.')
    unknown(s,'lvchen','閭麈（綸山原词）','Lüchen (Lun, captured term)','其獸多閭麈麢㚟')
    unknown(s,'ling','麢（綸山）','Ling beasts (Lun)','其獸多閭麈麢㚟')
    add(s,'beast','chuo','㚟（綸山）','Chuo (Lun)','其獸多閭麈麢㚟','Chuo occurs in the beast list.',
        '形貌依据是郭注似菟而鹿脚青色；兔状鹿足青色据注，四条分蹄腿、耳长、毛纹、浅色刻线及站姿为艺术解释，不加鹿角或翼。音勑略反跨314—315连续。',
        'Hare-like form, deer feet and blue-green color follow commentary. Four cloven-hoofed legs, ear proportions, fur hatching, light cut strokes and pose are artistic; no antlers or wings are added.',
        commentary='㚟似菟而鹿脚青色音勑；略反',en_commentary='Guo Pu describes a hare-like form with deer feet and blue-green coloring; the pronunciation gloss continues into unit 315.')
    s='r08-lugui'
    products(s,[('tufu-jade','㻬琈之玉','Tufu jade','其上多㻬琈之玉','Tufu jade is abundant above.'),
                ('e','堊','E','其下多堊','E is abundant below.')])
    products(s,[('niu','杻','Niu trees','其木多杻橿','Niu trees are abundant.'),
                ('jiang','橿','Jiang trees','其木多杻橿','Jiang trees are abundant.')],'plant')
    s='r08-guang'
    product(s,'bi','碧','Bi','其上多碧','Bi is abundant above.')
    product(s,'trees','木（未列种）','Unnamed trees','其下多木','Many unnamed trees occur below.','plant')
    pool=add(s,'water','zhang-pool','漳淵（光山）','Zhang pool (Guang)','恒遊于漳淵',
             'Jimeng habitually wanders in the Zhang pool.','神游处漳渊单列；不将渊默并入漳水，亦不并驕山睢漳之渊。')
    god=add(s,'deity','jimeng','計蒙（光山）','Jimeng (Guang)','神計蒙處之其狀人身而龍首恒遊于漳淵出入必有飄風暴雨',
            'Jimeng has a human body and dragon head, wanders in the Zhang pool and brings whirling wind and torrential rain on entering or leaving.',
            '人身龙首据正文；双人臂双人腿、衣装、龙角须、色彩及站姿为艺术解释，不补蛇躯、尾翼、虎爪或气象背景。',
            'Human body and dragon head are explicit; two human arms and legs, clothing, horn and whisker design, colors and pose are artistic. The image adds no serpent body, tail, wings or tiger claws; weather stays a textual claim.')
    LINKS.append((pool,god))
    s='r08-qi'
    products(s,[('red-metal','赤金（阳）','Red metal, sunny side','其陽多赤金','Red metal is abundant on the sunny side.'),
                ('gold','金（上）','Gold above','其上多金玉','Gold is abundant above.'),
                ('jade','玉（上）','Jade above','其上多金玉','Jade is abundant above.'),
                ('qinghu','青䨼（下）','Qinghu below','其下多青䨼','Qinghu is abundant below.')])
    product(s,'white-min','白珉（阴）','White min, shaded side','其隂多白珉','White min is abundant on the shaded side.',
            commentary='石似；玉者音旻',en_commentary='The gloss continues across units 321–322: stone resembling jade, with min pronunciation.')
    product(s,'chu','樗','Chu trees','其木多樗','Chu trees are abundant.','plant')
    add(s,'deity','shetuo','涉𧕦（岐山）','Shetuo (Qi)','神涉𧕦處之其狀人身而方面三足',
        'Shetuo dwells here with a human body, a square face and three feet.',
        '人身、方面、三足据正文，图中三条人腿与三只足分离可数；双臂、衣装、年龄、比例、配色及站姿为解释。不增龙首、羊角虎爪；异字𧔳只存郭注。',
        'A human body, square face and three feet are explicit. Three separate human legs with three feet are visible. Two arms, clothing, age, proportions, colors and pose are artistic; no dragon head, goat horns or tiger paws are added.',
        commentary='徒河切一作𧔳笑逰切',en_commentary='Guo Pu gives pronunciation and a variant name character; these do not describe another deity form.')
    s='r08-tong'
    products(s,[('gold','金','Gold','其上多金銀鐵','Gold is abundant above.'),
                ('silver','銀','Silver','其上多金銀鐵','Silver is abundant above.'),
                ('iron','鐵','Iron','其上多金銀鐵','Iron is abundant above.')])
    products(s,[('gu','榖','Gu trees','其木多榖柞','Gu trees are abundant.'),
                ('zuo','柞','Zuo trees','其木多榖柞','Zuo trees are abundant.'),
                ('zha','柤','Zha trees','柤栗橘櫾','Zha trees are abundant.'),
                ('li','栗','Li trees','柤栗橘櫾','Li trees are abundant.'),
                ('ju','橘','Ju trees','柤栗橘櫾','Ju trees are abundant.'),
                ('you','櫾','You trees','柤栗橘櫾','You trees are abundant.')],'plant')
    unknown(s,'leopard','豹（銅山）','Leopards (Tong)','其獸多豹')
    s='r08-mei'
    for key,name,en,q in [('si','兕','Si beasts','其獸多兕牛'),('cattle','牛','Cattle','其獸多兕牛'),
                          ('lvchen','閭麈','Lüchen','多閭麈'),('pig','豕','Pigs','多豕鹿'),('deer','鹿','Deer','多豕鹿')]:
        unknown(s,key,name+'（羙山）',en+' (Mei)',q)
    products(s,[('gold','金','Gold','其上多金','Gold is abundant above.'),
                ('qinghu','青䨼','Qinghu','其下多青䨼','Qinghu is abundant below.')])
    s='r08-dayao'
    products(s,[('song','松','Song trees','其木多松栢','Song trees are abundant.'),
                ('bai','栢','Bai trees','其木多松栢','Bai trees are abundant.'),
                ('zi','梓','Zi trees','多梓桑','Zi trees are abundant.'),
                ('sang','桑','Mulberry trees','多梓桑','Mulberry trees are abundant.'),
                ('ji','机','Ji trees','多机','Ji trees are abundant.'),
                ('bamboo','竹','Bamboo','其草多竹','Bamboo occurs in the grass list.')],'plant')
    for key,name,en in [('leopard','豹','Leopards'),('tiger','虎','Tigers'),('ling','麢','Ling beasts'),('chuo','㚟','Chuo beasts')]:
        unknown(s,key,name+'（大堯）',en+' (Dayao)','其獸多豹虎麢㚟')
    s='r08-ling'
    products(s,[('gold','金','Gold','其上多金玉','Gold is abundant above.'),
                ('jade','玉','Jade','其上多金玉','Jade is abundant above.'),
                ('qinghu','青䨼','Qinghu','其下多青䨼','Qinghu is abundant below.')])
    products(s,[('tao','桃','Tao trees','其木多桃李梅杏','Tao trees are abundant.'),
                ('li','李','Li trees','其木多桃李梅杏','Li trees are abundant.'),
                ('xing','杏','Xing trees','其木多桃李梅杏','Xing trees are abundant.')],'plant')
    product(s,'mei','梅','Mei trees','其木多桃李梅杏','Mei trees are abundant.','plant',
            commentary='梅似杏而酢也',en_commentary='The captured commentary compares mei with sour xing-like fruit; the comparison does not assert botanical identity.')
    s='r08-long'
    product(s,'yumu','寓木','Yumu','上多寓木','Yumu is abundant above.','plant',
            commentary='寄生也一名宛童見爾雅',en_commentary='Guo Pu glosses parasitic growth, also named Wantong, citing Erya; no host or detailed anatomy is given.')
    products(s,[('bi','碧','Bi','其上多碧','Bi is abundant above.'),
                ('red-tin','赤錫','Red tin','其下多赤錫','Red tin is abundant below.')])
    products(s,[('taozhi','桃枝','Taozhi','其草多桃枝鈎端','Taozhi occurs in the grass list.'),
                ('gouduan','鈎端','Gouduan','其草多桃枝鈎端','Gouduan occurs in the grass list.')],'plant')
    s='r08-heng'
    products(s,[('yumu','寓木','Yumu','上多寓木榖柞','Yumu is abundant above; the captured character is restored from the scan.'),
                ('gu','榖','Gu trees','上多寓木榖柞','Gu trees are abundant above.'),
                ('zuo','柞','Zuo trees','上多寓木榖柞','Zuo trees are abundant above.')],'plant')
    products(s,[('yellow-e','黄堊','Yellow e','多黄堊白堊','Yellow e is abundant.'),
                ('white-e','白堊','White e','多黄堊白堊','White e is abundant.')])
    s='r08-shi'
    products(s,[('gold','金','Gold','其上多金','Gold is abundant above.'),
                ('qinghu','青䨼','Qinghu','其下多青䨼','Qinghu is abundant below.')])
    product(s,'yumu','寓木','Yumu','多寓木','Yumu is abundant; its name continues across two units.','plant')
    s='r08-ruo'
    product(s,'tufu-jade','㻬琈之玉','Tufu jade','其上多㻬琈之玉','Tufu jade is abundant above.')
    product(s,'ochre','赭','Ochre','多赭','Ochre is abundant.',commentary='赤土',en_commentary='Guo Pu glosses red earth.')
    product(s,'gui-stone','邽石','Gui stone','多邽石','Gui stone is abundant.',commentary='未詳',en_commentary='Guo Pu explicitly leaves this unidentified.')
    products(s,[('yumu','寓木','Yumu','多寓木','Yumu is abundant.'),
                ('zhe','柘','Zhe trees','多柘','Zhe trees are abundant.')],'plant')
    s='r08-zhi'
    product(s,'fine-stone','羙石','Fine stones','多羙石','Fine stones are abundant.')
    product(s,'zhe','柘','Zhe trees','多柘','Zhe trees are abundant.','plant')
    s='r08-yu'
    products(s,[('gold','金','Gold','其上多金玉','Gold is abundant above.'),
                ('jade','玉','Jade','其上多金玉','Jade is abundant above.'),
                ('bi','碧','Bi','其下多碧鐵','Bi is abundant below.'),
                ('iron','鐵','Iron','其下多碧鐵','Iron is abundant below.')])
    product(s,'bai','栢','Bai trees','其木多栢','Bai trees are abundant.','plant',
            commentary='一作楢',en_commentary='You is recorded as a variant tree name, not an additional local species.')
    return out

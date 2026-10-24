"""Reviewed continuation of Western ranges three and four; source snapshot stays immutable."""

STAGES = [
    ('kunlun', '崑崙之丘', 'Kunlun Hill', 223, 241, 3,
     '槐江西南四百里至崑崙，是帝之下都，陸吾司天之九部及帝之囿时。土螻、欽原、鶉鳥与沙棠、薲草分别记述；河、赤、洋、黑四水各有方向与所注。末句怪鸟兽不按郭注例子另造正文物种。',
     'Four hundred li southwest is Kunlun, the emperor’s lower capital. Luwu has a tiger body, nine tails, a human face and tiger claws, overseeing the nine heavenly divisions and the seasons of the imperial garden. Tulou resembles a four-horned sheep and eats people. Qinyuan resembles a bee as large as a mandarin duck; its sting kills birds and beasts and withers trees. Chun birds oversee the emperor’s equipment. Shatang resembles tang, with yellow flowers and red, plum-flavored, seedless fruit; eating it is said to prevent drowning. Pin grass resembles kui and tastes like scallion; eating it relieves fatigue. The He flows south, then east to Wuda; the Chi southeast to Fantian’s water; the Yang southwest to Choutu’s water; the Hei west to Dayu. Many strange birds and beasts occur here.'),
    ('leyou', '樂游之山', 'Mount Leyou', 242, 244, 3,
     '崑崙向西三百七十里至樂游。桃水西注稷澤，多白玉，水中滑魚蛇状四足、食鱼；不与其他鱼或同名稷泽的形貌混合。',
     'Three hundred and seventy li west is Leyou. The Tao rises here and flows west into Jize. There is much white jade, and the water contains many Huayu, snake-shaped with four feet, which eat fish.'),
    ('luomushan', '蠃母之山', 'Mount Luomu', 245, 247, 3,
     '从樂游向西水行四百里到流沙，再二百里至蠃母。神長乗人状犳尾，司此山，称天之九德；山上多玉，下多青石而无水。山名蠃母不作槐江水中蠃母的形貌。',
     'Traveling west by water for four hundred li reaches Liusha; another two hundred li reaches Luomu. Changcheng oversees it and embodies heaven’s nine virtues. The deity is human-shaped with a leopard tail. Jade is abundant above, blue-green stone below, and there is no water.'),
    ('yushan', '玉山', 'Mount Yu', 248, 262, 3,
     '向西三百五十里至玉山，西王母人状豹尾虎齿、善啸、蓬发戴胜，司天之厉与五残。狡犬状豹文牛角，胜遇翟状而赤、食鱼；各自声音及灾异分开，穆王长注不当作正文事件。',
     'Three hundred and fifty li west is Mount Yu, home of Xiwangmu. She is human-shaped, with a leopard tail and tiger teeth, a powerful whistle, disheveled hair and a sheng headdress, overseeing heavenly calamities and the five destructive forces. Jiao resembles a dog with leopard markings and ox-like horns, sounds like a barking dog, and its appearance foretells a plentiful year. Shengyu is a red, zhai-shaped bird that eats fish and sounds like lu; its appearance foretells flooding.'),
    ('xuanyuan', '軒轅之丘', 'Xuanyuan Hill', 263, 265, 3,
     '玉山向西四百八十里至軒轅之丘，无草木。洵水南注黑水，其中多丹粟、青雄黄；黄帝娶西陵氏的解释属于郭注。',
     'Four hundred and eighty li west is Xuanyuan Hill, without vegetation. The Xun rises here and flows south into the Hei. Its waters contain much dansu and qing xionghuang.'),
    ('jishi', '積石之山', 'Mount Jishi', 266, 268, 3,
     '向西三百里至積石，山下有石门，河水冐而西流。万物无不有焉保留为概称，不据此穷举未列物种；郭注冐猶覆及古地理另列。',
     'Three hundred li west is Jishi. Beneath it stands a stone gate; the He passes under a covering and flows west. The text says that nothing is absent from this mountain, without enumerating additional species.'),
    ('changliu', '長留之山', 'Mount Changliu', 269, 272, 3,
     '向西二百里至長留，神白帝少昊居之，兽皆文尾、鸟皆文首，多文玉石。員神磈氏之宫及主司反景另存，不擅将两神合为同一身份或补全形貌。',
     'Two hundred li west is Changliu, inhabited by the White Emperor Shaohao. Its beasts have patterned tails and its birds patterned heads; patterned jade and stone are abundant. It is the palace of the yuan deity Weishi, who oversees the returning light. The commentary explains the light as the eastern reflection after sunset.'),
    ('zhange', '章莪之山', 'Mount Zhange', 273, 277, 3,
     '向西二百八十里至章莪，无草木，多瑶碧，所为甚怪。狰赤豹状五尾一角，音如击石；畢方鹤状一足、赤文青质白喙，鸣自叫，见则邑有譌火。',
     'Two hundred and eighty li west is Zhange, without vegetation, rich in yaobi and unusual things. Zheng resembles a red leopard with five tails and one horn, sounding like struck stones. Bifang resembles a crane, with one foot, red markings, a blue-green body and a white beak. It calls its own name; its appearance foretells an uncanny fire in the settlement.'),
    ('yinshan3', '隂山（西次三经）', 'Mount Yin (third range)', 278, 280, 3,
     '向西三百里至本列隂山。濁浴水南注蕃澤，水中多文貝。天狗狸状白首，音如榴榴，可以御凶；不并入西次四经首山隂山。',
     'Three hundred li west is Yin. The Zhuoyu rises here and flows south into Fan Marsh, containing many patterned shells. Tiangou resembles a li with a white head and sounds like liuliu; it is said to ward off harm. This is distinct from the first mountain of the fourth range.'),
    ('futang', '符愓之山', 'Mount Fuyang', 281, 282, 3,
     '向西二百里至符愓，上多㯶柟，下多金玉。神江疑居之，山多怪雨，为风云所出；江疑没有形貌，不借英招或其他神祇器官。',
     'Two hundred li west is Fuyang, with zong and nan trees above and gold and jade below. The deity Jiangyi dwells here. The mountain has strange rain and is a source of winds and clouds; the text gives no bodily description of Jiangyi.'),
    ('sanwei', '三危之山', 'Mount Sanwei', 283, 288, 3,
     '向西二百二十里至三危，广员百里，三青鳥居之。𢕟𢓨牛状白身四角、毛如披蓑而食人；鴟一首三身、状如𪇱。郭注疑有脱错，不把欽原螫害文移作鴟能力。',
     'Two hundred and twenty li west is Sanwei, a hundred li across, where the three blue-green birds dwell. Aoye resembles an ox, with a white body, four horns and hair like a rain cape, and eats people. A bird called Chi has one head and three bodies and resembles luo. Commentary discusses a possible displaced passage, without establishing another power for Chi.'),
    ('guishan3', '騩山（西次三经）', 'Mount Gui (third range)', 289, 290, 3,
     '向西一百九十里至本列騩山，多玉而无石，神𦒿童居之，音常如钟磬。山下多積蛇；与首列騩山分开，不借老童别篇形貌。',
     'One hundred and ninety li west is Gui, with much jade and no stone. The deity Qitong dwells here and continually sounds like bells and chimes. Many jishes occur below. This mountain is distinct from the namesake in the first range.'),
    ('tianshan', '天山', 'Mount Tian', 291, 295, 3,
     '向西三百五十里至天山，多金玉、青雄黄。英水西南注湯谷。帝江黄囊状、赤如丹火、六足四翼、浑敦无面目，识歌舞；郭注混沌寓言分列。',
     'Three hundred and fifty li west is Tian, rich in gold, jade and qing xionghuang. The Ying flows southwest into Tang Valley. Dijiang resembles a yellow sack, red like cinnabar fire, with six feet and four wings, a rounded body and no face or eyes. It understands song and dance; the commentary’s Hundun allegory remains separate.'),
    ('youshan', '泑山', 'Mount You', 296, 299, 3,
     '向西二百九十里至泑山，神蓐𭣣居之。上多嬰短之玉，阳多瑾瑜，阴多青雄黄；西望日入，其气员，红光所司。蓐收形貌在郭注，红光形貌未闻，不混为一神。',
     'Two hundred and ninety li west is You, inhabited by Rushou. Yingduan jade occurs above, jinyu jade on the sunny side and qing xionghuang on the shaded side. To the west is the setting sun, with circular vapor overseen by Hongguang. Rushou’s form is described only in commentary; Hongguang’s form is unknown.'),
    ('yiwang', '翼望之山', 'Mount Yiwang', 300, 305, 3,
     '向西水行百里至翼望，无草木，多金玉。讙狸状一目三尾、音夺百声；鵸䳜乌状三首六尾而善笑。服用与御凶说法按经文保留，不将古说扩为现实疗效。',
     'Traveling west by water for a hundred li reaches Yiwang, without vegetation and rich in gold and jade. Huan resembles a li with one eye and three tails, producing a multitude of sounds; it is said to ward off harm and relieve jaundice when worn or consumed. Qiyu resembles a crow with three heads and six tails and laughs readily; wearing or consuming it is said to prevent nightmares and ward off harm.'),
    ('range3-summary', '西次三经总括与祠礼', 'Third Western range: summary and rites', 306, 308, 3,
     '本列总括从崇吾至翼望，底本记二十三山、六千七百四十四里，神皆羊身人面。祠礼用一吉玉瘗，糈用稷米。逐名实际22山与底本23并存，不补造缺山或修改总数。',
     'The third range runs from Chongwu to Yiwang. The edition states twenty-three mountains and 6,744 li. Its deities all have sheep bodies and human faces. The rite buries one auspicious jade object and offers millet grain. The enumerated route has twenty-two named mountains; the stated total is retained without inventing another mountain.'),
    ('yinshan4', '隂山（西次四经）', 'Mount Yin (fourth range)', 309, 310, 4,
     '西次四经首山隂山，上多榖而无石，草多茆蕃，隂水西注洛。本列另起，不从翼望补造跨列距离，也不与第三列同名山合并。',
     'The fourth Western range begins at Yin, with many gu trees, no stone and abundant mao and fan plants. The Yin River rises here and flows west into the Luo. This begins a new range without an invented distance from Yiwang.'),
    ('laoshan', '勞山', 'Mount Lao', 311, 312, 4,
     '隂山向北五十里至勞山，多茈草；弱水西注洛。茈草染紫为郭注，弱水不借别篇神话或现代河道。',
     'Fifty li north is Lao, with much zicao. The Ruo rises here and flows west into the Luo. The use of zicao as a purple dye belongs to commentary.'),
    ('bafu', '罷父之山', 'Mount Bafu', 313, 314, 4,
     '勞山向西五十里至罷父，洱水西注洛，水中多茈碧；不由洱名定位现代湖泊。',
     'Fifty li west is Bafu. The Er rises here and flows west into the Luo; its waters contain much zibi.'),
    ('shenshan', '申山', 'Mount Shen', 315, 316, 4,
     '向北一百七十里至申山，上多榖柞，下多杻橿，阳多金玉；區水东注河。上下与山阳物产分别保留。',
     'One hundred and seventy li north is Shen. Gu and zuo trees grow above, niu and jiang below; gold and jade occur on the sunny side. The Qu rises here and flows east into the He.'),
    ('niaoshan', '鳥山', 'Mount Niao', 317, 318, 4,
     '向北二百里至鳥山，上桑下楮，阴铁阳玉；辱水东注河。山名鳥不据此新增未记鸟类。',
     'Two hundred li north is Niao. Mulberry grows above and chu trees below; iron occurs on the shaded side and jade on the sunny side. The Ru rises here and flows east into the He.'),
    ('shangshen', '上申之山', 'Mount Shangshen', 319, 322, 4,
     '向北一百二十里至上申，上无草木而多硌石，下多榛楛，兽多白鹿。當扈雉状、以髯飞，食之不眴目；湯水东注河。髯咽下须毛来自郭注，不画成人的双臂或额外翼。',
     'One hundred and twenty li north is Shangshen. Its upper slopes have no vegetation and many large stones; hazel and hu grow below. White deer are abundant. Danghu resembles a pheasant and flies by means of its beard; eating it is said to prevent dizziness of the eyes. The Tang rises here and flows east into the He.'),
    ('zhuci', '諸次之山', 'Mount Zhuci', 323, 324, 4,
     '向北一百八十里至諸次，諸次水东注河。山多木无草，鸟兽莫居而多众蛇；两句照录，不擅以现代分类消除表述。',
     'One hundred and eighty li north is Zhuci. The Zhuci River flows east into the He. The mountain has many trees but no grass; birds and beasts do not dwell here, yet many snakes occur, as the edition states.'),
    ('haoshan', '號山', 'Mount Hao', 325, 327, 4,
     '向北一百八十里至號山，多漆㯶、葯䖀芎藭及汵石；端水东注河。葯与䖀、芎藭分存，郭注未详不据此定现代矿物。',
     'One hundred and eighty li north is Hao. Lacquer and zong trees, yao, xian and xiongqiong herbs and qin stone are abundant. The Duan rises here and flows east into the He.'),
    ('yushan4', '盂山', 'Mount Yu (fourth range)', 328, 330, 4,
     '向北二百二十里至盂山，阴铁阳铜，白狼白虎、白雉白翟列名；生水东注河。仅毛色或羽色描述，不借郭注穆王故事造额外个体。',
     'Two hundred and twenty li north is Yu. Iron occurs on the shaded side and copper on the sunny side. White wolves, white tigers, white pheasants and white zhai are abundant. The Sheng rises here and flows east into the He.'),
    ('baiyu', '白於之山', 'Mount Baiyu', 331, 333, 4,
     '向西二百五十里至白於，上松柏下櫟檀，有㸲牛、羬羊、鴞。洛水出阳东注渭，夾水出阴东注生水；不与别段同名水强合地理。',
     'Two hundred and fifty li west is Baiyu. Pines and cypresses grow above, li and tan trees below; zuoniu, qianyang and xiao birds occur here. The Luo rises on the sunny side and flows east into the Wei; the Jia rises on the shaded side and flows east into the Sheng.'),
    ('shenshou', '申首之山', 'Mount Shenshou', 334, 335, 4,
     '向西北三百里至申首，无草木，冬夏有雪。申水出于上而潜于下，多白玉；不补未明示的出流方向和所注。',
     'Three hundred li northwest is Shenshou, without vegetation and snowy in winter and summer. The Shen rises above and disappears below; white jade is abundant. No receiving river or flow direction is specified.'),
    ('jinggu', '涇谷之山', 'Mount Jinggu', 336, 337, 4,
     '向西五十五里至涇谷，涇水东南注渭，多白金白玉。或无之山二字、现代涇水对应未详的郭注分列。',
     'Fifty-five li west is Jinggu. The Jing rises here and flows southeast into the Wei. White metal and white jade are abundant. Commentary records a title variant and uncertainty about identifying the river.'),
    ('gangshan', '剛山', 'Mount Gang', 338, 340, 4,
     '向西一百二十里至剛山，多柒木、㻬琈玉；剛水北注渭。神𩳁人面兽身、一足一手，音如欽；不补成常规四足或人身。',
     'One hundred and twenty li west is Gang, with many qi trees and tufuyu jade. The Gang flows north into the Wei. Many divine beings occur here, with a human face, beast body, one foot and one hand, sounding like qin.'),
    ('gangwei', '剛山之尾', 'Tail of Mount Gang', 341, 342, 4,
     '向西二百里至剛山之尾，洛水北注河，水中蠻蠻鼠身鳖首、音如吠犬。与崇吾比翼鸟蠻蠻严格分开。',
     'Two hundred li west is the tail of Mount Gang. The Luo rises here and flows north into the He. Its waters contain Manman, with a mouse body and a softshell-turtle head, sounding like a barking dog. These are distinct from Chongwu’s one-winged birds.'),
    ('yingdi', '英鞮之山', 'Mount Yingdi', 343, 346, 4,
     '向西三百五十里至英鞮，上多𣾰木，下多金玉，鸟兽尽白。涴水北注𨹧羊泽，多冉遺魚，鱼身蛇首六足、目如马耳；不把目如马耳改画成另长马耳。',
     'Three hundred and fifty li west is Yingdi, with many trees bearing the edition’s water-radical name above and gold and jade below. Its birds and beasts are entirely white. The Wan flows north into Lingyang Marsh. Ranyi fish have fish bodies, snake heads, six feet and eyes shaped like horses’ ears; eating them is said to prevent nightmares and ward off harm.'),
    ('zhongqu', '中曲之山', 'Mount Zhongqu', 347, 352, 4,
     '向西三百里至中曲，阳玉、阴雄黄白玉及金。駮马状白身黑尾、一角、虎牙爪、音如鼓，食虎豹而御兵；櫰木棠状圆叶赤实、实如木瓜，食之多力。',
     'Three hundred li west is Zhongqu. Jade occurs on the sunny side; xionghuang, white jade and gold on the shaded side. Bo resembles a horse with a white body, black tail, one horn and tiger teeth and claws, sounding like a drum. It eats tigers and leopards and is said to ward off weapons. Huai trees resemble tang, with round leaves and red fruit as large as mugua fruit; eating the fruit is said to increase strength.'),
    ('guishan4', '邽山', 'Mount Gui (fourth range)', 353, 357, 4,
     '向西二百六十里至邽山。窮竒正文牛状蝟毛、音如獋狗而食人；虎状有翼为郭注异说，不能拼为同一形象。𪷟水南注洋水，多黄贝、蠃魚，蠃魚鱼身鸟翼、音如鸳鸯。',
     'Two hundred and sixty li west is Gui. Qiongqi resembles an ox with hedgehog-like hair, sounds like a howling dog and eats people. A tiger-like winged form is an alternative in commentary, not combined with the main-text form. The Meng flows south into the Yang, containing yellow shells and Luoyu, fish-bodied with bird wings and mandarin-duck-like calls; their appearance foretells flooding.'),
    ('niaoshu', '鳥鼠同穴之山', 'Mount Niaoshu Tongxue', 358, 365, 4,
     '向西二百二十里至鳥鼠同穴，上多白虎白玉。渭水东注河，多鰠魚，鱣状而动则邑有兵。濫水自西出而西注漢，多𩶯魮，覆铫状、鸟首鱼翼鱼尾、音磬石、生珠玉；共穴鸟鼠细节仅郭注。',
     'Two hundred and twenty li west is Niaoshu Tongxue, with many white tigers and white jade. The Wei flows east into the He and contains Saoyu, resembling zhan fish; their movement foretells warfare. The Lan rises on the western side and flows west into the Han, containing Rupi fish, shaped like overturned pans with bird heads, fish fins and fish tails. They sound like struck chimes and stones and produce pearls and jade. Details of birds and mice sharing holes belong to commentary.'),
    ('yanzi', '崦嵫之山', 'Mount Yanzi', 366, 373, 4,
     '向西南三百六十里至崦嵫，多丹木，叶榖状、果如瓜、赤符黑理；阳多龟阴多玉。苕水西注海，多砥砺。孰湖马身鸟翼、人面蛇尾，好举人；末鸟鴞状人面、蜼身犬尾，名自号，见则邑旱，不擅补鸟名。',
     'Three hundred and sixty li southwest is Yanzi. Dan trees have gu-like leaves and melon-sized fruit, with red outer coloring and black markings; eating them is said to relieve jaundice and ward off fire. Turtles occur on the sunny side and jade on the shaded side. The Tiao flows west into the sea and contains whetstones. Shuhu has a horse body, bird wings, a human face and a snake tail, and likes lifting people. Another bird resembles a xiao but has a human face, wei-like body and dog tail; its name follows its cry, without a captured name, and its appearance foretells drought.'),
    ('range4-summary', '西次四经总括与祠礼', 'Fourth Western range: summary and rites', 374, 376, 4,
     '本列从隂山至崦嵫，十九山、三千六百八十里。祠祀用一白鸡祈，糈以稻米，白管为席；白管按底本保留，不补写神貌或当作现代仪式建议。',
     'The fourth range runs from Yin to Yanzi: nineteen mountains and 3,680 li. Its rite uses one white chicken in prayer, rice grain as the offering and white guan for the mat. The edition wording is retained without inventing a deity’s form.'),
    ('western-total', '西山经篇末总计', 'Western Mountains: closing total', 377, 378, 5,
     '篇末记西经七十七山、一万七千五百一十七里。各山列原报里程相加为17521里，与篇末17517里相差四里；第三列报23山但列名22，均保留而不擅校成一致。',
     'The closing total states seventy-seven mountains and 17,517 li. The range distances sum to 17,521 li, four li more; the third range states twenty-three mountains while naming twenty-two. These textual discrepancies are retained rather than silently reconciled.'),
]

# Each line is an editorially selected, contiguous main-text excerpt, not an inferred species.
ENTITY_TEXT = '''
kunlun|deity|luwu|陸吾|Luwu|神陸吾司之其神状虎身而九尾人面而虎𤓰是神也司天之九部及帝之囿時|虎身九尾、人面虎爪，司天九部及帝囿时；不与海内西经九首开明兽混同。|Luwu has a tiger body, nine tails, a human face and tiger claws, overseeing the nine heavenly divisions and seasons of the imperial garden.
kunlun|beast|tulou|土螻|Tulou|有獸焉其状如羊而四角名曰土螻是食人|羊状四角、食人；不补其他器官。|Tulou resembles a sheep with four horns and eats people.
kunlun|bird|qinyuan|欽原|Qinyuan|有鳥焉其状如蜂大如鴛鴦名曰欽原蠚鳥獸則死蠚木則枯|虽列于有鸟焉，形如蜂、大如鸳鸯，螫鸟兽死、螫木枯；不画成普通鸟。|Listed as a bird, Qinyuan resembles a bee as large as a mandarin duck; its sting kills birds and beasts and withers trees.
kunlun|bird?|chun|鶉鳥|Chun bird|有鳥焉其名曰鶉鳥是司帝之百服|仅列名与司百服之职，无形貌；器服与服事为郭注两说。|Chun birds oversee the emperor’s hundred items of equipment; commentary also offers service as a reading. Their form is unspecified.
kunlun|plant|shatang|沙棠|Shatang|有木焉其状如棠華黄赤實其味如李而無核名曰沙棠可以禦水食之使人不溺|棠状，黄花赤实，味李而无核；御水不溺是古籍食用记述。|Shatang resembles tang, with yellow flowers and red, plum-flavored seedless fruit; eating it is said to prevent drowning.
kunlun|plant|pin|薲草|Pin grass|有草焉名曰薲草其状如葵其味如葱食之已勞|葵状、味葱，食之已劳为古籍记述，不鉴定现代草种。|Pin grass resembles kui, tastes like scallion and is said to relieve fatigue when eaten.
kunlun|water|he|河水（崑崙段）|He (Kunlun)|河水出焉而南流東注于無逹|河水先南流、再东注无逹；郭注无逹为山名。|The He rises here, flows south and then east into Wuda, glossed as a mountain name.
kunlun|place|wuda|無逹|Wuda|南流東注于無逹|河水所注，郭注为山名，不据注字补现代点位。|Wuda receives the He and is glossed as a mountain name, without modern coordinates.
kunlun|water|chi|赤水（崑崙段）|Chi (Kunlun)|赤水出焉而東南流注于汜天之水|赤水东南注汜天之水，与其他山段同名分存。|The Chi flows southeast into Fantian’s water; other namesake sources remain distinct.
kunlun|water|fantian|汜天之水|Fantian water|東南流注于汜天之水|正文写水，郭注释汜天亦山名，保留经注差别。|The receiving water is called Fantian; commentary also treats Fantian as a mountain name.
kunlun|water|yang|洋水（崑崙段）|Yang (Kunlun)|洋水出焉而西南流注于醜塗之水|洋水西南注醜塗之水，清为郭注异文。|The Yang flows southwest into Choutu’s water; Qing is an alternative in commentary.
kunlun|water|choutu|醜塗之水|Choutu water|西南流注于醜塗之水|洋水所注，郭注醜塗亦山名，不把南极注说换算现代位置。|Choutu’s water receives the Yang; its name is also glossed as a mountain, without a modern location.
kunlun|water|hei|黑水（崑崙段）|Hei (Kunlun)|黑水出焉而西流于大杅|黑水西流大杅；不与南山黑水或黑色解释混同。|The Hei rises here and flows west to Dayu; namesakes in other books remain separate.
kunlun|place|dayu|大杅|Dayu|西流于大杅|黑水所至，郭注释山名，杅音于。|Dayu is the destination of the west-flowing Hei and is glossed as a mountain name.
kunlun|beast?|strange|怪鳥獸（崑崙段）|Strange birds and beasts (Kunlun)|是多怪鳥獸|正文集称，无个体形貌；郭注九首兽六首鸟是例说，不另建正文物种。|A collective main-text designation without individual forms; commentary’s nine-headed beast and six-headed bird remain examples, not additional named species.
leyou|water|tao|桃水|Tao River|桃水出焉西流注于稷澤|桃水西注稷澤。|The Tao rises here and flows west into Jize.
leyou|water|jize|稷澤（樂游段）|Jize (Leyou)|桃水出焉西流注于稷澤|桃水所注，与峚段丹水出处分别索引，不造现代水网。|Jize receives the Tao; the separate Dan River context is not a reconstructed modern network.
leyou|material|jade|白玉（樂游段）|White jade (Leyou)|是多白玉|多白玉承接桃水稷泽记述，不转为滑鱼身体颜色。|White jade occurs in the Tao–Jize account; it is not the fish’s body color.
leyou|beast|huayu|滑魚|Huayu|其中多滑魚其状如蛇而四足是食魚|蛇状四足、食鱼；无鱼头鱼鳍的明文，不因鱼名补鳍。|Huayu is snake-shaped with four feet and eats fish; its name does not establish extra fins.
luomushan|deity|changcheng|長乗|Changcheng|神長乗司之是天之九徳也其神状如人而犳尾|人状犳尾，天之九德；不与槐江蠃母或后世人物混同。|Changcheng is human-shaped with a leopard tail, overseeing this mountain as heaven’s nine virtues.
luomushan|material|jade|玉（蠃母山上）|Jade above Luomu|其上多玉|玉在山上。|Jade is abundant on the upper mountain.
luomushan|material|stone|青石（蠃母山下）|Blue-green stone below Luomu|其下多青石而無水|青石在山下，与无水同句；不定现代石种。|Blue-green stone occurs below, where no water is recorded; no modern stone species is assigned.
yushan|deity|xiwangmu|西王母（玉山段）|Xiwangmu (Mount Yu)|西王母其状如人豹尾虎齒而善嘯蓬髮戴勝是司天之厲及五殘|人状豹尾虎齿、蓬发戴胜而善啸；不画成无尾的宫装王后，不把郭注穆王事迹充入正文。|Human-shaped with a leopard tail, tiger teeth, disheveled hair and a sheng headdress, Xiwangmu whistles and oversees heavenly calamities and destructive forces.
yushan|beast|jiao|狡|Jiao|有獸焉其状如犬而豹文其角如牛其名曰狡其音如吠犬見則其國大穰|犬状豹文、牛状角，犬吠音；郭注无前两脚疑说不作正文形貌。|Jiao is dog-shaped with leopard markings and ox-like horns; it barks like a dog and foretells a plentiful year. A doubtful commentary specimen is separate.
yushan|bird|shengyu|胜遇|Shengyu|有鳥焉其状如翟而赤名曰胜遇是食魚其音如録見則其國大水|翟状赤色、食鱼、音如録；不将大水画为鸟主动施法。|Shengyu is a red zhai-shaped bird that eats fish, sounds like lu and foretells flooding.
xuanyuan|water|xun|洵水|Xun River|洵水出焉南流注于黒水|洵水南注黑水，音询是郭注。|The Xun flows south into the Hei; its pronunciation is glossed in commentary.
xuanyuan|water|hei|黑水（軒轅段）|Hei (Xuanyuan)|南流注于黒水|本段洵水所注，不强合现代水系。|The receiving Hei in the Xuanyuan passage, without a joined modern river course.
xuanyuan|material|dansu|丹粟（洵水段）|Dansu (Xun)|其中多丹粟|丹粟承接洵水正文。|Dansu occurs in the Xun water account.
xuanyuan|material|xionghuang|青雄黄（洵水段）|Qing xionghuang (Xun)|多靑雄黄|本段青雄黄与丹粟并记，不拆青字造新物。|Qing xionghuang is recorded alongside dansu, without splitting qing into another substance.
jishi|place|gate|石門（積石段）|Stone gate (Jishi)|其下有石門河水冐以西流|石门在山下，河水冐以西流；冐猶覆为注。|The stone gate lies below Jishi; the He passes beneath a covering and flows west.
jishi|water|he|河水（積石段）|He (Jishi)|河水冐以西流|河水在本段记西流，不与崑崙南流东注统一改向。|The He flows west here, without overwriting Kunlun’s separately stated directions.
changliu|deity?|shaohao|白帝少昊|White Emperor Shaohao|其神白帝少昊居之|少昊居長留，正文无形貌，不与員神磈氏强合身份。|Shaohao dwells at Changliu; no form is given and identity with Weishi is not asserted.
changliu|beast?|beasts|文尾兽（長留段）|Pattern-tailed beasts|其獸皆文尾|只记兽皆文尾，未具名，不穷举物种或补肢角。|An unnamed collective whose tails are patterned, without individually specified species or limbs.
changliu|bird?|birds|文首鸟（長留段）|Pattern-headed birds|其鳥皆文首|只记鸟皆文首，未具名，不借他山鸟形。|An unnamed collective with patterned heads, without borrowing forms from other mountains.
changliu|material|jade|文玉石|Patterned jade and stone|是多文玉石|文玉石照录，文或作长仅郭注。|Patterned jade and stone are abundant; long is a commentary variant of patterned.
changliu|deity?|weishi|員神磈氏|Yuan deity Weishi|實惟員神磈氏之宫是神也主司反景|磈氏司反景，无形貌；员不因字义画为圆形神。|Weishi oversees returning light; no bodily form or round body is inferred from the wording.
zhange|material|yaobi|瑶碧|Yaobi|無草木多瑶碧|瑶碧与无草木同段，郭注碧亦玉属，不定现代矿物。|Yaobi occurs on the vegetation-free mountain; commentary classes bi with jade.
zhange|beast|zheng|狰|Zheng|有獸焉其状如赤豹五尾一角其音如擊石其名如狰|赤豹状，五尾一角，音如击石。|Zheng resembles a red leopard with five tails and one horn, sounding like struck stones.
zhange|bird|bifang|畢方|Bifang|有鳥焉其状如鶴一足赤文青質而白喙名曰畢方其鳴自呌也見則其邑有譌火|鹤状一足，赤文青质白喙，鸣自叫；不添第二足或火焰器官。|Bifang is crane-shaped with one foot, red markings, a blue-green body and white beak; it calls its own name and foretells uncanny fire.
yinshan3|water|zhuoyu|濁浴之水|Zhuoyu River|濁浴之水出焉而南流注于蕃澤|濁浴水南注蕃泽。|The Zhuoyu rises here and flows south into Fan Marsh.
yinshan3|water|fan|蕃澤|Fan Marsh|南流注于蕃澤|本段濁浴所注。|Fan Marsh receives the south-flowing Zhuoyu.
yinshan3|material|shell|文貝|Patterned shells|其中多文貝|文贝见于本段水中，郭注余泉蚳类，不定现代贝种。|Patterned shells occur in the waters; commentary comparisons do not identify a modern species.
yinshan3|beast|tiangou|天狗|Tiangou|有獸焉其状如狸而白首名曰天狗其音如榴榴可以禦凶|狸状白首，音榴榴，御凶为古籍记述；不画后世食日黑犬。|Tiangou resembles a li with a white head and a liuliu call, and is said to ward off harm; it is not the later sun-eating black dog.
futang|plant|zong|㯶（符愓段）|Zong (Fuyang)|其上多㯶柟|㯶与柟分列，上部物产，无现代种鉴定。|Zong is recorded with nan among the upper-slope trees, without a modern species identification.
futang|plant|nan|柟（符愓段）|Nan (Fuyang)|其上多㯶柟|柟为山上树木，不由同名移入别段形貌。|Nan is an upper-slope tree; forms from other passages are not transferred.
futang|material|gold|金（符愓山下）|Gold below Fuyang|下多金玉|金在下部，与玉分列。|Gold occurs below, alongside jade.
futang|material|jade|玉（符愓山下）|Jade below Fuyang|下多金玉|玉在下部。|Jade occurs on the lower slopes.
futang|deity?|jiangyi|江疑|Jiangyi|神江疑居之|江疑居山，未述形貌；风云所出是山的记述，不补神祇器官。|Jiangyi dwells here without a stated form; the mountain’s winds and clouds do not establish the deity’s anatomy.
sanwei|bird?|bluebirds|三青鳥（三危段）|Three blue-green birds|三青鳥居之|只记三青鸟居此，郭注为西王母取食另存；不借别篇三足或人面。|Three blue-green birds dwell here; commentary links them to feeding Xiwangmu, without specifying extra legs or human faces.
sanwei|beast|aoyu|𢕟𢓨|Aoye|其上有獸焉其状如牛白身四角其毫如披蓑其名曰𢕟𢓨是食人|牛状白身四角，毛如披蓑、食人；音傲噎为郭注。|Aoyu is ox-shaped with a white body, four horns and cape-like hair, and eats people.
sanwei|bird|chi|鴟（三危段）|Chi (Sanwei)|有鳥焉一首而三身其状如𪇱其名曰鴟|一首三身，状如𪇱；𪇱似雕黑文赤颈为郭注，不把三身改为三首。|Chi has one head and three bodies and resembles luo; the eagle-like form, black markings and red neck come from commentary.
guishan3|material|jade|玉（西次三经騩山）|Jade (third-range Gui)|其上多玉而無石|多玉而无石照录，不人为协调古籍分类。|Much jade but no stone is recorded, retaining the edition’s distinction.
guishan3|deity?|qitong|𦒿童|Qitong|神𦒿童居之其音常如鍾磬|神居此，音常如钟磬；老童颛顼子是郭注，本段无形貌。|Qitong dwells here and sounds like bells and chimes; the identification as Laotong, Zhuanxu’s son, belongs to commentary. No form is given.
guishan3|beast?|jishes|積蛇|Jishes|其下多積蛇|只记下多积蛇，不凭积字添首足或指定现代种。|Jishes are numerous below; the wording does not specify extra heads, legs or a modern species.
tianshan|material|gold|金（天山）|Gold (Tian)|多金玉|天山所记金，不移入帝江体色。|Gold is a mountain resource, not Dijiang’s body color.
tianshan|material|jade|玉（天山）|Jade (Tian)|多金玉|天山玉与金分列。|Jade is recorded alongside gold.
tianshan|material|xionghuang|青雄黄（天山）|Qing xionghuang (Tian)|有青雄黄|正文保留青雄黄组词。|The edition’s qing xionghuang grouping is retained.
tianshan|water|ying|英水|Ying River|英水出焉而西南流注于湯谷|英水西南注汤谷，不因同名牵入海外扶桑叙事。|The Ying rises here and flows southwest into Tang Valley, without importing the overseas Fusang narrative.
tianshan|place|tang|湯谷（天山段）|Tang Valley (Tian)|西南流注于湯谷|英水所注地点，独立于海外东经汤谷扶桑。|The receiving place for the Ying remains separate from Tang Valley and Fusang in the overseas book.
tianshan|deity|dijiang|帝江|Dijiang|有神焉其状如黄囊赤如丹火六足四翼渾敦無靣目是識歌舞實惟帝江也|黄囊状、丹火赤，六足四翼、无面目；不加眼口面具。|Dijiang is sack-shaped, yellow with a cinnabar-red glow, with six feet and four wings, no face or eyes, and knowledge of song and dance.
youshan|deity?|rushou|蓐𭣣|Rushou|神蓐𭣣居之|正文仅记居此，无形貌；人面虎爪白尾执钺为郭注引外传，不按正文资格生图。|The main text only names Rushou as resident; the human face, tiger claws, white tail and axe are commentary, not a main-text depiction.
youshan|material|yingduan|嬰短之玉|Yingduan jade|其上多嬰短之玉|嬰短玉在山上，郭注未详，不补矿物鉴定。|Yingduan jade occurs above and is unexplained in commentary, without a modern mineral identity.
youshan|material|jinyu|瑾瑜之玉（泑山阳）|Jinyu jade (You)|其陽多瑾瑜之玉|瑾瑜归阳面。|Jinyu jade occurs on the sunny side.
youshan|material|xionghuang|青雄黄（泑山阴）|Qing xionghuang (You)|其隂多青雄黄|青雄黄归阴面。|Qing xionghuang occurs on the shaded side.
youshan|deity?|hongguang|紅光|Hongguang|是山也西望日之所入其氣員神紅光之所司也|红光司日入之气，郭注未闻其状，不从光色捏造神像。|Hongguang oversees the circular vapor at sunset; commentary explicitly says the form is unknown.
yiwang|material|gold|金（翼望段）|Gold (Yiwang)|無草木多金玉|翼望多金，不归怪兽身体。|Gold is a mountain resource, not a beast’s body color.
yiwang|material|jade|玉（翼望段）|Jade (Yiwang)|無草木多金玉|翼望玉与金分列。|Jade occurs alongside gold at Yiwang.
yiwang|beast|huan|讙|Huan|有獸焉其状如狸一目而三尾名曰讙其音如奪百聲是可以禦凶服之已癉|狸状一目三尾，音夺百声；不与南山灌灌混同。|Huan is li-shaped with one eye and three tails and many sounds; ancient protective and jaundice claims are retained separately from modern medicine.
yiwang|bird|qiyu|鵸䳜|Qiyu|有鳥焉其状如烏三首六尾而善𥬇名曰鵸䳜服之使人不厭又可以禦凶|乌状三首六尾、善笑；不擅添翼对数，食服与御凶为古说。|Qiyu resembles a crow with three heads and six tails and laughs readily; claims about nightmares and protection remain ancient accounts.
range3-summary|deity|sheep|羊身人面神（西次三经）|Sheep-bodied deities (third range)|其神状皆羊身人靣|本列集体神貌羊身人面，不拆23位具名神，不添人臂。|A collective divine form with sheep bodies and human faces, without inventing individually named deities or human arms.
range3-summary|rite|rite|吉玉稷米祠礼|Auspicious jade and millet rite|其祠之禮用一吉玉瘞糈用稷米|一吉玉瘗、稷米为糈；玉加采色是郭注，不现代化仪式步骤。|The rite buries one auspicious jade object and offers millet; coloring the jade is a commentary gloss, not a modern procedure.
'''

ENTITY_TEXT += '''
yinshan4|plant|gu|榖（西次四经隂山）|Gu (fourth-range Yin)|上多榖無石|榖在上部，无石另存，不据同音换字。|Gu trees grow above; the separate no-stone statement is retained.
yinshan4|plant|mao|茆（隂山段）|Mao (Yin)|其草多茆蕃|茆蕃并记，郭注跨309—310释茆为葵，分别列名。|Mao is recorded with fan; a commentary gloss continues across source lines.
yinshan4|plant|fan|蕃（隂山段）|Fan (Yin)|其草多茆蕃|蕃与茆分列，青蕃似莎而大为郭注。|Fan is distinct from mao; its sedge-like comparison belongs to commentary.
yinshan4|water|yin|隂水|Yin River|隂水出焉西流注于洛|隂水西注洛。|The Yin rises here and flows west into the Luo.
yinshan4|water|luo|洛（西次四经首段）|Luo (fourth-range opening)|西流注于洛|本段隂水所注，后段同名分存出处。|The Luo receives the Yin here, with namesake contexts retained separately.
laoshan|plant|zicao|茈草（勞山）|Zicao (Lao)|多茈草|茈草正文列名，染紫为注。|Zicao is named in the main text; its purple-dye use is commentary.
laoshan|water|ruo|弱水（勞山）|Ruo (Lao)|弱水出焉而西流注于洛|弱水西注洛，不补难渡或神力。|The Ruo flows west into the Luo, without an added impassability legend.
laoshan|water|luo|洛（勞山段）|Luo (Lao)|西流注于洛|勞山弱水所注，非现代汇流图。|The receiving Luo in the Lao passage, without a modern confluence map.
bafu|water|er|洱水|Er River|洱水出焉而西流注于洛|洱水西注洛，音耳为注，不定现代洱海。|The Er flows west into the Luo; its name does not identify modern Erhai.
bafu|water|luo|洛（罷父段）|Luo (Bafu)|西流注于洛|洱水所注，保留本段出处。|The Luo receives the Er in this passage.
bafu|material|zibi|茈碧|Zibi|其中多茈碧|茈碧见于水中，不定现代矿物。|Zibi occurs in the waters, without a modern mineral identification.
shenshan|plant|gu|榖（申山上）|Gu above Shen|其上多榖柞|榖在上部，与柞分别保存。|Gu grows above, separately indexed from zuo.
shenshan|plant|zuo|柞（申山上）|Zuo above Shen|其上多榖柞|柞在上部。|Zuo trees grow above.
shenshan|plant|niu|杻（申山下）|Niu below Shen|其下多杻橿|杻在下部，不借他山形貌。|Niu grows below without importing another mountain’s description.
shenshan|plant|jiang|橿（申山下）|Jiang below Shen|其下多杻橿|橿在下部。|Jiang grows below.
shenshan|material|gold|金（申山阳）|Gold on sunny Shen|其陽多金玉|金归阳面。|Gold occurs on the sunny side.
shenshan|material|jade|玉（申山阳）|Jade on sunny Shen|其陽多金玉|玉归阳面。|Jade occurs on the sunny side.
shenshan|water|qu|區水|Qu River|區水出焉而東流注于河|區水东注河。|The Qu flows east into the He.
shenshan|water|he|河（申山段）|He (Shen)|東流注于河|區水所注，与他段河水各存出处。|The He receives the Qu here; other passage contexts remain distinct.
niaoshan|plant|sang|桑（鳥山上）|Mulberry above Niao|其上多桑|桑在上部。|Mulberry grows above.
niaoshan|plant|chu|楮（鳥山下）|Chu below Niao|其下多楮|楮在下部。|Chu trees grow below.
niaoshan|material|iron|鐡（鳥山阴）|Iron on shaded Niao|其隂多鐡|铁归阴面。|Iron occurs on the shaded side.
niaoshan|material|jade|玊（鳥山阳）|Jade on sunny Niao|其陽多玊|玊保留底本字形，归阳面。|Jade occurs on the sunny side; the edition character is retained.
niaoshan|water|ru|辱水|Ru River|辱水出焉而東流注于河|辱水东注河。|The Ru flows east into the He.
niaoshan|water|he|河（鳥山段）|He (Niao)|東流注于河|辱水所注。|The He receives the Ru.
shangshen|material|stone|硌石|Large luo stones|上無草木而多硌石|山上无草木，多硌石；大石貌为郭注。|Large luo stones occur above where vegetation is absent; large stone is a commentary gloss.
shangshen|plant|zhen|榛（上申下）|Hazel below Shangshen|下多榛楛|榛在下，果味说明为注。|Hazel grows below; the nut description belongs to commentary.
shangshen|plant|hu|楛（上申下）|Hu below Shangshen|下多榛楛|楛在下，可为箭来自郭注。|Hu grows below; arrow-making belongs to commentary.
shangshen|beast?|deer|白鹿（上申段）|White deer (Shangshen)|獸多白鹿|仅列白鹿，无角形肢体等详细描述。|White deer are named without detailed antler or body descriptions.
shangshen|bird|danghu|當扈|Danghu|其鳥多當扈其状如雉以其髯飛食之不眴目|雉状、以髯飞，髯为咽下须毛来自注；不添独立手臂。|Danghu resembles a pheasant and flies with its beard, glossed as throat hair. Eating it is said to prevent dizziness of the eyes.
shangshen|water|tang|湯水|Tang River|湯水出焉東流注于河|汤水东注河，不与天山汤谷合并。|The Tang flows east into the He; it is not Tian’s Tang Valley.
shangshen|water|he|河（上申段）|He (Shangshen)|東流注于河|汤水所注。|The He receives the Tang.
zhuci|water|zhuci|諸次之水|Zhuci River|諸次之水出焉而東流注于河|諸次水东注河。|The Zhuci flows east into the He.
zhuci|water|he|河（諸次段）|He (Zhuci)|東流注于河|諸次水所注。|The He receives the Zhuci.
zhuci|beast?|snakes|衆蛇（諸次段）|Snakes (Zhuci)|鳥獸莫居是多衆蛇|正文并存鸟兽莫居与多众蛇；未述个体形貌，不指定蛇种。|The text juxtaposes birds and beasts not dwelling here with many snakes; no individual form is specified.
haoshan|plant|lacquer|漆（號山段）|Lacquer tree (Hao)|其木多漆㯶|漆与㯶分列，似樗为郭注。|Lacquer is separately indexed from zong; the chun comparison is commentary.
haoshan|plant|zong|㯶（號山段）|Zong (Hao)|其木多漆㯶|㯶为树木列名。|Zong is named among the trees.
haoshan|plant|yao|葯|Yao|其草多葯䖀芎藭|葯与䖀、芎藭分列，白芷别名是郭注。|Yao is indexed separately from xian and xiongqiong; its identification with baizhi belongs to commentary.
haoshan|plant|xian|䖀|Xian|其草多葯䖀芎藭|䖀为香草是郭注，不另定现代属种。|Xian is glossed as an aromatic herb, without a modern species assignment.
haoshan|plant|xiongqiong|芎藭|Xiongqiong|其草多葯䖀芎藭|芎藭为本段草名，江蘺别名仅注。|Xiongqiong is a named herb; Jiangli is a commentary alternative.
haoshan|material|qin|汵石|Qin stone|多汵石|郭注或音今、未详，保留不定。|Qin stone is unexplained; commentary offers a possible pronunciation only.
haoshan|water|duan|端水|Duan River|端水出焉而東流注于河|端水东注河。|The Duan flows east into the He.
haoshan|water|he|河（號山段）|He (Hao)|東流注于河|端水所注。|The He receives the Duan.
yushan4|material|iron|鐡（盂山阴）|Iron on shaded Yu|其隂多鐡|铁在阴面。|Iron occurs on the shaded side.
yushan4|material|copper|銅（盂山阳）|Copper on sunny Yu|其陽多銅|铜在阳面。|Copper occurs on the sunny side.
yushan4|beast?|wolf|白狼（盂山）|White wolves (Yu)|其獸多白狼白虎|白狼仅列名和白色，无详细形貌。|White wolves are named without further anatomy.
yushan4|beast?|tiger|白虎（盂山）|White tigers (Yu)|其獸多白狼白虎|白虎仅列名和白色，郭注穆王事迹不当正文。|White tigers are named; the Mu Wang story is commentary.
yushan4|bird?|pheasant|白雉（盂山）|White pheasants (Yu)|其鳥多白雉白翟|白雉与白翟分列，不借别山鸟形。|White pheasants and white zhai are separate entries, without borrowed forms.
yushan4|bird?|zhai|白翟（盂山）|White zhai (Yu)|其鳥多白雉白翟|白翟列名，或作白翠是郭注异文。|White zhai is named; white cui is a commentary variant.
yushan4|water|sheng|生水|Sheng River|生水出焉而東流注于河|生水东注河。|The Sheng flows east into the He.
yushan4|water|he|河（盂山段）|He (Yu)|東流注于河|生水所注。|The He receives the Sheng.
baiyu|plant|pine|松（白於上）|Pine above Baiyu|上多松柏|松在上部，与柏分列。|Pine grows above, separately indexed from cypress.
baiyu|plant|cypress|柏（白於上）|Cypress above Baiyu|上多松柏|柏在上部。|Cypress grows above.
baiyu|plant|li|櫟（白於下）|Li below Baiyu|下多櫟檀|櫟在下，郭注释柞。|Li grows below and is glossed as zuo.
baiyu|plant|tan|檀（白於下）|Tan below Baiyu|下多櫟檀|檀在下，不定现代树种。|Tan grows below, without a modern species assignment.
baiyu|beast?|zuoniu|㸲牛（白於段）|Zuoniu (Baiyu)|其獸多㸲牛羬羊|仅列名，不移入小华形貌。|Zuoniu is only named; Xiaohua’s form is not transferred.
baiyu|beast?|qianyang|羬羊（白於段）|Qianyang (Baiyu)|其獸多㸲牛羬羊|仅列名，不借钱来马尾。|Qianyang is only named, without importing Qianlai’s horse tail.
baiyu|bird?|xiao|鴞（白於段）|Xiao (Baiyu)|其鳥多鴞|正文仅列名，似鸠青色为郭注；图像明确参考郭注形貌。|Xiao is only named in the main text; its dove-like blue-green form is commentary and the illustration is attributed accordingly.
baiyu|water|luo|洛水（白於阳）|Luo (sunny Baiyu)|洛水出于其陽而東流注于渭|洛水自阳面东注渭，不合并剛山尾北注河的同名水。|The Luo rises on the sunny side and flows east into the Wei; Gangwei’s north-flowing namesake is separate.
baiyu|water|wei|渭（白於段）|Wei (Baiyu)|東流注于渭|阳面洛水所注。|The Wei receives the sunny-side Luo.
baiyu|water|jia|夾水|Jia River|夾水出于其隂東流注于生水|夹水自阴面东注生水。|The Jia rises on the shaded side and flows east into the Sheng.
baiyu|water|sheng|生水（白於段）|Sheng (Baiyu)|東流注于生水|夹水所注，与盂山源出另存出处。|The Sheng receives the Jia; Yu’s source passage remains separately indexed.
shenshou|water|shen|申水|Shen River|申水出于其上潜于其下|出上潜下，无流向与所注，不补水系。|The Shen rises above and disappears below; no flow direction or receiving water is specified.
shenshou|material|jade|白玉（申首段）|White jade (Shenshou)|是多白玉|本段多白玉，不作为冰雪颜色的推论。|White jade is recorded separately from the snow description.
jinggu|water|jing|涇水（涇谷段）|Jing (Jinggu)|涇水出焉東南流注于渭|涇水东南注渭，与高山东流句各存。|The Jing flows southeast into the Wei; Gao’s eastward statement stays in its own context.
jinggu|water|wei|渭（涇谷段）|Wei (Jinggu)|東南流注于渭|涇水所注。|The Wei receives the Jing.
jinggu|material|metal|白金（涇谷）|White metal (Jinggu)|是多白金白玉|白金不直接定为铂。|White metal is not identified as modern platinum.
jinggu|material|jade|白玉（涇谷）|White jade (Jinggu)|是多白金白玉|白玉与白金分列。|White jade is separately indexed from white metal.
gangshan|plant|qi|柒木|Qi trees|多柒木|柒木按底本文字保留，不直接校漆。|The edition’s qi character is retained rather than silently changed to lacquer.
gangshan|material|tufuyu|㻬琈之玉（剛山）|Tufuyu jade (Gang)|多㻬琈之玉|玉名保留，不借他山形状。|The jade name is retained without importing another mountain’s form.
gangshan|water|gang|剛水|Gang River|剛水出焉北流注于渭|剛水北注渭。|The Gang flows north into the Wei.
gangshan|water|wei|渭（剛山段）|Wei (Gang)|北流注于渭|剛水所注。|The Wei receives the Gang.
gangshan|deity|chi|神𩳁|One-footed divine being|是多神𩳁其状人靣獸身一足一手其音如欽|人面兽身，一足一手，音如欽；郭注音耻回反，保留𩳁，不补常规四足。|The divine being has a human face, beast body, one foot and one hand and sounds like qin; extra normal limbs are not supplied.
gangwei|water|luo|洛水（剛山尾）|Luo (Gangwei)|洛水出焉而北流注于河|洛水北注河，与白於洛水分存。|This Luo flows north into the He and remains separate from Baiyu’s namesake.
gangwei|water|he|河（剛山尾）|He (Gangwei)|北流注于河|洛水所注。|The He receives the Luo.
gangwei|beast|manman|蠻蠻（鼠身鳖首）|Manman (mouse body)|其中多蠻蠻其状鼠身而鼈首其音如吠犬|鼠身鳖首、犬吠音，是水中对象，不与崇吾独翼鸟共图。|An aquatic Manman with a mouse body and softshell-turtle head, sounding like a barking dog; it is distinct from the one-winged bird.
yingdi|plant|mu|𣾰木|Edition tree name (Yingdi)|上多𣾰木|原快照缺字图按影印补阅读层，保留捕获标签，不据字形定树种。|The water-radical tree name is restored only in the reading layer from the scan, with the captured glyph marker retained and no modern species asserted.
yingdi|material|gold|金（英鞮下）|Gold below Yingdi|下多金玉|金在下部。|Gold occurs below.
yingdi|material|jade|玉（英鞮下）|Jade below Yingdi|下多金玉|玉在下部。|Jade occurs below.
yingdi|beast?|white|白鸟兽（英鞮段）|White birds and beasts (Yingdi)|鳥獸盡白|集体只记尽白，未列名形貌，不拆造具体物种。|A collective described only as entirely white, without inventing individual species.
yingdi|water|wan|涴水|Wan River|涴水出焉而北注于𨹧羊之澤|涴水北注𨹧羊泽，郭注含缺字符，保留待核。|The Wan flows north into Lingyang Marsh; a missing commentary character remains explicitly unresolved.
yingdi|water|lingyang|𨹧羊之澤|Lingyang Marsh|北注于𨹧羊之澤|涴水所注，𨹧保留，不定现代泽地。|The receiving marsh of the Wan, without a modern identification.
yingdi|beast|ranyi|冉遺之魚|Ranyi fish|是多冉遺之魚魚身蛇首六足其目如馬耳食之使人不眯可以禦凶|鱼身蛇首六足，眼形如马耳；不把眼改为额外马耳，不添翼。|Ranyi has a fish body, snake head, six feet and eyes shaped like horses’ ears, without additional ears or wings.
zhongqu|material|jade-sun|玉（中曲阳）|Jade on sunny Zhongqu|其陽多玉|玉在阳面。|Jade occurs on the sunny side.
zhongqu|material|xionghuang|雄黄（中曲阴）|Xionghuang on shaded Zhongqu|其隂多雄黄白玉及金|雄黄在阴面，与白玉和金分列。|Xionghuang occurs on the shaded side alongside white jade and gold.
zhongqu|material|jade-shade|白玉（中曲阴）|White jade on shaded Zhongqu|其隂多雄黄白玉及金|白玉在阴面。|White jade occurs on the shaded side.
zhongqu|material|gold|金（中曲阴）|Gold on shaded Zhongqu|其隂多雄黄白玉及金|金在阴面。|Gold occurs on the shaded side.
zhongqu|beast|bo|駮|Bo|有獸焉其状如馬而白身黒尾一角虎牙爪音如皷音其名曰駮是食虎豹可以禦兵|马状白身黑尾，一角虎牙爪，鼓音，食虎豹；不沿用双角旧图。|Bo is horse-shaped with a white body, black tail, one horn, tiger teeth and claws and a drum-like voice; it eats tigers and leopards and is said to ward off weapons.
zhongqu|plant|huai|櫰木|Huai tree|有木焉其状如棠而員葉赤實實大如木𤓰名曰櫰木食之多力|棠状圆叶赤实，果如木瓜，食之多力为古籍记述。|Huai resembles tang with round leaves and red, mugua-sized fruit, said to increase strength when eaten.
guishan4|beast|qiongqi|窮竒（西山经）|Qiongqi (Western Mountains)|其上有獸焉其状如牛蝟毛名曰窮竒音如獋狗是食人|正文牛状蝟毛、犬吼音、食人；虎状有翼仅郭注异说，不合图。|Qiongqi is ox-shaped with hedgehog-like hair, howls like a dog and eats people; the winged tiger-like alternative belongs only to commentary.
guishan4|water|meng|𪷟水|Meng River|𪷟水出焉南流注于洋水|𪷟水南注洋水，音𫎇为郭注。|The Meng rises here and flows south into the Yang; its pronunciation is glossed in commentary.
guishan4|water|yang|洋水（邽山段）|Yang (Gui)|南流注于洋水|𪷟水所注，与崑崙洋水分存出处。|The Yang receives the Meng; Kunlun’s namesake remains separately sourced.
guishan4|material|shell|黄貝|Yellow shells|其中多黄貝|黄贝水中物，科斗形比拟为郭注，不推定现代贝种。|Yellow shells occur in the waters; the tadpole-like comparison belongs to commentary.
guishan4|beast|luoyu|蠃魚|Luoyu|蠃魚魚身而鳥翼音如鴛鴦見則其邑大水|鱼身鸟翼、鸳鸯音，与文鰩魚形貌颜色分开。|Luoyu has a fish body and bird wings, calls like a mandarin duck and foretells flooding; Wenyao’s colors are not transferred.
niaoshu|beast?|tiger|白虎（鳥鼠段）|White tigers (Niaoshu)|其上多白虎白玉|白虎只列名和白色，不借别山形貌。|White tigers are named without further anatomical detail.
niaoshu|material|jade|白玉（鳥鼠段）|White jade (Niaoshu)|其上多白虎白玉|白玉与白虎分列，不混为兽体。|White jade is separately indexed from white tigers.
niaoshu|water|wei|渭水（鳥鼠段）|Wei (Niaoshu)|渭水出焉而東流注于河|渭水本段有源出东流注河记述，不复原全河。|The Wei rises here and flows east into the He; no complete modern course is reconstructed.
niaoshu|water|he|河（鳥鼠段）|He (Niaoshu)|東流注于河|渭水所注。|The He receives the Wei.
niaoshu|beast|saoyu|鰠魚|Saoyu|其中多鰠魚其状如鱣魚動則其邑有大兵|鱣鱼状，口颔下体连甲为郭注；动则邑兵为古籍灾异。|Saoyu resembles zhan fish; commentary adds a lower mouth and linked body armor. Its movement foretells warfare.
niaoshu|water|lan|濫水|Lan River|濫水出于其西西流注于漢水|濫水西出西注汉，音槛为注。|The Lan rises on the western side and flows west into the Han.
niaoshu|water|han|漢水（鳥鼠段）|Han (Niaoshu)|西流注于漢水|濫水所注。|The Han receives the Lan.
niaoshu|beast|rupi|𩶯魮之魚|Rupi fish|多𩶯魮之魚其状如覆銚鳥首而魚翼魚尾音如磬石之聲是生珠玉|覆铫状，鸟首鱼翼鱼尾，音磬石，生珠玉；鱼翼按鳍，不改鸟翼。|Rupi is shaped like an overturned pan with a bird head, fish fins and fish tail; it sounds like chimes and stones and produces pearls and jade.
yanzi|plant|dan|丹木（崦嵫段）|Dan tree (Yanzi)|其上多丹木其葉如榖其實大如𤓰赤符而黑理食之已癉可以禦火|叶榖状、果瓜大赤符黑理；不借峚山丹木颜色补本段。|Dan has gu-like leaves and melon-sized red-colored fruit with black markings; the ancient jaundice and fire claims remain textual.
yanzi|beast?|turtle|龜（崦嵫阳）|Turtles (sunny Yanzi)|其陽多龜|仅列名，无形貌，不借旋龟鸟首蛇尾。|Turtles are only named; Xuangui’s bird head and snake tail are not transferred.
yanzi|material|jade|玉（崦嵫阴）|Jade on shaded Yanzi|其隂多玉|玉归阴面。|Jade occurs on the shaded side.
yanzi|water|tiao|苕水（崦嵫）|Tiao (Yanzi)|苕水出焉而西流注于海|苕水西注海，若为郭注异文。|The Tiao flows west into the sea; Ruo is a commentary variant.
yanzi|water|sea|海（崦嵫段）|Sea (Yanzi)|西流注于海|苕水所注，只称海，不强改西海。|The Tiao’s destination is called sea, without silently naming it Western Sea.
yanzi|material|whetstones|砥礪|Whetstones|其中多砥礪|精砥粗砺为郭注，作为一组磨石，不造现代矿物。|Whetstones occur in the waters; fine and coarse distinctions belong to commentary.
yanzi|beast|shuhu|孰湖|Shuhu|有獸焉其状馬身而鳥翼人靣蛇尾是好舉人名曰孰湖|马身鸟翼、人面蛇尾，好举人；与虎纹英招分开，不添虎纹。|Shuhu has a horse body, bird wings, a human face and snake tail and likes lifting people; Yingzhao’s tiger markings are not transferred.
yanzi|bird|unnamed|未名鸟（崦嵫末段）|Unnamed bird (Yanzi)|有鳥焉其状如鴞而人面蜼身犬尾其名自號也見則其邑大旱|鴞状人面、蜼身犬尾，名自号而未给字名；不擅命名。|The unnamed bird is xiao-like with a human face, wei body and dog tail; its name follows its cry and its appearance foretells drought.
range4-summary|rite|rite|白鸡稻米白管祠礼|White chicken, rice and white-guan rite|其祠祀禮皆用一白鷄祈糈以稲米白管為席|一白鸡祈、稻米为糈，白管为席；不添该列神貌或流程。|The rite uses one white chicken, rice grain and white guan as a mat; no deity form or extra procedure is invented.
'''


def main_translation(text):
    editorial = ('The commentary', 'Commentary', 'This is distinct', 'This mountain is distinct',
                 'This begins a new range', 'No receiving river', 'No bodily description',
                 'Details of birds', 'The edition wording', 'The range distances', 'The enumerated route',
                 'The use of zicao', 'A tiger-like winged form', 'Rushou’s form is described',
                 'These textual discrepancies')
    sentences = [s for s in text.split('. ') if not s.startswith(editorial)]
    text = '. '.join(sentences).replace('; the commentary’s Hundun allegory remains separate', '')
    text = text.replace(', without enumerating additional species', '').replace(', as the edition states', '')
    text = text.replace('; the text gives no bodily description of Jiangyi', '')
    return text.rstrip('.')+'.'


def entity_translation(slug, key, name, text):
    import re
    overrides = {
        ('kunlun','strange'): 'There are many strange birds and beasts.',
        ('kunlun','wuda'): 'The He flows south and then east into Wuda.',
        ('kunlun','fantian'): 'The Chi flows southeast into Fantian’s water.',
        ('kunlun','dayu'): 'The Hei flows west to Dayu.',
        ('changliu','beasts'): 'Its beasts all have patterned tails.',
        ('changliu','birds'): 'Its birds all have patterned heads.',
        ('sanwei','chi'): 'A bird has one head and three bodies, resembles luo and is named Chi.',
        ('youshan','rushou'): 'The deity Rushou dwells here.',
        ('youshan','hongguang'): 'To the west is where the sun enters; its vapor is circular, overseen by the deity Hongguang.',
        ('youshan','yingduan'): 'Above is much Yingduan jade.',
        ('guishan3','jade'): 'Above is much jade and no stone.',
        ('tianshan','gold'): 'There is much gold and jade.',
        ('yiwang','gold'): 'There is no vegetation and much gold and jade.',
        ('laoshan','zicao'): 'Much zicao grows here.',
        ('zhuci','snakes'): 'Birds and beasts do not dwell here; there are many snakes.',
        ('jinggu','metal'): 'There is much white metal and white jade.',
        ('haoshan','qin'): 'There is much qin stone.',
        ('baiyu','xiao'): 'Its birds include many xiao.',
        ('gangshan','qi'): 'There are many qi trees.',
        ('yingdi','mu'): 'Above grow many 𣾰 trees.',
        ('yingdi','white'): 'The birds and beasts are entirely white.',
        ('range3-summary','sheep'): 'All their deities have sheep bodies and human faces.',
        ('range3-summary','rite'): 'Their rite uses one auspicious jade object, buried, with millet grain as the offering.',
        ('range4-summary','rite'): 'The rite uses one white chicken in prayer, rice grain as the offering and white guan for a mat.',
    }
    if (slug,key) in overrides:
        return overrides[(slug,key)]
    first = text.split('. ')[0].split(';')[0]
    first = re.split(r',? (?:without |rather than |and is glossed |glossed as |with namesake contexts )', first)[0]
    if any(word in first.lower() for word in ['commentary', 'edition character', 'edition’s qi', 'is only named in the main text', 'an unnamed collective', 'retained', 'separately indexed', 'no form', 'does not identify']):
        return name+' is recorded in this passage.'
    return first.rstrip(' ,;.')+'.'


def extend(rows, entities, corrections):
    corrections.update({f'source-02-{n:04}': 58 + (n-225)//9 for n in range(225, 370, 9)})
    for slug, name, en_name, start, end, range_no, description, english in STAGES:
        rows.append(dict(slug=slug, name=name, en_name=en_name, units=(start, end), range=range_no,
                         batch='xishan-'+slug, description=description, en_description=english,
                         en_quote=main_translation(english), subjects=[name], is_summary='summary' in slug or slug=='western-total'))
    entities[:] = [e for e in entities if e['id'] != 'place-xishan-kunlun']
    core_ids = {'luwu': 'beast-luwu', 'tulou': 'beast-tulou', 'qinyuan': 'beast-qinyuan',
                'zheng': 'beast-zheng', 'bifang': 'beast-bifang', 'tiangou': 'beast-tian-gou',
                'dijiang': 'beast-dijiang', 'huan': 'beast-guan', 'bo': 'beast-bo',
                'qiongqi': 'beast-qiongqi-xishan', 'luoyu': 'beast-luoyu'}
    for line in ENTITY_TEXT.strip().splitlines():
        if not line.strip():
            continue
        slug, kind, key, name, en_name, quote, description, english = line.split('|')
        unknown = kind.endswith('?')
        kind = kind.rstrip('?')
        id = core_ids.get(key, f'{kind}-xishan-{key}-{slug}')
        # The old core beast IDs remain addressable rather than creating parallel species cards.
        group = 'beasts' if kind in {'beast', 'bird'} or id in core_ids.values() else 'text_entities' if kind in {'deity', 'place', 'rite'} else 'natural_features'
        entity = dict(id=id, slug=slug, kind=kind, group=group, name=name, en_name=en_name,
                      quote=quote, description=description, en_description=english,
                      en_quote=entity_translation(slug,key,en_name,english), art=None)
        if unknown:
            entity['appearance_unknown'] = True
        entities.append(entity)
        row = next(r for r in rows if r['slug'] == slug)
        row['subjects'].append(name)
    for entity in entities:
        if entity['id'] in {'deity-xishan-rushou-youshan','bird-xishan-xiao-baiyu'}:
            entity.pop('appearance_unknown', None)
            entity['art_reference'] = ('郭注形貌参考 · 正文仅列名或居处，图像为艺术演绎。', 'Form based on Guo Pu commentary · Main text only names the creature or its dwelling; the image is an artistic interpretation.')
        if entity['id'] == 'beast-xishan-saoyu-niaoshu':
            entity['art_reference'] = ('正文鱣状；颔下口与连甲参考郭注 · 木刻为艺术演绎。', 'Main-text zhan-like form; lower mouth and linked armor follow Guo Pu commentary · Artistic woodcut interpretation.')
        if entity['id'] == 'bird-xishan-chi-sanwei':
            entity['art_reference'] = ('正文一首三身；鵰状黑文赤颈参考郭注 · 木刻为艺术演绎。', 'Main text: one head and three bodies; eagle-like form, black markings and red neck follow Guo Pu commentary · Artistic interpretation.')
    for row in rows:
        if row['slug'] == 'yingdi':
            row['text_replacements'] = {'⟦缺字图:⿰氵𭝠--𣾰⟧': '𣾰'}
    glosses = {
        'luwu': '即有吾也莊周曰肩吾得之以處大山也；主九城之部界天帝苑圃之時節也',
        'qinyuan': '欽或作爰或作至也', 'chun': '服噐服也一曰服事也或作蔵',
        'shatang': '棠梨也；言体浮輕也沙棠為木不可得沉吕氏春秋曰果之羙者沙棠之實銘曰安得沙棠刻以為舟汎彼滄海以遨以遊',
        'xiao': '鴞似鳩而靑色',
        'pin': '音頻；吕氏春秋曰菜之羙者崑崙之蘋',
        'changcheng': '九徳九氣所生；之藥反',
        'xiwangmu': '蓬頭亂髪勝玉勝也音龐；主知灾厲五刑殘殺之氣也',
        'jiao': '或作羊；晉太康七年邵𨹧扶夷縣檻得一獸状如豹文有二角無前两脚時人謂之狡疑非此',
        'shengyu': '音姓；音録義未詳',
        'weishi': '音隗；日西入則景反東照主司察之',
        'zheng': '京氏易義曰音如石相擊音静也', 'bifang': '譌亦妖訛字',
        'tiangou': '或作豹；或作猫猫',
        'aoyu': '蓑辟雨之衣也音梭；傲噎二音',
        'chi': '𪇱似鵰黒文赤頸音洛下句或云扶狩則短扶木則枯應在上欽原下脫錯在此耳',
        'qitong': '𦒿童老童顓頊之子',
        'dijiang': '体色黄而精光赤也；夫形無全者則神自然靈照精無見者則闇與理㑹其帝江之謂乎莊生所云中央之帝混沌爲儵忽所鑿七竅而死者盖假此以寓言也',
        'rushou': '亦金神也；人靣虎𤓰白尾執龯見外傳云', 'hongguang': '未聞其状',
        'huan': '讙音歡或作原；言其作百種物聲也或曰奪百物名亦所未詳；黄癉病也音旦',
        'qiyu': '猗餘兩音；不厭夣也周書曰服者不昩音莫禮反或曰𭥻𭥻目也',
        'danghu': '或作户；髯咽下須毛也；音〔录文缺字待核〕',
        'ranyi': '',
        'bo': '爾雅駮不道有角及虎𤓰駮亦在畏狩𦘕中；養之辟兵刃也',
        'huai': '木𤓰如小𤓰；音懷；尸子曰木食之人多為仁者名為若木此之𩔗',
        'qiongqi': '或云似虎蝟毛有翼銘曰窮竒之獸厥形甚醜馳逐妖邪莫不奔走是以一名號曰神狗',
        'saoyu': '音騷；鱣魚大魚也口在頷下躰有連甲也或作鮎鯉；或脫無從動則以下語者',
        'rupi': '如玭两音；亦珠母蚌𩔗而生出之',
        'shuhu': '喜抱舉人',
        'unnamed': '蜼猕猴属也音贈遺之遺一音誄見中山經尾又作眥；或作設設亦呼耳疑此脫誤',
    }
    for entity in entities:
        if entity['slug'] not in {s[0] for s in STAGES}:
            continue
        key = next((line.split('|')[2] for line in ENTITY_TEXT.strip().splitlines() if line and line.split('|')[0] == entity['slug'] and line.split('|')[3] == entity['name']), '')
        if key in glosses and (key != 'chi' or entity['slug'] == 'sanwei'):
            entity['commentary_quote'] = glosses[key]
        if entity['id'] == 'deity-xishan-chi-gangshan':
            entity['commentary_quote'] = '𩳁亦魑魅之𩔗也音耻回反或作𩲶；欽亦吟字假音'
        if key in {'saoyu','chi','unnamed','rushou'}:
            entity['content_note'] = '正文与郭注形貌分层；本卡说明中明确标出的郭注比较不改写为正文。注文按电子捕获保留，未确认漏字不猜补。'
            entity['en_content_note'] = 'Main-text form and explicitly attributed commentary comparisons remain distinct. Captured glosses are retained without guessing unconfirmed missing characters.'


REUSE = {
    'beast-xishan-zhuyan-xiaoci': 'beast-zhuyan',
    'deity-xishan-yingzhao-huaijiang': 'beast-yingzhao',
    'beast-xishan-wenyao-taiqi': 'beast-wenyaoyu',
    **{id: id for id in ['beast-luwu', 'beast-tulou', 'beast-qinyuan', 'beast-zheng',
                        'beast-bifang', 'beast-tian-gou', 'beast-dijiang', 'beast-guan',
                        'beast-qiongqi-xishan', 'beast-luoyu']},
}


def finish(passages, records, en, relations):
    by_id = {r['id']: r for _, r in records}
    passage_by_slug = {p['id'].removeprefix('passage-xishan-'): p for p in passages}
    legacy_core = {'beast-luwu','beast-tulou','beast-qinyuan','beast-zheng','beast-bifang',
                   'beast-tian-gou','beast-dijiang','beast-guan','beast-bo','beast-qiongqi-xishan','beast-luoyu'}
    for id in legacy_core:
        by_id[id].update(reveal_stage=5, reveal_chapter='05', place_id='place-west-ranges',
                         place_basis='《西山经》山系篇目锚点·示意，不指向具体山峰。',
                         illustration_review='原文摘录已核对；图像按原文形态核验')
    aliases = {'beast-luwu':['陆吾'], 'beast-tulou':['土蝼'], 'beast-qinyuan':['钦原'], 'beast-bifang':['毕方'], 'beast-qiongqi-xishan':['穷奇'], 'beast-luoyu':['蠃鱼'], 'beast-bo':['驳']}
    for id, names in aliases.items():
        by_id[id]['aliases'] = names
    for id in ['passage-xishan-huaijiang','place-xishan-huaijiang']:
        en[id]['content_note'] = en[id]['content_note'].replace('Dan is retained as the edition name, not a modern Mount Heng.', 'The Chinese edition name is retained without asserting its ancient pronunciation or identifying a modern Mount Heng.')
        en[id]['description'] = en[id]['description'].replace('and four-tiered mountain','and a four-tiered mountain')
        by_id_record = passage_by_slug['huaijiang'] if id.startswith('passage-') else by_id['place-xishan-huaijiang']
        by_id_record['content_note'] = by_id_record['content_note'].replace('南望崑崙只先建上下文，下一崑崙主段尚未接入', '南望与崑崙主段已聚合到同一稳定山卡，两个出处分别保留')
        en[id]['content_note'] = en[id]['content_note'].replace('Kunlun’s southern view is documented here ahead of its own passage.', 'Kunlun’s southern view and main passage share a stable mountain ID while retaining separate sources.')
    kunlun = by_id['place-xishan-kunlun']
    huaijiang = passage_by_slug['huaijiang']
    kunlun['quote'] = '南望崑崙其光熊熊其氣魂魂；' + kunlun['quote']
    kunlun['source_passage_ids'].insert(0, huaijiang['id'])
    kunlun['related_entry_ids'].insert(0, huaijiang['id'])
    kunlun['context_place_ids'] = ['place-xishan-huaijiang', 'place-xishan-kunlun']
    for field in ['source_pages', 'source_unit_ids']:
        kunlun[field] = list(dict.fromkeys([*huaijiang[field], *kunlun[field]]))
    pages = sorted({int(url.rsplit('/', 1)[-1]) for url in kunlun['source_pages']})
    kunlun['source_locator'] = '卷第二 · 影印页 ' + '、'.join(map(str, pages))
    en[kunlun['id']]['source_locator'] = 'Volume 2 · scan pages ' + ', '.join(map(str, pages))
    kunlun['commentary_quote'] = '〔槐江南望注〕皆光氣炎盛相焜燿之貌\n' + kunlun['commentary_quote']
    kunlun['content_note'] = '分号分隔槐江南望与崑崙主段，不是连续经文；同山稳定ID复用，鍾段崑崙之阳仍为独立事件子地点，不补现代坐标。'
    en[kunlun['id']]['quote'] = 'To the south is Kunlun with brilliant light and vapor; in its separate main passage: ' + en[kunlun['id']]['quote']
    en[kunlun['id']]['content_note'] = 'The semicolon separates Huaijiang’s view from Kunlun’s main passage. The stable mountain ID is reused; Zhong’s sunny-side event location remains distinct.'
    huaijiang['related_entry_ids'].append(kunlun['id'])
    liusha = by_id['place-xishan-liusha']
    luomu = passage_by_slug['luomushan']
    liusha['description'] = liusha['description'].replace('；后文同名流沙待核时再增加出处。','。')
    en[liusha['id']]['description'] = en[liusha['id']]['description'].replace('; later namesake references remain to be reviewed.','.')
    liusha['quote'] += '；西水行四百里曰流沙二百里至于蠃母之山'
    liusha['description'] += ' 蠃母山段另记水行四百里至流沙、再二百里至蠃母；同名出处分别保留，不据此强合现代沙漠、水域或行程坐标。'
    liusha['source_passage_ids'].append(luomu['id'])
    liusha['related_entry_ids'].append(luomu['id'])
    for field in ['source_pages', 'source_unit_ids']:
        liusha[field] = list(dict.fromkeys([*liusha[field], *luomu[field]]))
    liusha['context_place_ids'] = ['place-xishan-taiqi', 'place-xishan-luomushan']
    liusha_pages = sorted({int(url.rsplit('/',1)[-1]) for url in liusha['source_pages']})
    liusha['source_locator'] = '卷第二 · 影印页 ' + '、'.join(map(str,liusha_pages))
    en[liusha['id']]['source_locator'] = 'Volume 2 · scan pages ' + ', '.join(map(str,liusha_pages))
    en[liusha['id']]['description'] += ' The separate Luomu route travels west by water for four hundred li to Liusha, then two hundred li to Luomu, without identifying a modern desert or waterway.'
    en[liusha['id']]['quote'] += ' Separately: west by water for four hundred li to Liusha, then two hundred li to Mount Luomu.'
    liusha['content_note'] = '分号分隔㤗噐水文与蠃母行程，不是连续经文；稳定ID和原始context保留，流沙不臆定为现代沙漠或水体。'
    en[liusha['id']]['content_note'] = 'The semicolon separates Taiqi’s water account from Luomu’s route. The stable ID and original context remain; no modern desert or waterbody is asserted.'
    luomu['related_entry_ids'].append(liusha['id'])
    relations.append(dict(ids=[liusha['id'],'place-xishan-luomushan'], source='《西山经》', quote='西水行四百里曰流沙二百里至于蠃母之山', labels=['后续二百里 · 蠃母山','前程流沙参照']))
    relations.append(dict(ids=['place-yushan','place-xishan-yushan'], source='《西山经》', quote='又西三百五十里曰玉山是西王母所居也', labels=['玉山完整山段索引','原有玉山入口']))
    relations.append(dict(ids=[kunlun['id'], 'place-xishan-kunlun-yang-zhongshan'], source='《西山经》',
                          quote='殺葆江于崑崙之陽', labels=['参见阳面事件地点', '所属山名索引']))
    # Cross-stage route links stop at range boundaries and preserve the edition's exact clauses.
    for range_no in [3, 4]:
        route = [p for p in passages if p['range'] == range_no and not p.get('is_summary')]
        for previous, current in zip(route, route[1:]):
            slug = current['id'].removeprefix('passage-xishan-')
            if slug not in {s[0] for s in STAGES}:
                continue
            quote = current['quote'].split('曰', 1)[0] if '曰' in current['quote'] else current['quote'][:30]
            if slug == 'luomushan':
                quote = '西水行四百里曰流沙二百里至于蠃母之山'
            relations.append(dict(ids=[previous['id'].replace('passage-', 'place-', 1), current['id'].replace('passage-', 'place-', 1)],
                                  source='《西山经》', quote=quote, labels=['下一山 · 原文里程', '上一山 · 篇内次序']))
    def edge(slug, left, right, labels):
        p = passage_by_slug[slug]
        a, b = by_id[left], by_id[right]
        quote = a['quote'] if len(a['quote']) >= len(b['quote']) else b['quote']
        assert quote in p['quote'], (slug, left, right)
        relations.append(dict(ids=[left, right], source='《西山经》', quote=quote, labels=labels))
    for slug, key, dest in [('kunlun','he','wuda'),('kunlun','chi','fantian'),('kunlun','yang','choutu'),
                            ('kunlun','hei','dayu'),('leyou','tao','jize'),('xuanyuan','xun','hei'),
                            ('yinshan3','zhuoyu','fan'),('tianshan','ying','tang'),('yinshan4','yin','luo'),
                            ('laoshan','ruo','luo'),('bafu','er','luo'),('shenshan','qu','he'),
                            ('niaoshan','ru','he'),('shangshen','tang','he'),('zhuci','zhuci','he'),
                            ('haoshan','duan','he'),('yushan4','sheng','he'),('baiyu','luo','wei'),
                            ('baiyu','jia','sheng'),('jinggu','jing','wei'),('gangshan','gang','wei'),
                            ('gangwei','luo','he'),('yingdi','wan','lingyang'),('guishan4','meng','yang'),
                            ('niaoshu','wei','he'),('niaoshu','lan','han'),('yanzi','tiao','sea')]:
        left = f'water-xishan-{key}-{slug}'
        right = f'water-xishan-{dest}-{slug}'
        if right not in by_id:
            right = f'place-xishan-{dest}-{slug}'
        edge(slug,left,right,['原文所注 · 详见流向','本段来水'])
    for slug, water, beast in [('leyou','tao','beast-xishan-huayu-leyou'),
                                ('gangwei','luo','beast-xishan-manman-gangwei'),
                                ('yingdi','wan','beast-xishan-ranyi-yingdi'),
                                ('guishan4','meng','beast-luoyu'),('niaoshu','wei','beast-xishan-saoyu-niaoshu'),
                                ('niaoshu','lan','beast-xishan-rupi-niaoshu')]:
        edge(slug,f'water-xishan-{water}-{slug}',beast,['本段水中生物','水文上下文'])
    for _, record in records:
        if record['kind'] == 'place' and record.get('context_place_ids'):
            record['context_place_ids'] = [id for id in record['context_place_ids'] if id != record['id']]
    for slug, p in passage_by_slug.items():
        if slug in {s[0] for s in STAGES}:
            assert p['source_unit_ids'] and p['related_entry_ids'] or slug == 'western-total'

"""Build a complete passage reader, preserving the captured transcription separately."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def read(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))
def write(path, value):
    (ROOT / path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Each row starts at an exact textual boundary, not at a modern geographic location.
ROWS = [
('zhaoyao','招摇之山','南山經之首',1,'西海之上的招摇山，多桂木、金玉。祝余形似韭草，迷谷有黑理而花光四照；白耳狌狌伏行其间。丽𪊨之水向西入海，水中记有形貌未详的育沛。经文另记食、佩这些对象的功效。','Mount Zhaoyao','Cassia, herbs and an unusual tree open the account above the Western Sea.','The Southern Mountains begin with the Que range. Its first mountain, Zhaoyao, overlooks the Western Sea and has cassia, metals and jade. Zhuyu resembles chives and has blue-green flowers; eating it is said to prevent hunger. Migu resembles gu, has dark grain and shining flowers; carrying it is said to prevent losing the way. Shengsheng resembles an ape with white ears, crouching and walking like a person; eating it is said to aid running. The Li𪊨 River flows west to the sea, with Yupei said to prevent abdominal affliction when worn.','招摇之山 桂 金玉 祝余 迷谷 狌狌 丽𪊨之水 育沛'),
('tangting','堂庭之山','又東三百里曰堂庭',1,'向东三百里是堂庭山。山中多棪木、白猿、水玉与黄金，记述没有展开异兽情节。郭注把水玉解释为水精，并说明棪的果实似柰而赤、可以食用；这属于注文层次。','Mount Tangting','Yan trees and white apes appear among the minerals of Tangting.','Three hundred li east is Mount Tangting, with many yan trees, white apes, water jade and gold.','堂庭之山 棪木 白猿 水玉 黄金'),
('yuanyi','猨翼之山','又東三百八十里曰猨翼',1,'再向东三百八十里，猨翼山多怪兽，水中多怪鱼，又有白玉、蝮虫、怪蛇与怪木。经文以“不可以上”收住，没有为这些怪异对象逐一取名，也没有叙述登山经过。','Mount Yuanyi','An inaccessible mountain is described through its strange creatures and trees.','Another 380 li east is Mount Yuanyi. It has unusual beasts, unusual fish in its waters, white jade, venomous creatures, strange snakes and strange trees. It cannot be ascended.','猨翼之山 怪兽 怪鱼 白玉 蝮虫 怪蛇 怪木'),
('niuyang','杻阳之山','又東三百七十里曰杻陽',1,'杻阳山向阳面多赤金，背阴面多白金。白首、虎纹、赤尾的鹿蜀鸣声如歌；怪水向东注入宪翼之水，随后出现鸟首虺尾的旋龟。郭注以铜、银分别解释赤金、白金。','Mount Niuyang','The account moves from the two mineral-bearing slopes to the Guai River.','Another 370 li east is Mount Niuyang: red metal on its sunny side and white metal on its shaded side. Lushu resembles a horse with a white head, tiger markings, a red tail and a singing cry; wearing it is said to favor descendants. The Guai River flows east into Xianyi. The following water description records dark turtles called Xuangui, with bird heads and serpent tails, calling like splitting wood. Wearing them is said to prevent deafness and treat ailments.','杻阳之山 赤金 白金 鹿蜀 怪水 宪翼之水 旋龟'),
('di','祗山','東三百里祗山',1,'向东三百里是底本所写的祗山，多水而无草木。鯥虽被列为鱼，却像牛，居于陆地，有蛇尾与生在胁下的翼，叫声与牛相类，所比之名含一个待核图字。经文写它冬死夏生；郭注将此解释为蛰伏，而非另造复生故事。','Fifth mountain','Lu combines the account’s categories of fish and land-dwelling form.','Three hundred li east is the fifth mountain, with much water but no vegetation. A fish called Lu resembles an ox, lives on land, has a serpent tail and wings beneath its flanks, and has a bovine-like cry; the precise comparison includes an unresolved image glyph. It is said to die in winter and live in summer; eating it is said to prevent swelling.','祗山 鯥'),
('danyuan','亶爰之山','又東四百里曰亶爰',1,'亶爰山多水，无草木，不可以上。山中之兽𩔗像狸而有髦，经文又写它自为牝牡，食者不妒。这里保留其特异形貌和古籍功效说法，不把它确定为今天的某一种动物。','Mount Danyuan','Water and an inaccessible slope surround a mane-bearing creature.','Another 400 li east is Mount Danyuan, with water but no vegetation; it cannot be ascended. A creature named 𩔗 resembles a wildcat with a mane and is described as both female and male. Eating it is said to prevent jealousy.','亶爰之山 𩔗'),
('jishan','基山','又東三百里曰基山',1,'基山阳面多玉，阴面多怪木。猼訑像羊，有九尾、四耳，眼在背上；𪁺𩿧像鸡，却有三首、六目、六足、三翼。佩猼訑不畏、食鸟无卧，均是经文中的记述。','Mount Ji','Two creatures are described by their unusually numbered body parts.','Another 300 li east is Mount Ji, with jade on its sunny side and strange trees on its shaded side. Boyi resembles a sheep with nine tails, four ears and eyes on its back; wearing it is said to prevent fear. The chicken-like bird 𪁺𩿧 has three heads, six eyes, six feet and three wings; eating it is said to prevent sleep.','基山 猼訑 𪁺𩿧'),
('qingqiu','青丘之山','又東三百里曰青丘',1,'青丘山阳面多玉，阴面多青雘。九尾狐的声音像婴儿，灌灌像鸠，鸣声仿佛人在相呼。英水向南流入即翼之泽，随后写到鱼身人面的赤鱬，并分别记述这些对象的食用或佩用功效。','Mount Qingqiu','Birds and beasts on the mountain give way to the Ying River.','Another 300 li east is Qingqiu, with jade on its sunny side and green mineral on its shaded side. A nine-tailed fox cries like an infant and can eat people; eating it is said to ward off gu. Guanguan resembles a dove and calls as if calling out; wearing it is said to prevent bewilderment. The Ying River flows south into Jiyi Marsh. These waters contain Chiru with fish bodies, human faces and mandarin-duck-like calls; eating them is said to prevent skin disease.','青丘之山 九尾狐 灌灌 英水 即翼之泽 赤鱬'),
('jiwei','箕尾之山','又東三百五十里曰箕尾',1,'箕尾山在前山以东三百五十里，山尾临着东海，多沙石。汸水从这里流出，向南汇入淯，水中多白玉。文字以山尾、海岸和水流，结束这一列山的逐山叙述。','Mount Jiwei','A mountain tail meets the eastern sea, with a river flowing south.','Another 350 li east is Mount Jiwei, whose tail sits above the Eastern Sea. It has sand and stones. The Fang River rises here and flows south into Yu, with much white jade in its waters.','箕尾之山 东海 汸水 淯 白玉'),
('range1','䧿山总述与祭祀','凡䧿山之首',1,'这一段回数招摇至箕尾的山列，底本写十山、二千九百五十里；山神皆鸟身龙首。祭礼涉及牲毛、璋玉瘗埋、稌米、稻米和白菅席。山数与逐项列名并不一致，这里照录而不凑补山名。','Que range · totals and rites','The mountain descriptions close with divine forms and offerings.','The Que range, from Zhaoyao to Jiwei, is stated to comprise ten mountains and 2,950 li. Its deities have bird bodies and dragon heads. The rite specifies a single animal offering by its coat, burial of a zhang jade, rice offerings, and a white-jian grass mat. The text also retains the phrase “one bi, rice.”','山神 鸟身龙首 祭祀 璋玉 稌米 稻米 白菅'),
('gui','柜山','南次二',2,'南次二经从柜山起。它西临流黄，北望诸毗，东望长右；英水向西南汇入赤水，多白玉与丹粟。狸力像豚而有距，鴸像鸱而足似人手；二者的出现分别与土功、放士相联系。此英水与青丘英水分段记录。','Mount Gui','A second range opens with named outlooks, another Ying River and two creatures.','The second Southern range begins at Gui: facing Liuhuang west, Zhupi north and Changyou east. Its Ying River flows southwest into Red Water, containing white jade and cinnabar grains. Lili resembles a pig with spurs and barks like a dog; its appearance is said to accompany earthworks. Zhu resembles a kite with human-hand-like feet, makes a bi-like sound and calls its name; its appearance is said to accompany dismissed officials.','柜山 流黄 诸毗 长右 英水 赤水 丹粟 狸力 鴸'),
('changyou','长右之山','東南四百五十里曰長右',2,'向东南四百五十里，长右山无草木而多水。名为长右的兽像禺，有四耳，声音如吟；郭注说像人的呻吟。经文把它的出现与郡县大水相连，是古籍中的征兆叙述。','Mount Changyou','A four-eared creature shares its name with the mountain.','Southeast for 450 li is Mount Changyou, with water but no vegetation. The ape-like, four-eared Changyou makes a moaning sound. Its appearance is said to foretell great floods in the district.','长右之山 长右 水灾征兆'),
('yaoguang','尧光之山','又東三百四十里曰堯光',2,'尧光山阳面多玉，阴面多金。猾褢像人，身有猪鬣，穴居而冬蛰，叫声像劈木。它出现时“县有大繇”；郭注解释为劳役，又保存作乱的异说。','Mount Yaoguang','A cave-dwelling, winter-dormant creature is heard like an axe on wood.','Another 340 li east is Mount Yaoguang, with jade on its sunny side and metal on its shaded side. Huahuai is human-like with pig bristles, lives in caves and is dormant in winter. It sounds like chopping wood; its appearance is said to accompany great labor levies in the district.','尧光之山 猾褢 大繇'),
('yu','羽山','又東三百五十里曰羽山',2,'羽山在前山以东三百五十里。山下多水，山上多雨，无草木，多蝮虫。郭注谈到后世所指的羽山，却又指出按这段道里推算似乎不合；这份疑问也应保留。','Mount Yu','Water below and rain above define this bare mountain.','Another 350 li east is Mount Yu. It has much water below and much rain above, no vegetation, and many venomous creatures.','羽山 蝮虫'),
('qufu','瞿父之山','又東三百七十里曰瞿父',2,'再向东三百七十里是瞿父山。经文只说它没有草木，多金玉，没有记名异兽、水流或祭礼。简短的物产记录也是原书的一部分，不另补出传说。','Mount Qufu','A short entry records absence of vegetation and the presence of minerals.','Another 370 li east is Mount Qufu, without vegetation and with much metal and jade.','瞿父之山 金玉'),
('gouyu','句余之山','又東四百里曰句餘',2,'句余山在前山以东四百里，无草木，多金玉。郭注另记会稽余姚、句章一带的地名解释。经文的物产与注文的后世地望分开呈现，不据此新增现代坐标。','Mount Gouyu','Minerals are recorded; later geographic identification belongs to the commentary.','Another 400 li east is Mount Gouyu, without vegetation and with much metal and jade.','句余之山 金玉'),
('fuyu','浮玉之山','又東五百里曰浮玉',2,'浮玉山北望具区，东望诸毗。彘像虎而有牛尾，叫声像犬，能食人。苕水从山阴流出，向北汇入具区，水中多鮆鱼。山上的兽和水中的鱼各依原文记录。','Mount Fuyu','Outlooks, a tiger-like beast and a northward river form one passage.','Another 500 li east is Fuyu, looking north to Juqu and east to Zhupi. Zhi resembles a tiger with an ox tail, barks like a dog and eats people. The Tiao River rises on the shaded side and flows north into Juqu, with many ji fish.','浮玉之山 具区 诸毗 彘 苕水 鮆鱼'),
('cheng','成山','又東五百里曰成山',2,'成山四方而有三重坛状层次，山上多金玉，山下多青雘。䦠水向南流入虖勺，水中多黄金。郭注用层叠的筑坛来解释山形，而非记载这里实际建有三座祭坛。','Mount Cheng','The mountain’s layered form is compared to terraces.','Another 500 li east is Mount Cheng, square and in three terrace-like tiers. Metals and jade occur above, green mineral below. A river flows south into Hushao and contains much gold.','成山 三坛 青雘 䦠水 虖勺 黄金'),
('kuaiji','会稽之山','又東五百里曰會稽',2,'向东五百里，会稽山呈四方之形，上多金玉，下多砆石。勺水从这里流出，向南汇入湨。郭注又解释砆石的颜色和纹理；它与玉的相似是注文中的说明。','Mount Kuaiji','A square mountain yields minerals and a southward river.','Another 500 li east is square Mount Kuaiji, with metals and jade above and fu stone below. The Shao River rises here and flows south into Ju.','会稽之山 砆石 勺水 湨'),
('yi','夷山','又東五百里曰夷山',2,'夷山无草木，多沙石。湨水从这里流出，向南注入列涂。它承接前段水名，却另有本山的出水记述；这里保留原文，不自行重建一条完整河道。','Mount Yi','Sand and stone surround the stated source of the Ju River.','Another 500 li east is Mount Yi, with no vegetation and much sand and stone. The Ju River rises here and flows south into Lietu.','夷山 湨水 列涂'),
('pugou','仆勾之山','又東五百里曰僕勾',2,'仆勾山上多金玉，下多草木，却没有鸟兽，也没有水。经文把有与无并列写出，没有进一步解释缘由。','Mount Pugou','Vegetation is present below, while birds, beasts and water are absent.','Another 500 li east is Mount Pugou: metals and jade above, vegetation below, but no birds or beasts and no water.','仆勾之山 金玉 草木'),
('xun','洵山','又東四百里曰洵山',2,'洵山阳面多金，阴面多玉。䍺像羊而无口，经文说不可杀；洵水向南流入阏之泽，水中多芘蠃。这一整段原先因电子录文缺页而漏收，现据第26页补录。','Mount Xun','The restored scan page records a mouthless sheep-like creature and a river.','Another 400 li east is Mount Xun, with metal on its sunny side and jade on its shaded side. Huan resembles a sheep but has no mouth and cannot be killed. The Xun River flows south into Yan Marsh and contains many piluo.','洵山 䍺 洵水 阏之泽 芘蠃'),
('hushao','虖勺之山','又東四百里曰虖勺',2,'虖勺山上多梓、楠，山下多荆、杞。滂水从这里流出，向东入海。它与前文作为流入对象的虖勺同名，山与水的称谓仍按各段保留，不据同名作额外判断。','Mount Hushao','Trees and shrubs are followed by an eastward outlet to the sea.','Another 400 li east is Mount Hushao, with zi and nan trees above and jing and qi shrubs below. The Pang River rises here and flows east into the sea.','虖勺之山 梓 楠 荆 杞 滂水'),
('quwu','区吴之山','又東五百里曰區吳',2,'区吴山无草木，多沙石。鹿水从这里流出，向南注入滂水。此前滂水已经出现在虖勺山段，这里只增加经文明确写出的汇入关系。','Mount Quwu','The Lu River joins Pang after flowing south from a bare mountain.','Another 500 li east is Mount Quwu, without vegetation and with much sand and stone. The Lu River rises here and flows south into Pang.','区吴之山 鹿水 滂水'),
('xianyin','咸阴之山','又東五百里曰咸隂',2,'咸阴山在前山以东五百里，无草木，也无水。原文止于这两项环境记述，没有更多形貌或异兽内容。','Mount Xianyin','Two absences make up this very brief mountain entry.','Another 500 li east is Mount Xianyin, without vegetation and without water.','咸阴之山'),
('luwu','鹿吴之山','又東五百里曰鹿吳',2,'鹿吴山上无草木，多金石。泽更之水向南注入滂水；水中有蛊雕，像雕而有角，声音像婴儿，能食人。底本明确从水中引出这只兽，不能把它的出现位置改写成纯陆地。','Mount Luwu','The horned Gudiao is introduced in a water description.','Another 500 li east is Luwu, without vegetation above and with metals and stones. Zegeng Water flows south into Pang. In the water is Gudiao, resembling an eagle with horns, crying like an infant and eating people.','鹿吴之山 泽更之水 滂水 蛊雕'),
('qiwu','漆吴之山','東五百里曰漆吳',2,'漆吴山无草木，多博石而无玉，处于海边，向东望丘山。经文写其光时出时入，称作日次；郭注以日景的止舍解释。这里保留这段光与方位的叙述，不补造天文位置。','Mount Qiwu','The passage ends with an eastern outlook and intermittent light.','Five hundred li east is Mount Qiwu, with no vegetation, many stones for game pieces and no jade. It stands by the sea, looking east to Qiushan. Its light appears and disappears; this is called a station of the sun.','漆吴之山 博石 丘山 日次'),
('range2','南次二经总述与祭祀','凡南次二經',2,'从柜山到漆吴山，底本总计十七山、七千二百里。山神皆龙身鸟首；祭礼简记牲毛、一璧瘗埋和以稌米为糈。总述与各山的物产、异兽并列保留。','Second range · totals and rites','A count and a sacrificial prescription close the second range.','The second Southern range, from Gui to Qiwu, is stated to contain seventeen mountains over 7,200 li. Its deities have dragon bodies and bird heads. The rite specifies an animal offering, burial of one bi jade and rice as the grain offering.','山神 龙身鸟首 祭祀 璧 稌米'),
('tianyu','天虞之山','南次三經',3,'南次三经以天虞山为首。山下多水，不可以上。经文没有在这里展开山顶、草木或鸟兽，而由这短短一句开启第三列山。','Mount Tianyu','Water below an inaccessible mountain opens the third range.','The third Southern range begins at Mount Tianyu. Below it is much water; it cannot be ascended.','天虞之山'),
('daoguo','祷过之山','東五百里曰禱過',3,'祷过山上多金玉，下多犀、兕、象。瞿如像鵁，有白首、三足、人面，鸣声自呼其名。泿水向南入海，水中虎蛟鱼身蛇尾、鸣如鸳鸯；经文还记其食用功效。','Mount Daoguo','Large animals, a three-footed bird and a fish-bodied creature share this passage.','Five hundred li east is Daoguo, with metal and jade above and rhinoceroses, si and elephants below. Quru resembles a jiao waterbird, with a white head, three feet and a human face, calling its own name. Yin Water flows south into the sea and contains Hujiao, with a fish body, serpent tail and a mandarin-duck-like call; eating it is said to prevent swelling and treat hemorrhoids.','祷过之山 犀 兕 象 瞿如 泿水 虎蛟'),
('danxue','丹穴之山','又東五百里曰丹穴',3,'丹穴山多金玉，丹水从这里向南流入㴾海。凤皇像鸡而有五彩纹，头、翼、背、胸、腹的纹分别被称为德、义、礼、仁、信。它饮食自然，自歌自舞，出现时天下安宁。','Mount Danxue','The Fenghuang is described through color, patterned virtues, song and dance.','Another 500 li east is Danxue, with metals and jade. Dan Water flows south into the Bohai named in this passage. Fenghuang resembles a chicken with five-colored patterns: virtue on the head, righteousness on the wings, ritual on the back, benevolence on the breast and trust on the belly. It feeds naturally, sings and dances of itself; its appearance is said to bring peace to the world.','丹穴之山 丹水 㴾海 凤皇 德 义 礼 仁 信'),
('fashuang','发爽之山','又東五百里曰發爽',3,'发爽山无草木，多水、多白猿。汎水从这里流出，向南注入㴾海。经文将白猿的出现和水流并记，没有为白猿附加新的功效或故事。','Mount Fashuang','White apes and flowing water occur on a mountain without vegetation.','Another 500 li east is Fashuang, without vegetation, with much water and many white apes. Fan Water rises here and flows south into the Bohai named in the text.','发爽之山 白猿 汎水 㴾海'),
('maowei','旄山之尾','又東四百里至于旄山',3,'向东四百里，到旄山之尾。南面有名叫育遗的谷地，多怪鸟，凯风从这里出来。山尾、谷名、怪鸟和风源共同构成这段记述；郭注把凯风解释为南风。','Tail of Mount Mao','A valley south of the mountain tail is named as the origin of a wind.','Another 400 li east reaches the tail of Mount Mao. To its south is Yuyi Valley, with many strange birds. The Kai wind emerges from it.','旄山之尾 育遗 凯风 怪鸟'),
('feitou','非山之首','又東四百里至于非山',3,'再向东四百里，到非山之首。山上多金玉而无水，山下多蝮虫。这里的“首”是原文对山体部位的称呼，不另画出现代行政边界。','Head of Mount Fei','Minerals above contrast with venomous creatures below.','Another 400 li east reaches the head of Mount Fei, with much metal and jade above but no water, and many venomous creatures below.','非山之首 蝮虫 金玉'),
('yangjia','阳夹之山','又東五百里曰陽夾',3,'阳夹山无草木，多水。原文只保留这两项环境特征，没有写出水名和去向，也没有记名鸟兽。','Mount Yangjia','Water is recorded without a named river or outlet.','Another 500 li east is Mount Yangjia, with no vegetation and much water.','阳夹之山'),
('guanxiang','灌湘之山','又東五百里曰灌湘',3,'灌湘山上多木而无草，多怪鸟而无兽。树木与草、鸟与兽在原文中分别表述，不能将“无兽”转述成没有任何动物。','Mount Guanxiang','Trees and birds are present, while grasses and beasts are absent.','Another 500 li east is Mount Guanxiang, with many trees but no grasses, many unusual birds but no beasts.','灌湘之山 木 怪鸟'),
('ji','鸡山','又東五百里曰鷄山',3,'鸡山上多金，下多丹雘。黑水向南流入海中，水中有鱄鱼，像鲋而有猪毛，声音像豚。它的出现被写作天下大旱的征兆，这属于古籍的灾异叙述。','Mount Ji · Chicken Mountain','Black Water contains a bristled fish associated with drought.','Another 500 li east is Chicken Mountain, with metal above and red mineral below. Black Water flows south into the sea and contains Zhuan fish, resembling crucian carp with pig bristles and pig-like cries. Their appearance is said to foretell great drought.','鸡山 丹雘 黑水 鱄鱼'),
('lingqiu','令丘之山','又東四百里曰令丘',3,'令丘山无草木，多火。南面的中谷是条风所出之处；山中鸟像枭，却有人面、四目、有耳，名作𪃍，鸣声自呼其名。它的出现也被记为大旱征兆。','Mount Lingqiu','A valley wind and an owl-like bird follow a description of fire.','Another 400 li east is Lingqiu, without vegetation and with much fire. To its south is Middle Valley, from which the Tiao wind emerges. A bird named 𪃍 resembles an owl with a human face, four eyes and ears; it calls its own name. Its appearance is said to foretell great drought.','令丘之山 中谷 条风 𪃍'),
('lunzhe','仑者之山','又東三百七十里曰侖者',3,'仑者山上多金玉，下多青雘。白䓘像榖木而有赤理，汁液如漆，味如饴。经文说食之不饥、可以释劳，又有“可以血玉”的记述；郭注将末句解释为可用于染玉。','Mount Lunzhe','A tree is described by grain, sap, taste and attributed uses.','Another 370 li east is Lunzhe, with metals and jade above and green mineral below. The tree named here resembles gu with red grain, lacquer-like sap and a sweet taste like malt syrup. Eating it is said to prevent hunger and relieve fatigue. It can be used to “blood jade,” explained by the commentary as dyeing jade.','仑者之山 白䓘 青雘 血玉'),
('yugao','禺槀之山','又東五百八十里曰禺槀',3,'禺槀山在前山以东五百八十里，多怪兽，多大蛇。原文没有为它们分别命名，也没有写出形貌，插画不能代替这份空缺。','Mount Yugao','Unusual beasts and large snakes are recorded without individual names.','Another 580 li east is Mount Yugao, with many unusual beasts and large snakes.','禺槀之山 怪兽 大蛇'),
('nanyu','南禺之山','東五百八十里曰南禺',3,'南禺山上多金玉，下多水。山穴中的水春入、夏出、冬闭；佐水向东南流入海中。经文末尾并记凤皇与鵷鶵，郭注将鵷鶵归入凤属，二者名称仍分别保留。','Mount Nanyu','Seasonal cave water, a river and two named birds close the mountain list.','Five hundred eighty li east is Nanyu, with metal and jade above and water below. Water enters a cave in spring, emerges in summer and is closed in winter. Zuo Water flows southeast into the sea. Fenghuang and Yuanchu are present.','南禺之山 佐水 凤皇 鵷鶵'),
('range3','南次三经总述与祭祀','凡南次三經',3,'从天虞到南禺，底本写十四山、六千五百三十里，山神皆龙身人面。祭祀用一白狗祈祷，以稌米为糈。所写山数与逐项列名有差异，保留底本记数，不自动补造一山。','Third range · totals and rites','Dragon-bodied, human-faced deities receive a distinct offering.','The third Southern range, from Tianyu to Nanyu, is stated to comprise fourteen mountains and 6,530 li. Its deities have dragon bodies and human faces. Each rite uses a white dog for prayer, with rice as the grain offering.','山神 龙身人面 白狗 祈祷 稌米'),
('total','南山经篇末总计','右南經之山志',3,'篇末总计南经大小四十山、万六千三百八十里。前面各列总述的山数相加，与本句并不一致，逐项列名也另有差异。这里将三种计数分别记录，既不删改原文，也不拿它们计算现代旅程。','Nanshan Jing · final total','The closing count is preserved alongside the differing range totals.','The preceding Southern mountain record totals forty mountains, large and small, over 16,380 li.','山数 里数 篇末总计'),
]

SUPPLEMENT = [
('又東四百里曰洵山其陽多金其陰多玉有獸焉其狀如羊而無口不可殺也其名曰䍺','洵作旬。䍺音還或音患。'),
('洵水出焉而南流注于閼之澤其中多芘蠃','洵音詢。閼音遏。芘蠃紫色螺也。'),
('又東四百里曰虖勺之山其上多梓柟其下多荆杞滂水出焉而東流注于海','梓山楸也。柟大木葉似桑。柟今作楠，音南。杞枸杞也子赤。滂音滂沱之滂。'),
('又東五百里曰區吳之山無草木多沙石鹿水出焉而南流注于滂水',''),
]

def build():
    snapshot = read('data/shanhaijing-reference.json')
    chapter = snapshot['chapters'][0]
    lines = []
    for i, line in enumerate(chapter['lines']):
        if i == 89:
            for j, (text, note) in enumerate(SUPPLEMENT):
                lines.append({'id': f'scan-01-26-{j+1:02}', 'text': text, 'annotations': [note] if note else [], 'page': 'Page:Sibu_Congkan0465-郭璞-山海經-2-1.djvu/26', 'review': 'manual_scan_transcription'})
        lines.append({**line, 'id': f'source-01-{i+1:04}'})
    content_lines = lines[2:]
    text = ''.join(line['text'] for line in content_lines)
    offsets, cursor = [], 0
    for line in content_lines:
        offsets.append((cursor, cursor+len(line['text']), line)); cursor += len(line['text'])
    boundaries = [text.index(row[2]) for row in ROWS] + [len(text)]
    assert boundaries == sorted(set(boundaries)), 'Passages must form one contiguous source sequence'
    world, english = read('frontend/public/data/myth-world.json'), read('frontend/src/locale-content-en.json')
    old = {entry['id']: entry for entry in world.get('passages', [])}
    passages, edits = [], []
    mapping = {'zhaoyao':['place-zhaoyao','plant-zhuyu','plant-migu','water-liji','material-yupei','beast-shengsheng'], 'niuyang':['place-niuyang','water-guai','water-xianyi','beast-lushu','beast-xuangui'], 'qingqiu':['place-qingqiu','water-ying-qingqiu','water-jiyi','beast-jiuweihu','beast-guanguan','beast-chiru'], 'jishan':['beast-boyi'], 'luwu':['beast-gudiao'], 'danxue':['beast-phoenix']}
    for number, row in enumerate(ROWS, 1):
        slug, title, anchor, group, desc, en_name, en_desc, en_quote, objects = row
        slug = slug.replace(' ', '')
        start, end = boundaries[number-1:number+1]
        raw = text[start:end]
        quotation = re.sub(r'⟦缺字图:([^⟧]+)⟧', lambda m: m[1] if m[1] in {'能', '狀', '經'} else m[0], raw)
        # Differences from the immutable snapshot are recorded, not silently overwritten there.
        corrections = {'一千九百五十里':'二千九百五十里', '猾裏':'猾褢'}
        for before, after in corrections.items():
            if before in quotation:
                edits.append({'passage': f'passage-nanshan-{slug}', 'captured': before, 'reviewed': after, 'basis': 'facsimile visual inspection'})
                quotation = quotation.replace(before, after)
        refs = [line for a,b,line in offsets if a < end and b > start or a == b and start <= a < end]
        pages = sorted({int(line['page'].split('/')[-1]) for line in refs})
        id = f'passage-nanshan-{slug}'
        notes = '\n'.join(f'〔影印页{line["page"].split("/")[-1]}〕' + '；'.join(line['annotations']) for line in refs if line['annotations'])
        entry = {**old.get(id, {}), 'id': id, 'kind': 'passage', 'name': title, 'range': group, 'order': number,
            'description': desc, 'quote': quotation, 'captured_text': raw, 'commentary_quote': notes,
            'source': '《山海经·南山经》（《四部丛刊》景明成化本，郭璞传）', 'source_chapter': '《南山经》',
            'region': '南山经', 'reveal_chapter': '02', 'source_locator': '卷第一 · 影印页 ' + '、'.join(map(str,pages)),
            'source_pages': ['https://zh.wikisource.org/wiki/'+line for line in dict.fromkeys(r['page'] for r in refs)],
            'url': 'https://zh.wikisource.org/wiki/'+refs[0]['page'], 'source_unit_ids': [line['id'] for line in refs],
            'source_span': [start,end], 'related_entry_ids': mapping.get(slug, []), 'subjects': objects.split(),
            'direction': '依底本篇内次序阅读；里数和方位不转换为现代地图坐标。',
            'editorial_note': '经文据影印页核对录文，未补标点；白话为项目整理。注文按录文行分存，续行可能跨句，须结合影印页阅读。食用、佩用、灾异与祭祀皆为古籍记述。',
            'review_status': 'facsimile_reviewed', 'content_batch': 'nanshan-full-passages'}
        passages.append(entry)
        english[id] = {'name': en_name, 'description': en_desc, 'quote': en_quote, 'source': 'Shanhaijing · Nanshan Jing (Sibu Congkan facsimile; Guo Pu commentary)',
            'source_chapter': 'Nanshan Jing', 'region': 'Nanshan Jing', 'source_locator': 'Volume 1 · scan pages '+', '.join(map(str,pages)),
            'direction': 'Read in the order of this edition. Recorded directions and li are not converted to modern coordinates.',
            'editorial_note': 'The Chinese transcription was compared with the scans and retains unpunctuated text. The explanation and English rendering are editorial. Commentary is retained by transcription line; continuations can cross sentence boundaries. Uses, omens and rituals are ancient textual accounts.'}
        scene = {'zhaoyao':'zhaoyao','niuyang':'niuyang','qingqiu':'qingqiu','tangting':'tangting','xun':'xun','danxue':'danxue'}.get(slug)
        if scene:
            entry['artwork'] = f'nanshan/{scene}-v1.webp'
            entry['artwork_caption'] = '地点场景示意 · 山形、植被、矿物和水流为艺术解释，不复原真实地理。'
            english[id]['artwork_caption'] = 'Place scene · Landforms, vegetation, minerals and water are artistic interpretations, not a reconstruction of real geography.'
    world['passages'] = passages + [p for p in world.get('passages', []) if not p['id'].startswith('passage-nanshan-')]
    world['revision'] = 'myth-world-2026-10-19-nanshan-reader-v3'
    write('frontend/public/data/myth-world.json',world)
    write('frontend/src/locale-content-en.json',english)
    write('data/nanshan-edition-review.json', {'snapshot_sha256': hashlib.sha256((ROOT/'data/shanhaijing-reference.json').read_bytes()).hexdigest(), 'supplement_page':26, 'supplement': SUPPLEMENT, 'corrections':edits,
        'scan_pages':list(range(16,33)), 'confirmed_image_glyphs':['能','狀','經'], 'unresolved_image_glyphs':[{'passage':p['id'],'markers':re.findall(r'⟦缺字图:[^⟧]+⟧',p['quote'])} for p in passages if '⟦缺字图:' in p['quote']], 'limits':'逐山及总述说明齐备；不是所有对象均有独立实体卡，也不是各版本校勘定本。',
        'counts': {'mountain_passages':39, 'range_summaries':3, 'closing_total':1, 'printed_range_counts':[10,17,14], 'printed_closing_count':40},
        'passages':[{'id':p['id'],'source_span':p['source_span'],'source_unit_ids':p['source_unit_ids'],'subjects':p['subjects'],'status':p['review_status']} for p in passages]})
    print('Built',len(passages),'bilingual passages; covered',len(text),'source characters plus separate commentary')

if __name__ == '__main__':
    build()

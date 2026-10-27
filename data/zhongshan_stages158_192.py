"""Eleventh-range stages 158–192: local accounts, variant names and form limits."""
from zhongshan_next30 import R

ROWS = [
R('r11-jigu','即谷之山','Mount Jigu',
  '东南三十五里即谷，多美玉玄豹閭麈麢㚟，阳珉阴青䨼。玄豹黑豹与荆州黑虎为郭注分层记载，不把黑虎改作正文或据颜色补完整肖像。',
  'Thirty-five li southeast is Mount Jigu, with fine jade, black leopards, lüchen, ling and chuo beasts, min on its sunny side and qinghu on its shaded side.',
  'Guo Pu glosses the black leopard and separately mentions black tigers in Jingzhou. Local animal names provide no independent complete anatomy.'),
R('r11-ji','鷄山','Mount Ji',
  '东南四十里鷄山，上美梓桑，草多韭；鷄为山名不额外造鸡鸟条目，与其他列鷄山独立。',
  'Forty li southeast is Mount Ji, with fine zi and mulberry above and jiu herbs.',
  'The chicken mountain name supplies no bird account and is separate from namesakes in other ranges.'),
R('r11-gaoqian','髙前之山','Mount Gaoqian',
  '东南五十里髙前，上水甚寒而清，帝臺之浆、饮不心痛为古述；上金下赭。郭注浆或作潜与檀首盎浆的外地比拟分存，不把帝臺直接作现代帝王或添加形貌。',
  'Fifty li southeast is Mount Gaoqian. Cold clear water above is called Ditai’s drink and is said to avert heart pain; gold lies above and ochre below.',
  'A variant reads qian instead of jiang. Guo Pu compares an external spring at Tanshou near historical Xie county; no modern diagnosis, deity portrait or merged spring is inferred.'),
R('r11-youxi','游戯之山','Mount Youxi',
  '东南三十里游戯，多杻橿榖玉封石。477在54页末，非捕获55页；山名不转作游戏事件。',
  'Thirty li southeast is Mount Youxi, with niu, jiang and gu trees, jade and feng stone.',
  'Unit 477 is on scan 54 rather than captured scan 55. The mountain name adds no separate narrative event.'),
R('r11-cong','從山','Mount Cong',
  '东南三十五里從，上松栢下竹，從水上出下潜；三足鼈枝尾、食无蛊疫为古述，郭注名能引尔雅。图为三足鳖与尾端分叉，肢位、鳖壳纹色及姿态为艺术解释，不借前文三足龟或六目比较图。',
  'Thirty-five li southeast is Mount Cong, with song and bai above and bamboo below. Cong water emerges above and disappears below, with three-footed softshell turtles with branching tails, said to avert harmful afflictions and epidemics when eaten.',
  'The commentary calls the three-footed turtle Neng and cites Erya across units 479–480. Three legs and a split tail follow the text; limb arrangement, shell texture, colors and pose are artistic. No six-eyed comparison is imported.'),
R('r11-yingzhen','嬰䃌之山','Mount Yingzhen',
  '东南三十里嬰䃌，上松栢、下梓櫄。䃌音真属于山名，櫄仅列名，不移用他段香木形貌。',
  'Thirty li southeast is Mount Yingzhen, with song and bai above and zi and chun below.',
  'The zhen pronunciation belongs to the mountain name. The named chun tree receives no anatomy borrowed from another account.'),
R('r11-bi','畢山','Mount Bi',
  '东南三十里畢，帝苑水东北注视，水玉与蛟分别录，山上㻬琈玉。受水视与后文葴山出水视分立账户，不凭同名强定同一现代水系；本段蛟仅名留空。',
  'Thirty li southeast is Mount Bi. Diyuan water flows northeast into the Shi, with water jade and Jiao; tufu jade occurs above on the mountain.',
  'The recipient index remains separate from Zhen mountain’s Shi source account. This Jiao name does not inherit Kuang-water anatomy.'),
R('r11-lema','樂馬之山','Mount Lema',
  '东南二十里樂馬，𤟑状如彚、赤如丹火，疫兆为古述；485在55页末、486续56页。彚比拟未在本段释完整形貌，保留赤色与原词、用占位，不把马名或近字火兽补入画像。',
  'Twenty li southeast is Mount Lema. Li resembles hui and is red like cinnabar fire; its appearance is an ancient epidemic omen.',
  'The passage spans scans 55–56. The local hui comparison lacks an independently explained complete form, so the placeholder adds neither a horse nor an invented fiery creature.'),
R('r11-zhen','葴山','Mount Zhen',
  '东南二十五里葴，视水东南注汝，水中人鱼蛟頡分录；郭注视宜为瀙为异说，不覆盖正文。頡如青狗可据注作犬形青色图，四足毛纹体比姿态为解释；人鱼蛟无本地细部留空。',
  'Twenty-five li southeast is Mount Zhen. Shi water flows southeast into the Ru, with Renyu, Jiao and Jie.',
  'Guo Pu suggests Qin as a variant of Shi, without replacing the main text, and compares Jie with a blue-green dog. Four legs, fur, proportions and pose are artistic. Renyu and Jiao lack independent local detailed forms.'),
R('r11-ying','嬰山','Mount Ying',
  '东四十里嬰山，下青䨼、上金玉；上下位置按原文保存，不与嬰䃌或嬰侯合山。',
  'Forty li east is Mount Ying, with qinghu below and gold and jade above.',
  'The upper and lower positions remain explicit. Yingzhen and Yinghou are separate route mountains.'),
R('r11-hushou','虎首之山','Mount Hushou',
  '东三十里虎首，多苴椆椐；郭注椆未详音雕。虎首仅山名，不生造虎兽或虎头神。',
  'Thirty li east is Mount Hushou, with ju, chou and ju-wood growth.',
  'Guo Pu leaves chou unexplained and supplies pronunciation. The tiger-head mountain name adds no animal or deity.'),
R('r11-yinghou','嬰侯之山','Mount Yinghou',
  '东二十里嬰侯，上封石下赤锡；保留石名与上下位置，不把嬰侯按人名造传记。',
  'Twenty li east is Mount Yinghou, with feng stone above and red tin below.',
  'The product name and positions remain textual; the mountain name adds no biographical figure.'),
R('r11-dashu','大孰之山','Mount Dashu',
  '东五十里大孰，杀水东北注视水，水中白垩独立于山地物产，不以杀字编造战争事件。',
  'Fifty li east is Mount Dashu. Sha water flows northeast into Shi water, with white e in it.',
  'White e belongs to the water account. The water name adds no warfare narrative or modern river identification.'),
R('r11-bei','卑山','Mount Bei',
  '东四十里卑，多桃李苴梓纍；郭注纍为虎豆狸豆之属、一名縢音诔，跨494—495。豆名虎狸不造动物，不强定现代豆科种。',
  'Forty li east is Mount Bei, with tao, li, ju and zi growth and lei.',
  'Across 494–495, Guo Pu compares lei with hu-dou and li-dou, also naming it Teng and supplying pronunciation. These bean names add no tiger or cat account.'),
R('r11-yidi','倚帝之山','Mount Yidi',
  '东三十里倚帝，上玉下金；狙如似鼣鼠、白耳白喙，兵兆为古述。郭注明言所比鼠形未详，保留白耳白喙而留占位，不套犬吠读音补犬身。',
  'Thirty li east is Mount Yidi, with jade above and gold below. Juru resembles fei-shu, with white ears and a white muzzle, and is an ancient warfare omen.',
  'Guo Pu explicitly leaves the compared mouse form unknown. A pronunciation compared with barking does not establish a dog body; the placeholder supplies no invented anatomy.'),
R('r11-ni','鯢山','Mount Ni',
  '东三十里鯢，鯢水上出下潜，水中美垩；山上金下青䨼。鯢为山水名，不另造鯢鱼。',
  'Thirty li east is Mount Ni. Ni water emerges above and disappears below and has fine e; the mountain has gold above and qinghu below.',
  'The mountain and water names do not add a salamander or fish account or an unstated recipient.'),
R('r11-ya','雅山','Mount Ya',
  '东三十里雅，灃水东注视水，水中大鱼；上美桑、下苴赤金。郭注音礼今澧水出南阳保留原字与历史叙述，不静默把正文灃全改澧，也不与章山受水澧直接合并。',
  'Thirty li east is Mount Ya. Feng water flows east into Shi water and has large fish; fine mulberry grows above, with ju and red metal below.',
  'The commentary gives li pronunciation and a historical Li-water account. Main-text Feng and commentary Li spellings remain distinct, without forcing a merger with Zhang’s recipient.'),
R('r11-xuan','宣山','Mount Xuan',
  '东五十里宣，沦水东南注视、水中蛟仅名；帝女桑大五十尺，郭注围五丈，非高五十尺。枝四衢、叶尺余、赤理黄华青柎分存，柎部位不强定；504在57页末、505—506续58页，不造帝女神形。',
  'Fifty li east is Mount Xuan. Lun water flows southeast into Shi water and has Jiao. A mulberry called Dinü has a size of fifty chi, four-way branches, leaves over one chi, red markings, yellow flowers and blue-green fu.',
  'Guo Pu explains the size as five zhang in girth, not height, and four-way intersecting branches; the name is related to women’s sericulture. The fu body-part remains unresolved and supplies no deity portrait. The account spans scans 57–58.'),
R('r11-heng','衡山','Mount Heng (eleventh range)',
  '东四十五里衡，多青䨼桑鸜鹆；郭注衡阳湘南县南岳、俗名岣嵝为历史地理说，不换算现代坐标；鸜鹆仅名，不借又原郭注补本段形。',
  'Forty-five li east is Mount Heng, with qinghu, mulberry and Quyu birds.',
  'Guo Pu gives a historical southern-sacred-mountain association and a Gou-lou name. No modern coordinates or bird anatomy are inferred; the earlier Heng and Quyu accounts remain separate.'),
R('r11-feng-second','豐山','Mount Feng (second eleventh-range account)',
  '东四十里豐，上封石、多桑羊桃；羊桃状如桃方茎，可为皮张与郭注治皮肿为古述，非制皮工艺。与前文雍和耕父豐山独立，不移接其神兽或钟。',
  'Forty li east is a second Mount Feng, with feng stone above, mulberry and Yangtao resembling tao with square stems and an ancient skin-swelling claim.',
  'The skin wording and commentary remain historical claims rather than a leather-making process or modern treatment. This is not merged with the earlier Yonghe, Gengfu and bells account.'),
R('r11-yu-mountain','嫗山','Mount Yu (eleventh range)',
  '东七十里嫗，上美玉下金、草鸡榖。仅本段名目，不借兎牀鸡榖卵形根部补本地详细植物。',
  'Seventy li east is Mount Yu, with fine jade above, gold below and Jigu herbs.',
  'This local Jigu name does not inherit the earlier Tuchuang root-base description.'),
R('r11-xian','鮮山','Mount Xian',
  '东三十里鮮，多楢杻苴𧄸冬，阳金阴铁。𤝻即如膜大、赤喙赤目白尾，火兆为古述；膜比拟字形与分词有疑，不强定貘形，暂留占位。513在58页末、514—515续59页。',
  'Thirty li east is Mount Xian, with you, niu and ju growth and ren-dong, gold on its sunny side and iron on its shaded side. Yiji has a difficult mo-da comparison, a red muzzle, red eyes and a white tail, with an ancient fire omen.',
  'The comparison character and division remain unresolved; no tapir or other modern form is imposed. The account spans scans 58–59. The stated colors remain documented despite the placeholder.'),
R('r11-zhang','章山','Mount Zhang',
  '东三十里章，阳金阴美石，皋水东注澧水，水中脆石郭注未闻音鱼脆反；山名或作童山与石名未闻分开，不因脆字强定易碎矿物。',
  'Thirty li east is Mount Zhang, with gold on its sunny side and fine stone on its shaded side. Gao water flows east into Li water and has cui stone.',
  'Tong is a mountain-name variant. Guo Pu leaves cui stone unknown and supplies pronunciation; its name is not a modern mineral-property determination.'),
R('r11-dazhi','大支之山','Mount Dazhi',
  '东二十五里大支，阳金、木多榖柞，末又记无草木；两句并存说明，不删一句消除矛盾，也不强改成无草而有木。',
  'Twenty-five li east is Mount Dazhi, with gold on its sunny side. It lists abundant gu and zuo trees, then states that there are no grasses or trees.',
  'Both statements are preserved as a textual tension, without silently deleting or rewriting either.'),
R('r11-quwu','區吴之山','Mount Quwu',
  '东五十里區吴，多苴；吴字保留捕获原词，不并他篇句吴、鉤吾。',
  'Fifty li east is Mount Quwu, with abundant ju growth.',
  'The captured name is retained without merging similarly written mountains in other chapters.'),
R('r11-shengxiong','聲匈之山','Mount Shengxiong',
  '东五十里聲匈，多榖玉、上封石；山名不据匈字衍生族群事件。',
  'Fifty li east is Mount Shengxiong, with gu trees and jade and feng stone above.',
  'The mountain name adds no ethnic or historical event account.'),
R('r11-dagui','大騩之山','Mount Dagui',
  '东五十里大騩，阳赤金阴砥石。郭注上已有此山疑同名，作为作者疑问存，不强与前列騩山或帝祀山合并；522在59页末、523续60页。',
  'Fifty li east is Mount Dagui, with red metal on its sunny side and di stone on its shaded side.',
  'Guo Pu notes an earlier mountain and suspects a shared name; uncertainty is retained without a forced merger. The account spans scans 59–60.'),
R('r11-zhongjiu','踵臼之山','Mount Zhongjiu',
  '东十里踵臼，无草木；不由臼字衍生器具或祭礼。',
  'Ten li east is Mount Zhongjiu, with no grasses or trees.',
  'The mountain name adds no mortar object or ritual account.'),
R('r11-lishi','歴石之山','Mount Lishi',
  '东北七十里歴石，多荆芑、阳黄金阴砥石，歴或作磨为山名异说。梁渠如狸、白首虎爪，兵兆为古述；图为狸状白头虎爪，四足毛色尾比与姿态为解释，独立于北山同名条目。',
  'Seventy li northeast is Mount Lishi, with jing and qi growth, gold on its sunny side and di stone on its shaded side. Liangqu resembles a li animal with a white head and tiger claws, with an ancient warfare omen.',
  'Mo is a mountain-name variant. The image uses cat-like form, a white head and tiger claws; four legs, fur, tail proportions and pose are artistic. The Northern Liangqu account remains independently sourced.'),
R('r11-qiu','求山','Mount Qiu',
  '东南一百里求，求水上出下潜、中美赭，木苴䉋、阳金阴铁。䉋篠属为郭注，不借食疗或叶形补竹种。',
  'A hundred li southeast is Mount Qiu. Qiu water emerges above and disappears below, with fine ochre in it; ju and mei growth occur, with gold on the sunny side and iron on the shaded side.',
  'Guo Pu classifies mei with xiao bamboo. No species, leaf form or unstated water recipient is inferred.'),
R('r11-chouyang','丑陽之山','Mount Chouyang',
  '东二百里丑陽，多椆椐；𩢢餘如乌赤足，可御火为古述。图为乌状红足鸟，双足羽色尾姿为艺术解释，不因𩢢的马旁画马；531在60页末。',
  'Two hundred li east is Mount Chouyang, with chou and ju trees. Zhiyu resembles a crow with red feet and is said to avert fire.',
  'The image preserves crow-like form and red feet. Two legs, feather color and tail/pose are artistic; the horse radical adds no horse body. Units 530–531 are both on scan 60.'),
R('r11-ao','奧山','Mount Ao',
  '东三百里奧，多栢杻橿、阳㻬琈玉，奥水东注视水；奧山与奥水原字分别存，不混敖岸。',
  'Three hundred li east is Mount Ao, with bai, niu and jiang trees and tufu jade on its sunny side. Ao water flows east into Shi water.',
  'The captured mountain and water spellings remain distinct from the earlier Aoan name and from modern geographic identifications.'),
R('r11-fu','服山','Mount Fu',
  '东三十五里服，多苴、上封石下赤锡；物产方位保存，不把服当服药行为。',
  'Thirty-five li east is Mount Fu, with ju growth, feng stone above and red tin below.',
  'The mountain name adds no medicine-taking instruction.'),
R('r11-yao','杳山','Mount Yao',
  '东三百里杳，上嘉荣草金玉；仅列名目，不借他山嘉荣注补本地形貌。',
  'Three hundred li east is Mount Yao, with Jiarong herbs, gold and jade above.',
  'The product name provides no independently detailed local plant form.'),
R('r11-ji-mountain','几山','Mount Ji (end of eleventh route)',
  '东三百五十里几，多楢檀杻香草。聞𧲂如彘、黄身白头白尾，风兆为古述；图为猪躯三色，四蹄耳尾比与姿态为艺术解释，不借依軲獜犬形鳞甲。郭注异体捕获缺字明确标未定，不猜补。',
  'Three hundred and fifty li east is Mount Ji, with you, tan and niu trees and fragrant herbs. Wenlin resembles a pig, with a yellow body, white head and white tail; its appearance is an ancient great-wind omen.',
  'The image retains pig form and the three stated color regions; four hooves, ears, tail proportions and pose are artistic. Yiku Lin anatomy is not borrowed. The captured commentary variant has an unresolved character, explicitly marked rather than guessed.')
]
LINKS = []
SHARES = []


def entities(E):
    LINKS.clear(); SHARES.clear(); out=[]
    def add(s,kind,key,n,en,q,eq,cn='',note='',**extra):
        out.append(E(s,kind,key+'-'+s[4:]+'11',n,en,q,cn or '原名、物产位置与经注层次分别保存，不强定现代种属、成分或坐标。',eq,(eq+' '+note).strip(),**extra))
        return out[-1]['id']
    def product(s,k,n,en,q,eq,kind='material',**extra):
        r=next(r for r in ROWS if r['slug']==s)
        return add(s,kind,k,n+'（'+r['name']+'）',en+' ('+r['en_name']+')',q,eq,**extra)
    def products(s,items):
        for k,n,en,q,eq in items:product(s,k,n,en,q,eq)
    def plants(s,items,q):
        for k,n,en in items:product(s,k,n,en,q,en+' are listed here.','plant')
    def unknown(s,k,n,en,q,kind='animal',eq=None,**extra):
        return add(s,kind,k,n,en,q,eq or en+' are recorded here.','本段完整形貌或比拟对象依据不足，保留颜色及原名，暂留占位，不借同名他段或现代物种补形。','Incomplete independent form evidence; the placeholder supplies no invented anatomy.',unknown=True,**extra)
    def water(s,k,n,en,q,eq,**extra):
        return add(s,'water',k,n,en,q,eq,'出水、方向、受水与上下位置按本段保存；不定现代坐标或强合近名河道。',**extra)
    def beast(s,k,n,en,q,eq,cn,note='',**extra):return add(s,'beast',k,n,en,q,eq,cn,note,**extra)
    def shi_share(s,q,eq):SHARES.append((shi,s,q,eq))

    s='r11-jigu'
    products(s,[('fine-jade','羙玉','Fine jade','多羙玉','Fine jade is abundant.'),('min','珉','Min','其陽多珉','Min occurs on the sunny side.'),('qinghu','青䨼','Qinghu','其隂多青䨼','Qinghu occurs on the shaded side.')])
    unknown(s,'black-leopard','玄豹（即谷）','Black leopards (Jigu)','多玄豹',commentary='黒豹也則',en_commentary='Guo Pu glosses a black leopard; the captured final ze remains explicit.')
    for k,n,en in [('lvchen','閭麈','Lüchen'),('ling','麢','Ling beasts'),('chuo','㚟','Chuo beasts')]:unknown(s,k,n+'（即谷）',en+' (Jigu)','多閭麈多麢㚟')
    unknown(s,'black-tiger-comparison','黑虎（荆州郭注比较）','Black tigers (Jingzhou commentary comparison)','今荆州山中出黒虎也',eq='The commentary records black tigers in the Jingzhou mountains.',commentary_only=True,comparison_only=True)
    s='r11-ji';plants(s,[('fine-zi','羙梓','Fine zi trees'),('mulberry','桑','Mulberry trees')],'其上多羙梓多桑');plants(s,[('jiu','韭','Jiu herbs')],'其草多韭')
    s='r11-gaoqian'
    cold=water(s,'ditai-drink','帝臺之漿（髙前寒水）','Ditai drink (Gaoqian cold water)','其上有水焉甚寒而清帝臺之漿也飲之者不心痛','Cold clear water above is called Ditai’s drink and is said to avert heart pain.',commentary='或作潜',en_commentary='A variant reads qian rather than jiang; the ancient health claim is not a modern diagnosis.')
    god=unknown(s,'ditai','帝臺（髙前水名关联）','Ditai (Gaoqian water association)','帝臺之漿也',kind='deity',eq='The water is called Ditai’s drink; no body form is supplied.');LINKS.append((cold,god))
    spring=add(s,'place','tanshou-comparison','盎漿（檀首郭注比较）','Angjiang (Tanshou commentary comparison)','今河東觧縣南檀首山上有水潜出停不流俗名為盎漿即此𩔖也','Guo Pu compares a spring at Tanshou near historical Xie county, emerging and standing without flowing, called Angjiang.',commentary_only=True,comparison_only=True);LINKS.append((cold,spring))
    products(s,[('gold','金','Gold','其上有金','Gold occurs above.'),('ochre','赭','Ochre','其下有赭','Ochre occurs below.')])
    s='r11-youxi';plants(s,[('niu','杻','Niu trees'),('jiang','橿','Jiang trees'),('gu','榖','Gu trees')],'多杻橿榖');products(s,[('jade','玉','Jade','多玉','Jade is abundant.'),('feng-stone','封石','Feng stone','多封石','Feng stone is abundant.')])
    s='r11-cong';plants(s,[('song','松','Song trees'),('bai','栢','Bai trees')],'其上多松栢');plants(s,[('bamboo','竹','Bamboo')],'其下多竹')
    cong=water(s,'cong','從水','Cong water','從水出于其上潜于其下','Cong water emerges above and disappears below.')
    turtle=beast(s,'threeleg','三足鼈（從水）','Three-footed softshell turtle (Cong water)','其中多三足鼈枝尾食之無蠱疫','The water has three-footed softshell turtles with branching tails, said to avert afflictions and epidemics when eaten.','鳖形三足枝尾据正文，图为两前足一后足、尾末分叉；肢位、壳纹颜色与姿态为艺术解释，无六目或第四足。','Two front legs and one rear leg, shell texture, colors and pose are artistic; exactly three feet and one split tail are shown.',water=True,commentary='三足龞名能見；爾雅',en_commentary='The Neng and Erya gloss spans 479–480.');LINKS.append((cong,turtle))
    s='r11-yingzhen';plants(s,[('song','松','Song trees'),('bai','栢','Bai trees')],'其上多松栢');plants(s,[('zi','梓','Zi trees'),('chun','櫄','Chun trees')],'其下多梓櫄')
    s='r11-bi'
    diyuan=water(s,'diyuan','帝苑之水','Diyuan water','帝苑之水出焉東北流注于視','Diyuan water rises here and flows northeast into the Shi.')
    shi=water(s,'shi-recipient','視/視水（次十一受水文本索引）','Shi (eleventh-range recipient index)','東北流注于視','Diyuan water flows northeast into the Shi.');LINKS.append((diyuan,shi))
    jade=product(s,'water-jade','水玉','Water jade','其中多水玉','Water jade is abundant in the water account.');jiao=unknown(s,'jiao','蛟（帝苑水）','Jiao (Diyuan water)','多蛟',water=True);LINKS.extend([(diyuan,jade),(diyuan,jiao)])
    product(s,'tufu','㻬琈之玉','Tufu jade','其上多㻬琈之玉','Tufu jade occurs above.')
    s='r11-lema';unknown(s,'li','𤟑（樂馬）','Li (Lema)','有獸焉其狀如彚赤如丹火其名曰𤟑見則其國大疫',kind='beast',eq='Li resembles hui and is red like cinnabar fire; its appearance is an ancient epidemic omen.',commentary='音戾',en_commentary='Guo Pu gives li pronunciation. The hui comparison and red color are retained without an invented complete body.')
    s='r11-zhen'
    source=water(s,'shi-source','視水（葴山出水）','Shi water rising at Zhen','視水出焉東南流注于汝水','Shi water rises here and flows southeast into Ru water.',commentary='或曰視冝為瀙瀙水今在南陽；也',en_commentary='A suggested Qin spelling and historical Nanyang account span 487–488, without replacing the main text.')
    ru=water(s,'ru-recipient','汝水（葴山受水）','Ru water (Zhen recipient)','東南流注于汝水','Shi water flows southeast into Ru water.');LINKS.append((source,ru))
    for k,n,en,q in [('renyu','人魚','Renyu','其中多人魚'),('jiao','蛟','Jiao','多蛟')]:
        a=unknown(s,k,n+'（葴山视水）',en+' (Zhen Shi water)',q,water=True);LINKS.append((source,a))
    jie=beast(s,'jie','頡（葴山视水）','Jie (Zhen Shi water)','多頡','Jie occur in the water account.','郭注如青狗据以作犬形青色图，四足、犬耳毛纹体比与姿态为艺术解释，不添鳞甲鱼鳍角翼。','Dog form and blue-green color follow commentary; four legs, ear shape, fur and pose are artistic.',water=True,commentary='如青狗',en_commentary='Guo Pu compares Jie with a blue-green dog.');LINKS.append((source,jie))
    s='r11-ying';products(s,[('qinghu','青䨼','Qinghu','其下多青䨼','Qinghu is abundant below.'),('gold','金','Gold','其上多金玉','Gold is abundant above.'),('jade','玉','Jade','其上多金玉','Jade is abundant above.')])
    s='r11-hushou';plants(s,[('ju-growth','苴','Ju growth'),('ju-wood','椐','Ju wood')],'多苴椆椐');product(s,'chou','椆','Chou trees','多苴椆椐','Chou trees are listed.','plant',commentary='椆未詳也音彫',en_commentary='Guo Pu leaves chou unexplained and gives pronunciation.')
    s='r11-yinghou';products(s,[('feng-stone','封石','Feng stone','其上多封石','Feng stone is abundant above.'),('red-tin','赤錫','Red tin','其下多赤錫','Red tin is abundant below.')])
    s='r11-dashu';sha=water(s,'sha','殺水','Sha water','殺水出焉東北流注于視水','Sha water rises here and flows northeast into Shi water.');shi_share(s,'東北流注于視水','Sha water flows northeast into Shi water.');LINKS.append((sha,shi));e=product(s,'white-e','白堊（水中）','White e in water','其中多白堊','White e is abundant in the water.');LINKS.append((sha,e))
    s='r11-bei';plants(s,[('tao','桃','Tao trees'),('li','李','Li trees'),('ju','苴','Ju growth'),('zi','梓','Zi trees')],'其上多桃李苴梓')
    product(s,'lei','纍','Lei growth','多纍','Lei growth is abundant.','plant',commentary='今虎豆狸豆之；属纍一名縢音誄',en_commentary='The bean comparison, Teng alias and pronunciation span 494–495. Tiger and cat characters occur in bean names, not animal accounts.')
    s='r11-yidi';products(s,[('jade','玉','Jade','其上多玉','Jade is abundant above.'),('gold','金','Gold','其下多金','Gold is abundant below.')])
    unknown(s,'juru','狙如（倚帝）','Juru (Yidi)','有獸焉其狀如鼣鼠白耳白喙名曰狙如見則其國有大兵',kind='beast',eq='Juru resembles fei-shu, with white ears and a white muzzle; its appearance is an ancient warfare omen.',commentary='爾雅說鼠有十三種中有此鼠形所未詳也音狗吠之吠；音即蛆',en_commentary='Guo Pu explicitly leaves the compared mouse form unknown and supplies pronunciation glosses. White ears and muzzle remain documented without a modern rodent portrait.')
    s='r11-ni';ni=water(s,'ni','鯢水','Ni water','鯢水出于其上潜于其下','Ni water emerges above and disappears below.');e=product(s,'fine-e','羙堊（水中）','Fine e in water','其中多羙堊','Fine e is abundant in the water.');LINKS.append((ni,e));products(s,[('gold','金','Gold','其上多金','Gold is abundant above.'),('qinghu','青䨼','Qinghu','其下多青䨼','Qinghu is abundant below.')])
    s='r11-ya';feng=water(s,'feng','灃水（雅山）','Feng water (Ya)','灃水出焉東流注于視水','Feng water rises here and flows east into Shi water.',commentary='音禮今澧水出南陽',en_commentary='The captured gloss gives li pronunciation and a historical Li-water account; main-text Feng is not silently replaced.');shi_share(s,'東流注于視水','Ya Feng water flows east into Shi water.');LINKS.append((feng,shi));fish=unknown(s,'large-fish','大魚（雅山灃水）','Large fish (Ya Feng water)','其中多大魚',water=True);LINKS.append((feng,fish));plants(s,[('fine-mulberry','羙桑','Fine mulberry')],'其上多羙桑');plants(s,[('ju','苴','Ju growth')],'其下多苴');product(s,'red-metal','赤金','Red metal','多赤金','Red metal is abundant.')
    s='r11-xuan';lun=water(s,'lun','淪水（宣山）','Lun water (Xuan)','淪水出焉東南流注于視水','Lun water rises here and flows southeast into Shi water.');shi_share(s,'東南流注于視水','Lun water flows southeast into Shi water.');LINKS.append((lun,shi));jiao=unknown(s,'jiao','蛟（淪水）','Jiao (Lun water)','其中多蛟',water=True);LINKS.append((lun,jiao))
    add(s,'plant','dinu-mulberry','帝女之桑（宣山）','Dinü mulberry (Xuan)','其上有桑焉大五十尺其枝四衢其葉大尺餘赤理黃華青柎名曰帝女之桑','A mulberry called Dinü has a size of fifty chi, four-way branches, leaves over one chi, red markings, yellow flowers and blue-green fu.','五十尺据注为围五丈，不作高度；赤理、黄华、青柎原词分存，柎部位未强定，不补完整画像或帝女神。','The size is girth rather than height; the fu body-part remains unresolved, with no invented plant reconstruction or goddess.',commentary='圍五丈也；言枝交互；四出；婦女主蚕；故以名桑',en_commentary='The girth, intersecting four-way branches and women’s sericulture naming gloss spans 504–506.')
    s='r11-heng';product(s,'qinghu','青䨼','Qinghu','多青䨼','Qinghu is abundant.');plants(s,[('mulberry','桑','Mulberry trees')],'多桑');unknown(s,'quyu','鸜鵒（次十一衡山）','Quyu birds (eleventh-range Heng)','其鳥多鸜鵒')
    s='r11-feng-second';product(s,'feng-stone','封石','Feng stone','其上多封石','Feng stone is abundant above.');plants(s,[('mulberry','桑','Mulberry trees')],'其木多桑')
    add(s,'plant','yangtao','羊桃（后豐山）','Yangtao (second Feng)','多羊桃狀如桃而方莖可以為皮張','Yangtao resembles tao with square stems and an ancient skin-swelling claim.','桃状方茎据正文；皮张与郭注皮肿为古述，不解作皮革制造或现代疗法，不补未载花果叶形。',commentary='一名桃；治皮腫起',en_commentary='The captured Tao alias and historical swelling gloss remain separate from modern treatment claims.')
    s='r11-yu-mountain';products(s,[('fine-jade','羙玉','Fine jade','其上多羙玉','Fine jade is abundant above.'),('gold','金','Gold','其下多金','Gold is abundant below.')]);plants(s,[('jigu','鷄榖','Jigu herbs')],'其草多鷄榖')
    s='r11-xian';plants(s,[('you','楢','You trees'),('niu','杻','Niu trees'),('ju','苴','Ju growth')],'其木多楢杻苴');plants(s,[('rendong','𧄸冬','Ren-dong herbs')],'其草多𧄸冬');products(s,[('gold','金','Gold','其陽多金','Gold occurs on the sunny side.'),('iron','鐵','Iron','其隂多鐵','Iron occurs on the shaded side.')])
    unknown(s,'yiji','𤝻即（鮮山）','Yiji (Xian)','有獸焉其狀如膜大赤喙赤目白尾見則其邑有火名曰𤝻即',kind='beast',eq='Yiji has a difficult mo-da comparison, a red muzzle, red eyes and a white tail; its appearance is an ancient fire omen.',commentary='音移',en_commentary='The yi pronunciation, red muzzle and eyes, and white tail are retained. The difficult mo-da comparison is not resolved into a modern tapir or another complete form.')
    s='r11-zhang';products(s,[('gold','金','Gold','其陽多金','Gold occurs on the sunny side.'),('fine-stone','羙石','Fine stone','其隂多羙石','Fine stone occurs on the shaded side.')]);gao=water(s,'gao','臯水（章山）','Gao water (Zhang)','臯水出焉東流注于澧水','Gao water rises here and flows east into Li water.');li=water(s,'li-recipient','澧水（章山受水）','Li water (Zhang recipient)','東流注于澧水','Gao water flows east into Li water.');LINKS.append((gao,li));cui=product(s,'cui-stone','脆石（水中）','Cui stone in water','其中多脆石','Cui stone is abundant in the water.',commentary='未聞魚脆反',en_commentary='Guo Pu leaves the stone unknown and supplies pronunciation.');LINKS.append((gao,cui))
    s='r11-dazhi';product(s,'gold','金','Gold','其陽多金','Gold occurs on the sunny side.');plants(s,[('gu','榖','Gu trees'),('zuo','柞','Zuo trees')],'其木多榖柞')
    s='r11-quwu';plants(s,[('ju','苴','Ju growth')],'其木多苴')
    s='r11-shengxiong';plants(s,[('gu','榖','Gu trees')],'其木多榖');products(s,[('jade','玉','Jade','多玉','Jade is abundant.'),('feng-stone','封石','Feng stone','上多封石','Feng stone occurs above.')])
    s='r11-dagui';products(s,[('red-metal','赤金','Red metal','其陽多赤金','Red metal occurs on the sunny side.'),('di','砥石','Di stone','其隂多砥石','Di stone occurs on the shaded side.')])
    s='r11-lishi';plants(s,[('jing','荆','Jing growth'),('qi','芑','Qi growth')],'其木多荆芑');products(s,[('gold','黄金','Gold','其陽多黄金','Gold occurs on the sunny side.'),('di','砥石','Di stone','其隂多砥石','Di stone occurs on the shaded side.')])
    beast(s,'liangqu','梁渠（歴石）','Liangqu (Lishi)','有獸焉其狀如狸而白首虎爪名曰梁渠見則其國有大兵','Liangqu resembles a li animal with a white head and tiger claws, with an ancient warfare omen.','狸状白首虎爪据正文，四足猫状躯体、身色、尾比与姿态为艺术解释；不并北山同名条目。','Four legs, cat-like trunk, body color, tail proportions and pose are artistic; the Northern account remains independently sourced.')
    s='r11-qiu';qiu=water(s,'qiu','求水','Qiu water','求水出于其上潜于其下','Qiu water emerges above and disappears below.');e=product(s,'fine-ochre','羙赭（水中）','Fine ochre in water','中有羙赭','Fine ochre occurs in the water.');LINKS.append((qiu,e));plants(s,[('ju','苴','Ju growth')],'其木多苴');product(s,'mei','䉋','Mei bamboo','多䉋','Mei growth is abundant.','plant',commentary='篠属',en_commentary='Guo Pu places it with xiao bamboo; no complete species form is supplied.');products(s,[('gold','金','Gold','其陽多金','Gold occurs on the sunny side.'),('iron','鐵','Iron','其隂多鐵','Iron occurs on the shaded side.')])
    s='r11-chouyang';plants(s,[('chou','椆','Chou trees'),('ju','椐','Ju trees')],'其上多椆椐')
    beast(s,'juyu','𩢢餘（丑陽）','Zhiyu (Chouyang)','有鳥焉其狀如烏而赤足名曰𩢢餘可以禦火','Zhiyu resembles a crow with red feet and an ancient fire-averting claim.','乌状赤足据正文，双足、暗色羽纹、尾比与姿态为解释；不据字旁添马身蹄足，不画火灾。','Two legs, dark plumage, tail proportions and pose are artistic; no horse body or fire scene.',commentary='音如枳柑之枳',en_commentary='Guo Pu compares the name pronunciation with zhi in a tree name.')
    s='r11-ao';plants(s,[('bai','栢','Bai trees'),('niu','杻','Niu trees'),('jiang','橿','Jiang trees')],'其上多栢杻橿');product(s,'tufu','㻬琈之玉','Tufu jade','其陽多㻬琈之玉','Tufu jade occurs on the sunny side.');ao=water(s,'ao','奥水','Ao water','奥水出焉東流注于視水','Ao water rises here and flows east into Shi water.');shi_share(s,'東流注于視水','Ao water flows east into Shi water.');LINKS.append((ao,shi))
    s='r11-fu';plants(s,[('ju','苴','Ju growth')],'其木多苴');products(s,[('feng-stone','封石','Feng stone','其上多封石','Feng stone occurs above.'),('red-tin','赤錫','Red tin','其下多赤錫','Red tin occurs below.')])
    s='r11-yao';plants(s,[('jiarong','嘉榮草','Jiarong herbs')],'其上多嘉榮草');products(s,[('gold','金','Gold','多金玉','Gold is abundant.'),('jade','玉','Jade','多金玉','Jade is abundant.')])
    s='r11-ji-mountain';plants(s,[('you','楢','You trees'),('tan','檀','Tan trees'),('niu','杻','Niu trees')],'其木多楢檀杻');plants(s,[('fragrant-herbs','香','Fragrant herbs')],'其草多香')
    beast(s,'wenlin','聞𧲂（几山）','Wenlin (Ji)','有獸焉其狀如彘黃身白頭白尾名曰聞𧲂見則天下大風','Wenlin resembles a pig with a yellow body, white head and white tail, with an ancient great-wind omen.','彘状黄身白头白尾据正文；四蹄、耳尾比例及姿态为艺术解释，无犬躯虎爪角翼鳞甲；郭注异体缺字不猜补。','Four hooves, ear/tail proportions and pose are artistic; no Yiku dog form, tiger paws, horns, wings or scales.',commentary='音隣；𧲂一作〔捕获缺字未定〕音瓶',en_commentary='The name has lin pronunciation; a variant with an unresolved captured character and a ping gloss is retained explicitly.')
    return out

"""Central stages 128–157, retaining local forms and source-layer distinctions."""
from zhongshan_next30 import R

ROWS = [
R('r09-fengyu','風雨之山','Mount Fengyu',
  '东一百五十里風雨，上白金下石𣵀，木棷樿杨；宣余水东注江，水中蛇，兽閭麋麈豹虎，鸟白鷮。棷木未详与樿白理中栉为注，不能据用途补完整树形。',
  'A hundred and fifty li east is Mount Fengyu, with white metal above, stone nie below, and zou, shan and yang trees. Xuanyu water flows east into the Jiang and has snakes. Animals include lümi, zhu, leopards and tigers; birds include white jiao.',
  'The commentary leaves zou wood unknown and describes white-grained shan wood suitable for combs. Named animals have no independent complete anatomy here.'),
R('r09-yu','玉山','Mount Yu (ninth range)',
  '东北二百里玉山，阳铜阴赤金，多豫樟楢杻，兽豕鹿麢㚟、鸟鴆。均按本段名目分录，不借前文綸山㚟或女几鴆形貌；与次八玉山分开。',
  'Two hundred li northeast is Mount Yu, with copper on its sunny side, red metal on its shaded side, yuzhang, you and niu trees, pigs, deer, ling and chuo beasts, and Zhen birds.',
  'This ninth-range mountain is separate from the eighth-range namesake. No form is imported from the earlier Chuo or Zhen commentary.'),
R('r09-xiong','熊山','Mount Xiong',
  '东一百五十里熊山，熊穴恒出神人，夏开冬闭，冬开兵兆为古述；上白玉下白金，多樗柳寇脱。396起45页末，397—399续46页。邺西北鼓山石鼓为郭注外地比较，不把鼓声当熊穴原文，也不凭神人名造神像。',
  'A hundred and fifty li east is Mount Xiong. Its cave is said to produce divine beings, opening in summer and closing in winter; winter opening is an ancient warfare omen. White jade lies above, white metal below, with chu and liu trees and koutuo herbs.',
  'The passage starts on scan 45 and continues on 46. Guo Pu compares an external stone-drum omen; that comparison is not a local cave feature or a detailed divine figure.'),
R('r09-gui','騩山','Mount Gui (ninth range)',
  '东一百四十里騩山，阳美玉赤金、阴铁，多桃枝荆𦬊；保留𦬊原词，不补未载受水、神或现代定位，与其他列騩山分开。',
  'A hundred and forty li east is Mount Gui, with fine jade and red metal on its sunny side, iron on its shaded side, and taozhi, jing and qi growth.',
  'The captured qi spelling is retained. Same-name mountains elsewhere do not supply additional waters, gods or geographic coordinates.'),
R('r09-ge-mountain','葛山','Mount Ge (ninth range)',
  '东二百里葛山，上赤金下瑊石，木柤栗橘櫾楢杻，兽麢㚟，草嘉荣。瑊石劲石似玉、音缄为跨402—403注文，不借别山动物形。',
  'Two hundred li east is Mount Ge, with red metal above, jian stone below, zha, li, ju, you, you-oak and niu trees, ling and chuo beasts, and Jiarong herbs.',
  'The stone gloss continues across units 402–403 and compares a hard stone with jade. Animal names do not establish independent anatomy.'),
R('r09-jiachao','賈超之山','Mount Jiachao',
  '东一百七十里賈超，阳黄垩阴美赭，木柤栗橘櫾，多龙修。405在46页末，406—407在47页。龙须似莞而细、生石穴、茎倒垂可席为郭注，非龙兽；未载完整叶花不补全株。',
  'A hundred and seventy li east is Mount Jiachao, with yellow e on its sunny side, fine ochre on its shaded side, zha, li, ju and you trees, and Longxiu.',
  'The account spans scans 46–47. Longxiu is glossed as Longxu, fine and guan-like, growing in rock holes with hanging stems used for mats; its dragon name adds no animal.'),
R('r09-summary','次9总括与祭礼','Ninth-range summary and rites',
  '岷山首自女几至賈超，报十六山三千五百里，神马身龙首。雄鸡瘗稌的一般礼与文山勾檷风雨醜诸冢、熊山席之酒牢璧舞分录；女几/女凡、文山/岷山、醜山未见独立山段等差异照存，不造新山凑数。',
  'The Min range is reported from Nüji to Jiachao as sixteen mountains and 3,500 li. Its gods have horse bodies and dragon heads. General rites use a rooster, burial and tu grain; Wen, Goumi, Fengyu and Chou have separate rites, and Xiong has wine, livestock, jade and dances.',
  'The summary names Nüji where the route begins with Nüfan, and includes Wen and Chou without forcing new route mountains. General and mountain-specific rites remain distinct; ritual animals are not deity anatomy.'),
R('r10-shouyang','首陽之山','Mount Shouyang',
  '中次十首陽，多金玉、无草木。414在47页末，非捕获48页；仅录原文物产，不以无草木推断现代气候。',
  'The tenth Central range begins at Mount Shouyang, with gold and jade and no grasses or trees.',
  'Unit 414 is on scan 47 rather than captured scan 48. The statement is an ancient account, not a modern climate diagnosis.'),
R('r10-huwei','虎尾之山','Mount Huwei',
  '西五十里虎尾，多椒椐封石，阳赤金阴铁；虎尾为山名，不添加虎兽；封石不强定现代成分。',
  'Fifty li west is Mount Huwei, with jiao and ju trees and feng stone, red metal on its sunny side and iron on its shaded side.',
  'The tiger-tail mountain name supplies no animal. Product names remain textual rather than modern identifications.'),
R('r10-fanhui','繁繢之山','Mount Fanhui',
  '西南五十里繁繢，多楢杻枝勾。繢音溃及今山中有此草分别存注，枝勾作为原词不倒作勾枝。',
  'Fifty li southwest is Mount Fanhui, with you and niu trees and Zhigou herbs.',
  'The mountain pronunciation and the commentary statement that this herb existed in the mountains remain separate from a modern botanical identity.'),
R('r10-yongshi','勇石之山','Mount Yongshi',
  '西南二十里勇石，无草木、多白金多水。水仅泛称，无出水名向或受水体，不编造河道。',
  'Twenty li southwest is Mount Yongshi, with no grasses or trees, abundant white metal and much water.',
  'The unnamed water is not assigned a river name, direction, recipient or coordinate.'),
R('r10-fuzhou','復州之山','Mount Fuzhou',
  '西二十里復州，多檀、阳黄金；跂踵如鸮、一足彘尾，疫兆与铭文为古述。图保留一条可数鸟腿、猪尾，不借铭中似夔改为牛形或添第二足。',
  'Twenty li west is Mount Fuzhou, with tan trees and gold on its sunny side. Qizhong resembles an owl but has one foot and a pig tail; its appearance is an ancient epidemic omen.',
  'The illustration keeps exactly one bird leg and a pig tail. Feather pattern, colors and pose are artistic. The commentary inscription compares its single foot with Kui, without replacing its owl body.'),
R('r10-chu','楮山','Mount Chu',
  '西三十里楮山，多寓木椒椐柘垩；一作渚州之山为异说。423在48页末；不把山名楮当正文额外列出的楮树。',
  'Thirty li west is Mount Chu, with yumu, jiao, ju and zhe trees and e.',
  'The commentary variant is Mount Zhuzhou. Unit 423 is on scan 48; the mountain name itself adds no separate chu-tree product.'),
R('r10-youyuan','又原之山','Mount Youyuan',
  '西二十里又原，阳青䨼阴铁，多鸜鹆。郭注鴝鹆与传曰来巢、音臞分存，不凭现代八哥外形强画；又原名保留。',
  'Twenty li west is Mount Youyuan, with qinghu on its sunny side, iron on its shaded side and Quyu birds.',
  'The commentary supplies a Quyu spelling, a cited nesting account and pronunciation, without independent complete form evidence.'),
R('r10-zhuo','涿山','Mount Zhuo',
  '西五十里涿山，多榖柞杻，阳㻬琈之玉跨426—427连读；不拆出第二种无名玉。',
  'Fifty li west is Mount Zhuo, with gu, zuo and niu trees and tufu jade on its sunny side.',
  'The jade name continues across units 426–427 and remains one product.'),
R('r10-bing','丙山','Mount Bing',
  '西七十里丙山，多梓檀弞杻。郭注弞义未详，只保留原名与未详，不猜植物形貌或把弞杻强合一词。',
  'Seventy li west is Mount Bing, with zi, tan, yin and niu trees.',
  'Guo Pu explicitly leaves yin unexplained. The listed terms are retained without a reconstructed plant form or forced compound.'),
R('r10-summary','次10总括与祭礼','Tenth-range summary and rites',
  '首陽首自首山至丙山报九山二百六十七里，神龙身人面；逐段明列里程合三百一十里与总报不合，分别保留。一般雄鸡瘗五种糈，堵山冢与騩山帝专礼分录；后两山未见本列独立山段，不借外列同名山凑数。432实际49页，433续50页。',
  'The Shouyang range is reported from Shou to Bing as nine mountains and 267 li. Its gods have dragon bodies and human faces. General rites use a rooster, burial and five kinds of grain; Du and Gui have separate livestock, wine, jade and dance rites.',
  'The route distances total 310 li, distinct from the reported 267. Du and Gui lack separate route accounts in this range and are not imported from elsewhere. The final rites span scans 49–50.'),
R('r11-yiwang','翼望之山','Mount Yiwang',
  '次十一荆山首翼望，湍水东注济、贶水东南注汉，各出水分开。贶水中蛟依郭注似蛇四脚小头细颈白瘿；不加角翼。山上松栢下漆梓、阳赤金阴珉。古南阳穰县入清水为湍水注文，与正文济不改合。',
  'The eleventh Central range, Jing, begins at Mount Yiwang. Tuan water flows east into the Ji; Kuang water flows southeast into the Han and has Jiao. Song and bai grow above, lacquer and zi below, with red metal on the sunny side and min on the shaded side.',
  'Commentary describes Jiao as snake-like with four feet, a small head, thin neck and white neck swelling; the image adds no horns or wings. The historical Tuan-to-Qing route remains separate from the main-text Ji recipient.'),
R('r11-chaoge','朝歌之山','Mount Chaoge',
  '东北一百五十里朝歌，潕水东南注荣，多人鱼；梓柟麢麋莽草分录，毒鱼为古述不作使用指引。441实际50页，非51；人鱼仅名不借北山人面四足鱼图。',
  'A hundred and fifty li northeast is Mount Chaoge. Wu water flows southeast into the Rong and has Renyu. Zi and nan trees, ling and mi beasts, and Mangcao occur; the herb is said in the ancient text to poison fish.',
  'Units 439–441 are on scan 50. Renyu has no local independent anatomy; no form is borrowed from the Northern account. The ancient plant claim is not practical advice.'),
R('r11-diqun','帝囷之山','Mount Diqun',
  '东南二百里帝囷，阳㻬琈玉阴铁，帝囷水上出下潜，多鸣蛇；原文未载受水体，也无本地四翼描述，不借鮮水鸣蛇补形。',
  'Two hundred li southeast is Mount Diqun, with tufu jade on its sunny side and iron on its shaded side. Diqun water emerges above and disappears below, with Mingshe.',
  'No recipient is supplied. Mingshe is only named here; the earlier Xian-water four-winged form is not transferred.'),
R('r11-shi','視山','Mount Shi',
  '东南五十里視山，多韭桑美垩金玉；天井夏水冬竭单列，古季节记载不扩为现代水文规律。',
  'Fifty li southeast is Mount Shi, with jiu herbs, mulberry, fine e, gold and jade. A well named Tianjing has water in summer and dries in winter.',
  'The seasonal well account remains textual, without a modern hydrological diagnosis or coordinates.'),
R('r11-qian','前山','Mount Qian',
  '东南二百里前山，多櫧栢、阳金阴赭。櫧似柞、子可食、冬夏生、屋柱难腐及或作储为跨446—447郭注；古用途不补完整树形。',
  'Two hundred li southeast is Mount Qian, with zhu and bai trees, gold on its sunny side and ochre on its shaded side.',
  'The zhu gloss spans 446–447: a zuo comparison, edible seeds, winter-and-summer growth, durable building use and a character variant. These are commentary rather than a modern species determination.'),
R('r11-feng-first','豐山','Mount Feng (first eleventh-range account)',
  '东南三百里豐山，雍和如蝯、赤目赤喙黄身，恐兆为古述；耕父常游清泠渊出入有光，败兆不补神形。九钟霜鸣与山上金、下榖柞杻橿分录；450在51页末、451—452续52页。此豐山与后文同名分开。',
  'Three hundred li southeast is Mount Feng. Yonghe resembles an ape, with red eyes, a red muzzle and a yellow body, and is an ancient fear omen. Gengfu frequents the Qingling pool, entering and leaving with light, with an ancient defeat omen. Nine bells respond to frost; gold lies above and gu, zuo, niu and jiang grow below.',
  'The first Feng account spans scans 51–52 and stays separate from its later namesake. Yonghe limb proportions and pose are artistic; Gengfu has no supplied body form. The bells are objects, not additional creatures.'),
R('r11-tuchuang','兎牀之山','Mount Tuchuang',
  '东北八百里兎牀，阳铁，木多藷藇，草鸡榖，本如鸡卵、味酸甘；利人为古述。阅读层恢复影印兎字，捕获缺字图保留，不从兎名造兔兽，也不把鸡卵比拟当整株形貌。',
  'Eight hundred li northeast is Mount Tuchuang, with iron on its sunny side, shuyu in the wood list, and Jigu herbs with a base resembling a chicken egg and a sour-sweet taste, said to benefit people.',
  'The scan rabbit character is restored only in the reading layer; the captured missing-image marker remains. The egg comparison does not establish the whole plant form or add an animal.'),
R('r11-pi','皮山','Mount Pi',
  '东六十里皮山，多垩赭松栢。物产各存，不借皮字增加兽皮或动物。',
  'Sixty li east is Mount Pi, with e, ochre, song and bai trees.',
  'Products retain the local wording. The mountain name adds no skins or animal account.'),
R('r11-yaobi','瑶碧之山','Mount Yaobi',
  '东六十里瑶碧，多梓柟，阴青䨼阳白金。鴆如雉、恒食蜚，郭注明说此更一种鸟非食蛇之鴆；食物名蜚与捕获郭注蜚盘字样分存，不强释疑字。图为雉状鸟，不画蛇或添加毒性。',
  'Sixty li east is Mount Yaobi, with zi and nan trees, qinghu on its shaded side and white metal on its sunny side. Its Zhen bird resembles a pheasant and habitually eats fei.',
  'Guo Pu explicitly distinguishes this bird from the snake-eating Zhen. The captured prey gloss is retained without resolving the difficult character or turning the prey into the earlier Fei beast. Feather colors, two legs and pose are artistic.'),
R('r11-zhili','支離之山','Mount Zhili',
  '东四十里支離，济水南注汉。嬰勺如鹊、赤目赤喙白身、尾若勺、鸣自呼；图保留白身与勺形单尾，不当金属器具。㸲牛羬羊仅名留空；459在52页末、460—462续53页。',
  'Forty li east is Mount Zhili. Ji water flows south into the Han. Yingshao resembles a magpie, with red eyes and bill, a white body and a ladle-like tail, and calls its own name. Zuo cattle and qian sheep also occur.',
  'The passage spans scans 52–53. The tail comparison is feathered anatomy rather than an attached utensil; exact tail construction, legs and pose are artistic. The named cattle and sheep lack local detailed forms.'),
R('r11-zhidiao','祑𥮐之山','Mount Zhidiao',
  '东北五十里祑𥮐，多松栢机栢；机栢郭注栢叶似柳、皮黄等跨463—464，原捕获不措/棟/间香缨等疑字照存，叶似柳与用途不移给一般栢木。',
  'Fifty li northeast is Mount Zhidiao, with song, bai and ji-bai trees.',
  'The ji-bai gloss spans 463–464 and describes willow-like leaves, yellow bark, seeds and historical uses. Captured difficult words remain explicit; this gloss is not transferred to ordinary bai trees or turned into modern use instructions.'),
R('r11-jinli','堇理之山','Mount Jinli',
  '西北一百里堇理，多松栢美梓，阴丹䨼与金，兽豹虎；青耕如鹊、青身白喙白目白尾、鸣自叫，御疫为古述。图保留四项体色，不加药物器具或以图证明功效。',
  'A hundred li northwest is Mount Jinli, with song, bai and fine zi trees, danhu and gold on its shaded side, leopards and tigers. Qinggeng resembles a magpie, with a blue-green body and white bill, eyes and tail, calling its own name; averting epidemics is an ancient claim.',
  'The image preserves the stated color regions. Feather detail, two legs and pose are artistic, with no medical equipment or efficacy claim.'),
R('r11-yiku','依軲之山','Mount Yiku',
  '东南三十里依軲，多杻橿苴；苴郭注未详。獜如犬、虎爪有甲，郭注体有鳞甲、善跳跃，食者不风为不畏天风古述。468实际53页，469—470在54页；图为犬躯虎爪鳞甲，不改麒麟鹿角蹄。',
  'Thirty li southeast is Mount Yiku, with niu and jiang trees and ju growth. Lin resembles a dog with tiger claws and armor, and is adept at leaping. Eating it is said to avert wind.',
  'The passage spans scans 53–54. Commentary specifies body scales and explains the wind as weather, not a modern disease. Four legs, scale arrangement, colors and pose are artistic; no qilin antlers or hooves are added.')
]
LINKS = []
SHARES = []


def entities(E):
    LINKS.clear(); SHARES.clear(); out=[]
    def add(s,kind,key,name,en,q,eq,cn='',note='',**extra):
        suffix=s[4:]+s[1:3]
        out.append(E(s,kind,key+'-'+suffix,name,en,q,cn or '按本段原文、位置及经注层次分录，不强定现代种属、成分或坐标。',eq,(eq+' '+note).strip(),**extra))
        return out[-1]['id']
    def product(s,key,n,en,q,eq,kind='material',**extra):
        r=next(r for r in ROWS if r['slug']==s)
        return add(s,kind,key,n+'（'+r['name']+'）',en+' ('+r['en_name']+')',q,eq,**extra)
    def products(s,items,kind='material'):
        for key,n,en,q,eq in items: product(s,key,n,en,q,eq,kind)
    def unknown(s,key,n,en,q,**extra):
        return add(s,'animal',key,n,en,q,en+' occur in the account.',
                   '本段独立完整形貌不足；保留原名与经注差异，不借别山描述或现代物种补形。',
                   'Insufficient independent local form evidence; no anatomy is borrowed from a namesake elsewhere.',unknown=True,**extra)
    def trees(s,names,q):
        for key,n,en in names: product(s,key,n,en,q,en+' are listed here.','plant')
    def water(s,key,n,en,q,eq,**extra):
        return add(s,'water',key,n,en,q,eq,'出水、流向与受水据本段分别保存，不定现代河道或坐标。',**extra)
    def creature(s,key,n,en,q,eq,cn,note='',**extra):
        return add(s,'beast',key,n,en,q,eq,cn,note,**extra)

    s='r09-fengyu'
    products(s,[('white-metal','白金','White metal','其上多白金','White metal is abundant above.'),('stone-nie','石𣵀','Stone nie','其下多石𣵀','Stone nie is abundant below.')])
    product(s,'zou','棷','Zou trees','其木多棷樿','Zou trees are listed.','plant',commentary='棷木未詳也',en_commentary='Guo Pu leaves zou wood unknown.')
    product(s,'shan','樿','Shan trees','其木多棷樿','Shan trees are listed.','plant',commentary='樿木白理中擳騶善二音',en_commentary='Guo Pu describes white-grained wood suitable for combs and gives pronunciation glosses; the captured zhi spelling is retained.')
    trees(s,[('yang','楊','Yang trees')],'多楊')
    xu=water(s,'xuanyu','宣余之水','Xuanyu water','宣余之水出焉東流注于江','Xuanyu water rises here and flows east into the Jiang.')
    SHARES.append(('water-zhongshan-jiang-range9-nvfan9',s,'東流注于江','Xuanyu water flows east into the Jiang.')); LINKS.append((xu,'water-zhongshan-jiang-range9-nvfan9'))
    snake=unknown(s,'snake','蛇（宣余水）','Snakes (Xuanyu water)','其中多蛇',water=True);LINKS.append((xu,snake))
    for key,n,en,q in [('lvmi','閭麋','Lümi','其獸多閭麋'),('zhu','麈','Zhu beasts','多麈豹虎'),('leopard','豹','Leopards','多麈豹虎'),('tiger','虎','Tigers','多麈豹虎'),('white-jiao','白鷮','White Jiao birds','其鳥多白鷮')]: unknown(s,key,n+'（風雨）',en+' (Fengyu)',q)
    s='r09-yu'
    products(s,[('copper','銅','Copper','其陽多銅','Copper occurs on the sunny side.'),('red-metal','赤金','Red metal','其隂多赤金','Red metal occurs on the shaded side.')])
    trees(s,[('yuzhang','豫樟','Yuzhang'),('you','楢','You trees'),('niu','杻','Niu trees')],'其木多豫樟楢杻')
    for key,n,en,q in [('pig','豕','Pigs','其獸多豕鹿麢㚟'),('deer','鹿','Deer','其獸多豕鹿麢㚟'),('ling','麢','Ling beasts','其獸多豕鹿麢㚟'),('chuo','㚟','Chuo beasts','其獸多豕鹿麢㚟'),('zhen','鴆','Zhen birds','其鳥多鴆')]:unknown(s,key,n+'（次九玉山）',en+' (ninth-range Yu)',q)
    s='r09-xiong'
    cave=add(s,'place','cave','熊之穴','Xiong cave','有穴焉熊之穴恒出神人夏啓而冬閉是穴也冬啓乃必有兵','Xiong cave is said to produce divine beings, opening in summer and closing in winter; winter opening is an ancient warfare omen.','洞穴季节与兵兆为古述；不并郭注外地鼓山石鼓，也不造现代坐标。')
    god=add(s,'deity','divine-beings','神人（熊穴）','Divine beings (Xiong cave)','熊之穴恒出神人','Divine beings are said to emerge from Xiong cave.','仅神人名目，无独立形貌，不作肖像。',unknown=True);LINKS.append((cave,god))
    add(s,'place','drum-comparison','皷山石皷（郭注比较）','Gu mountain stone drum (commentary comparison)','今鄴西北有皷山下有石皷象懸著山旁鳴則有軍事與此穴殊象而同應','The commentary compares an external stone drum near Ye, with a similar warfare omen.','郭注外地比较，非熊山当地石鼓；跨397—398连读。',commentary_only=True,comparison_only=True)
    products(s,[('white-jade','白玉','White jade','其上多白玉','White jade is abundant above.'),('white-metal','白金','White metal','其下多白金','White metal is abundant below.')])
    trees(s,[('chu','樗','Chu trees'),('liu','柳','Liu trees')],'其木多樗柳');trees(s,[('koutuo','寇脱','Koutuo herbs')],'其草多寇脱')
    s='r09-gui'
    products(s,[('fine-jade','羙玉','Fine jade','其陽多羙玉赤金','Fine jade occurs on the sunny side.'),('red-metal','赤金','Red metal','其陽多羙玉赤金','Red metal occurs on the sunny side.'),('iron','鐵','Iron','其隂多鐵','Iron occurs on the shaded side.')])
    trees(s,[('taozhi','桃枝','Taozhi'),('jing','荆','Jing growth'),('qi','𦬊','Qi growth')],'其木多桃枝荆𦬊')
    s='r09-ge-mountain'
    product(s,'red-metal','赤金','Red metal','其上多赤金','Red metal is abundant above.')
    product(s,'jian-stone','瑊石','Jian stone','其下多瑊石','Jian stone is abundant below.',commentary='瑊石勁石；似玉也音緘',en_commentary='The gloss spans 402–403: hard stone resembling jade, with jian pronunciation.')
    trees(s,[('zha','柤','Zha trees'),('li','栗','Li trees'),('ju','橘','Ju trees'),('you-citrus','櫾','You citrus trees'),('you','楢','You trees'),('niu','杻','Niu trees')],'其木多柤栗橘櫾楢杻')
    for k,n,en in [('ling','麢','Ling beasts'),('chuo','㚟','Chuo beasts')]:unknown(s,k,n+'（葛山）',en+' (Ge)','其獸多麢㚟')
    trees(s,[('jiarong','嘉榮','Jiarong herbs')],'其草多嘉榮')
    s='r09-jiachao'
    products(s,[('yellow-e','黄堊','Yellow e','其陽多黄堊','Yellow e occurs on the sunny side.'),('fine-ochre','羙赭','Fine ochre','其隂多羙赭','Fine ochre occurs on the shaded side.')])
    trees(s,[('zha','柤','Zha trees'),('li','栗','Li trees'),('ju','橘','Ju trees'),('you','櫾','You trees')],'其木多柤栗橘櫾')
    product(s,'longxiu','龍脩','Longxiu','其中多龍脩','Longxiu is abundant here.','plant',commentary='龍須也似莞而細生山石穴中；莖倒垂可以為席',en_commentary='Across 406–407: Longxu, fine and guan-like, growing in rock holes, with hanging stems used for mats.')
    s='r09-summary'
    add(s,'deity','horsedragon','次九山神（马身龙首）','Ninth-range gods (horse body, dragon head)','其神狀皆馬身而龍首','The gods have horse bodies and dragon heads.','完整马躯龙首据正文，四蹄、龙角须、体色与姿态为艺术解释，不作人身或添翼。','Horse anatomy, horns, whiskers, colors and pose are artistic; no human torso or wings.')
    for k,n,en,q,eq in [('rooster','雄雞','Rooster offering','其祠毛用一雄雞瘞','The general rite uses one rooster and burial.'),('tu','稌','Tu grain','糈用稌','The offering grain is tu.'),('special','诸冢专祀','Special principal-mountain rites','文山勾檷風雨醜之山是皆冢也其祠之羞酒少牢具嬰毛一吉玉','Wen, Goumi, Fengyu and Chou have wine, lesser livestock and jade rites.'),('xiong','熊山席与舞礼','Xiong seat and dance rites','熊山席也其祠羞酒大牢具嬰毛一璧干儛用兵以禳祈璆冕舞','Xiong has wine, greater livestock, jade and dances with shields and weapons.')]:add(s,'rite',k,n,en,q,eq,'一般与专祀、地位与舞礼分录，原名差异保留，不把祭牲作神形。')
    s='r10-shouyang';products(s,[('gold','金','Gold','其上多金玉','Gold is abundant above.'),('jade','玉','Jade','其上多金玉','Jade is abundant above.')])
    s='r10-huwei';trees(s,[('jiao','椒','Jiao trees'),('ju','椐','Ju trees')],'其木多椒椐')
    products(s,[('feng-stone','封石','Feng stone','多封石','Feng stone is abundant.'),('red-metal','赤金','Red metal','其陽多赤金','Red metal occurs on the sunny side.'),('iron','鐵','Iron','其隂多鐵','Iron occurs on the shaded side.')])
    s='r10-fanhui';trees(s,[('you','楢','You trees'),('niu','杻','Niu trees')],'其木多楢杻')
    product(s,'zhigou','枝勾','Zhigou herbs','其草多枝勾','Zhigou herbs are abundant.','plant',commentary='今山中有此草',en_commentary='Guo Pu says this herb exists in the mountains, without a complete form description.')
    s='r10-yongshi';product(s,'white-metal','白金','White metal','多白金','White metal is abundant.');water(s,'unnamed-water','水（勇石泛称）','Unnamed water (Yongshi)','多水','There is much water here.')
    s='r10-fuzhou';trees(s,[('tan','檀','Tan trees')],'其木多檀');product(s,'gold','黄金','Gold','其陽多黄金','Gold occurs on the sunny side.')
    creature(s,'qizhong','跂踵（復州）','Qizhong (Fuzhou)','有鳥焉其狀如鴞而一足彘尾其名曰跂踵見則其國大疫','Qizhong resembles an owl, with one foot and a pig tail, and an ancient epidemic omen.','鴞状一足彘尾据正文，一条鸟腿须可数；色羽与姿态为艺术解释，不借铭中似夔改牛形。','One visible bird leg and pig tail; feather detail, colors and pose are artistic.',commentary='音企；銘曰跂踵為鳥一足似䕫不為樂興反以來悲',en_commentary='Pronunciation and an inscription compare the single foot with Kui; no replacement of the owl form is intended.')
    s='r10-chu';trees(s,[('yumu','寓木','Yumu'),('jiao','椒','Jiao trees'),('ju','椐','Ju trees'),('zhe','柘','Zhe trees')],'多寓木多椒椐多柘');product(s,'e','堊','E','多堊','E is abundant.')
    s='r10-youyuan';products(s,[('qinghu','青䨼','Qinghu','其陽多青䨼','Qinghu occurs on the sunny side.'),('iron','鐵','Iron','其隂多鐵','Iron occurs on the shaded side.')])
    unknown(s,'quyu','鸜鵒（又原）','Quyu birds (Youyuan)','其鳥多鸜鵒',commentary='鴝鵒也傳曰鴝鵒來巢音臞',en_commentary='A character gloss, cited nesting account and pronunciation; no complete anatomy.')
    s='r10-zhuo';trees(s,[('gu','榖','Gu trees'),('zuo','柞','Zuo trees'),('niu','杻','Niu trees')],'其木多榖柞杻');product(s,'tufu','㻬琈之玉','Tufu jade','其陽多㻬琈之玉','Tufu jade occurs on the sunny side.')
    s='r10-bing';trees(s,[('zi','梓','Zi trees'),('tan','檀','Tan trees')],'其木多梓檀');trees(s,[('niu','杻','Niu trees')],'多弞杻');product(s,'yin','弞','Yin trees','多弞杻','Yin trees are listed.','plant',commentary='弞義所未詳',en_commentary='Guo Pu explicitly leaves the meaning of yin unknown.')
    s='r10-summary';add(s,'deity','human-dragon','次十山神（龙身人面）','Tenth-range gods (dragon body, human face)','其神狀皆龍身而人面','The gods have dragon bodies and human faces.','龙躯人面据正文，曲躯、鳞纹、四足、角须与配色为艺术解释，不画人身披龙袍。','Coiled body, scales, feet, horns, whiskers, colors and pose are artistic; no human torso.')
    for k,n,en,q,eq in [('rooster','雄雞','Rooster offering','其祠之毛用一雄雞瘞','The general rite uses one rooster and burial.'),('grain','五種糈','Five grains','糈用五種之糈','Five kinds of grain are used.'),('du','堵山专祀','Du-specific rite','堵山冢也其祠之少牢具羞酒祠嬰毛一璧瘞','Du has lesser-livestock, wine, jade and burial rites.'),('gui','騩山帝专祀','Gui imperial rite','騩山帝也其祠羞酒太牢其合巫祝二人儛嬰一璧','Gui has wine, greater livestock, two ritual specialists dancing and a bi jade.')]:add(s,'rite',k,n,en,q,eq,'按总括礼制分录；堵与騩不造本列未载山段，祭牲不作神形。')
    s='r11-yiwang'
    tuan=water(s,'tuan','湍水（翼望）','Tuan water (Yiwang)','湍水出焉東流注于濟','Tuan water rises here and flows east into the Ji.',commentary='鹿摶反；今湍水逕南陽穰縣而入清水',en_commentary='Pronunciation and a historical Tuan-to-Qing route, kept distinct from the main-text Ji recipient.')
    ji=water(s,'ji-recipient','濟（翼望受水体）','Ji (Yiwang recipient)','東流注于濟','Tuan water flows east into the Ji.');LINKS.append((tuan,ji))
    kuang=water(s,'kuang','貺水（翼望）','Kuang water (Yiwang)','貺水出焉東南流注于漢','Kuang water rises here and flows southeast into the Han.',commentary='音况',en_commentary='Guo Pu supplies kuang pronunciation.')
    han=water(s,'han-recipient','漢（次十一受水索引）','Han (eleventh-range recipient)','東南流注于漢','Kuang water flows southeast into the Han.');LINKS.append((kuang,han))
    jiao=creature(s,'jiao','蛟（貺水）','Jiao (Kuang water)','其中多蛟','Jiao are abundant in the water.','郭注似蛇四脚小头细颈白瘿为据；卵量与吞人古述存注，图不加角翼，鳞色姿态为解释。','Snake form, four feet, small head, thin neck and white neck swelling follow commentary; scale colors and pose are artistic.',water=True,commentary='似蛇而四脚小頭細頸頸有白癭大者十數圍卵如一二石甕；吞人',en_commentary='The gloss spans 436–437: snake-like with four feet, small head, thin neck, white neck swelling, large size and eggs, with an ancient feeding claim.');LINKS.append((kuang,jiao))
    trees(s,[('song','松','Song trees'),('bai','栢','Bai trees')],'其上多松栢');trees(s,[('lacquer','漆','Lacquer trees'),('zi','梓','Zi trees')],'其下多漆梓')
    products(s,[('red-metal','赤金','Red metal','其陽多赤金','Red metal occurs on the sunny side.'),('min','珉','Min','其隂多珉','Min occurs on the shaded side.')])
    s='r11-chaoge';wu=water(s,'wu','潕水（朝歌）','Wu water (Chaoge)','潕水出焉東南流注于榮','Wu water rises here and flows southeast into the Rong.',commentary='潕水今在南陽；舞陽縣音武',en_commentary='The historical Wuyang gloss spans 439–440 and gives wu pronunciation.')
    rong=water(s,'rong','榮（潕水受水体）','Rong (Wu recipient)','東南流注于榮','Wu water flows southeast into the Rong.');LINKS.append((wu,rong))
    fish=unknown(s,'renyu','人魚（潕水）','Renyu (Wu water)','其中多人魚',water=True);LINKS.append((wu,fish))
    trees(s,[('zi','梓','Zi trees'),('nan','柟','Nan trees')],'其上多梓柟')
    for k,n,en in [('ling','麢','Ling beasts'),('mi','麋','Mi beasts')]:unknown(s,k,n+'（朝歌）',en+' (Chaoge)','其獸多麢麋')
    add(s,'plant','mangcao','莽草（朝歌）','Mangcao (Chaoge)','有草焉名曰莽草可以毒魚','Mangcao is an herb said in the ancient text to poison fish.','古毒鱼说存录，不作现代种属、剂量或使用建议。',commentary='今用之殺魚',en_commentary='Guo Pu records a historical fish-killing use, not practical guidance.')
    s='r11-diqun';products(s,[('tufu','㻬琈之玉','Tufu jade','其陽多㻬琈之玉','Tufu jade occurs on the sunny side.'),('iron','鐵','Iron','其隂多鐵','Iron occurs on the shaded side.')])
    di=water(s,'diqun','帝囷之水','Diqun water','帝囷之水出于其上潜于其下','Diqun water emerges above and disappears below.')
    ming=unknown(s,'mingshe','鳴蛇（帝囷）','Mingshe (Diqun)','多鳴蛇',water=True);LINKS.append((di,ming))
    s='r11-shi';trees(s,[('jiu','韭','Jiu herbs')],'其上多韭');trees(s,[('mulberry','桑','Mulberry trees')],'其上多桑')
    water(s,'tianjing','天井（視山）','Tianjing (Shi)','有井焉名曰天井夏有水冬竭','A well called Tianjing has water in summer and dries in winter.')
    products(s,[('fine-e','羙堊','Fine e','多羙堊金玉','Fine e is abundant.'),('gold','金','Gold','多羙堊金玉','Gold is abundant.'),('jade','玉','Jade','多羙堊金玉','Jade is abundant.')])
    s='r11-qian';product(s,'zhu','櫧','Zhu trees','其木多櫧','Zhu trees are abundant.','plant',commentary='音諸似柞子可食冬夏生作屋柱難；腐或作儲',en_commentary='Across 446–447: pronunciation, zuo-like form, edible seed, perennial growth, building use and a spelling variant.')
    trees(s,[('bai','栢','Bai trees')],'多栢');products(s,[('gold','金','Gold','其陽多金','Gold occurs on the sunny side.'),('ochre','赭','Ochre','其隂多赭','Ochre occurs on the shaded side.')])
    s='r11-feng-first';creature(s,'yonghe','雍和（豐山）','Yonghe (Feng)','有獸焉其狀如蝯赤目赤喙黄身名曰雍和見則國有大恐','Yonghe resembles an ape with red eyes, red muzzle and yellow body, and is an ancient fear omen.','蝯状赤目赤喙黄身据正文；喙按猿口鼻解释，不添鸟嘴。四肢比例、毛纹姿态为艺术解释。','The ape muzzle interpretation, limb proportions, fur pattern and pose are artistic; no bird beak or omen scene.')
    geng=add(s,'deity','gengfu','耕父（豐山）','Gengfu (Feng)','神耕父處之常逰清泠之淵出入有光見則其國為敗','Gengfu dwells here and frequents the Qingling pool, entering and leaving with light; its appearance is an ancient defeat omen.','只载活动与光，不载躯体形貌，留占位不造神像。',unknown=True)
    pool=water(s,'qingling','清泠之淵（豐山）','Qingling pool (Feng)','常逰清泠之淵','Gengfu frequents the Qingling pool.',commentary='清冷水在西號郊縣山上神來時水赤有光耀今有屋祠之',en_commentary='The captured historical place spelling and red-water/light/shrine account remain commentary.');LINKS.append((geng,pool))
    add(s,'rite','nine-bells','九鐘（豐山）','Nine bells (Feng)','有九鐘焉是知霜鳴','Nine bells are said to sound in response to frost.','钟与霜应为古述，不归作生物；跨451—452感应注文分存。',commentary='霜降則鍾鳴故言知也物有自然感；應而不可為也',en_commentary='Guo Pu explains the sounding at frost as a natural response; the gloss continues across units 451–452.')
    product(s,'gold','金','Gold','其上多金','Gold is abundant above.');trees(s,[('gu','榖','Gu trees'),('zuo','柞','Zuo trees'),('niu','杻','Niu trees'),('jiang','橿','Jiang trees')],'其下多榖柞杻橿')
    s='r11-tuchuang';product(s,'iron','鐵','Iron','其陽多鐵','Iron occurs on the sunny side.');trees(s,[('shuyu','藷藇','Shuyu')],'其木多藷藇')
    add(s,'plant','jigu','雞榖（兎牀）','Jigu (Tuchuang)','其草多雞榖其本如雞卵其味酸甘食者利於人','Jigu has an egg-like base and sour-sweet taste and is said to benefit people when eaten.','鸡卵只比拟本部，不补叶花与完整株形；利人为古述。')
    s='r11-pi';products(s,[('e','堊','E','多堊','E is abundant.'),('ochre','赭','Ochre','多赭','Ochre is abundant.')]);trees(s,[('song','松','Song trees'),('bai','栢','Bai trees')],'其木多松栢')
    s='r11-yaobi';trees(s,[('zi','梓','Zi trees'),('nan','柟','Nan trees')],'其木多梓柟');products(s,[('qinghu','青䨼','Qinghu','其隂多青䨼','Qinghu occurs on the shaded side.'),('white-metal','白金','White metal','其陽多白金','White metal occurs on the sunny side.')])
    zhen=creature(s,'zhen','鴆（瑶碧雉状鸟）','Zhen (Yaobi pheasant-like bird)','有鳥焉其狀如雉𢘆食蜚名曰鴆','This Zhen resembles a pheasant and habitually eats fei.','雉状据正文，郭注另种非食蛇鴆；羽色双足姿态为艺术解释，不添毒蛇或毒性。','Feather colors, two legs and pose are artistic; this is explicitly distinct from the snake-eating Zhen.',commentary='蜚盤也；音翡此更一種鳥非食蛇之鴆也',en_commentary='The captured prey gloss reads fei-pan and is retained without resolving the difficult character. Guo Pu explicitly calls this another bird, not the snake-eating Zhen.')
    prey=unknown(s,'fei-prey','蜚（瑶碧鴆食物）','Fei (Yaobi Zhen prey)','𢘆食蜚',commentary='蜚盤也',en_commentary='The captured gloss is retained; no form is borrowed from the earlier Fei beast.');LINKS.append((zhen,prey))
    s='r11-zhili';ji=water(s,'ji-source','濟水（支離出水）','Ji water rising at Zhili','濟水出焉南流注于漢','Ji water rises here and flows south into the Han.',commentary='今濟；水出酈縣西北山中南入漢酈離音字亦同',en_commentary='The historical Li-county source and southward Han route span 459–460; no modern coordinates are supplied.')
    SHARES.append((han,s,'南流注于漢','Zhili Ji water flows south into the Han.'));LINKS.append((ji,han))
    creature(s,'yingshao','嬰勺（支離）','Yingshao (Zhili)','有鳥焉其名曰嬰勺其狀如鵲赤目赤喙白身其尾若勺其鳴自呼','Yingshao resembles a magpie, with red eyes and bill, white body and a ladle-like tail, calling its own name.','鹊状赤目赤喙白身、尾如酒勺据经注；尾羽勺形布局、双足与姿态为解释，不附金属勺。','The feathered ladle-tail construction, two feet and pose are artistic; no metal utensil is attached.',commentary='似酒勺形',en_commentary='Guo Pu compares the tail shape with a wine ladle.')
    for k,n,en,q in [('zuo-cattle','㸲牛','Zuo cattle','多㸲牛'),('qian-sheep','羬羊','Qian sheep','多羬羊')]:unknown(s,k,n+'（支離）',en+' (Zhili)',q)
    s='r11-zhidiao';trees(s,[('song','松','Song trees'),('bai','栢','Bai trees')],'其上多松栢机栢')
    product(s,'jibai','机栢','Ji-bai trees','其上多松栢机栢','Ji-bai trees are listed.','plant',commentary='栢葉；似栁皮黄不措子似棟着酒中飲之辟惡氣浣衣去垢核堅正黒可以間香纓一名括樓也',en_commentary='The gloss spans 463–464. Willow-like leaves, yellow bark, seeds and historical uses are retained with captured difficult words, without a modern species or practical-use determination.')
    s='r11-jinli';trees(s,[('song','松','Song trees'),('bai','栢','Bai trees')],'其上多松栢');trees(s,[('fine-zi','羙梓','Fine zi trees')],'多羙梓')
    products(s,[('danhu','丹䨼','Danhu','其隂多丹䨼多金','Danhu occurs on the shaded side.'),('gold','金','Gold','其隂多丹䨼多金','Gold occurs on the shaded side.')])
    for k,n,en in [('leopard','豹','Leopards'),('tiger','虎','Tigers')]:unknown(s,k,n+'（堇理）',en+' (Jinli)','其獸多豹虎')
    creature(s,'qinggeng','青耕（堇理）','Qinggeng (Jinli)','有鳥焉其狀如鵲青身白喙白目白尾名曰青耕可以禦疫其鳴自呌','Qinggeng resembles a magpie with a blue-green body and white bill, eyes and tail, calling its own name; warding off epidemics is an ancient claim.','鹊状青身白喙白目白尾据正文；羽纹双足姿态为艺术解释，不画医药符号或声称功效。','Feather pattern, two feet and pose are artistic, without medical symbolism or an efficacy claim.')
    s='r11-yiku';trees(s,[('niu','杻','Niu trees'),('jiang','橿','Jiang trees')],'其上多杻橿')
    product(s,'ju','苴','Ju growth','多苴','Ju growth is listed.','plant',commentary='未詳',en_commentary='Guo Pu leaves this term unexplained.')
    creature(s,'lin','獜（依軲）','Lin (Yiku)','有獸焉其狀如犬虎爪有甲其名曰獜善駚𤘝食者不風','Lin resembles a dog with tiger claws and armor, is adept at leaping and is said to avert wind when eaten.','犬形虎爪鳞甲据经注；四足鳞片布局色姿为艺术解释，不加麒麟角蹄。风为不畏天风古述，不改现代病名。','Four legs, scale layout, colors and pose are artistic; no qilin horns or hooves. The wind claim concerns weather in the commentary.',commentary='言體有鱗甲音吝；跳躍自撲也鞅奮兩音；不畏天風',en_commentary='Body scales and pronunciation, leaping behavior and fearlessness of weather wind are separate commentary glosses.')
    return out

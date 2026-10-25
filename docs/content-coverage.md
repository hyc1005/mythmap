# 《山海经》内容覆盖盘点

盘点基准：《四部丛刊》景江安傅氏双鉴楼藏明成化庚寅刊本，晋郭璞传。电子录文取自[维基文库](https://zh.wikisource.org/wiki/%E5%B1%B1%E6%B5%B7%E7%B6%93_(%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC))，快照日期 2026-10-19。

## 统计口径

- 十八篇录文块清单见 `data/shanhaijing-inventory.json`，每项保存页码、原文、注文与待核状态。《南山经》43段、《西山经》82段、《北山经》92段与《东山经》51段已接入说明；其余结构候选的段界、实体、关系和影印仍待人工核定。不是全书穷尽实体索引，也不是各版本校勘定本。
- 已保存十八篇逐行正文、注文、影印页锚点、校对状态和固定修订链接，见 `data/shanhaijing-reference.json`。录文中缺字图保留显式标记，不猜字补齐。
- 下表按当前条目声明的出处计数；同一条目可引用多篇，同名异篇保持分开。地点锚点、神域、异兽、故事不是同一统计单位，不能相加后声称全书覆盖率。
- 14条地点记录含4条山列集合锚点；3条神域与相关地点分别建档。259条异兽记录，同名异篇分开；746条自然条目含草木、水域、物产。43条事件记录含拆分子事件、归档、组和未开放资料，不等于43个独立故事。
- “常规入口”是地图、图鉴、章节目录中的独立条目；“非默认条目”是归档/组，仍可从搜索或直链打开；“未开放”指数据已有记录，但没有可用章节入口。引用某篇不等于完整收录该篇。
- 项目共 1718 条上述记录（含271条经文阅读段，与独立实体不是同一统计单位）：常规入口 1708，非默认条目 3，未开放 7。另有39条书目记录、32条现代地点关联，不混入该统计。

## 十八篇对应清单

| 篇目 | 常规入口记录 | 非默认条目 | 未开放记录 | 当前状态 |
| --- | ---: | ---: | ---: | --- |
| [南山经](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E4%B8%80&oldid=2652851) | 161 | 0 | 0 | 全篇43段说明可读；独立实体仍选编 |
| [西山经](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E4%BA%8C&oldid=2652852) | 596 | 0 | 2 | 82段、508张新卡已接入；其余仍待核 |
| [北山经](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E4%B8%89&oldid=2652853) | 601 | 0 | 0 | 全篇92阅读段、507张独立卡已核；形貌不足者留占位 |
| [东山经](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E5%9B%9B&oldid=2652854) | 289 | 0 | 0 | 全篇51阅读段接入；疑难字与数字差异明确保留 |
| [中山经](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E4%BA%94&oldid=2652856) | 17 | 0 | 0 | 准备阶段完成；212阶段已规划、3阶段接入；逐阶段影印与实体仍待复核 |
| [海外南经](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E5%85%AD&oldid=2652857) | 0 | 0 | 1 | 仅数据存留，未形成网页收录 |
| [海外西经](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E4%B8%83&oldid=2652858) | 1 | 0 | 1 | 选编，篇内仍有遗漏 |
| [海外北经](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E5%85%AB&oldid=2652859) | 2 | 0 | 2 | 选编，篇内仍有遗漏 |
| [海外东经](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E4%B9%9D&oldid=2652860) | 2 | 0 | 2 | 选编，篇内仍有遗漏 |
| [海内南经](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E5%8D%81&oldid=2652861) | 0 | 0 | 0 | 尚无明确篇目对应 |
| [海内西经](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E5%8D%81%E4%B8%80&oldid=2652862) | 3 | 0 | 0 | 选编，篇内仍有遗漏 |
| [海内北经](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E5%8D%81%E4%BA%8C&oldid=2652863) | 1 | 0 | 0 | 选编，篇内仍有遗漏 |
| [海内东经](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E5%8D%81%E4%B8%89&oldid=2652864) | 0 | 0 | 0 | 尚无明确篇目对应 |
| [大荒东经](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E5%8D%81%E5%9B%9B&oldid=2652865) | 0 | 0 | 1 | 仅数据存留，未形成网页收录 |
| [大荒南经](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E5%8D%81%E4%BA%94&oldid=2652866) | 0 | 0 | 1 | 仅数据存留，未形成网页收录 |
| [大荒西经](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E5%8D%81%E5%85%AD&oldid=2652867) | 0 | 0 | 1 | 仅数据存留，未形成网页收录 |
| [大荒北经](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E5%8D%81%E4%B8%83&oldid=2652868) | 8 | 0 | 2 | 选编，篇内仍有遗漏 |
| [海内经](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E5%8D%81%E5%85%AB&oldid=2652869) | 1 | 0 | 0 | 选编，篇内仍有遗漏 |

## 逐篇已收录与待补方向

### 01 南山经

- 常规入口：狌狌（`beast-shengsheng`）；鹿蜀（`beast-lushu`）；九尾狐（`beast-jiuweihu`）；赤鱬（`beast-chiru`）；猼訑（`beast-boyi`）；旋龟（`beast-xuangui`）；蛊雕（`beast-gudiao`）；凤皇（`beast-phoenix`）；灌灌（`beast-guanguan`）；鯥（`beast-nanshan-lu`）；𩔗（`beast-nanshan-lei`）；𪁺𩿧（`beast-nanshan-changfu`）；狸力（`beast-nanshan-lili`）；鴸（`beast-nanshan-zhu`）；长右（`beast-nanshan-changyou`）；猾褢（`beast-nanshan-huahuai`）；彘（`beast-nanshan-zhi`）；䍺（`beast-nanshan-huan-xun`）；瞿如（`beast-nanshan-quru`）；虎蛟（`beast-nanshan-hujiao`）；鱄鱼（`beast-nanshan-zhuan`）；𪃍（`beast-nanshan-yulingqiu`）；鵷鶵（`beast-nanshan-yuanchu`）；青丘之山（`place-qingqiu`）；南山经山列（`place-south-ranges`）；招摇之山（`place-zhaoyao`）；杻阳之山（`place-niuyang`）；祝余（`plant-zhuyu`）；迷谷（`plant-migu`）；丽𪊨之水（`water-liji`）；怪水（`water-guai`）；宪翼之水（`water-xianyi`）；英水（`water-ying-qingqiu`）；即翼之泽（`water-jiyi`）；育沛（`material-yupei`）；汸水（`water-nanshan-fang`）；淯（`water-nanshan-yu-receiver`）；英水 · 柜山（`water-nanshan-ying-gui`）；赤水 · 柜山段（`water-nanshan-chishui-gui`）；苕水（`water-nanshan-tiao`）；具区（`water-nanshan-juqu`）；诸毗 · 浮玉段（`water-nanshan-zhupi-fuyu`）；䦠水（`water-nanshan-shu`）；虖勺 · 成山流入对象（`water-nanshan-hushao-receiver`）；勺水（`water-nanshan-shao`）；湨（`water-nanshan-ju`）；列涂（`water-nanshan-lietu`）；洵水（`water-nanshan-xun`）；阏之泽（`water-nanshan-yan-marsh`）；滂水（`water-nanshan-pang`）；鹿水（`water-nanshan-lu`）；泽更之水（`water-nanshan-zegeng`）；泿水（`water-nanshan-yin`）；丹水（`water-nanshan-dan`）；㴾海 · 南山经（`water-nanshan-bohai-south`）；汎水（`water-nanshan-fan`）；黑水 · 鸡山（`water-nanshan-hei`）；佐水（`water-nanshan-zuo`）；棪木（`plant-nanshan-yan`）；白䓘（`plant-nanshan-baigao`）；西海 · 南山经（`water-nanshan-west-sea`）；东海 · 南山经（`water-nanshan-east-sea`）；招摇之山（`passage-nanshan-zhaoyao`）；堂庭之山（`passage-nanshan-tangting`）；猨翼之山（`passage-nanshan-yuanyi`）；杻阳之山（`passage-nanshan-niuyang`）；祗山（`passage-nanshan-di`）；亶爰之山（`passage-nanshan-danyuan`）；基山（`passage-nanshan-jishan`）；青丘之山（`passage-nanshan-qingqiu`）；箕尾之山（`passage-nanshan-jiwei`）；䧿山总述与祭祀（`passage-nanshan-range1`）；柜山（`passage-nanshan-gui`）；长右之山（`passage-nanshan-changyou`）；尧光之山（`passage-nanshan-yaoguang`）；羽山（`passage-nanshan-yu`）；瞿父之山（`passage-nanshan-qufu`）；句余之山（`passage-nanshan-gouyu`）；浮玉之山（`passage-nanshan-fuyu`）；成山（`passage-nanshan-cheng`）；会稽之山（`passage-nanshan-kuaiji`）；夷山（`passage-nanshan-yi`）；仆勾之山（`passage-nanshan-pugou`）；洵山（`passage-nanshan-xun`）；虖勺之山（`passage-nanshan-hushao`）；区吴之山（`passage-nanshan-quwu`）；咸阴之山（`passage-nanshan-xianyin`）；鹿吴之山（`passage-nanshan-luwu`）；漆吴之山（`passage-nanshan-qiwu`）；南次二经总述与祭祀（`passage-nanshan-range2`）；天虞之山（`passage-nanshan-tianyu`）；祷过之山（`passage-nanshan-daoguo`）；丹穴之山（`passage-nanshan-danxue`）；发爽之山（`passage-nanshan-fashuang`）；旄山之尾（`passage-nanshan-maowei`）；非山之首（`passage-nanshan-feitou`）；阳夹之山（`passage-nanshan-yangjia`）；灌湘之山（`passage-nanshan-guanxiang`）；鸡山（`passage-nanshan-ji`）；令丘之山（`passage-nanshan-lingqiu`）；仑者之山（`passage-nanshan-lunzhe`）；禺槀之山（`passage-nanshan-yugao`）；南禺之山（`passage-nanshan-nanyu`）；南次三经总述与祭祀（`passage-nanshan-range3`）；南山经篇末总计（`passage-nanshan-total`）；堂庭之山（`place-nanshan-tangting`）；猨翼之山（`place-nanshan-yuanyi`）；祗山（`place-nanshan-di`）；亶爰之山（`place-nanshan-danyuan`）；基山（`place-nanshan-jishan`）；箕尾之山（`place-nanshan-jiwei`）；柜山（`place-nanshan-gui`）；长右之山（`place-nanshan-changyou`）；尧光之山（`place-nanshan-yaoguang`）；羽山（`place-nanshan-yu`）；瞿父之山（`place-nanshan-qufu`）；句余之山（`place-nanshan-gouyu`）；浮玉之山（`place-nanshan-fuyu`）；成山（`place-nanshan-cheng`）；会稽之山（`place-nanshan-kuaiji`）；夷山（`place-nanshan-yi`）；仆勾之山（`place-nanshan-pugou`）；洵山（`place-nanshan-xun`）；虖勺之山（`place-nanshan-hushao`）；区吴之山（`place-nanshan-quwu`）；咸阴之山（`place-nanshan-xianyin`）；鹿吴之山（`place-nanshan-luwu`）；漆吴之山（`place-nanshan-qiwu`）；天虞之山（`place-nanshan-tianyu`）；祷过之山（`place-nanshan-daoguo`）；丹穴之山（`place-nanshan-danxue`）；发爽之山（`place-nanshan-fashuang`）；旄山之尾（`place-nanshan-maowei`）；非山之首（`place-nanshan-feitou`）；阳夹之山（`place-nanshan-yangjia`）；灌湘之山（`place-nanshan-guanxiang`）；鸡山（`place-nanshan-ji`）；令丘之山（`place-nanshan-lingqiu`）；仑者之山（`place-nanshan-lunzhe`）；禺槀之山（`place-nanshan-yugao`）；南禺之山（`place-nanshan-nanyu`）；育遗（`valley-nanshan-yuyi`）；中谷（`valley-nanshan-zhonggu`）；凯风（`wind-nanshan-kai`）；条风（`wind-nanshan-tiao`）；流黄（`place-nanshan-reference-liuhuang`）；诸毗 · 柜山段（`place-nanshan-reference-zhupi`）；丘山（`place-nanshan-reference-qiushan`）；白猿（`animal-nanshan-white-ape`）；蝮虫（`animal-nanshan-fu`）；鮆鱼（`animal-nanshan-ji-fish`）；芘蠃（`animal-nanshan-piluo`）；犀（`animal-nanshan-xi`）；兕（`animal-nanshan-si`）；象（`animal-nanshan-elephant`）；䧿山诸神（`deity-nanshan-1`）；䧿山祭礼（`rite-nanshan-1`）；南次二经诸神（`deity-nanshan-2`）；南次二经祭礼（`rite-nanshan-2`）；南次三经诸神（`deity-nanshan-3`）；南次三经祭礼（`rite-nanshan-3`）。
- 待补方向：43段正文与39座逐述山入口已接入；新增97张独立卡涵盖山水、异兽、草木、动物、谷风、山神和祭礼。本轮51幅插画已审51幅、待补或待审0幅；验收以最新交接记录为准，不将文本接入称为全量完成。
- 校核入口：[该篇固定修订](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E4%B8%80&oldid=2652851)；全篇已对照影印页16–32，补录第26页；经文、底本注文和白话分存。电子快照原样保留，差异见`data/nanshan-edition-review.json`。

### 02 西山经

- 常规入口：朱厌（`beast-zhuyan`）；英招（`beast-yingzhao`）；文鳐鱼（`beast-wenyaoyu`）；羬羊（`beast-xishan-qianyang`）；䳋渠（`beast-xishan-tongqu`）；肥𧔥（太华山）（`beast-xishan-feiyi-taihua`）；赤鷩（`beast-xishan-chibie`）；葱聾（`beast-xishan-conglong`）；鴖（`beast-xishan-min`）；䰷鱼（`beast-xishan-bangyu-ying`）；羬羊（英山段）（`beast-xishan-qianyang-ying`）；肥遗（英山鸟）（`beast-xishan-feiyi-ying`）；人鱼（竹山段）（`beast-xishan-renyu-zhushan`）；毫彘（`beast-xishan-haozhi-zhushan`）；囂（羭次兽）（`beast-xishan-xiao-yuci`）；槖𩇯（`beast-xishan-tuofei-yuci`）；猛豹（西山经南山段）（`beast-xishan-mengbao-nanshan`）；尸鳩（西山经南山段）（`beast-xishan-shijiu-nanshan`）；犀（嶓冡段）（`animal-xishan-xi-bozhong`）；兕（嶓冡段）（`animal-xishan-si-bozhong`）；熊（嶓冡段）（`animal-xishan-bear-bozhong`）；羆（嶓冡段）（`animal-xishan-pi-bozhong`）；白翰（嶓冡段）（`bird-xishan-baihan-bozhong`）；赤鷩（嶓冡段）（`bird-xishan-chibie-bozhong`）；谿邊（天帝山）（`beast-xishan-xibian-tiandi`）；櫟（天帝山鸟）（`beast-xishan-li-tiandi`）；𤣎如（皐塗段）（`beast-xishan-yingru-gaotu`）；數斯（皐塗段）（`beast-xishan-shusi-gaotu`）；𤛎（黄山段）（`beast-xishan-min-huangshan`）；鸚䳇（黄山段）（`beast-xishan-yingmu-huangshan`）；旄牛（翠山段）（`animal-xishan-maoniu-cuishan`）；麢（翠山段）（`animal-xishan-ling-cuishan`）；麝（翠山段）（`animal-xishan-she-cuishan`）；鸓（翠山段）（`bird-xishan-lei-cuishan`）；白蛇（㤗冐段）（`beast-xishan-white-snake-taimao`）；鸚䳇（數歴段）（`beast-xishan-yingmu-shuli`）；虎（女牀段）（`animal-xishan-tiger-nvchuang`）；豹（女牀段）（`animal-xishan-leopard-nvchuang`）；犀（女牀段）（`animal-xishan-xi-nvchuang`）；兕（女牀段）（`animal-xishan-si-nvchuang`）；鸞鳥（女牀段）（`beast-xishan-luan-nvchuang`）；㸲牛（鹿臺段）（`animal-xishan-zuoniu-lutai`）；羬羊（鹿臺段）（`beast-xishan-qianyang-lutai`）；白豪（鹿臺段）（`animal-xishan-baihao-lutai`）；鳬徯（鹿臺段）（`beast-xishan-fuxi-lutai`）；朱厭（小次段）（`beast-xishan-zhuyan-xiaoci`）；㸲牛（大次段）（`animal-xishan-zuoniu-daci`）；麢羊（大次段）（`animal-xishan-lingyang-daci`）；犀（𢇨陽段）（`animal-xishan-xi-quyang`）；兕（𢇨陽段）（`animal-xishan-si-quyang`）；虎（𢇨陽段）（`animal-xishan-tiger-quyang`）；犳（𢇨陽段）（`animal-xishan-zhuo-quyang`）；㸲牛（𢇨陽段）（`animal-xishan-zuoniu-quyang`）；犀（衆獸段）（`animal-xishan-xi-zhongshou`）；兕（衆獸段）（`animal-xishan-si-zhongshou`）；麋（西皇段）（`animal-xishan-mi-xihuang`）；鹿（西皇段）（`animal-xishan-deer-xihuang`）；㸲牛（西皇段）（`animal-xishan-zuoniu-xihuang`）；羅羅（萊山段）（`bird-xishan-luoluo-laishan`）；舉父（崇吾段）（`beast-xishan-jufu-chongwu`）；蠻蠻（崇吾段）（`bird-xishan-manman-chongwu`）；竒鳥（峚鍾泽间）（`bird-xishan-birds-mi-zhong`）；怪獸（峚鍾泽间）（`beast-xishan-beasts-mi-zhong`）；竒魚（峚鍾泽间）（`beast-xishan-fish-mi-zhong`）；大鶚（欽䲹所化）（`bird-xishan-qinpi-e-zhongshan`）；鵕鳥（皷所化）（`bird-xishan-gu-jun-zhongshan`）；文鰩魚（㤗噐段）（`beast-xishan-wenyao-taiqi`）；蠃母（槐江水中）（`beast-xishan-luomu-huaijiang`）；鷹（槐江北望）（`bird-xishan-ying-huaijiang`）；鸇（槐江北望）（`bird-xishan-zhan-huaijiang`）；陸吾（`beast-luwu`）；土螻（`beast-tulou`）；欽原（`beast-qinyuan`）；鶉鳥（`bird-xishan-chun-kunlun`）；怪鳥獸（崑崙段）（`beast-xishan-strange-kunlun`）；滑魚（`beast-xishan-huayu-leyou`）；狡（`beast-xishan-jiao-yushan`）；胜遇（`bird-xishan-shengyu-yushan`）；文尾兽（長留段）（`beast-xishan-beasts-changliu`）；文首鸟（長留段）（`bird-xishan-birds-changliu`）；狰（`beast-zheng`）；畢方（`beast-bifang`）；天狗（`beast-tian-gou`）；三青鳥（三危段）（`bird-xishan-bluebirds-sanwei`）；𢕟𢓨（`beast-xishan-aoyu-sanwei`）；鴟（三危段）（`bird-xishan-chi-sanwei`）；積蛇（`beast-xishan-jishes-guishan3`）；帝江（`beast-dijiang`）；讙（`beast-guan`）；鵸䳜（`bird-xishan-qiyu-yiwang`）；白鹿（上申段）（`beast-xishan-deer-shangshen`）；當扈（`bird-xishan-danghu-shangshen`）；衆蛇（諸次段）（`beast-xishan-snakes-zhuci`）；白狼（盂山）（`beast-xishan-wolf-yushan4`）；白虎（盂山）（`beast-xishan-tiger-yushan4`）；白雉（盂山）（`bird-xishan-pheasant-yushan4`）；白翟（盂山）（`bird-xishan-zhai-yushan4`）；㸲牛（白於段）（`beast-xishan-zuoniu-baiyu`）；羬羊（白於段）（`beast-xishan-qianyang-baiyu`）；鴞（白於段）（`bird-xishan-xiao-baiyu`）；蠻蠻（鼠身鳖首）（`beast-xishan-manman-gangwei`）；白鸟兽（英鞮段）（`beast-xishan-white-yingdi`）；冉遺之魚（`beast-xishan-ranyi-yingdi`）；駮（`beast-bo`）；窮竒（西山经）（`beast-qiongqi-xishan`）；蠃魚（`beast-luoyu`）；白虎（鳥鼠段）（`beast-xishan-tiger-niaoshu`）；鰠魚（`beast-xishan-saoyu-niaoshu`）；𩶯魮之魚（`beast-xishan-rupi-niaoshu`）；龜（崦嵫阳）（`beast-xishan-turtle-yanzi`）；孰湖（`beast-xishan-shuhu-yanzi`）；未名鸟（崦嵫末段）（`bird-xishan-unnamed-yanzi`）；玉山（`place-yushan`）；西山经山列（`place-west-ranges`）；玉山 · 西王母所居（`domain-yushan`）；濩水（`water-xishan-huo`）；渭（西山经）（`water-xishan-wei`）；萆荔（`plant-xishan-bili`）；文茎（`plant-xishan-wenjing`）；條（符禺山）（`plant-xishan-tiao-fuyu`）；符禺之水（`water-xishan-fuyu`）；條（石脆山）（`plant-xishan-tiao-shicui`）；灌水（`water-xishan-guan`）；禺水（石脆山段）（`water-xishan-yu-shicui`）；流赭（`material-xishan-liuzhe`）；禺水（英山段）（`water-xishan-yu-ying`）；招水（英山段）（`water-xishan-zhao-ying`）；黄雚（`plant-xishan-huangguan`）；竹水（`water-xishan-zhu`）；丹水（竹山段）（`water-xishan-dan-zhushan`）；洛水（竹山段）（`water-xishan-luo-zhushan`）；水玉（竹山段）（`material-xishan-shuiyu-zhushan`）；盼木（`plant-xishan-panmu`）；薰草（`plant-xishan-xuncao`）；漆水（羭次段）（`water-xishan-qi-yuci`）；嬰垣之玉（`material-xishan-yingyuan-yuci`）；逐水（时山段）（`water-xishan-zhu-shishan`）；水玉（时山段）（`material-xishan-shuiyu-shishan`）；丹水（西山经南山段）（`water-xishan-dan-nanshan`）；丹粟（西山经南山段）（`material-xishan-dansu-nanshan`）；涔水（大时段）（`water-xishan-qian-dashi`）；清水（大时段）（`water-xishan-qing-dashi`）；汉水（西山经首列）（`water-xishan-han-dashi`）；银（大时段）（`material-xishan-silver-dashi`）；白玉（大时段）（`material-xishan-white-jade-dashi`）；沔（嶓冡段）（`water-xishan-mian-bozhong`）；囂水（嶓冡段）（`water-xishan-xiao-bozhong`）；汤水（嶓冡段）（`water-xishan-tang-bozhong`）；桃枝（嶓冡段）（`plant-xishan-taozhi-bozhong`）；鈎端（嶓冡段）（`plant-xishan-gouduan-bozhong`）；蓇蓉（嶓冡段）（`plant-xishan-gurong-bozhong`）；杜衡（天帝山）（`plant-xishan-duheng-tiandi`）；薔水（皐塗段）（`water-xishan-se-gaotu`）；诸资之水（皐塗段）（`water-xishan-zhuzi-gaotu`）；塗水（皐塗段）（`water-xishan-tu-gaotu`）；集获之水（皐塗段）（`water-xishan-jihuo-gaotu`）；丹粟（皐塗段）（`material-xishan-dansu-gaotu`）；银（皐塗段）（`material-xishan-silver-gaotu`）；黄金（皐塗段）（`material-xishan-gold-gaotu`）；桂木（皐塗段）（`plant-xishan-gui-gaotu`）；礜（皐塗段）（`material-xishan-yu-gaotu`）；無條（皐塗段）（`plant-xishan-wutiao-gaotu`）；竹箭（黄山段）（`plant-xishan-zhujian-huangshan`）；盼水（黄山段）（`water-xishan-pan-huangshan`）；赤水（西山经）（`water-xishan-chi-huangshan`）；玉（黄山水文段）（`material-xishan-jade-huangshan`）；㯶（翠山段）（`plant-xishan-zong-cuishan`）；枏（翠山段）（`plant-xishan-nan-cuishan`）；竹箭（翠山段）（`plant-xishan-zhujian-cuishan`）；黄金（翠山段）（`material-xishan-gold-cuishan`）；玉（翠山段）（`material-xishan-jade-cuishan`）；西海（西山经）（`water-xishan-westsea-guishan`）；玉（騩山段）（`material-xishan-jade-guishan`）；淒水（騩山段）（`water-xishan-qi-guishan`）；采石（騩山水文段）（`material-xishan-caishi-guishan`）；黄金（騩山水文段）（`material-xishan-gold-guishan`）；丹粟（騩山段）（`material-xishan-dansu-guishan`）；铜（鈐山段）（`material-xishan-copper-qianshan`）；玉（鈐山段）（`material-xishan-jade-qianshan`）；杻（鈐山段）（`plant-xishan-niu-qianshan`）；橿（鈐山段）（`plant-xishan-jiang-qianshan`）；金（㤗冐段）（`material-xishan-jin-taimao`）；铁（㤗冐段）（`material-xishan-iron-taimao`）；浴水（㤗冐段）（`water-xishan-yu-taimao`）；河（西山经）（`water-xishan-he-taimao`）；藻玉（㤗冐段）（`material-xishan-zaoyu-taimao`）；黄金（數歴段）（`material-xishan-gold-shuli`）；银（數歴段）（`material-xishan-silver-shuli`）；杻（數歴段）（`plant-xishan-niu-shuli`）；橿（數歴段）（`plant-xishan-jiang-shuli`）；楚水（數歴段）（`water-xishan-chu-shuli`）；珠（數歴水文段）（`material-xishan-pearl-shuli`）；银（髙山段）（`material-xishan-silver-gaoshan`）；青碧（髙山下）（`material-xishan-qingbi-gaoshan`）；雄黄（髙山段）（`material-xishan-xionghuang-gaoshan`）；㯶（髙山段）（`plant-xishan-zong-gaoshan`）；竹（髙山段）（`plant-xishan-bamboo-gaoshan`）；涇水（西山经次二列）（`water-xishan-jing-gaoshan`）；磬石（髙山水文段）（`material-xishan-qingshi-gaoshan`）；青碧（髙山水文段）（`material-xishan-qingbi-water-gaoshan`）；赤铜（女牀段）（`material-xishan-red-copper-nvchuang`）；石𣵀（女牀段）（`material-xishan-shinie-nvchuang`）；黄金（龍首山阳面）（`material-xishan-gold-longshou`）；鐡（龍首山阴面）（`material-xishan-iron-longshou`）；苕水（龍首山）（`water-xishan-tiao-longshou`）；羙玉（龍首山水文）（`material-xishan-fine-jade-longshou`）；白玉（鹿臺山上）（`material-xishan-white-jade-lutai`）；銀（鹿臺山下）（`material-xishan-silver-lutai`）；磬石（鳥危山阳面）（`material-xishan-qingshi-niaowei`）；檀（鳥危山阴面）（`plant-xishan-tan-niaowei`）；楮（鳥危山阴面）（`plant-xishan-chu-niaowei`）；女牀（鳥危段·所指未詳）（`material-xishan-nvchuang-niaowei`）；鳥危之水（`water-xishan-niaowei`）；丹粟（鳥危段水文）（`material-xishan-dansu-niaowei`）；白玉（小次山上）（`material-xishan-white-jade-xiaoci`）；赤銅（小次山下）（`material-xishan-red-copper-xiaoci`）；堊（大次山阳面）（`material-xishan-e-daci`）；碧（大次山阴面）（`material-xishan-bi-daci`）；金（薰吳段）（`material-xishan-jin-xunwu`）；玉（薰吳段）（`material-xishan-jade-xunwu`）；稷（𢇨陽段）（`plant-xishan-ji-quyang`）；柟（𢇨陽段）（`plant-xishan-nan-quyang`）；豫章（𢇨陽段）（`plant-xishan-yuzhang-quyang`）；㻬琈之玉（衆獸山上）（`material-xishan-tufu-zhongshou`）；檀（衆獸山下）（`plant-xishan-tan-zhongshou`）；楮（衆獸山下）（`plant-xishan-chu-zhongshou`）；黄金（衆獸山下）（`material-xishan-gold-zhongshou`）；金（皇人山上）（`material-xishan-jin-huangren`）；玉（皇人山上）（`material-xishan-jade-huangren`）；青雄黄（皇人山下）（`material-xishan-qingxionghuang-huangren`）；皇水（皇人段）（`water-xishan-huang-huangren`）；丹粟（皇人段水文）（`material-xishan-dansu-huangren`）；黄金（中皇山上）（`material-xishan-gold-zhonghuang`）；蕙棠（中皇山下）（`plant-xishan-huitang-zhonghuang`）；金（西皇山阳面）（`material-xishan-jin-xihuang`）；鐡（西皇山阴面）（`material-xishan-iron-xihuang`）；檀（萊山段）（`plant-xishan-tan-laishan`）；楮（萊山段）（`plant-xishan-chu-laishan`）；䍃之澤（崇吾段）（`water-xishan-yaoze-chongwu`）；䗡淵（崇吾段）（`water-xishan-yanyuan-chongwu`）；未名木（崇吾段）（`plant-xishan-unnamed-chongwu`）；泚水（長沙段）（`water-xishan-ci-changsha`）；泑水（西山经）（`water-xishan-you-changsha`）；青雄黄（長沙段）（`material-xishan-qingxionghuang-changsha`）；泑澤（不周段）（`water-xishan-youze-buzhou`）；嘉果（不周段·未命名）（`plant-xishan-jia-guo-buzhou`）；丹木（峚山段）（`plant-xishan-danmu-mishan`）；丹水（峚山段）（`water-xishan-dan-mishan`）；稷澤（峚山段）（`water-xishan-jize-mishan`）；白玉（峚山丹水）（`material-xishan-white-jade-mishan`）；玉膏（峚山段）（`material-xishan-yugao-mishan`）；𤣥玉（峚山段）（`material-xishan-xuanyu-mishan`）；玉榮（峚山段）（`material-xishan-yurong-mishan`）；瑾瑜之玉（峚山段）（`material-xishan-jinyu-mishan`）；泽地（峚至鍾）（`water-xishan-wetlands-mi-zhong`）；𮗚水（㤗噐段）（`water-xishan-guan-taiqi`）；東海（㤗噐段）（`water-xishan-eastsea-taiqi`）；丘時之水（槐江段）（`water-xishan-qiushi-huaijiang`）；青雄黃（槐江山上）（`material-xishan-qingxionghuang-huaijiang`）；藏琅玕（槐江段）（`material-xishan-langgan-huaijiang`）；黄金（槐江山上）（`material-xishan-gold-above-huaijiang`）；玉（槐江山上）（`material-xishan-jade-above-huaijiang`）；丹粟（槐江阳面）（`material-xishan-dansu-huaijiang`）；采黄金銀（槐江阴面）（`material-xishan-shaded-goods-huaijiang`）；大澤（槐江西望）（`water-xishan-daze-huaijiang`）；玉（槐江西望大澤）（`material-xishan-jade-daze-huaijiang`）；榣木之有若（槐江西望）（`plant-xishan-yaomu-ruo-huaijiang`）；滛水（槐江东望）（`water-xishan-flowing-huaijiang`）；沙棠（`plant-xishan-shatang-kunlun`）；薲草（`plant-xishan-pin-kunlun`）；河水（崑崙段）（`water-xishan-he-kunlun`）；赤水（崑崙段）（`water-xishan-chi-kunlun`）；汜天之水（`water-xishan-fantian-kunlun`）；洋水（崑崙段）（`water-xishan-yang-kunlun`）；醜塗之水（`water-xishan-choutu-kunlun`）；黑水（崑崙段）（`water-xishan-hei-kunlun`）；桃水（`water-xishan-tao-leyou`）；稷澤（樂游段）（`water-xishan-jize-leyou`）；白玉（樂游段）（`material-xishan-jade-leyou`）；玉（蠃母山上）（`material-xishan-jade-luomushan`）；青石（蠃母山下）（`material-xishan-stone-luomushan`）；洵水（`water-xishan-xun-xuanyuan`）；黑水（軒轅段）（`water-xishan-hei-xuanyuan`）；丹粟（洵水段）（`material-xishan-dansu-xuanyuan`）；青雄黄（洵水段）（`material-xishan-xionghuang-xuanyuan`）；河水（積石段）（`water-xishan-he-jishi`）；文玉石（`material-xishan-jade-changliu`）；瑶碧（`material-xishan-yaobi-zhange`）；濁浴之水（`water-xishan-zhuoyu-yinshan3`）；蕃澤（`water-xishan-fan-yinshan3`）；文貝（`material-xishan-shell-yinshan3`）；㯶（符愓段）（`plant-xishan-zong-futang`）；柟（符愓段）（`plant-xishan-nan-futang`）；金（符愓山下）（`material-xishan-gold-futang`）；玉（符愓山下）（`material-xishan-jade-futang`）；玉（西次三经騩山）（`material-xishan-jade-guishan3`）；金（天山）（`material-xishan-gold-tianshan`）；玉（天山）（`material-xishan-jade-tianshan`）；青雄黄（天山）（`material-xishan-xionghuang-tianshan`）；英水（`water-xishan-ying-tianshan`）；嬰短之玉（`material-xishan-yingduan-youshan`）；瑾瑜之玉（泑山阳）（`material-xishan-jinyu-youshan`）；青雄黄（泑山阴）（`material-xishan-xionghuang-youshan`）；金（翼望段）（`material-xishan-gold-yiwang`）；玉（翼望段）（`material-xishan-jade-yiwang`）；榖（西次四经隂山）（`plant-xishan-gu-yinshan4`）；茆（隂山段）（`plant-xishan-mao-yinshan4`）；蕃（隂山段）（`plant-xishan-fan-yinshan4`）；隂水（`water-xishan-yin-yinshan4`）；洛（西次四经首段）（`water-xishan-luo-yinshan4`）；茈草（勞山）（`plant-xishan-zicao-laoshan`）；弱水（勞山）（`water-xishan-ruo-laoshan`）；洛（勞山段）（`water-xishan-luo-laoshan`）；洱水（`water-xishan-er-bafu`）；洛（罷父段）（`water-xishan-luo-bafu`）；茈碧（`material-xishan-zibi-bafu`）；榖（申山上）（`plant-xishan-gu-shenshan`）；柞（申山上）（`plant-xishan-zuo-shenshan`）；杻（申山下）（`plant-xishan-niu-shenshan`）；橿（申山下）（`plant-xishan-jiang-shenshan`）；金（申山阳）（`material-xishan-gold-shenshan`）；玉（申山阳）（`material-xishan-jade-shenshan`）；區水（`water-xishan-qu-shenshan`）；河（申山段）（`water-xishan-he-shenshan`）；桑（鳥山上）（`plant-xishan-sang-niaoshan`）；楮（鳥山下）（`plant-xishan-chu-niaoshan`）；鐡（鳥山阴）（`material-xishan-iron-niaoshan`）；玊（鳥山阳）（`material-xishan-jade-niaoshan`）；辱水（`water-xishan-ru-niaoshan`）；河（鳥山段）（`water-xishan-he-niaoshan`）；硌石（`material-xishan-stone-shangshen`）；榛（上申下）（`plant-xishan-zhen-shangshen`）；楛（上申下）（`plant-xishan-hu-shangshen`）；湯水（`water-xishan-tang-shangshen`）；河（上申段）（`water-xishan-he-shangshen`）；諸次之水（`water-xishan-zhuci-zhuci`）；河（諸次段）（`water-xishan-he-zhuci`）；漆（號山段）（`plant-xishan-lacquer-haoshan`）；㯶（號山段）（`plant-xishan-zong-haoshan`）；葯（`plant-xishan-yao-haoshan`）；䖀（`plant-xishan-xian-haoshan`）；芎藭（`plant-xishan-xiongqiong-haoshan`）；汵石（`material-xishan-qin-haoshan`）；端水（`water-xishan-duan-haoshan`）；河（號山段）（`water-xishan-he-haoshan`）；鐡（盂山阴）（`material-xishan-iron-yushan4`）；銅（盂山阳）（`material-xishan-copper-yushan4`）；生水（`water-xishan-sheng-yushan4`）；河（盂山段）（`water-xishan-he-yushan4`）；松（白於上）（`plant-xishan-pine-baiyu`）；柏（白於上）（`plant-xishan-cypress-baiyu`）；櫟（白於下）（`plant-xishan-li-baiyu`）；檀（白於下）（`plant-xishan-tan-baiyu`）；洛水（白於阳）（`water-xishan-luo-baiyu`）；渭（白於段）（`water-xishan-wei-baiyu`）；夾水（`water-xishan-jia-baiyu`）；生水（白於段）（`water-xishan-sheng-baiyu`）；申水（`water-xishan-shen-shenshou`）；白玉（申首段）（`material-xishan-jade-shenshou`）；涇水（涇谷段）（`water-xishan-jing-jinggu`）；渭（涇谷段）（`water-xishan-wei-jinggu`）；白金（涇谷）（`material-xishan-metal-jinggu`）；白玉（涇谷）（`material-xishan-jade-jinggu`）；柒木（`plant-xishan-qi-gangshan`）；㻬琈之玉（剛山）（`material-xishan-tufuyu-gangshan`）；剛水（`water-xishan-gang-gangshan`）；渭（剛山段）（`water-xishan-wei-gangshan`）；洛水（剛山尾）（`water-xishan-luo-gangwei`）；河（剛山尾）（`water-xishan-he-gangwei`）；𣾰木（`plant-xishan-mu-yingdi`）；金（英鞮下）（`material-xishan-gold-yingdi`）；玉（英鞮下）（`material-xishan-jade-yingdi`）；涴水（`water-xishan-wan-yingdi`）；𨹧羊之澤（`water-xishan-lingyang-yingdi`）；玉（中曲阳）（`material-xishan-jade-sun-zhongqu`）；雄黄（中曲阴）（`material-xishan-xionghuang-zhongqu`）；白玉（中曲阴）（`material-xishan-jade-shade-zhongqu`）；金（中曲阴）（`material-xishan-gold-zhongqu`）；櫰木（`plant-xishan-huai-zhongqu`）；𪷟水（`water-xishan-meng-guishan4`）；洋水（邽山段）（`water-xishan-yang-guishan4`）；黄貝（`material-xishan-shell-guishan4`）；白玉（鳥鼠段）（`material-xishan-jade-niaoshu`）；渭水（鳥鼠段）（`water-xishan-wei-niaoshu`）；河（鳥鼠段）（`water-xishan-he-niaoshu`）；濫水（`water-xishan-lan-niaoshu`）；漢水（鳥鼠段）（`water-xishan-han-niaoshu`）；丹木（崦嵫段）（`plant-xishan-dan-yanzi`）；玉（崦嵫阴）（`material-xishan-jade-yanzi`）；苕水（崦嵫）（`water-xishan-tiao-yanzi`）；海（崦嵫段）（`water-xishan-sea-yanzi`）；砥礪（`material-xishan-whetstones-yanzi`）；钱来之山（`passage-xishan-qianlai`）；松果之山（`passage-xishan-songguo`）；太华之山（`passage-xishan-taihua`）；小华之山（`passage-xishan-xiaohua`）；符禺之山（`passage-xishan-fuyu`）；石脆之山（`passage-xishan-shicui`）；英山（`passage-xishan-ying`）；竹山（`passage-xishan-zhushan`）；浮山（`passage-xishan-fushan`）；羭次之山（`passage-xishan-yuci`）；时山（`passage-xishan-shishan`）；南山（西山经）（`passage-xishan-nanshan-west`）；大时之山（`passage-xishan-dashi`）；嶓冡之山（`passage-xishan-bozhong`）；天帝之山（`passage-xishan-tiandi`）；皐塗之山（`passage-xishan-gaotu`）；黄山（西山经）（`passage-xishan-huangshan`）；翠山（`passage-xishan-cuishan`）；騩山（`passage-xishan-guishan`）；西山首列总括与祭礼（`passage-xishan-range1-summary`）；鈐山（`passage-xishan-qianshan`）；㤗冐之山（`passage-xishan-taimao`）；數歴之山（`passage-xishan-shuli`）；髙山（`passage-xishan-gaoshan`）；女牀之山（`passage-xishan-nvchuang`）；龍首之山（`passage-xishan-longshou`）；鹿臺之山（`passage-xishan-lutai`）；鳥危之山（`passage-xishan-niaowei`）；小次之山（`passage-xishan-xiaoci`）；大次之山（`passage-xishan-daci`）；薰吳之山（`passage-xishan-xunwu`）；𢇨陽之山（`passage-xishan-quyang`）；衆獸之山（`passage-xishan-zhongshou`）；皇人之山（`passage-xishan-huangren`）；中皇之山（`passage-xishan-zhonghuang`）；西皇之山（`passage-xishan-xihuang`）；萊山（`passage-xishan-laishan`）；西次二经总括与祭礼（`passage-xishan-range2-summary`）；崇吾之山（`passage-xishan-chongwu`）；長沙之山（`passage-xishan-changsha`）；不周之山（`passage-xishan-buzhou`）；峚山（`passage-xishan-mishan`）；鍾山（`passage-xishan-zhongshan`）；㤗噐之山（`passage-xishan-taiqi`）；槐江之山（`passage-xishan-huaijiang`）；崑崙之丘（`passage-xishan-kunlun`）；樂游之山（`passage-xishan-leyou`）；蠃母之山（`passage-xishan-luomushan`）；玉山（`passage-xishan-yushan`）；軒轅之丘（`passage-xishan-xuanyuan`）；積石之山（`passage-xishan-jishi`）；長留之山（`passage-xishan-changliu`）；章莪之山（`passage-xishan-zhange`）；隂山（西次三经）（`passage-xishan-yinshan3`）；符愓之山（`passage-xishan-futang`）；三危之山（`passage-xishan-sanwei`）；騩山（西次三经）（`passage-xishan-guishan3`）；天山（`passage-xishan-tianshan`）；泑山（`passage-xishan-youshan`）；翼望之山（`passage-xishan-yiwang`）；西次三经总括与祠礼（`passage-xishan-range3-summary`）；隂山（西次四经）（`passage-xishan-yinshan4`）；勞山（`passage-xishan-laoshan`）；罷父之山（`passage-xishan-bafu`）；申山（`passage-xishan-shenshan`）；鳥山（`passage-xishan-niaoshan`）；上申之山（`passage-xishan-shangshen`）；諸次之山（`passage-xishan-zhuci`）；號山（`passage-xishan-haoshan`）；盂山（`passage-xishan-yushan4`）；白於之山（`passage-xishan-baiyu`）；申首之山（`passage-xishan-shenshou`）；涇谷之山（`passage-xishan-jinggu`）；剛山（`passage-xishan-gangshan`）；剛山之尾（`passage-xishan-gangwei`）；英鞮之山（`passage-xishan-yingdi`）；中曲之山（`passage-xishan-zhongqu`）；邽山（`passage-xishan-guishan4`）；鳥鼠同穴之山（`passage-xishan-niaoshu`）；崦嵫之山（`passage-xishan-yanzi`）；西次四经总括与祠礼（`passage-xishan-range4-summary`）；西山经篇末总计（`passage-xishan-western-total`）；钱来之山（`place-xishan-qianlai`）；松果之山（`place-xishan-songguo`）；太华之山（`place-xishan-taihua`）；小华之山（`place-xishan-xiaohua`）；㸲牛（小华山）（`animal-xishan-zuoniu`）；符禺之山（`place-xishan-fuyu`）；石脆之山（`place-xishan-shicui`）；英山（`place-xishan-ying`）；㸲牛（英山段）（`animal-xishan-zuoniu-ying`）；竹山（`place-xishan-zhushan`）；浮山（`place-xishan-fushan`）；羭次之山（`place-xishan-yuci`）；时山（`place-xishan-shishan`）；南山（西山经）（`place-xishan-nanshan-west`）；大时之山（`place-xishan-dashi`）；嶓冡之山（`place-xishan-bozhong`）；天帝之山（`place-xishan-tiandi`）；皐塗之山（`place-xishan-gaotu`）；黄山（西山经）（`place-xishan-huangshan`）；翠山（`place-xishan-cuishan`）；騩山（`place-xishan-guishan`）；华山冢与太牢祠礼（`rite-xishan-hua-range1`）；羭山燭礼与玉器（`rite-xishan-yu-range1`）；其余十七山祠礼（`rite-xishan-seventeen-range1`）；鈐山（`place-xishan-qianshan`）；㤗冐之山（`place-xishan-taimao`）；數歴之山（`place-xishan-shuli`）；髙山（`place-xishan-gaoshan`）；女牀之山（`place-xishan-nvchuang`）；龍首之山（`place-xishan-longshou`）；鹿臺之山（`place-xishan-lutai`）；鳥危之山（`place-xishan-niaowei`）；小次之山（`place-xishan-xiaoci`）；大次之山（`place-xishan-daci`）；薰吳之山（`place-xishan-xunwu`）；𢇨陽之山（`place-xishan-quyang`）；衆獸之山（`place-xishan-zhongshou`）；皇人之山（`place-xishan-huangren`）；中皇之山（`place-xishan-zhonghuang`）；西皇之山（`place-xishan-xihuang`）；萊山（`place-xishan-laishan`）；十神·人靣馬身（西次二经）（`deity-xishan-horse-range2`）；七神·人靣牛身（西次二经）（`deity-xishan-ox-range2`）；少牢与白菅之席（西次二经）（`rite-xishan-shaolao-range2`）；十軰神雄鷄之祠（西次二经）（`rite-xishan-rooster-range2`）；崇吾之山（`place-xishan-chongwu`）；冡遂（崇吾段）（`place-xishan-zhongsui-chongwu`）；帝之摶獸之丘（崇吾段）（`place-xishan-tuan-shou-qiu-chongwu`）；長沙之山（`place-xishan-changsha`）；不周之山（`place-xishan-buzhou`）；諸毗之山（西山经）（`place-xishan-zhupi-buzhou`）；嶽崇之山（不周段）（`place-xishan-yuechong-buzhou`）；峚山（`place-xishan-mishan`）；黃帝（峚山段）（`deity-xishan-huangdi-mishan`）；天地鬼神（峚山段）（`deity-xishan-heaven-earth-mishan`）；鍾山（`place-xishan-zhongshan`）；皷（鍾山龙身）（`deity-xishan-gu-zhongshan`）；欽䲹（鍾山原身）（`deity-xishan-qinpi-zhongshan`）；葆江（鍾山段）（`deity-xishan-baojiang-zhongshan`）；帝（鍾山段·未具名）（`deity-xishan-di-zhongshan`）；崑崙之陽（鍾山段）（`place-xishan-kunlun-yang-zhongshan`）；𡺯崖（鍾山之东）（`place-xishan-yaoya-zhongshan`）；㤗噐之山（`place-xishan-taiqi`）；流沙（㤗噐段）（`place-xishan-liusha`）；槐江之山（`place-xishan-huaijiang`）；帝之平圃（槐江段）（`place-xishan-pingpu-huaijiang`）；英招（槐江段）（`deity-xishan-yingzhao-huaijiang`）；后稷（槐江西望）（`deity-xishan-houji-huaijiang`）；槐鬼離侖（槐江北望）（`deity-xishan-lilun-huaijiang`）；怛山（槐江东望）（`place-xishan-danshan-huaijiang`）；有窮鬼（槐江东望）（`deity-xishan-youqiong-huaijiang`）；未名天神（槐江末段）（`deity-xishan-ox-eight-huaijiang`）；崑崙之丘（`place-xishan-kunlun`）；無逹（`place-xishan-wuda-kunlun`）；大杅（`place-xishan-dayu-kunlun`）；樂游之山（`place-xishan-leyou`）；蠃母之山（`place-xishan-luomushan`）；長乗（`deity-xishan-changcheng-luomushan`）；玉山（`place-xishan-yushan`）；西王母（玉山段）（`deity-xishan-xiwangmu-yushan`）；軒轅之丘（`place-xishan-xuanyuan`）；積石之山（`place-xishan-jishi`）；石門（積石段）（`place-xishan-gate-jishi`）；長留之山（`place-xishan-changliu`）；白帝少昊（`deity-xishan-shaohao-changliu`）；員神磈氏（`deity-xishan-weishi-changliu`）；章莪之山（`place-xishan-zhange`）；隂山（西次三经）（`place-xishan-yinshan3`）；符愓之山（`place-xishan-futang`）；江疑（`deity-xishan-jiangyi-futang`）；三危之山（`place-xishan-sanwei`）；騩山（西次三经）（`place-xishan-guishan3`）；𦒿童（`deity-xishan-qitong-guishan3`）；天山（`place-xishan-tianshan`）；湯谷（天山段）（`place-xishan-tang-tianshan`）；泑山（`place-xishan-youshan`）；蓐𭣣（`deity-xishan-rushou-youshan`）；紅光（`deity-xishan-hongguang-youshan`）；翼望之山（`place-xishan-yiwang`）；羊身人面神（西次三经）（`deity-xishan-sheep-range3-summary`）；吉玉稷米祠礼（`rite-xishan-rite-range3-summary`）；隂山（西次四经）（`place-xishan-yinshan4`）；勞山（`place-xishan-laoshan`）；罷父之山（`place-xishan-bafu`）；申山（`place-xishan-shenshan`）；鳥山（`place-xishan-niaoshan`）；上申之山（`place-xishan-shangshen`）；諸次之山（`place-xishan-zhuci`）；號山（`place-xishan-haoshan`）；盂山（`place-xishan-yushan4`）；白於之山（`place-xishan-baiyu`）；申首之山（`place-xishan-shenshou`）；涇谷之山（`place-xishan-jinggu`）；剛山（`place-xishan-gangshan`）；神𩳁（`deity-xishan-chi-gangshan`）；剛山之尾（`place-xishan-gangwei`）；英鞮之山（`place-xishan-yingdi`）；中曲之山（`place-xishan-zhongqu`）；邽山（`place-xishan-guishan4`）；鳥鼠同穴之山（`place-xishan-niaoshu`）；崦嵫之山（`place-xishan-yanzi`）；白鸡稻米白管祠礼（`rite-xishan-rite-range4-summary`）。
- 数据未开放：昆仑之丘（`08-03`）；西王母（早期形态）（`08-07`）。
- 待补方向：钱来之山、松果之山、太华之山、小华之山、符禺之山、石脆之山、英山、竹山、浮山、羭次之山、时山、南山（西山经）、大时之山、嶓冡之山、天帝之山、皐塗之山、黄山（西山经）、翠山、騩山、西山首列总括与祭礼、鈐山、㤗冐之山、數歴之山、髙山、女牀之山、龍首之山、鹿臺之山、鳥危之山、小次之山、大次之山、薰吳之山、𢇨陽之山、衆獸之山、皇人之山、中皇之山、西皇之山、萊山、西次二经总括与祭礼、崇吾之山、長沙之山、不周之山、峚山、鍾山、㤗噐之山、槐江之山、崑崙之丘、樂游之山、蠃母之山、玉山、軒轅之丘、積石之山、長留之山、章莪之山、隂山（西次三经）、符愓之山、三危之山、騩山（西次三经）、天山、泑山、翼望之山、西次三经总括与祠礼、隂山（西次四经）、勞山、罷父之山、申山、鳥山、上申之山、諸次之山、號山、盂山、白於之山、申首之山、涇谷之山、剛山、剛山之尾、英鞮之山、中曲之山、邽山、鳥鼠同穴之山、崦嵫之山、西次四经总括与祠礼、西山经篇末总计共82段和508张独立卡已核对接入；保留原有异兽与玉山等ID。全篇正文、山水物产与主要具名神祇已接入；第三列报山数与里程合计差异保留。配图仍按形貌依据审核，不宣称多版本逐字校勘或实体穷尽。
- 校核入口：[该篇固定修订](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E4%BA%8C&oldid=2652852)；已核全篇77个列名山段、4列总括和篇末总计共82段，对照影印34–75页，页码与缺字图差异见`data/xishan-edition-review.json`；各列总数及里程不强行改成一致。

### 03 北山经

- 常规入口：滑魚（求如）（`beast-beishan-huayu-qiuru`）；水馬（求如）（`beast-beishan-shuima-qiuru`）；䑏䟽（帶山）（`beast-beishan-huanshu-daishan`）；鵸䳜（帶山）（`beast-beishan-qitu-daishan`）；儵魚（帶山）（`beast-beishan-youyu-daishan`）；何羅之魚（`beast-beishan-heluo-qiaoming`）；孟槐（`beast-beishan-menghuai-qiaoming`）；鰼鰼之魚（`beast-beishan-xixi-zhuoguang`）；麢羊（涿光）（`beast-beishan-lingyang-zhuoguang`）；蕃（涿光）（`beast-beishan-fan-zhuoguang`）；橐駝（虢山）（`beast-beishan-tuotuo-guoshan`）；寓（虢山）（`beast-beishan-yu-guoshan`）；耳䑕（`beast-beishan-ershu-danxun`）；孟極（`beast-beishan-mengji-shizhe`）；幽鴳（`beast-beishan-youan-bianchun`）；足訾（`beast-beishan-zuzi-manlian`）；鵁（`beast-beishan-jiao-manlian`）；諸犍（`beast-zhu-jian`）；白鵺（`beast-beishan-baiye-danzhang`）；那父（`beast-beishan-nafu-guanti`）；竦斯（`beast-beishan-songsi-guanti`）；旄牛（潘侯）（`beast-beishan-maoniu-panhou`）；長蛇（大咸）（`beast-beishan-changshe-daxian`）；赤鮭（敦薨）（`beast-beishan-chigui-dunhong`）；兕（敦薨）（`beast-beishan-si-dunhong`）；旄牛（敦薨）（`beast-beishan-maoniu-dunhong`）；鳲鳩（敦薨）（`beast-beishan-shijiu-dunhong`）；窫窳（少咸）（`beast-beishan-yayu-shaoxian`）；䰽䰽之魚（`beast-beishan-peipei-shaoxian`）；䲃魚（`beast-beishan-zao-yufa`）；山𤟤（`beast-beishan-shanhui-yufa`）；諸懐（`beast-beishan-zhuhuai-beiyue`）；鮨魚（`beast-beishan-yi-beiyue`）；肥遺（渾夕蛇）（`beast-beishan-feiyi-hunxi`）；野马（羆差郭注）（`beast-beishan-yema-bicha`）；马（北鮮）（`beast-beishan-ma-beixian`）；马（隄山）（`beast-beishan-ma-dishan`）；狕（`beast-beishan-yao-dishan`）；龍龜（隄山）（`beast-beishan-longgui-dishan`）；閭（縣雍）（`beast-beishan-lv-xianyong`）；麋（縣雍）（`beast-beishan-mi-xianyong`）；白翟（縣雍）（`beast-beishan-white-di-xianyong`）；白䳑（縣雍）（`beast-beishan-white-you-xianyong`）；鮆魚（縣雍）（`beast-beishan-ci-xianyong`）；𩣡馬（敦頭）（`beast-beishan-boma-duntou`）；狍鴞（`beast-beishan-paoxiao-gouwu`）；獨𤞞（`beast-beishan-dugu-beixiao`）；𪄀𪃑（`beast-beishan-banmao-beixiao`）；居暨（`beast-beishan-juji-liangqu`）；囂（梁渠鸟）（`beast-beishan-xiao-liangqu`）；马（湖灌）（`beast-beishan-ma-huguan`）；䱇（湖灌）（`beast-beishan-shan-huguan`）；怪蛇（洹山）（`beast-beishan-strange-snakes-huan`）；䮝（歸山）（`beast-beishan-hui-guishan`）；䴅（歸山）（`beast-beishan-fen-guishan`）；人魚（龍侯）（`beast-beishan-renyu-longhou`）；天馬（馬成）（`beast-beishan-tianma-macheng`）；鶌鶋（`beast-beishan-quju-macheng`）；飛䑕（天池）（`beast-beishan-feishu-tianchi`）；領胡（`beast-beishan-linghu-yangshan`）；𧰼蛇（陽山鸟）（`beast-beishan-xiangshe-yangshan`）；𩹴父之魚（`beast-beishan-xianfu-yangshan`）；酸與（景山）（`beast-beishan-suanyu-jingshan`）；肥遺之蛇（彭毗）（`beast-beishan-feiyi-pengpi`）；鴣𪄶（小侯）（`beast-beishan-guxi-xiaohou`）；黄鳥（軒轅）（`beast-beishan-huangniao-xuanyuan`）；白蛇（神囷）（`beast-beishan-white-snakes-shenqun`）；飛蟲（神囷）（`beast-beishan-flying-insects-shenqun`）；精衛（`beast-jingwei`）；鱯黽（繡山物名异说）（`beast-beishan-huomin-xiushan`）；䍶䍶（泰戱）（`beast-beishan-dongdong-taixi`）；槖駝（饒山）（`beast-beishan-tuotuo-raoshan`）；鶹歷（饒山）（`beast-beishan-liuli-raoshan`）；師魚（饒山）（`beast-beishan-shiyu-raoshan`）；獂（乾山）（`beast-beishan-yuan-ganshan`）；羆（倫山麋状兽）（`beast-beishan-pi-lunshan`）；蒲夷之魚（碣石）（`beast-beishan-puyi-jieshi`）；赤首白身大蛇（末段）（`beast-beishan-redhead-snake-mufeng`）；北山经山列（`place-north-ranges`）；發鳩之山（`place-fajiu`）；机木（`plant-beishan-ji-danhu`）；華草（單狐）（`plant-beishan-huacao-danhu`）；漨水（單狐）（`water-beishan-feng-danhu`）；泑水（北山经）（`water-beishan-you-danhu`）；芘石（單狐水文）（`material-beishan-pishi-danhu`）；文石（單狐水文）（`material-beishan-wenshi-danhu`）；铜（求如）（`material-beishan-copper-qiuru`）；玉（求如）（`material-beishan-jade-qiuru`）；滑水（求如）（`water-beishan-hua-qiuru`）；諸毗之水（北山经）（`water-beishan-zhupi-qiuru`）；玉（帶山）（`material-beishan-jade-daishan`）；青碧（帶山）（`material-beishan-qingbi-daishan`）；彭水（帶山）（`water-beishan-peng-daishan`）；芘湖之水（帶山）（`water-beishan-pihu-daishan`）；譙水（譙明）（`water-beishan-qiao-qiaoming`）；青雄黄（譙明）（`material-beishan-qingxionghuang-qiaoming`）；囂水（涿光）（`water-beishan-xiao-zhuoguang`）；松（涿光）（`plant-beishan-pine-zhuoguang`）；栢（涿光）（`plant-beishan-bai-zhuoguang`）；㯶（涿光）（`plant-beishan-zong-zhuoguang`）；橿（涿光）（`plant-beishan-jiang-zhuoguang`）；漆（虢山）（`plant-beishan-qi-guoshan`）；桐（虢山）（`plant-beishan-tong-guoshan`）；椐（虢山）（`plant-beishan-ju-guoshan`）；玉（虢山）（`material-beishan-jade-guoshan`）；铁（虢山）（`material-beishan-iron-guoshan`）；伊水（虢山）（`water-beishan-yi-guoshan`）；玉（虢山之尾）（`material-beishan-jade-guowei`）；魚水（虢山之尾）（`water-beishan-yu-guowei`）；文貝（虢山之尾）（`material-beishan-wenbei-guowei`）；樗（丹熏）（`plant-beishan-chu-danxun`）；柏（丹熏）（`plant-beishan-bai-danxun`）；韭（丹熏）（`plant-beishan-jiu-danxun`）；薤（丹熏）（`plant-beishan-xie-danxun`）；丹雘（丹熏）（`material-beishan-danhuo-danxun`）；熏水（丹熏）（`water-beishan-xun-danxun`）；棠水（丹熏）（`water-beishan-tang-danxun`）；瑶碧（石者）（`material-beishan-yaobi-shizhe`）；泚水（石者）（`water-beishan-ci-shizhe`）；葱（邊春）（`plant-beishan-cong-bianchun`）；葵（邊春）（`plant-beishan-kui-bianchun`）；韭（邊春）（`plant-beishan-jiu-bianchun`）；桃（邊春）（`plant-beishan-tao-bianchun`）；李（邊春）（`plant-beishan-li-bianchun`）；杠水（北山经）（`water-beishan-gang`）；泑澤（北山经）（`water-beishan-youze`）；櫟水（單張）（`water-beishan-li-danzhang`）；樗（灌題）（`plant-beishan-chu-guanti`）；柘（灌題）（`plant-beishan-zhe-guanti`）；流沙（灌題）（`material-beishan-sand-guanti`）；砥（灌題）（`material-beishan-whetstone-guanti`）；匠韓之水（`water-beishan-jianghan-guanti`）；磁石（灌題水文）（`material-beishan-magnetic-guanti`）；松（潘侯）（`plant-beishan-pine-panhou`）；栢（潘侯）（`plant-beishan-bai-panhou`）；榛（潘侯）（`plant-beishan-zhen-panhou`）；楛（潘侯）（`plant-beishan-hu-panhou`）；玉（潘侯）（`material-beishan-jade-panhou`）；铁（潘侯）（`material-beishan-iron-panhou`）；邊水（潘侯）（`water-beishan-bian-panhou`）；櫟澤（潘侯）（`water-beishan-lize-panhou`）；玉（大咸）（`material-beishan-jade-daxian`）；㯶（敦薨）（`plant-beishan-zong-dunhong`）；柟（敦薨）（`plant-beishan-nan-dunhong`）；茈草（敦薨）（`plant-beishan-zicao-dunhong`）；敦薨之水（`water-beishan-dunhong`）；青碧（少咸）（`material-beishan-qingbi-shaoxian`）；敦水（少咸）（`water-beishan-dun-shaoxian`）；鴈門之水（`water-beishan-yanmen-shaoxian`）；瀤澤之水（`water-beishan-huaize-yufa`）；㤗澤（北山经）（`water-beishan-taize`）；枳（北嶽）（`plant-beishan-zhi-beiyue`）；𣗥（北嶽）（`plant-beishan-ji-beiyue`）；刚木（北嶽）（`plant-beishan-gang-beiyue`）；諸懐之水（`water-beishan-zhuhuai-beiyue`）；囂水（北嶽—渾夕）（`water-beishan-xiao-beiyue-hunxi`）；铜（渾夕）（`material-beishan-copper-hunxi`）；玉（渾夕）（`material-beishan-jade-hunxi`）；海（渾夕水文）（`water-beishan-sea-hunxi`）；葱（北單）（`plant-beishan-cong-beidan`）；韭（北單）（`plant-beishan-jiu-beidan`）；鮮水（`water-beishan-xian-beixian`）；涂吾之水（`water-beishan-tuwu-beixian`）；隄水（`water-beishan-di-dishan`）；玉（管涔）（`material-beishan-jade-guancen`）；汾水（管涔）（`water-beishan-fen-guancen`）；玉（少陽）（`material-beishan-jade-shaoyang`）；赤銀（`material-beishan-red-silver-shaoyang`）；酸水（`water-beishan-suan-shaoyang`）；羙赭（少陽）（`material-beishan-ochre-shaoyang`）；玉（縣雍）（`material-beishan-jade-xianyong`）；铜（縣雍）（`material-beishan-copper-xianyong`）；晉水（`water-beishan-jin-xianyong`）；青碧（狐岐）（`material-beishan-qingbi-huqi`）；勝水（`water-beishan-sheng-huqi`）；蒼玉（狐岐）（`material-beishan-dark-jade-huqi`）；鮪水（`water-beishan-wei-baisha`）；白玉（白沙）（`material-beishan-white-jade-baisha`）；狂水（`water-beishan-kuang`）；浮水（狂山）（`water-beishan-fu-kuang`）；羙玉（狂山）（`material-beishan-fine-jade-kuang`）；铜（諸餘）（`material-beishan-copper-zhuyu`）；玉（諸餘）（`material-beishan-jade-zhuyu`）；松（諸餘）（`plant-beishan-pine-zhuyu`）；栢（諸餘）（`plant-beishan-bai-zhuyu`）；諸餘之水（`water-beishan-zhuyu`）；旄水（諸餘—敦頭）（`water-beishan-mao`）；金（敦頭）（`material-beishan-gold-duntou`）；玉（敦頭）（`material-beishan-jade-duntou`）；印澤（`water-beishan-yinze-duntou`）；玉（鉤吾）（`material-beishan-jade-gouwu`）；铜（鉤吾）（`material-beishan-copper-gouwu`）；碧（北囂）（`material-beishan-bi-beixiao`）；玉（北囂）（`material-beishan-jade-beixiao`）；涔水（北囂）（`water-beishan-cen-beixiao`）；卭澤（`water-beishan-qiongze-beixiao`）；金（梁渠）（`material-beishan-gold-liangqu`）；玉（梁渠）（`material-beishan-jade-liangqu`）；脩水（梁渠）（`water-beishan-xiu-liangqu`）；鴈門（梁渠水名）（`water-beishan-yanmen-liangqu`）；玉（湖灌）（`material-beishan-jade-huguan`）；碧（湖灌）（`material-beishan-bi-huguan`）；湖灌之水（`water-beishan-huguan`）；海（湖灌）（`water-beishan-sea-huguan`）；赤理无名木（湖灌）（`plant-beishan-redgrain-huguan`）；金（洹山）（`material-beishan-gold-huan`）；玉（洹山）（`material-beishan-jade-huan`）；三桑（洹山）（`plant-beishan-sansang-huan`）；百果树（洹山）（`plant-beishan-fruit-trees-huan`）；金（敦題）（`material-beishan-gold-dunti`）；玉（敦題）（`material-beishan-jade-dunti`）；北海（敦題）（`water-beishan-north-sea-dunti`）；金（歸山）（`material-beishan-gold-guishan`）；玉（歸山）（`material-beishan-jade-guishan`）；碧（歸山）（`material-beishan-bi-guishan`）；金（龍侯）（`material-beishan-gold-longhou`）；玉（龍侯）（`material-beishan-jade-longhou`）；决决之水（`water-beishan-juejue-longhou`）；文石（馬成）（`material-beishan-wenstone-macheng`）；金（馬成）（`material-beishan-gold-macheng`）；玉（馬成）（`material-beishan-jade-macheng`）；玉（咸山）（`material-beishan-jade-xianshan`）；铜（咸山）（`material-beishan-copper-xianshan`）；條菅之水（`water-beishan-tiaojian-xianshan`）；長澤（咸山）（`water-beishan-changze-xianshan`）；松（咸山）（`plant-beishan-pine-xianshan`）；栢（咸山）（`plant-beishan-bai-xianshan`）；茈草（咸山）（`plant-beishan-zi-xianshan`）；噐酸（未详物产）（`material-beishan-qisuan-xianshan`）；文石（天池）（`material-beishan-wenstone-tianchi`）；黄堊（天池）（`material-beishan-yellow-e-tianchi`）；澠水（天池）（`water-beishan-sheng-tianchi`）；玉（陽山）（`material-beishan-jade-yangshan`）；金（陽山）（`material-beishan-gold-yangshan`）；铜（陽山）（`material-beishan-copper-yangshan`）；留水（`water-beishan-liu-yangshan`）；蒼玉（賁聞）（`material-beishan-dark-jade-benwen`）；黄堊（賁聞）（`material-beishan-yellow-e-benwen`）；𣵀石（賁聞）（`material-beishan-nie-stone-benwen`）；石（王屋）（`material-beishan-stones-wangwu`）；㶌水（王屋）（`water-beishan-lian-wangwu`）；玉（教山）（`material-beishan-jade-jiaoshan`）；金（發丸）（`material-beishan-gold-fawan`）；玉（發丸）（`material-beishan-jade-fawan`）；教水（乾河）（`water-beishan-jiao-jiaoshan`）；赭（景山）（`material-beishan-ochre-jingshan`）；玉（景山）（`material-beishan-jade-jingshan`）；𬐱販之澤（景山南望）（`water-beishan-yanfan-jingshan`）；少澤（景山北望）（`water-beishan-shaoze-jingshan`）；藷藇（景山）（`plant-beishan-zhuyu-jingshan`）；秦椒（景山）（`plant-beishan-qinjiao-jingshan`）；蒼玉（孟門）（`material-beishan-dark-jade-mengmen`）；金（孟門）（`material-beishan-gold-mengmen`）；黄堊（孟門）（`material-beishan-yellow-e-mengmen`）；𣵀石（孟門）（`material-beishan-nie-mengmen`）；羙玉（平山）（`material-beishan-fine-jade-pingshan`）；平水（`water-beishan-ping-pingshan`）；羙玉（京山）（`material-beishan-fine-jade-jingshan-east`）；赤铜（京山）（`material-beishan-red-copper-jingshan-east`）；𤣥䃤（京山黑砥）（`material-beishan-xuansu-jingshan-east`）；漆木（京山）（`plant-beishan-lacquer-jingshan-east`）；竹（京山）（`plant-beishan-bamboo-jingshan-east`）；髙水（京山）（`water-beishan-gao-jingshan-east`）；金（虫尾）（`material-beishan-gold-chongwei`）；玉（虫尾）（`material-beishan-jade-chongwei`）；青碧（虫尾）（`material-beishan-qingbi-chongwei`）；竹（虫尾）（`plant-beishan-bamboo-chongwei`）；丹水（虫尾）（`water-beishan-dan-chongwei`）；薄水（虫尾）（`water-beishan-bo-chongwei`）；黄澤（虫尾、小侯）（`water-beishan-huangze-chongwei`）；金（彭毗）（`material-beishan-gold-pengpi`）；玉（彭毗）（`material-beishan-jade-pengpi`）；蚤林之水（`water-beishan-zaolin-pengpi`）；肥水（彭毗）（`water-beishan-fei-pengpi`）；牀水（肥水所注）（`water-beishan-chuang-pengpi`）；明漳之水（`water-beishan-mingzhang-xiaohou`）；金（泰頭）（`material-beishan-gold-taitou`）；玉（泰頭）（`material-beishan-jade-taitou`）；竹箭（泰頭）（`plant-beishan-arrow-bamboo-taitou`）；共水（泰頭）（`water-beishan-gong-taitou`）；虖池／虖沱（北山经文本索引）（`water-beishan-huchi-taitou`）；铜（軒轅）（`material-beishan-copper-xuanyuan`）；竹（軒轅）（`plant-beishan-bamboo-xuanyuan`）；金（謁戾）（`material-beishan-gold-yeli`）；玉（謁戾）（`material-beishan-jade-yeli`）；松（謁戾）（`plant-beishan-pine-yeli`）；栢（謁戾）（`plant-beishan-bai-yeli`）；沁水（謁戾、泰戱文本索引）（`water-beishan-qin-yeli`）；丹林之水（`water-beishan-danlin-yeli`）；嬰侯之水（`water-beishan-yinghou-yeli`）；汜水（嬰侯所注）（`water-beishan-fan-yeli`）；金（沮洳）（`material-beishan-gold-juru`）；玉（沮洳）（`material-beishan-jade-juru`）；濝水（沮洳）（`water-beishan-qi-juru`）；文石（神囷）（`material-beishan-wenstone-shenqun`）；黄水（神囷）（`water-beishan-huang-shenqun`）；洹水（黄水所注）（`water-beishan-huan-shenqun`）；滏水（神囷、錫山）（`water-beishan-fu-shenqun`）；歐水（滏水所注）（`water-beishan-ou-shenqun`）；柘木（發鳩）（`plant-beishan-zhe-fajiu`）；東海（精衛叙事）（`water-beishan-donghai-fajiu`）；漳水、濁漳（發鳩、少山）（`water-beishan-zhang-fajiu`）；木（精衛所衔）（`material-beishan-wood-fajiu`）；石（精衛所衔）（`material-beishan-stones-fajiu`）；金（少山）（`material-beishan-gold-shaoshan`）；玉（少山）（`material-beishan-jade-shaoshan`）；铜（少山）（`material-beishan-copper-shaoshan`）；清漳之水（`water-beishan-qingzhang-shaoshan`）；玉（錫山）（`material-beishan-jade-xishan-north`）；砥（錫山）（`material-beishan-whetstone-xishan-north`）；牛首之水（錫山）（`water-beishan-niushou-xishan-north`）；羙玉（錫山北景山）（`material-beishan-fine-jade-jingshan-after-xi`）；景水（錫山北景山）（`water-beishan-jing-after-xi`）；海澤（景水所注）（`water-beishan-haize-jingshan-after-xi`）；玉（題首）（`material-beishan-jade-tishou`）；石（題首）（`material-beishan-stones-tishou`）；玉（繡山）（`material-beishan-jade-xiushan`）；青碧（繡山）（`material-beishan-qingbi-xiushan`）；栒（繡山木）（`plant-beishan-xun-xiushan`）；芍藥（繡山）（`plant-beishan-shaoyao-xiushan`）；芎窮（繡山）（`plant-beishan-qiongqiong-xiushan`）；洧水（繡山、柘山文本索引）（`water-beishan-wei-xiushan`）；陽水（松山）（`water-beishan-yang-songshan`）；金（敦與）（`material-beishan-gold-dunyu`）；玉（敦與）（`material-beishan-jade-dunyu`）；溹水（敦與）（`water-beishan-suo-dunyu`）；泰陸之水（`water-beishan-tailu-dunyu`）；泜水（敦與）（`water-beishan-zhi-dunyu`）；彭水（敦與受水名）（`water-beishan-peng-dunyu`）；槐水（敦與）（`water-beishan-huai-dunyu`）；泜澤（槐水所注）（`water-beishan-zhize-dunyu`）；金（柘山）（`material-beishan-gold-zheshan`）；玉（柘山）（`material-beishan-jade-zheshan`）；铁（柘山）（`material-beishan-iron-zheshan`）；歷聚之水（`water-beishan-liju-zheshan`）；碧玉（維龍）（`material-beishan-green-jade-weilong`）；金（維龍）（`material-beishan-gold-weilong`）；铁（維龍）（`material-beishan-iron-weilong`）；肥水（維龍）（`water-beishan-fei-weilong`）；皐澤（維龍）（`water-beishan-gaoze-weilong`）；敞鐡之水（`water-beishan-changtie-weilong`）；大澤（敞鐡所注）（`water-beishan-daze-weilong`）；礨石（維龍）（`material-beishan-leishi-weilong`）；石玉（白馬）（`material-beishan-shiyu-baima`）；鐡（白馬）（`material-beishan-iron-baima`）；赤铜（白馬）（`material-beishan-red-copper-baima`）；木馬之水（`water-beishan-muma-baima`）；空桑之水（北山经）（`water-beishan-kongsang-north`）；金（泰戱）（`material-beishan-gold-taixi`）；玉（泰戱）（`material-beishan-jade-taixi`）；漊水（泰戱所注）（`water-beishan-lou-taixi`）；液女之水（`water-beishan-yenu-taixi`）；金（石山）（`material-beishan-gold-shishan`）；玉（石山）（`material-beishan-jade-shishan`）；濩濩之水（`water-beishan-huohuo-shishan`）；鮮于之水（石山）（`water-beishan-xianyu-shishan`）；皐涂之水（`water-beishan-gaotu-tongrong`）；漊液水（童戎受水名）（`water-beishan-louye-tongrong`）；㯶（髙是木）（`plant-beishan-zong-gaoshi`）；條草（髙是）（`plant-beishan-tiao-gaoshi`）；滋水（髙是）（`water-beishan-zi-gaoshi`）；𣸦水（髙是）（`water-beishan-kou-gaoshi`）；羙玉（陸山）（`material-beishan-fine-jade-lushan`）；𨜰水（陸山）（`water-beishan-tan-lushan`）；般水（沂山）（`water-beishan-ban-yishan`）；嬰石（燕山）（`material-beishan-yingstone-yanshan`）；燕水（燕山）（`water-beishan-yan-yanshan`）；瑶碧（饒山）（`material-beishan-yaobi-raoshan`）；歷虢之水（`water-beishan-liguo-raoshan`）；金（乾山）（`material-beishan-gold-ganshan`）；玉（乾山）（`material-beishan-jade-ganshan`）；鐡（乾山）（`material-beishan-iron-ganshan`）；倫水（`water-beishan-lun-lunshan`）；玉（碣石）（`material-beishan-jade-jieshi`）；青碧（碣石）（`material-beishan-qingbi-jieshi`）；繩水（碣石）（`water-beishan-sheng-jieshi`）；玉（帝都）（`material-beishan-jade-didu`）；金（帝都）（`material-beishan-gold-didu`）；泰澤（帝都水行）（`water-beishan-taize-didu`）；浴水（幽都相邻记述）（`water-beishan-yu-youdu-mufeng`）；河（北山经）（`water-beishan-he`）；單狐之山（`passage-beishan-danhu`）；求如之山（`passage-beishan-qiuru`）；帶山（`passage-beishan-daishan`）；譙明之山（`passage-beishan-qiaoming`）；涿光之山（`passage-beishan-zhuoguang`）；虢山（`passage-beishan-guoshan`）；虢山之尾（`passage-beishan-guowei`）；丹熏之山（`passage-beishan-danxun`）；石者之山（`passage-beishan-shizhe`）；邊春之山（`passage-beishan-bianchun`）；蔓聮之山（`passage-beishan-manlian`）；單張之山（`passage-beishan-danzhang`）；灌題之山（`passage-beishan-guanti`）；潘侯之山（`passage-beishan-panhou`）；小咸之山（`passage-beishan-xiaoxian`）；大咸之山（`passage-beishan-daxian`）；敦薨之山（`passage-beishan-dunhong`）；少咸之山（`passage-beishan-shaoxian`）；獄法之山（`passage-beishan-yufa`）；北嶽之山（`passage-beishan-beiyue`）；渾夕之山（`passage-beishan-hunxi`）；北單之山（`passage-beishan-beidan`）；羆差之山（`passage-beishan-bicha`）；北鮮之山（`passage-beishan-beixian`）；隄山（`passage-beishan-dishan`）；北山经首列总括与祭礼（`passage-beishan-range1-summary`）；管涔之山（`passage-beishan-guancen`）；少陽之山（`passage-beishan-shaoyang`）；縣雍之山（`passage-beishan-xianyong`）；狐岐之山（`passage-beishan-huqi`）；白沙山（`passage-beishan-baisha`）；爾是之山（`passage-beishan-ershi`）；狂山（`passage-beishan-kuang`）；諸餘之山（`passage-beishan-zhuyu`）；敦頭之山（`passage-beishan-duntou`）；鉤吾之山（`passage-beishan-gouwu`）；北囂之山（`passage-beishan-beixiao`）；梁渠之山（`passage-beishan-liangqu`）；姑灌之山（`passage-beishan-guguan`）；湖灌之山（`passage-beishan-huguan`）；洹山（`passage-beishan-huan`）；敦題之山（`passage-beishan-dunti`）；北次二经总括与祭礼（`passage-beishan-range2-summary`）；太行之山（`passage-beishan-taihang`）；龍侯之山（`passage-beishan-longhou`）；馬成之山（`passage-beishan-macheng`）；咸山（`passage-beishan-xianshan`）；天池之山（`passage-beishan-tianchi`）；陽山（`passage-beishan-yangshan`）；賁聞之山（`passage-beishan-benwen`）；王屋之山（`passage-beishan-wangwu`）；教山（`passage-beishan-jiaoshan`）；景山（`passage-beishan-jingshan`）；孟門之山（`passage-beishan-mengmen`）；平山（`passage-beishan-pingshan`）；京山（`passage-beishan-jingshan-east`）；虫尾之山（`passage-beishan-chongwei`）；彭毗之山（`passage-beishan-pengpi`）；小侯之山（`passage-beishan-xiaohou`）；泰頭之山（`passage-beishan-taitou`）；軒轅之山（`passage-beishan-xuanyuan`）；謁戾之山（`passage-beishan-yeli`）；沮洳之山（`passage-beishan-juru`）；神囷之山（`passage-beishan-shenqun`）；發鳩之山（`passage-beishan-fajiu`）；少山（`passage-beishan-shaoshan`）；錫山（`passage-beishan-xishan-north`）；景山（錫山北）（`passage-beishan-jingshan-after-xi`）；題首之山（`passage-beishan-tishou`）；繡山（`passage-beishan-xiushan`）；松山（`passage-beishan-songshan`）；敦與之山（`passage-beishan-dunyu`）；柘山（`passage-beishan-zheshan`）；維龍之山（`passage-beishan-weilong`）；白馬之山（`passage-beishan-baima`）；空桑之山（北山经）（`passage-beishan-kongsang-north`）；泰戱之山（`passage-beishan-taixi`）；石山（`passage-beishan-shishan`）；童戎之山（`passage-beishan-tongrong`）；髙是之山（`passage-beishan-gaoshi`）；陸山（`passage-beishan-lushan`）；沂山（`passage-beishan-yishan`）；燕山（`passage-beishan-yanshan`）；饒山（`passage-beishan-raoshan`）；乾山（`passage-beishan-ganshan`）；倫山（`passage-beishan-lunshan`）；碣石之山（`passage-beishan-jieshi`）；鴈門之山（北水行）（`passage-beishan-yanmenshan`）；泰澤水行與帝都之山（`passage-beishan-taize-didu`）；錞于母逢之山（`passage-beishan-mufeng`）；北次三经总括与祭礼（`passage-beishan-range3-summary`）；北山经篇末总计与数字核对（`passage-beishan-book-total`）；單狐之山（`place-beishan-danhu`）；求如之山（`place-beishan-qiuru`）；諸毗山（北山郭注）（`place-beishan-zhupi-qiuru`）；帶山（`place-beishan-daishan`）；譙明之山（`place-beishan-qiaoming`）；涿光之山（`place-beishan-zhuoguang`）；虢山（`place-beishan-guoshan`）；虢山之尾（`place-beishan-guowei`）；丹熏之山（`place-beishan-danxun`）；石者之山（`place-beishan-shizhe`）；邊春之山（`place-beishan-bianchun`）；蔓聮之山（`place-beishan-manlian`）；單張之山（`place-beishan-danzhang`）；灌題之山（`place-beishan-guanti`）；潘侯之山（`place-beishan-panhou`）；小咸之山（`place-beishan-xiaoxian`）；大咸之山（`place-beishan-daxian`）；敦薨之山（`place-beishan-dunhong`）；崑崙（敦薨水文）（`place-beishan-kunlun-dunhong`）；少咸之山（`place-beishan-shaoxian`）；鴈門山（郭注）（`place-beishan-yanmen-shaoxian`）；獄法之山（`place-beishan-yufa`）；北嶽之山（`place-beishan-beiyue`）；渾夕之山（`place-beishan-hunxi`）；北單之山（`place-beishan-beidan`）；羆差之山（`place-beishan-bicha`）；北鮮之山（`place-beishan-beixian`）；隄山（`place-beishan-dishan`）；北山经首列总括与祭礼（`rite-beishan-range1-summary`）；首列山神（人面蛇身）（`deity-beishan-human-serpent-range1-summary`）；首列牲祭与瘗埋（`rite-beishan-offerings-range1-summary`）；珪（首列祭玉）（`rite-beishan-gui-range1-summary`）；山北生食记述（`rite-beishan-raw-food-range1-summary`）；管涔之山（`place-beishan-guancen`）；少陽之山（`place-beishan-shaoyang`）；縣雍之山（`place-beishan-xianyong`）；狐岐之山（`place-beishan-huqi`）；白沙山（`place-beishan-baisha`）；爾是之山（`place-beishan-ershi`）；狂山（`place-beishan-kuang`）；諸餘之山（`place-beishan-zhuyu`）；敦頭之山（`place-beishan-duntou`）；鉤吾之山（`place-beishan-gouwu`）；北囂之山（`place-beishan-beixiao`）；梁渠之山（`place-beishan-liangqu`）；姑灌之山（`place-beishan-guguan`）；湖灌之山（`place-beishan-huguan`）；洹山（`place-beishan-huan`）；流沙（洹山行程）（`place-beishan-liusha-huan`）；敦題之山（`place-beishan-dunti`）；北次二经总括与祭礼（`rite-beishan-range2-summary`）；次二山神（蛇身人面）（`deity-beishan-human-serpent-range2-summary`）；次二牲祭瘗埋（`rite-beishan-animal-burial-range2`）；次二投玉不糈（`rite-beishan-jade-casting-range2`）；璧（次二祭玉）（`rite-beishan-bi-range2`）；珪（次二祭玉）（`rite-beishan-gui-range2`）；太行之山（`place-beishan-taihang`）；歸山（太行之首）（`place-beishan-guishan`）；龍侯之山（`place-beishan-longhou`）；馬成之山（`place-beishan-macheng`）；咸山（`place-beishan-xianshan`）；天池之山（`place-beishan-tianchi`）；陽山（`place-beishan-yangshan`）；賁聞之山（`place-beishan-benwen`）；王屋之山（`place-beishan-wangwu`）；教山（`place-beishan-jiaoshan`）；發丸之山（两山记述）（`place-beishan-fawan`）；景山（`place-beishan-jingshan`）；孟門之山（`place-beishan-mengmen`）；平山（`place-beishan-pingshan`）；京山（`place-beishan-jingshan-east`）；虫尾之山（`place-beishan-chongwei`）；彭毗之山（`place-beishan-pengpi`）；小侯之山（`place-beishan-xiaohou`）；泰頭之山（`place-beishan-taitou`）；軒轅之山（`place-beishan-xuanyuan`）；謁戾之山（`place-beishan-yeli`）；丹林（謁戾东林）（`place-beishan-danlin-forest-yeli`）；沮洳之山（`place-beishan-juru`）；神囷之山（`place-beishan-shenqun`）；西山（精衛取材叙事）（`place-beishan-western-mountains-fajiu`）；少山（`place-beishan-shaoshan`）；錫山（`place-beishan-xishan-north`）；景山（錫山北）（`place-beishan-jingshan-after-xi`）；題首之山（`place-beishan-tishou`）；繡山（`place-beishan-xiushan`）；松山（`place-beishan-songshan`）；敦與之山（`place-beishan-dunyu`）；柘山（`place-beishan-zheshan`）；維龍之山（`place-beishan-weilong`）；白馬之山（`place-beishan-baima`）；空桑之山（北山经）（`place-beishan-kongsang-north`）；泰戱之山（`place-beishan-taixi`）；石山（`place-beishan-shishan`）；童戎之山（`place-beishan-tongrong`）；髙是之山（`place-beishan-gaoshi`）；陸山（`place-beishan-lushan`）；沂山（`place-beishan-yishan`）；燕山（`place-beishan-yanshan`）；饒山（`place-beishan-raoshan`）；乾山（`place-beishan-ganshan`）；倫山（`place-beishan-lunshan`）；碣石之山（`place-beishan-jieshi`）；鴈門之山（北水行）（`place-beishan-yanmenshan`）；泰澤水行與帝都之山（`place-beishan-taize-didu`）；帝都之山（泰澤中）（`place-beishan-didu`）；錞于母逢之山（`place-beishan-mufeng`）；鷄號之山（北望）（`place-beishan-jihao-mufeng`）；幽都之山（西望）（`place-beishan-youdu-mufeng`）；如䬅之风（末段）（`wind-beishan-li-mufeng`）；北次三经总括与祭礼（`rite-beishan-range3-summary`）；次三二十神（馬身人面）（`deity-beishan-horse-human-range3`）；次三十四神（彘身載玉）（`deity-beishan-pig-jade-range3`）；次三十神（彘身八足蛇尾）（`deity-beishan-pig-eight-snake-range3`）；次三馬身神藻茝瘗礼（`rite-beishan-zaozhi-burial-range3`）；次三載玉神祭玉不瘗（`rite-beishan-jade-not-buried-range3`）；次三八足神一璧瘗礼（`rite-beishan-bi-burial-range3`）；次三四十四神稌糈与不火食（`rite-beishan-grain-no-fire-range3`）；藻（次三祭物）（`plant-beishan-zao-range3`）；茝（次三祭物）（`plant-beishan-zhi-range3`）；稌（次三祭米）（`plant-beishan-tu-range3`）；玉（次三神所載）（`material-beishan-jade-carried-range3`）；璧（次三瘗礼）（`rite-beishan-bi-range3`）；糈米（次三祭物）（`material-beishan-rice-range3`）；北山经篇末总计与数字核对（`rite-beishan-book-total`）；八十七山（北经原报总数）（`rite-beishan-mountains-book-total`）；二萬三千二百三十里（原报总程）（`rite-beishan-distance-book-total`）；精卫填海（`03-04`）。
- 待补方向：全篇92阅读段、507张独立卡已核，對照76—108页影印。北山57幅新图已审，諸犍与精衛复用旧图；26个形貌不足对象留占位。297录文块含1标题与296正文/注文块，全部映射到阅读段。三列原报山数合88、里程23530，与篇末87山、23230里分别保留；列名阅读山段25/16/47与原报25/17/46分开，不补删凑数。独立实体仍为项目整理，不宣称多版本逐字校勘或全书完成。
- 校核入口：[该篇固定修订](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E4%B8%89&oldid=2652853)；北山经全篇92阅读段已核76—108页，数字差异与形貌不足占位保留，详见data/beishan-edition-review.json。

- 單狐至篇末source-03-0002—0297已对照76—108页，32处实际页界另存、9处缺字图恢复保留捕获。次三总括0290—0296与篇末0297独立；錞于母逢与总括無逢写法分别保留，未统一改字。

### 04 东山经

- 常规入口：鱅鱅之魚（`beast-dongshan-yongyong-suzhu`）；活師（藟山）（`beast-dongshan-huoshi-leishan`）；從從（`beast-dongshan-congcong-xunzhuang`）；䖪䑕（`beast-dongshan-zishu-xunzhuang`）；箴魚（栒状）（`beast-dongshan-zhen-xunzhuang`）；鱤魚（番條）（`beast-dongshan-gan-fantiao`）；堪㐨之魚（`beast-dongshan-kanyu-chai`）；夸父状彘毛兽（犲山未名）（`beast-dongshan-kuafu-like-chai`）；䖺䗤（`beast-dongshan-tiaoyong-dushan`）；狪狪（`beast-dongshan-tongtong-taishan`）；茈羸（竹山）（`beast-dongshan-zilei-zhu`）；軨軨（东次二）（`beast-dongshan-lingling-kongsang-east`）；蜃（嶧皐）（`beast-dongshan-shen-yigao`）；珧（嶧皐）（`beast-dongshan-yao-yigao`）；珠蟞魚（葛山之首）（`beast-dongshan-zhubie-geshan-head`）；犰狳（餘峩）（`beast-dongshan-qiuyu-yue`）；大蛇（东山文本索引）（`beast-dongshan-large-snake`）；朱獳（`beast-dongshan-zhunou-gengshan`）；𪁐鶘（盧其）（`beast-dongshan-lihu-luqi`）；獙獙（姑逢）（`beast-dongshan-bibi-gufeng`）；蠪姪（`beast-dongshan-longzhi-fuli`）；峳峳（`beast-dongshan-youyou-zhenshan`）；絜鈎（`beast-dongshan-jiegou-zhenshan`）；妴胡（`beast-dongshan-yuanhu-shihu`）；𥧌魚（諸鈎）（`beast-dongshan-qin-zhugou`）；鱣（孟子）（`beast-dongshan-zhan-mengzi`）；鮪（孟子）（`beast-dongshan-wei-mengzi`）；蠵龜（深澤）（`beast-dongshan-xigui-qizhong`）；鮯鮯之魚（`beast-dongshan-gege-qizhong`）；精精（踇隅）（`beast-dongshan-jingjing-muyu`）；猲狙（`beast-dongshan-xieju-beihao`）；鬿雀（`beast-dongshan-qique-beihao`）；鱃魚（东山文本索引）（`beast-dongshan-qiu-maoshan`）；茈魚（東始）（`beast-dongshan-zi-dongshi`）；薄魚（女烝）（`beast-dongshan-bo-nvzheng`）；当康（`beast-dangkang`）；䱻魚（子桐）（`beast-dongshan-hua-zitong`）；合窳（`beast-heyu`）；蜚（`beast-fei`）；东山经山列（`place-east-ranges`）；食水（东山文本索引）（`water-dongshan-shi`）；海（东山水文文本索引）（`water-dongshan-sea`）；玉（藟山）（`material-dongshan-jade-leishan`）；金（藟山）（`material-dongshan-gold-leishan`）；湖水（藟山、栒状文本索引）（`water-dongshan-hu`）；金（栒状）（`material-dongshan-gold-xunzhuang`）；玉（栒状）（`material-dongshan-jade-xunzhuang`）；青碧石（栒状）（`material-dongshan-qingbistone-xunzhuang`）；𣲵水（栒状）（`water-dongshan-zhi-xunzhuang`）；沙（番條）（`material-dongshan-sand-fantiao`）；減水（番條）（`water-dongshan-jian-fantiao`）；漆（姑兒）（`plant-dongshan-qi-guer`）；桑（姑兒）（`plant-dongshan-sang-guer`）；柘（姑兒）（`plant-dongshan-zhe-guer`）；姑兒之水（`water-dongshan-guer`）；玉（髙氏山上）（`material-dongshan-jade-gaoshi-east`）；金（諸繩水文）（`material-dongshan-gold-zhusheng`）；玉（諸繩水文）（`material-dongshan-jade-zhusheng`）；諸繩之水（`water-dongshan-zhusheng`）；澤（髙氏受水体）（`water-dongshan-ze-gaoshi`）；箴石（髙氏）（`material-dongshan-zhenstone-gaoshi`）；桑（嶽山）（`plant-dongshan-sang-yue`）；樗（嶽山）（`plant-dongshan-chu-yue`）；金（濼水文）（`material-dongshan-gold-luo`）；玉（濼水文）（`material-dongshan-jade-luo`）；濼水（`water-dongshan-luo`）；澤（嶽山受水体）（`water-dongshan-ze-yue`）；水（犲山下）（`water-dongshan-unnamed-chai`）；金（獨山）（`material-dongshan-gold-du`）；玉（獨山）（`material-dongshan-jade-du`）；羙石（獨山）（`material-dongshan-fine-stone-du`）；末塗之水（`water-dongshan-motu`）；沔（末塗受水体）（`water-dongshan-mian`）；玉（泰山）（`material-dongshan-jade-tai`）；金（泰山）（`material-dongshan-gold-tai`）；水玉（環水文）（`material-dongshan-water-jade-huan`）；環水（`water-dongshan-huan`）；江（泰山、竹山文本索引）（`water-dongshan-jiang`）；瑶碧（竹山）（`material-dongshan-yaobi-zhu`）；激水（竹山）（`water-dongshan-ji-zhu`）；娶檀之水（`water-dongshan-qutan`）；湣澤（`water-dongshan-min-marsh`）；榖（曹夕）（`plant-dongshan-gu-caoxi`）；金（嶧皐）（`material-dongshan-gold-yigao`）；玉（嶧皐）（`material-dongshan-jade-yigao`）；白堊（嶧皐）（`material-dongshan-white-earth-yigao`）；嶧皐之水（`water-dongshan-yigao`）；激女之水（`water-dongshan-jinv`）；砥礪（葛山之尾）（`material-dongshan-dili-geshan-tail`）；澧水（葛山之首）（`water-dongshan-li-geshan-head`）；余澤（澧水受水体）（`water-dongshan-yu-marsh`）；雜余之水（`water-dongshan-zayu`）；黄水（雜余受水体）（`water-dongshan-huang-yue`）；梓（餘峩）（`plant-dongshan-zi-yue`）；柟（餘峩）（`plant-dongshan-nan-yue`）；荆（餘峩）（`plant-dongshan-jing-yue`）；𦬊（餘峩）（`plant-dongshan-qi-yue`）；水（杜父未名）（`water-dongshan-unnamed-dufu`）；水碧（耿山）（`material-dongshan-shuibi-geng`）；沙（盧其）（`material-dongshan-sand-luqi`）；石（盧其）（`material-dongshan-stone-luqi`）；沙水（盧其）（`water-dongshan-sha-luqi`）；涔水（`water-dongshan-cen`）；水（姑射未名）（`water-dongshan-unnamed-gushe`）；石（北姑射）（`material-dongshan-stone-north-gushe`）；水（南姑射未名）（`water-dongshan-unnamed-south-gushe`）；碧（碧山）（`material-dongshan-bi-bishan`）；水玉（碧山）（`material-dongshan-water-jade-bishan`）；金（維氏）（`material-dongshan-gold-weishi`）；玉（維氏）（`material-dongshan-jade-weishi`）；原水（維氏）（`water-dongshan-yuan-weishi`）；沙澤（原水受水体）（`water-dongshan-sha-marsh`）；金（姑逢）（`material-dongshan-gold-gufeng`）；玉（姑逢）（`material-dongshan-jade-gufeng`）；金（鳬麗）（`material-dongshan-gold-fuli`）；玉（鳬麗）（`material-dongshan-jade-fuli`）；箴石（鳬麗）（`material-dongshan-zhenstone-fuli`）；䃌水（`water-dongshan-zhen`）；湖澤（䃌山东望）（`water-dongshan-hu-marsh`）；金（尸胡）（`material-dongshan-gold-shihu`）；玉（尸胡）（`material-dongshan-jade-shihu`）；𣗥（尸胡）（`plant-dongshan-ji-shihu`）；桃（岐山）（`plant-dongshan-peach-qi`）；李（岐山）（`plant-dongshan-plum-qi`）；沙（諸鈎）（`material-dongshan-sand-zhugou`）；石（諸鈎）（`material-dongshan-stone-zhugou`）；沙（中父）（`material-dongshan-sand-zhongfu`）；沙（胡射）（`material-dongshan-sand-hushe`）；石（胡射）（`material-dongshan-stone-hushe`）；梓（孟子）（`plant-dongshan-zi-mengzi`）；桐（孟子）（`plant-dongshan-tong-mengzi`）；桃（孟子）（`plant-dongshan-peach-mengzi`）；李（孟子）（`plant-dongshan-plum-mengzi`）；菌蒲（孟子）（`plant-dongshan-junpu-mengzi`）；碧陽水（孟子）（`water-dongshan-biyang`）；玉（跂踵）（`material-dongshan-jade-qizhong`）；深澤（跂踵）（`water-dongshan-shen-marsh`）；金（踇隅）（`material-dongshan-gold-muyu`）；玉（踇隅）（`material-dongshan-jade-muyu`）；赭（踇隅）（`material-dongshan-ochre-muyu`）；幼海（無皐南望）（`water-dongshan-you-sea`）；北海（北號所临）（`water-dongshan-north-sea`）；木（北號未名）（`plant-dongshan-unnamed-tree-beihao`）；蒼體之水（`water-dongshan-cangti`）；展水（`water-dongshan-zhan-water`）；蒼玉（東始）（`material-dongshan-cang-jade-dongshi`）；𦬊木（東始）（`plant-dongshan-qi-tree-dongshi`）；泚水（東始）（`water-dongshan-ci-dongshi`）；羙貝（東始水文）（`material-dongshan-fine-shell-dongshi`）；石膏水（女烝）（`water-dongshan-shigao`）；鬲水（`water-dongshan-ge-water`）；金（欽山）（`material-dongshan-gold-qinshan`）；玉（欽山）（`material-dongshan-jade-qinshan`）；師水（欽山）（`water-dongshan-shi-qinshan`）；皐澤（師水受水体）（`water-dongshan-gao-marsh`）；文貝（欽山水文）（`material-dongshan-patterned-shell-qin`）；子桐之水（`water-dongshan-zitong`）；餘如之澤（`water-dongshan-yuru-marsh`）；金（剡山）（`material-dongshan-gold-yanshan`）；玉（剡山）（`material-dongshan-jade-yanshan`）；金（太山）（`material-dongshan-gold-taishan-range4`）；玉（太山）（`material-dongshan-jade-taishan-range4`）；楨木（太山）（`plant-dongshan-zhenwood-tai4`）；鈎水（太山）（`water-dongshan-gou-tai4`）；勞水（`water-dongshan-lao-water`）；樕𧑤之山（`passage-dongshan-suzhu`）；藟山（`passage-dongshan-leishan`）；栒状之山（`passage-dongshan-xunzhuang`）；勃亝之山（`passage-dongshan-boqi`）；番條之山（`passage-dongshan-fantiao`）；姑兒之山（`passage-dongshan-guer`）；髙氏之山（`passage-dongshan-gaoshi-east`）；嶽山（`passage-dongshan-yueshan`）；犲山（`passage-dongshan-chaishan`）；獨山（`passage-dongshan-dushan`）；泰山（`passage-dongshan-taishan-range1`）；竹山（`passage-dongshan-zhushan`）；首列总括与祭礼（`passage-dongshan-range1-summary`）；空桑之山（`passage-dongshan-kongsang-east`）；曹夕之山（`passage-dongshan-caoxi`）；嶧皐之山（`passage-dongshan-yigao`）；葛山之尾（`passage-dongshan-geshan-tail`）；葛山之首（`passage-dongshan-geshan-head`）；餘峩之山（`passage-dongshan-yue`）；杜父之山（`passage-dongshan-dufu`）；耿山（`passage-dongshan-gengshan`）；盧其之山（`passage-dongshan-luqi`）；姑射之山（`passage-dongshan-gushe`）；北姑射之山（`passage-dongshan-north-gushe`）；南姑射之山（`passage-dongshan-south-gushe`）；碧山（`passage-dongshan-bishan`）；維氏之山（`passage-dongshan-weishi`）；姑逢之山（`passage-dongshan-gufeng`）；鳬麗之山（`passage-dongshan-fuli`）；䃌山（`passage-dongshan-zhenshan`）；次二总括与祭礼（`passage-dongshan-range2-summary`）；尸胡之山（`passage-dongshan-shihu`）；岐山（`passage-dongshan-qishan`）；諸鈎之山（`passage-dongshan-zhugou`）；中父之山（`passage-dongshan-zhongfu`）；胡射之山（`passage-dongshan-hushe`）；孟子之山（`passage-dongshan-mengzi`）；跂踵之山（`passage-dongshan-qizhong`）；踇隅之山（`passage-dongshan-muyu`）；無皐之山（`passage-dongshan-wugao`）；次三总括与祭礼（`passage-dongshan-range3-summary`）；北號之山（`passage-dongshan-beihao`）；旄山（`passage-dongshan-maoshan`）；東始之山（`passage-dongshan-dongshi`）；女烝之山（`passage-dongshan-nvzheng`）；欽山（`passage-dongshan-qinshan`）；子桐之山（`passage-dongshan-zitong`）；剡山（`passage-dongshan-yanshan`）；太山（`passage-dongshan-taishan-range4`）；次四总括（`passage-dongshan-range4-summary`）；东山经篇末总计（`passage-dongshan-book-total`）；樕𧑤之山（`place-dongshan-suzhu`）；乾昧之山（北临）（`place-dongshan-qianmei-suzhu`）；藟山（`place-dongshan-leishan`）；栒状之山（`place-dongshan-xunzhuang`）；勃亝之山（`place-dongshan-boqi`）；番條之山（`place-dongshan-fantiao`）；姑兒之山（`place-dongshan-guer`）；髙氏之山（`place-dongshan-gaoshi-east`）；嶽山（`place-dongshan-yueshan`）；犲山（`place-dongshan-chaishan`）；獨山（`place-dongshan-dushan`）；泰山（`place-dongshan-taishan-range1`）；竹山（`place-dongshan-zhushan`）；首列总括与祭礼（`rite-dongshan-range1-summary`）；人身龍首神（东山首列）（`deity-dongshan-human-dragon-range1`）；祠毛用一犬（首列祭礼）（`rite-dongshan-fur-offering-range1`）；祈䎶用魚（首列祭礼）（`rite-dongshan-fish-er-range1`）；空桑之山（`place-dongshan-kongsang-east`）；沮呉（空桑东望）（`place-dongshan-juwu`）；沙𨹧（空桑南望）（`place-dongshan-shaling`）；曹夕之山（`place-dongshan-caoxi`）；嶧皐之山（`place-dongshan-yigao`）；葛山之尾（`place-dongshan-geshan-tail`）；葛山之首（`place-dongshan-geshan-head`）；餘峩之山（`place-dongshan-yue`）；螽（餘峩灾异）（`animal-dongshan-zhong-yue`）；蝗（餘峩灾异）（`animal-dongshan-huang-insects-yue`）；杜父之山（`place-dongshan-dufu`）；耿山（`place-dongshan-gengshan`）；盧其之山（`place-dongshan-luqi`）；姑射之山（`place-dongshan-gushe`）；北姑射之山（`place-dongshan-north-gushe`）；南姑射之山（`place-dongshan-south-gushe`）；碧山（`place-dongshan-bishan`）；維氏之山（`place-dongshan-weishi`）；姑逢之山（`place-dongshan-gufeng`）；鳬麗之山（`place-dongshan-fuli`）；䃌山（`place-dongshan-zhenshan`）；次二总括与祭礼（`rite-dongshan-range2-summary`）；兽身人面载觡神（东次二）（`deity-dongshan-humanface-antlers-range2`）；祠毛一鷄（次二祭礼）（`rite-dongshan-chicken-range2`）；一璧瘞（次二祭礼）（`rite-dongshan-bi-burial-range2`）；尸胡之山（`place-dongshan-shihu`）；𦍙山（尸湖北望）（`place-dongshan-xiang-shihu`）；岐山（`place-dongshan-qishan`）；虎（岐山泛称）（`animal-dongshan-tiger-qi`）；諸鈎之山（`place-dongshan-zhugou`）；中父之山（`place-dongshan-zhongfu`）；胡射之山（`place-dongshan-hushe`）；孟子之山（`place-dongshan-mengzi`）；麋（孟子泛称）（`animal-dongshan-mi-mengzi`）；鹿（孟子泛称）（`animal-dongshan-lu-mengzi`）；跂踵之山（`place-dongshan-qizhong`）；踇隅之山（`place-dongshan-muyu`）；無皐之山（`place-dongshan-wugao`）；榑木（無皐东望）（`plant-dongshan-fu-wood-wugao`）；风（無皐）（`wind-dongshan-wind-wugao`）；次三总括与祭礼（`rite-dongshan-range3-summary`）；人身羊角神（东次三）（`deity-dongshan-human-ramhorn-range3`）；一牡羊（次三祭礼）（`rite-dongshan-ram-offering-range3`）；𮮐（次三祭米）（`material-dongshan-millet-range3`）；北號之山（`place-dongshan-beihao`）；旄山（`place-dongshan-maoshan`）；東始之山（`place-dongshan-dongshi`）；女烝之山（`place-dongshan-nvzheng`）；欽山（`place-dongshan-qinshan`）；子桐之山（`place-dongshan-zitong`）；剡山（`place-dongshan-yanshan`）；蟲（合窳食性泛称）（`animal-dongshan-insects-yanshan`）；蛇（合窳食性泛称）（`animal-dongshan-snakes-yanshan`）；太山（`place-dongshan-taishan-range4`）；次四总括（`rite-dongshan-range4-summary`）；东山经篇末总计（`rite-dongshan-book-total`）。
- 待补方向：已核影印109—124页段界并规划51阶段：46列名山段、4总括、1篇末；141录文块含2标题/署名与139正文/注文块，42结构候选不等于阶段数。次三列名9与原报19、四列原报合56与篇末46并存；里程合18860与篇末一致。已接入51阅读段、237独立卡，余0阶段；已审图34幅、形貌不足占位14项。食/湖/海/江与鱤鱼的不同出处分别保留。计划及15页界修正见data/dongshan-edition-review.json。
- 校核入口：[该篇固定修订](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E5%9B%9B&oldid=2652854)；109—124页段界已核，前5段已核文并接入双语及对象，其余仍待接入，不将51阶段规划视为阅读已完成。

- 阶段总表（状态以各阶段交接验收为准）：

| 阶段 | 范围 | 来源块 | 实际影印页 | 内容状态 |
| --- | --- | --- | --- | --- |
| 1 | 樕𧑤之山 | source-04-0003—0005 | 109 | 已接入，验收见交接 |
| 2 | 藟山 | source-04-0006—0007 | 109 | 已接入，验收见交接 |
| 3 | 栒状之山 | source-04-0008—0012 | 109、110 | 已接入，验收见交接 |
| 4 | 勃亝之山 | source-04-0013—0013 | 110 | 已接入，验收见交接 |
| 5 | 番條之山 | source-04-0014—0015 | 110 | 已接入，验收见交接 |
| 6 | 姑兒之山 | source-04-0016—0017 | 110 | 已接入，验收见交接 |
| 7 | 髙氏之山 | source-04-0018—0019 | 110、111 | 已接入，验收见交接 |
| 8 | 嶽山 | source-04-0020—0021 | 111 | 已接入，验收见交接 |
| 9 | 犲山 | source-04-0022—0024 | 111 | 已接入，验收见交接 |
| 10 | 獨山 | source-04-0025—0027 | 111 | 已接入，验收见交接 |
| 11 | 泰山 | source-04-0028—0031 | 112 | 已接入，验收见交接 |
| 12 | 竹山 | source-04-0032—0033 | 112 | 已接入，验收见交接 |
| 13 | 首列总括与祭礼 | source-04-0034—0036 | 112 | 已接入，验收见交接 |
| 14 | 空桑之山 | source-04-0037—0040 | 113 | 已接入，验收见交接 |
| 15 | 曹夕之山 | source-04-0041—0041 | 113 | 已接入，验收见交接 |
| 16 | 嶧皐之山 | source-04-0042—0044 | 113 | 已接入，验收见交接 |
| 17 | 葛山之尾 | source-04-0045—0046 | 113、114 | 已接入，验收见交接 |
| 18 | 葛山之首 | source-04-0047—0050 | 114 | 已接入，验收见交接 |
| 19 | 餘峩之山 | source-04-0051—0054 | 114 | 已接入，验收见交接 |
| 20 | 杜父之山 | source-04-0055—0055 | 115 | 已接入，验收见交接 |
| 21 | 耿山 | source-04-0056—0058 | 115 | 已接入，验收见交接 |
| 22 | 盧其之山 | source-04-0059—0061 | 115 | 已接入，验收见交接 |
| 23 | 姑射之山 | source-04-0062—0062 | 115 | 已接入，验收见交接 |
| 24 | 北姑射之山 | source-04-0063—0064 | 115、116 | 已接入，验收见交接 |
| 25 | 南姑射之山 | source-04-0065—0065 | 116 | 已接入，验收见交接 |
| 26 | 碧山 | source-04-0066—0066 | 116 | 已接入，验收见交接 |
| 27 | 維氏之山 | source-04-0067—0068 | 116 | 已接入，验收见交接 |
| 28 | 姑逢之山 | source-04-0069—0071 | 116 | 已接入，验收见交接 |
| 29 | 鳬麗之山 | source-04-0072—0074 | 116、117 | 已接入，验收见交接 |
| 30 | 䃌山 | source-04-0075—0078 | 117 | 已接入，验收见交接 |
| 31 | 次二总括与祭礼 | source-04-0079—0081 | 117 | 已接入，验收见交接 |
| 32 | 尸胡之山 | source-04-0082—0084 | 118 | 已接入，验收见交接 |
| 33 | 岐山 | source-04-0085—0085 | 118 | 已接入，验收见交接 |
| 34 | 諸鈎之山 | source-04-0086—0087 | 118 | 已接入，验收见交接 |
| 35 | 中父之山 | source-04-0088—0088 | 118 | 已接入，验收见交接 |
| 36 | 胡射之山 | source-04-0089—0089 | 118 | 已接入，验收见交接 |
| 37 | 孟子之山 | source-04-0090—0093 | 118、119 | 已接入，验收见交接 |
| 38 | 跂踵之山 | source-04-0094—0099 | 119 | 已接入，验收见交接 |
| 39 | 踇隅之山 | source-04-0100—0102 | 120 | 已接入，验收见交接 |
| 40 | 無皐之山 | source-04-0103—0105 | 120 | 已接入，验收见交接 |
| 41 | 次三总括与祭礼 | source-04-0106—0108 | 120 | 已接入，验收见交接 |
| 42 | 北號之山 | source-04-0109—0113 | 121 | 已接入，验收见交接 |
| 43 | 旄山 | source-04-0114—0116 | 121 | 已接入，验收见交接 |
| 44 | 東始之山 | source-04-0117—0121 | 121、122 | 已接入，验收见交接 |
| 45 | 女烝之山 | source-04-0122—0124 | 122 | 已接入，验收见交接 |
| 46 | 欽山 | source-04-0125—0127 | 122、123 | 已接入，验收见交接 |
| 47 | 子桐之山 | source-04-0128—0130 | 123 | 已接入，验收见交接 |
| 48 | 剡山 | source-04-0131—0133 | 123 | 已接入，验收见交接 |
| 49 | 太山 | source-04-0134—0138 | 123、124 | 已接入，验收见交接 |
| 50 | 次四总括 | source-04-0139—0140 | 124 | 已接入，验收见交接 |
| 51 | 东山经篇末总计 | source-04-0141—0141 | 124 | 已接入，验收见交接 |

- 跨行与形貌风险以data/dongshan-edition-review.json各阶段note为准；保留当康、蜚、合窳与东山山列既有稳定ID。

### 05 中山经

- 常规入口：㔮（甘棗）（`beast-zhongshan-nuo-gancao`）；豪魚（渠豬）（`beast-zhongshan-hao-quzhu`）；共水（甘棗）（`water-zhongshan-gong-gancao`）；河（中山首列文本索引）（`water-zhongshan-he`）；杻木（甘棗）（`plant-zhongshan-niu-gancao`）；蘀（甘棗）（`plant-zhongshan-tuo-gancao`）；橿（歴兒）（`plant-zhongshan-jiang-lier`）；櫔木（歴兒）（`plant-zhongshan-li-lier`）；竹（渠豬）（`plant-zhongshan-bamboo-quzhu`）；渠豬之水（`water-zhongshan-quzhu`）；甘棗之山（`passage-zhongshan-r01-gancao`）；歴兒之山（`passage-zhongshan-r01-lier`）；渠豬之山（`passage-zhongshan-r01-quzhu`）；甘棗之山（`place-zhongshan-r01-gancao`）；歴兒之山（`place-zhongshan-r01-lier`）；揀（櫔实比拟）（`plant-zhongshan-jian-comparison-lier`）；渠豬之山（`place-zhongshan-r01-quzhu`）。
- 待补方向：准备阶段已保存下册2—70页69张影印并规划212阶段：197列名山、12总括祭礼、3收束；首五段影印段界核定，其余仍需逐阶段复核。614录文块含1标题与613正文/注文块；200结构候选不是已核阶段数。次五15列名与原报16、各列原报合198与篇末197、里程合28595与篇末21371分别保留。已接入3阅读段，剩209阶段；疑字、同名异篇、纯注文与字体缺口详见data/zhongshan-edition-review.json。
- 校核入口：[该篇固定修订](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E4%BA%94&oldid=2652856)；录文尚需与影印页对校，不把自动导入视为已核对。

### 06 海外南经

- 数据未开放：海外诸国（`08-01`）。
- 待补方向：国家、异人、神祇及明确方位关系未形成完整可达条目。
- 校核入口：[该篇固定修订](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E5%85%AD&oldid=2652857)；录文尚需与影印页对校，不把自动导入视为已核对。

### 07 海外西经

- 常规入口：刑天舞干戚（`03-03`）。
- 数据未开放：海外诸国（`08-01`）。
- 待补方向：刑天故事之外，诸国、异人与神祇关系待系统整理。
- 校核入口：[该篇固定修订](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E4%B8%83&oldid=2652858)；录文尚需与影印页对校，不把自动导入视为已核对。

### 08 海外北经

- 常规入口：夸父逐日（`03-05`）；禹杀相柳（`05-02`）。
- 数据未开放：海外诸国（`08-01`）；烛龙（`08-06`）。
- 待补方向：夸父、相柳之外的国家、神祇与方位关系仍有大量缺口。
- 校核入口：[该篇固定修订](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E5%85%AB&oldid=2652859)；录文尚需与影印页对校，不把自动导入视为已核对。

### 09 海外东经

- 常规入口：黑齿国（方位参照）（`place-heichi`）；汤谷／扶桑（`place-fusang`）。
- 数据未开放：海外诸国（`08-01`）；扶桑（`08-05`）。
- 待补方向：黑齿、扶桑等是片段；诸国、异人与日月相关记载仍待按篇建立。
- 校核入口：[该篇固定修订](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E4%B9%9D&oldid=2652860)；录文尚需与影印页对校，不把自动导入视为已核对。

### 10 海内南经

- 待补方向：以该篇为单位建立现有条目对应和未收录实体清单。
- 校核入口：[该篇固定修订](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E5%8D%81&oldid=2652861)；录文尚需与影印页对校，不把自动导入视为已核对。

### 11 海内西经

- 常规入口：开明兽（`beast-kaiming`）；昆仑之墟（`place-kunlun`）；昆仑 · 帝之下都（`domain-kunlun`）。
- 待补方向：昆仑等片段之外，其他地域、神兽与人物关系尚未系统整理。
- 校核入口：[该篇固定修订](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E5%8D%81%E4%B8%80&oldid=2652862)；录文尚需与影印页对校，不把自动导入视为已核对。

### 12 海内北经

- 常规入口：穷奇（海内北经）（`beast-qiongqi-hainei`）。
- 待补方向：穷奇等条目之外，异人、山水与国家仍待补齐。
- 校核入口：[该篇固定修订](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E5%8D%81%E4%BA%8C&oldid=2652863)；录文尚需与影印页对校，不把自动导入视为已核对。

### 13 海内东经

- 待补方向：优先梳理水道及相关地点；不将文学方位自动换成现代坐标。
- 校核入口：[该篇固定修订](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E5%8D%81%E4%B8%89&oldid=2652864)；录文尚需与影印页对校，不把自动导入视为已核对。

### 14 大荒东经

- 数据未开放：大荒异兽（`08-02`）。
- 待补方向：异兽片段之外，国家、谱系、山川与日月运行记载待补。
- 校核入口：[该篇固定修订](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E5%8D%81%E5%9B%9B&oldid=2652865)；录文尚需与影印页对校，不把自动导入视为已核对。

### 15 大荒南经

- 数据未开放：大荒异兽（`08-02`）。
- 待补方向：数据总述不能算全篇收录；诸国、人物、山川需逐项核对。
- 校核入口：[该篇固定修订](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E5%8D%81%E4%BA%94&oldid=2652866)；录文尚需与影印页对校，不把自动导入视为已核对。

### 16 大荒西经

- 数据未开放：大荒异兽（`08-02`）。
- 待补方向：不同篇目的西王母等形象须分开记录，国家及山川关系待补。
- 校核入口：[该篇固定修订](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E5%8D%81%E5%85%AD&oldid=2652867)；录文尚需与影印页对校，不把自动导入视为已核对。

### 17 大荒北经

- 常规入口：彊良（强良）（`beast-qiangliang`）；烛龙（`beast-zhulong`）；相柳（`beast-xiangliu`）；赤水（`place-chishui`）；章尾山（`place-zhangwei`）；章尾山 · 烛龙所居（`domain-zhangwei`）；夸父逐日（`03-05`）；禹杀相柳（`05-02`）。
- 数据未开放：大荒异兽（`08-02`）；烛龙（`08-06`）。
- 待补方向：烛龙等片段之外，人物、山川及谱系待补；相繇与相柳分篇保存。
- 校核入口：[该篇固定修订](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E5%8D%81%E4%B8%83&oldid=2652868)；录文尚需与影印页对校，不把自动导入视为已核对。

### 18 海内经

- 常规入口：鲧窃息壤（`04-04`）。
- 待补方向：鲧禹故事之外的谱系、国家、水系与其他记载仍待系统整理。
- 校核入口：[该篇固定修订](https://zh.wikisource.org/w/index.php?title=%E5%B1%B1%E6%B5%B7%E7%B6%93_%28%E5%9B%9B%E9%83%A8%E5%8F%A2%E5%88%8A%E6%9C%AC%29/%E5%8D%B7%E7%AC%AC%E5%8D%81%E5%85%AB&oldid=2652869)；录文尚需与影印页对校，不把自动导入视为已核对。

## 西山经已核山段：钱来之山、松果之山、太华之山、小华之山、符禺之山、石脆之山、英山、竹山、浮山、羭次之山、时山、南山（西山经）、大时之山、嶓冡之山、天帝之山、皐塗之山、黄山（西山经）、翠山、騩山、西山首列总括与祭礼、鈐山、㤗冐之山、數歴之山、髙山、女牀之山、龍首之山、鹿臺之山、鳥危之山、小次之山、大次之山、薰吳之山、𢇨陽之山、衆獸之山、皇人之山、中皇之山、西皇之山、萊山、西次二经总括与祭礼、崇吾之山、長沙之山、不周之山、峚山、鍾山、㤗噐之山、槐江之山、崑崙之丘、樂游之山、蠃母之山、玉山、軒轅之丘、積石之山、長留之山、章莪之山、隂山（西次三经）、符愓之山、三危之山、騩山（西次三经）、天山、泑山、翼望之山、西次三经总括与祠礼、隂山（西次四经）、勞山、罷父之山、申山、鳥山、上申之山、諸次之山、號山、盂山、白於之山、申首之山、涇谷之山、剛山、剛山之尾、英鞮之山、中曲之山、邽山、鳥鼠同穴之山、崦嵫之山、西次四经总括与祠礼、西山经篇末总计

- 已盘点378个来源录文块、81个结构候选段，涉及影印页34–75；其中11个录文块含缺字图标记。候选段不等于已核定山数、实体数或已完成阅读段。
- 底本继续采用《四部丛刊》景明成化本，先核对影印与郭注、剔除标题元信息，再确定段界及中英文说明；保留歧义，不按图字替代文本猜字或读音。
- 本篇现有记录的稳定ID保留，尤其`beast-guan`为讙，不与南山经灌灌合并；同名异山、山中与水中关系分别核定。现有对应记录：朱厌（`beast-zhuyan`）；英招（`beast-yingzhao`）；文鳐鱼（`beast-wenyaoyu`）；羬羊（`beast-xishan-qianyang`）；䳋渠（`beast-xishan-tongqu`）；肥𧔥（太华山）（`beast-xishan-feiyi-taihua`）；赤鷩（`beast-xishan-chibie`）；葱聾（`beast-xishan-conglong`）；鴖（`beast-xishan-min`）；䰷鱼（`beast-xishan-bangyu-ying`）；羬羊（英山段）（`beast-xishan-qianyang-ying`）；肥遗（英山鸟）（`beast-xishan-feiyi-ying`）；人鱼（竹山段）（`beast-xishan-renyu-zhushan`）；毫彘（`beast-xishan-haozhi-zhushan`）；囂（羭次兽）（`beast-xishan-xiao-yuci`）；槖𩇯（`beast-xishan-tuofei-yuci`）；猛豹（西山经南山段）（`beast-xishan-mengbao-nanshan`）；尸鳩（西山经南山段）（`beast-xishan-shijiu-nanshan`）；犀（嶓冡段）（`animal-xishan-xi-bozhong`）；兕（嶓冡段）（`animal-xishan-si-bozhong`）；熊（嶓冡段）（`animal-xishan-bear-bozhong`）；羆（嶓冡段）（`animal-xishan-pi-bozhong`）；白翰（嶓冡段）（`bird-xishan-baihan-bozhong`）；赤鷩（嶓冡段）（`bird-xishan-chibie-bozhong`）；谿邊（天帝山）（`beast-xishan-xibian-tiandi`）；櫟（天帝山鸟）（`beast-xishan-li-tiandi`）；𤣎如（皐塗段）（`beast-xishan-yingru-gaotu`）；數斯（皐塗段）（`beast-xishan-shusi-gaotu`）；𤛎（黄山段）（`beast-xishan-min-huangshan`）；鸚䳇（黄山段）（`beast-xishan-yingmu-huangshan`）；旄牛（翠山段）（`animal-xishan-maoniu-cuishan`）；麢（翠山段）（`animal-xishan-ling-cuishan`）；麝（翠山段）（`animal-xishan-she-cuishan`）；鸓（翠山段）（`bird-xishan-lei-cuishan`）；白蛇（㤗冐段）（`beast-xishan-white-snake-taimao`）；鸚䳇（數歴段）（`beast-xishan-yingmu-shuli`）；虎（女牀段）（`animal-xishan-tiger-nvchuang`）；豹（女牀段）（`animal-xishan-leopard-nvchuang`）；犀（女牀段）（`animal-xishan-xi-nvchuang`）；兕（女牀段）（`animal-xishan-si-nvchuang`）；鸞鳥（女牀段）（`beast-xishan-luan-nvchuang`）；㸲牛（鹿臺段）（`animal-xishan-zuoniu-lutai`）；羬羊（鹿臺段）（`beast-xishan-qianyang-lutai`）；白豪（鹿臺段）（`animal-xishan-baihao-lutai`）；鳬徯（鹿臺段）（`beast-xishan-fuxi-lutai`）；朱厭（小次段）（`beast-xishan-zhuyan-xiaoci`）；㸲牛（大次段）（`animal-xishan-zuoniu-daci`）；麢羊（大次段）（`animal-xishan-lingyang-daci`）；犀（𢇨陽段）（`animal-xishan-xi-quyang`）；兕（𢇨陽段）（`animal-xishan-si-quyang`）；虎（𢇨陽段）（`animal-xishan-tiger-quyang`）；犳（𢇨陽段）（`animal-xishan-zhuo-quyang`）；㸲牛（𢇨陽段）（`animal-xishan-zuoniu-quyang`）；犀（衆獸段）（`animal-xishan-xi-zhongshou`）；兕（衆獸段）（`animal-xishan-si-zhongshou`）；麋（西皇段）（`animal-xishan-mi-xihuang`）；鹿（西皇段）（`animal-xishan-deer-xihuang`）；㸲牛（西皇段）（`animal-xishan-zuoniu-xihuang`）；羅羅（萊山段）（`bird-xishan-luoluo-laishan`）；舉父（崇吾段）（`beast-xishan-jufu-chongwu`）；蠻蠻（崇吾段）（`bird-xishan-manman-chongwu`）；竒鳥（峚鍾泽间）（`bird-xishan-birds-mi-zhong`）；怪獸（峚鍾泽间）（`beast-xishan-beasts-mi-zhong`）；竒魚（峚鍾泽间）（`beast-xishan-fish-mi-zhong`）；大鶚（欽䲹所化）（`bird-xishan-qinpi-e-zhongshan`）；鵕鳥（皷所化）（`bird-xishan-gu-jun-zhongshan`）；文鰩魚（㤗噐段）（`beast-xishan-wenyao-taiqi`）；蠃母（槐江水中）（`beast-xishan-luomu-huaijiang`）；鷹（槐江北望）（`bird-xishan-ying-huaijiang`）；鸇（槐江北望）（`bird-xishan-zhan-huaijiang`）；陸吾（`beast-luwu`）；土螻（`beast-tulou`）；欽原（`beast-qinyuan`）；鶉鳥（`bird-xishan-chun-kunlun`）；怪鳥獸（崑崙段）（`beast-xishan-strange-kunlun`）；滑魚（`beast-xishan-huayu-leyou`）；狡（`beast-xishan-jiao-yushan`）；胜遇（`bird-xishan-shengyu-yushan`）；文尾兽（長留段）（`beast-xishan-beasts-changliu`）；文首鸟（長留段）（`bird-xishan-birds-changliu`）；狰（`beast-zheng`）；畢方（`beast-bifang`）；天狗（`beast-tian-gou`）；三青鳥（三危段）（`bird-xishan-bluebirds-sanwei`）；𢕟𢓨（`beast-xishan-aoyu-sanwei`）；鴟（三危段）（`bird-xishan-chi-sanwei`）；積蛇（`beast-xishan-jishes-guishan3`）；帝江（`beast-dijiang`）；讙（`beast-guan`）；鵸䳜（`bird-xishan-qiyu-yiwang`）；白鹿（上申段）（`beast-xishan-deer-shangshen`）；當扈（`bird-xishan-danghu-shangshen`）；衆蛇（諸次段）（`beast-xishan-snakes-zhuci`）；白狼（盂山）（`beast-xishan-wolf-yushan4`）；白虎（盂山）（`beast-xishan-tiger-yushan4`）；白雉（盂山）（`bird-xishan-pheasant-yushan4`）；白翟（盂山）（`bird-xishan-zhai-yushan4`）；㸲牛（白於段）（`beast-xishan-zuoniu-baiyu`）；羬羊（白於段）（`beast-xishan-qianyang-baiyu`）；鴞（白於段）（`bird-xishan-xiao-baiyu`）；蠻蠻（鼠身鳖首）（`beast-xishan-manman-gangwei`）；白鸟兽（英鞮段）（`beast-xishan-white-yingdi`）；冉遺之魚（`beast-xishan-ranyi-yingdi`）；駮（`beast-bo`）；窮竒（西山经）（`beast-qiongqi-xishan`）；蠃魚（`beast-luoyu`）；白虎（鳥鼠段）（`beast-xishan-tiger-niaoshu`）；鰠魚（`beast-xishan-saoyu-niaoshu`）；𩶯魮之魚（`beast-xishan-rupi-niaoshu`）；龜（崦嵫阳）（`beast-xishan-turtle-yanzi`）；孰湖（`beast-xishan-shuhu-yanzi`）；未名鸟（崦嵫末段）（`bird-xishan-unnamed-yanzi`）；玉山（`place-yushan`）；西山经山列（`place-west-ranges`）；玉山 · 西王母所居（`domain-yushan`）；濩水（`water-xishan-huo`）；渭（西山经）（`water-xishan-wei`）；萆荔（`plant-xishan-bili`）；文茎（`plant-xishan-wenjing`）；條（符禺山）（`plant-xishan-tiao-fuyu`）；符禺之水（`water-xishan-fuyu`）；條（石脆山）（`plant-xishan-tiao-shicui`）；灌水（`water-xishan-guan`）；禺水（石脆山段）（`water-xishan-yu-shicui`）；流赭（`material-xishan-liuzhe`）；禺水（英山段）（`water-xishan-yu-ying`）；招水（英山段）（`water-xishan-zhao-ying`）；黄雚（`plant-xishan-huangguan`）；竹水（`water-xishan-zhu`）；丹水（竹山段）（`water-xishan-dan-zhushan`）；洛水（竹山段）（`water-xishan-luo-zhushan`）；水玉（竹山段）（`material-xishan-shuiyu-zhushan`）；盼木（`plant-xishan-panmu`）；薰草（`plant-xishan-xuncao`）；漆水（羭次段）（`water-xishan-qi-yuci`）；嬰垣之玉（`material-xishan-yingyuan-yuci`）；逐水（时山段）（`water-xishan-zhu-shishan`）；水玉（时山段）（`material-xishan-shuiyu-shishan`）；丹水（西山经南山段）（`water-xishan-dan-nanshan`）；丹粟（西山经南山段）（`material-xishan-dansu-nanshan`）；涔水（大时段）（`water-xishan-qian-dashi`）；清水（大时段）（`water-xishan-qing-dashi`）；汉水（西山经首列）（`water-xishan-han-dashi`）；银（大时段）（`material-xishan-silver-dashi`）；白玉（大时段）（`material-xishan-white-jade-dashi`）；沔（嶓冡段）（`water-xishan-mian-bozhong`）；囂水（嶓冡段）（`water-xishan-xiao-bozhong`）；汤水（嶓冡段）（`water-xishan-tang-bozhong`）；桃枝（嶓冡段）（`plant-xishan-taozhi-bozhong`）；鈎端（嶓冡段）（`plant-xishan-gouduan-bozhong`）；蓇蓉（嶓冡段）（`plant-xishan-gurong-bozhong`）；杜衡（天帝山）（`plant-xishan-duheng-tiandi`）；薔水（皐塗段）（`water-xishan-se-gaotu`）；诸资之水（皐塗段）（`water-xishan-zhuzi-gaotu`）；塗水（皐塗段）（`water-xishan-tu-gaotu`）；集获之水（皐塗段）（`water-xishan-jihuo-gaotu`）；丹粟（皐塗段）（`material-xishan-dansu-gaotu`）；银（皐塗段）（`material-xishan-silver-gaotu`）；黄金（皐塗段）（`material-xishan-gold-gaotu`）；桂木（皐塗段）（`plant-xishan-gui-gaotu`）；礜（皐塗段）（`material-xishan-yu-gaotu`）；無條（皐塗段）（`plant-xishan-wutiao-gaotu`）；竹箭（黄山段）（`plant-xishan-zhujian-huangshan`）；盼水（黄山段）（`water-xishan-pan-huangshan`）；赤水（西山经）（`water-xishan-chi-huangshan`）；玉（黄山水文段）（`material-xishan-jade-huangshan`）；㯶（翠山段）（`plant-xishan-zong-cuishan`）；枏（翠山段）（`plant-xishan-nan-cuishan`）；竹箭（翠山段）（`plant-xishan-zhujian-cuishan`）；黄金（翠山段）（`material-xishan-gold-cuishan`）；玉（翠山段）（`material-xishan-jade-cuishan`）；西海（西山经）（`water-xishan-westsea-guishan`）；玉（騩山段）（`material-xishan-jade-guishan`）；淒水（騩山段）（`water-xishan-qi-guishan`）；采石（騩山水文段）（`material-xishan-caishi-guishan`）；黄金（騩山水文段）（`material-xishan-gold-guishan`）；丹粟（騩山段）（`material-xishan-dansu-guishan`）；铜（鈐山段）（`material-xishan-copper-qianshan`）；玉（鈐山段）（`material-xishan-jade-qianshan`）；杻（鈐山段）（`plant-xishan-niu-qianshan`）；橿（鈐山段）（`plant-xishan-jiang-qianshan`）；金（㤗冐段）（`material-xishan-jin-taimao`）；铁（㤗冐段）（`material-xishan-iron-taimao`）；浴水（㤗冐段）（`water-xishan-yu-taimao`）；河（西山经）（`water-xishan-he-taimao`）；藻玉（㤗冐段）（`material-xishan-zaoyu-taimao`）；黄金（數歴段）（`material-xishan-gold-shuli`）；银（數歴段）（`material-xishan-silver-shuli`）；杻（數歴段）（`plant-xishan-niu-shuli`）；橿（數歴段）（`plant-xishan-jiang-shuli`）；楚水（數歴段）（`water-xishan-chu-shuli`）；珠（數歴水文段）（`material-xishan-pearl-shuli`）；银（髙山段）（`material-xishan-silver-gaoshan`）；青碧（髙山下）（`material-xishan-qingbi-gaoshan`）；雄黄（髙山段）（`material-xishan-xionghuang-gaoshan`）；㯶（髙山段）（`plant-xishan-zong-gaoshan`）；竹（髙山段）（`plant-xishan-bamboo-gaoshan`）；涇水（西山经次二列）（`water-xishan-jing-gaoshan`）；磬石（髙山水文段）（`material-xishan-qingshi-gaoshan`）；青碧（髙山水文段）（`material-xishan-qingbi-water-gaoshan`）；赤铜（女牀段）（`material-xishan-red-copper-nvchuang`）；石𣵀（女牀段）（`material-xishan-shinie-nvchuang`）；黄金（龍首山阳面）（`material-xishan-gold-longshou`）；鐡（龍首山阴面）（`material-xishan-iron-longshou`）；苕水（龍首山）（`water-xishan-tiao-longshou`）；羙玉（龍首山水文）（`material-xishan-fine-jade-longshou`）；白玉（鹿臺山上）（`material-xishan-white-jade-lutai`）；銀（鹿臺山下）（`material-xishan-silver-lutai`）；磬石（鳥危山阳面）（`material-xishan-qingshi-niaowei`）；檀（鳥危山阴面）（`plant-xishan-tan-niaowei`）；楮（鳥危山阴面）（`plant-xishan-chu-niaowei`）；女牀（鳥危段·所指未詳）（`material-xishan-nvchuang-niaowei`）；鳥危之水（`water-xishan-niaowei`）；丹粟（鳥危段水文）（`material-xishan-dansu-niaowei`）；白玉（小次山上）（`material-xishan-white-jade-xiaoci`）；赤銅（小次山下）（`material-xishan-red-copper-xiaoci`）；堊（大次山阳面）（`material-xishan-e-daci`）；碧（大次山阴面）（`material-xishan-bi-daci`）；金（薰吳段）（`material-xishan-jin-xunwu`）；玉（薰吳段）（`material-xishan-jade-xunwu`）；稷（𢇨陽段）（`plant-xishan-ji-quyang`）；柟（𢇨陽段）（`plant-xishan-nan-quyang`）；豫章（𢇨陽段）（`plant-xishan-yuzhang-quyang`）；㻬琈之玉（衆獸山上）（`material-xishan-tufu-zhongshou`）；檀（衆獸山下）（`plant-xishan-tan-zhongshou`）；楮（衆獸山下）（`plant-xishan-chu-zhongshou`）；黄金（衆獸山下）（`material-xishan-gold-zhongshou`）；金（皇人山上）（`material-xishan-jin-huangren`）；玉（皇人山上）（`material-xishan-jade-huangren`）；青雄黄（皇人山下）（`material-xishan-qingxionghuang-huangren`）；皇水（皇人段）（`water-xishan-huang-huangren`）；丹粟（皇人段水文）（`material-xishan-dansu-huangren`）；黄金（中皇山上）（`material-xishan-gold-zhonghuang`）；蕙棠（中皇山下）（`plant-xishan-huitang-zhonghuang`）；金（西皇山阳面）（`material-xishan-jin-xihuang`）；鐡（西皇山阴面）（`material-xishan-iron-xihuang`）；檀（萊山段）（`plant-xishan-tan-laishan`）；楮（萊山段）（`plant-xishan-chu-laishan`）；䍃之澤（崇吾段）（`water-xishan-yaoze-chongwu`）；䗡淵（崇吾段）（`water-xishan-yanyuan-chongwu`）；未名木（崇吾段）（`plant-xishan-unnamed-chongwu`）；泚水（長沙段）（`water-xishan-ci-changsha`）；泑水（西山经）（`water-xishan-you-changsha`）；青雄黄（長沙段）（`material-xishan-qingxionghuang-changsha`）；泑澤（不周段）（`water-xishan-youze-buzhou`）；嘉果（不周段·未命名）（`plant-xishan-jia-guo-buzhou`）；丹木（峚山段）（`plant-xishan-danmu-mishan`）；丹水（峚山段）（`water-xishan-dan-mishan`）；稷澤（峚山段）（`water-xishan-jize-mishan`）；白玉（峚山丹水）（`material-xishan-white-jade-mishan`）；玉膏（峚山段）（`material-xishan-yugao-mishan`）；𤣥玉（峚山段）（`material-xishan-xuanyu-mishan`）；玉榮（峚山段）（`material-xishan-yurong-mishan`）；瑾瑜之玉（峚山段）（`material-xishan-jinyu-mishan`）；泽地（峚至鍾）（`water-xishan-wetlands-mi-zhong`）；𮗚水（㤗噐段）（`water-xishan-guan-taiqi`）；東海（㤗噐段）（`water-xishan-eastsea-taiqi`）；丘時之水（槐江段）（`water-xishan-qiushi-huaijiang`）；青雄黃（槐江山上）（`material-xishan-qingxionghuang-huaijiang`）；藏琅玕（槐江段）（`material-xishan-langgan-huaijiang`）；黄金（槐江山上）（`material-xishan-gold-above-huaijiang`）；玉（槐江山上）（`material-xishan-jade-above-huaijiang`）；丹粟（槐江阳面）（`material-xishan-dansu-huaijiang`）；采黄金銀（槐江阴面）（`material-xishan-shaded-goods-huaijiang`）；大澤（槐江西望）（`water-xishan-daze-huaijiang`）；玉（槐江西望大澤）（`material-xishan-jade-daze-huaijiang`）；榣木之有若（槐江西望）（`plant-xishan-yaomu-ruo-huaijiang`）；滛水（槐江东望）（`water-xishan-flowing-huaijiang`）；沙棠（`plant-xishan-shatang-kunlun`）；薲草（`plant-xishan-pin-kunlun`）；河水（崑崙段）（`water-xishan-he-kunlun`）；赤水（崑崙段）（`water-xishan-chi-kunlun`）；汜天之水（`water-xishan-fantian-kunlun`）；洋水（崑崙段）（`water-xishan-yang-kunlun`）；醜塗之水（`water-xishan-choutu-kunlun`）；黑水（崑崙段）（`water-xishan-hei-kunlun`）；桃水（`water-xishan-tao-leyou`）；稷澤（樂游段）（`water-xishan-jize-leyou`）；白玉（樂游段）（`material-xishan-jade-leyou`）；玉（蠃母山上）（`material-xishan-jade-luomushan`）；青石（蠃母山下）（`material-xishan-stone-luomushan`）；洵水（`water-xishan-xun-xuanyuan`）；黑水（軒轅段）（`water-xishan-hei-xuanyuan`）；丹粟（洵水段）（`material-xishan-dansu-xuanyuan`）；青雄黄（洵水段）（`material-xishan-xionghuang-xuanyuan`）；河水（積石段）（`water-xishan-he-jishi`）；文玉石（`material-xishan-jade-changliu`）；瑶碧（`material-xishan-yaobi-zhange`）；濁浴之水（`water-xishan-zhuoyu-yinshan3`）；蕃澤（`water-xishan-fan-yinshan3`）；文貝（`material-xishan-shell-yinshan3`）；㯶（符愓段）（`plant-xishan-zong-futang`）；柟（符愓段）（`plant-xishan-nan-futang`）；金（符愓山下）（`material-xishan-gold-futang`）；玉（符愓山下）（`material-xishan-jade-futang`）；玉（西次三经騩山）（`material-xishan-jade-guishan3`）；金（天山）（`material-xishan-gold-tianshan`）；玉（天山）（`material-xishan-jade-tianshan`）；青雄黄（天山）（`material-xishan-xionghuang-tianshan`）；英水（`water-xishan-ying-tianshan`）；嬰短之玉（`material-xishan-yingduan-youshan`）；瑾瑜之玉（泑山阳）（`material-xishan-jinyu-youshan`）；青雄黄（泑山阴）（`material-xishan-xionghuang-youshan`）；金（翼望段）（`material-xishan-gold-yiwang`）；玉（翼望段）（`material-xishan-jade-yiwang`）；榖（西次四经隂山）（`plant-xishan-gu-yinshan4`）；茆（隂山段）（`plant-xishan-mao-yinshan4`）；蕃（隂山段）（`plant-xishan-fan-yinshan4`）；隂水（`water-xishan-yin-yinshan4`）；洛（西次四经首段）（`water-xishan-luo-yinshan4`）；茈草（勞山）（`plant-xishan-zicao-laoshan`）；弱水（勞山）（`water-xishan-ruo-laoshan`）；洛（勞山段）（`water-xishan-luo-laoshan`）；洱水（`water-xishan-er-bafu`）；洛（罷父段）（`water-xishan-luo-bafu`）；茈碧（`material-xishan-zibi-bafu`）；榖（申山上）（`plant-xishan-gu-shenshan`）；柞（申山上）（`plant-xishan-zuo-shenshan`）；杻（申山下）（`plant-xishan-niu-shenshan`）；橿（申山下）（`plant-xishan-jiang-shenshan`）；金（申山阳）（`material-xishan-gold-shenshan`）；玉（申山阳）（`material-xishan-jade-shenshan`）；區水（`water-xishan-qu-shenshan`）；河（申山段）（`water-xishan-he-shenshan`）；桑（鳥山上）（`plant-xishan-sang-niaoshan`）；楮（鳥山下）（`plant-xishan-chu-niaoshan`）；鐡（鳥山阴）（`material-xishan-iron-niaoshan`）；玊（鳥山阳）（`material-xishan-jade-niaoshan`）；辱水（`water-xishan-ru-niaoshan`）；河（鳥山段）（`water-xishan-he-niaoshan`）；硌石（`material-xishan-stone-shangshen`）；榛（上申下）（`plant-xishan-zhen-shangshen`）；楛（上申下）（`plant-xishan-hu-shangshen`）；湯水（`water-xishan-tang-shangshen`）；河（上申段）（`water-xishan-he-shangshen`）；諸次之水（`water-xishan-zhuci-zhuci`）；河（諸次段）（`water-xishan-he-zhuci`）；漆（號山段）（`plant-xishan-lacquer-haoshan`）；㯶（號山段）（`plant-xishan-zong-haoshan`）；葯（`plant-xishan-yao-haoshan`）；䖀（`plant-xishan-xian-haoshan`）；芎藭（`plant-xishan-xiongqiong-haoshan`）；汵石（`material-xishan-qin-haoshan`）；端水（`water-xishan-duan-haoshan`）；河（號山段）（`water-xishan-he-haoshan`）；鐡（盂山阴）（`material-xishan-iron-yushan4`）；銅（盂山阳）（`material-xishan-copper-yushan4`）；生水（`water-xishan-sheng-yushan4`）；河（盂山段）（`water-xishan-he-yushan4`）；松（白於上）（`plant-xishan-pine-baiyu`）；柏（白於上）（`plant-xishan-cypress-baiyu`）；櫟（白於下）（`plant-xishan-li-baiyu`）；檀（白於下）（`plant-xishan-tan-baiyu`）；洛水（白於阳）（`water-xishan-luo-baiyu`）；渭（白於段）（`water-xishan-wei-baiyu`）；夾水（`water-xishan-jia-baiyu`）；生水（白於段）（`water-xishan-sheng-baiyu`）；申水（`water-xishan-shen-shenshou`）；白玉（申首段）（`material-xishan-jade-shenshou`）；涇水（涇谷段）（`water-xishan-jing-jinggu`）；渭（涇谷段）（`water-xishan-wei-jinggu`）；白金（涇谷）（`material-xishan-metal-jinggu`）；白玉（涇谷）（`material-xishan-jade-jinggu`）；柒木（`plant-xishan-qi-gangshan`）；㻬琈之玉（剛山）（`material-xishan-tufuyu-gangshan`）；剛水（`water-xishan-gang-gangshan`）；渭（剛山段）（`water-xishan-wei-gangshan`）；洛水（剛山尾）（`water-xishan-luo-gangwei`）；河（剛山尾）（`water-xishan-he-gangwei`）；𣾰木（`plant-xishan-mu-yingdi`）；金（英鞮下）（`material-xishan-gold-yingdi`）；玉（英鞮下）（`material-xishan-jade-yingdi`）；涴水（`water-xishan-wan-yingdi`）；𨹧羊之澤（`water-xishan-lingyang-yingdi`）；玉（中曲阳）（`material-xishan-jade-sun-zhongqu`）；雄黄（中曲阴）（`material-xishan-xionghuang-zhongqu`）；白玉（中曲阴）（`material-xishan-jade-shade-zhongqu`）；金（中曲阴）（`material-xishan-gold-zhongqu`）；櫰木（`plant-xishan-huai-zhongqu`）；𪷟水（`water-xishan-meng-guishan4`）；洋水（邽山段）（`water-xishan-yang-guishan4`）；黄貝（`material-xishan-shell-guishan4`）；白玉（鳥鼠段）（`material-xishan-jade-niaoshu`）；渭水（鳥鼠段）（`water-xishan-wei-niaoshu`）；河（鳥鼠段）（`water-xishan-he-niaoshu`）；濫水（`water-xishan-lan-niaoshu`）；漢水（鳥鼠段）（`water-xishan-han-niaoshu`）；丹木（崦嵫段）（`plant-xishan-dan-yanzi`）；玉（崦嵫阴）（`material-xishan-jade-yanzi`）；苕水（崦嵫）（`water-xishan-tiao-yanzi`）；海（崦嵫段）（`water-xishan-sea-yanzi`）；砥礪（`material-xishan-whetstones-yanzi`）；钱来之山（`passage-xishan-qianlai`）；松果之山（`passage-xishan-songguo`）；太华之山（`passage-xishan-taihua`）；小华之山（`passage-xishan-xiaohua`）；符禺之山（`passage-xishan-fuyu`）；石脆之山（`passage-xishan-shicui`）；英山（`passage-xishan-ying`）；竹山（`passage-xishan-zhushan`）；浮山（`passage-xishan-fushan`）；羭次之山（`passage-xishan-yuci`）；时山（`passage-xishan-shishan`）；南山（西山经）（`passage-xishan-nanshan-west`）；大时之山（`passage-xishan-dashi`）；嶓冡之山（`passage-xishan-bozhong`）；天帝之山（`passage-xishan-tiandi`）；皐塗之山（`passage-xishan-gaotu`）；黄山（西山经）（`passage-xishan-huangshan`）；翠山（`passage-xishan-cuishan`）；騩山（`passage-xishan-guishan`）；西山首列总括与祭礼（`passage-xishan-range1-summary`）；鈐山（`passage-xishan-qianshan`）；㤗冐之山（`passage-xishan-taimao`）；數歴之山（`passage-xishan-shuli`）；髙山（`passage-xishan-gaoshan`）；女牀之山（`passage-xishan-nvchuang`）；龍首之山（`passage-xishan-longshou`）；鹿臺之山（`passage-xishan-lutai`）；鳥危之山（`passage-xishan-niaowei`）；小次之山（`passage-xishan-xiaoci`）；大次之山（`passage-xishan-daci`）；薰吳之山（`passage-xishan-xunwu`）；𢇨陽之山（`passage-xishan-quyang`）；衆獸之山（`passage-xishan-zhongshou`）；皇人之山（`passage-xishan-huangren`）；中皇之山（`passage-xishan-zhonghuang`）；西皇之山（`passage-xishan-xihuang`）；萊山（`passage-xishan-laishan`）；西次二经总括与祭礼（`passage-xishan-range2-summary`）；崇吾之山（`passage-xishan-chongwu`）；長沙之山（`passage-xishan-changsha`）；不周之山（`passage-xishan-buzhou`）；峚山（`passage-xishan-mishan`）；鍾山（`passage-xishan-zhongshan`）；㤗噐之山（`passage-xishan-taiqi`）；槐江之山（`passage-xishan-huaijiang`）；崑崙之丘（`passage-xishan-kunlun`）；樂游之山（`passage-xishan-leyou`）；蠃母之山（`passage-xishan-luomushan`）；玉山（`passage-xishan-yushan`）；軒轅之丘（`passage-xishan-xuanyuan`）；積石之山（`passage-xishan-jishi`）；長留之山（`passage-xishan-changliu`）；章莪之山（`passage-xishan-zhange`）；隂山（西次三经）（`passage-xishan-yinshan3`）；符愓之山（`passage-xishan-futang`）；三危之山（`passage-xishan-sanwei`）；騩山（西次三经）（`passage-xishan-guishan3`）；天山（`passage-xishan-tianshan`）；泑山（`passage-xishan-youshan`）；翼望之山（`passage-xishan-yiwang`）；西次三经总括与祠礼（`passage-xishan-range3-summary`）；隂山（西次四经）（`passage-xishan-yinshan4`）；勞山（`passage-xishan-laoshan`）；罷父之山（`passage-xishan-bafu`）；申山（`passage-xishan-shenshan`）；鳥山（`passage-xishan-niaoshan`）；上申之山（`passage-xishan-shangshen`）；諸次之山（`passage-xishan-zhuci`）；號山（`passage-xishan-haoshan`）；盂山（`passage-xishan-yushan4`）；白於之山（`passage-xishan-baiyu`）；申首之山（`passage-xishan-shenshou`）；涇谷之山（`passage-xishan-jinggu`）；剛山（`passage-xishan-gangshan`）；剛山之尾（`passage-xishan-gangwei`）；英鞮之山（`passage-xishan-yingdi`）；中曲之山（`passage-xishan-zhongqu`）；邽山（`passage-xishan-guishan4`）；鳥鼠同穴之山（`passage-xishan-niaoshu`）；崦嵫之山（`passage-xishan-yanzi`）；西次四经总括与祠礼（`passage-xishan-range4-summary`）；西山经篇末总计（`passage-xishan-western-total`）；钱来之山（`place-xishan-qianlai`）；松果之山（`place-xishan-songguo`）；太华之山（`place-xishan-taihua`）；小华之山（`place-xishan-xiaohua`）；㸲牛（小华山）（`animal-xishan-zuoniu`）；符禺之山（`place-xishan-fuyu`）；石脆之山（`place-xishan-shicui`）；英山（`place-xishan-ying`）；㸲牛（英山段）（`animal-xishan-zuoniu-ying`）；竹山（`place-xishan-zhushan`）；浮山（`place-xishan-fushan`）；羭次之山（`place-xishan-yuci`）；时山（`place-xishan-shishan`）；南山（西山经）（`place-xishan-nanshan-west`）；大时之山（`place-xishan-dashi`）；嶓冡之山（`place-xishan-bozhong`）；天帝之山（`place-xishan-tiandi`）；皐塗之山（`place-xishan-gaotu`）；黄山（西山经）（`place-xishan-huangshan`）；翠山（`place-xishan-cuishan`）；騩山（`place-xishan-guishan`）；华山冢与太牢祠礼（`rite-xishan-hua-range1`）；羭山燭礼与玉器（`rite-xishan-yu-range1`）；其余十七山祠礼（`rite-xishan-seventeen-range1`）；鈐山（`place-xishan-qianshan`）；㤗冐之山（`place-xishan-taimao`）；數歴之山（`place-xishan-shuli`）；髙山（`place-xishan-gaoshan`）；女牀之山（`place-xishan-nvchuang`）；龍首之山（`place-xishan-longshou`）；鹿臺之山（`place-xishan-lutai`）；鳥危之山（`place-xishan-niaowei`）；小次之山（`place-xishan-xiaoci`）；大次之山（`place-xishan-daci`）；薰吳之山（`place-xishan-xunwu`）；𢇨陽之山（`place-xishan-quyang`）；衆獸之山（`place-xishan-zhongshou`）；皇人之山（`place-xishan-huangren`）；中皇之山（`place-xishan-zhonghuang`）；西皇之山（`place-xishan-xihuang`）；萊山（`place-xishan-laishan`）；十神·人靣馬身（西次二经）（`deity-xishan-horse-range2`）；七神·人靣牛身（西次二经）（`deity-xishan-ox-range2`）；少牢与白菅之席（西次二经）（`rite-xishan-shaolao-range2`）；十軰神雄鷄之祠（西次二经）（`rite-xishan-rooster-range2`）；崇吾之山（`place-xishan-chongwu`）；冡遂（崇吾段）（`place-xishan-zhongsui-chongwu`）；帝之摶獸之丘（崇吾段）（`place-xishan-tuan-shou-qiu-chongwu`）；長沙之山（`place-xishan-changsha`）；不周之山（`place-xishan-buzhou`）；諸毗之山（西山经）（`place-xishan-zhupi-buzhou`）；嶽崇之山（不周段）（`place-xishan-yuechong-buzhou`）；峚山（`place-xishan-mishan`）；黃帝（峚山段）（`deity-xishan-huangdi-mishan`）；天地鬼神（峚山段）（`deity-xishan-heaven-earth-mishan`）；鍾山（`place-xishan-zhongshan`）；皷（鍾山龙身）（`deity-xishan-gu-zhongshan`）；欽䲹（鍾山原身）（`deity-xishan-qinpi-zhongshan`）；葆江（鍾山段）（`deity-xishan-baojiang-zhongshan`）；帝（鍾山段·未具名）（`deity-xishan-di-zhongshan`）；崑崙之陽（鍾山段）（`place-xishan-kunlun-yang-zhongshan`）；𡺯崖（鍾山之东）（`place-xishan-yaoya-zhongshan`）；㤗噐之山（`place-xishan-taiqi`）；流沙（㤗噐段）（`place-xishan-liusha`）；槐江之山（`place-xishan-huaijiang`）；帝之平圃（槐江段）（`place-xishan-pingpu-huaijiang`）；英招（槐江段）（`deity-xishan-yingzhao-huaijiang`）；后稷（槐江西望）（`deity-xishan-houji-huaijiang`）；槐鬼離侖（槐江北望）（`deity-xishan-lilun-huaijiang`）；怛山（槐江东望）（`place-xishan-danshan-huaijiang`）；有窮鬼（槐江东望）（`deity-xishan-youqiong-huaijiang`）；未名天神（槐江末段）（`deity-xishan-ox-eight-huaijiang`）；崑崙之丘（`place-xishan-kunlun`）；無逹（`place-xishan-wuda-kunlun`）；大杅（`place-xishan-dayu-kunlun`）；樂游之山（`place-xishan-leyou`）；蠃母之山（`place-xishan-luomushan`）；長乗（`deity-xishan-changcheng-luomushan`）；玉山（`place-xishan-yushan`）；西王母（玉山段）（`deity-xishan-xiwangmu-yushan`）；軒轅之丘（`place-xishan-xuanyuan`）；積石之山（`place-xishan-jishi`）；石門（積石段）（`place-xishan-gate-jishi`）；長留之山（`place-xishan-changliu`）；白帝少昊（`deity-xishan-shaohao-changliu`）；員神磈氏（`deity-xishan-weishi-changliu`）；章莪之山（`place-xishan-zhange`）；隂山（西次三经）（`place-xishan-yinshan3`）；符愓之山（`place-xishan-futang`）；江疑（`deity-xishan-jiangyi-futang`）；三危之山（`place-xishan-sanwei`）；騩山（西次三经）（`place-xishan-guishan3`）；𦒿童（`deity-xishan-qitong-guishan3`）；天山（`place-xishan-tianshan`）；湯谷（天山段）（`place-xishan-tang-tianshan`）；泑山（`place-xishan-youshan`）；蓐𭣣（`deity-xishan-rushou-youshan`）；紅光（`deity-xishan-hongguang-youshan`）；翼望之山（`place-xishan-yiwang`）；羊身人面神（西次三经）（`deity-xishan-sheep-range3-summary`）；吉玉稷米祠礼（`rite-xishan-rite-range3-summary`）；隂山（西次四经）（`place-xishan-yinshan4`）；勞山（`place-xishan-laoshan`）；罷父之山（`place-xishan-bafu`）；申山（`place-xishan-shenshan`）；鳥山（`place-xishan-niaoshan`）；上申之山（`place-xishan-shangshen`）；諸次之山（`place-xishan-zhuci`）；號山（`place-xishan-haoshan`）；盂山（`place-xishan-yushan4`）；白於之山（`place-xishan-baiyu`）；申首之山（`place-xishan-shenshou`）；涇谷之山（`place-xishan-jinggu`）；剛山（`place-xishan-gangshan`）；神𩳁（`deity-xishan-chi-gangshan`）；剛山之尾（`place-xishan-gangwei`）；英鞮之山（`place-xishan-yingdi`）；中曲之山（`place-xishan-zhongqu`）；邽山（`place-xishan-guishan4`）；鳥鼠同穴之山（`place-xishan-niaoshu`）；崦嵫之山（`place-xishan-yanzi`）；白鸡稻米白管祠礼（`rite-xishan-rite-range4-summary`）；昆仑之丘（`08-03`）；西王母（早期形态）（`08-07`）。

| 首批范围 | 对象与关系 | 形貌与配图要求 | 来源候选与影印页 |
| --- | --- | --- | --- |
| 钱来山 | 山概况、羬羊；松与洗石先留在概况，郭注与经文分开。 | 羬羊须突出羊状与马尾的区别，尾部单独留空；不得直接画成普通山羊。 | `draft-02-0001`；影印页34 |
| 松果山 | 濩水北流入渭、䳋渠；水中铜与山段鸟类分层，不由共现推断水中栖居。 | 䳋渠先核原字与黑身赤足；用姿态和概括刻纹增强辨识，不添加未经文支持的器官。 | `draft-02-0002`；影印页34 |
| 太华山 | 削成四方的山势、肥𧔥；“鸟兽莫居”与蛇的记载照录，不改成现实地理结论。 | 肥𧔥须逐一数清六足四翼；保留蛇形，不把旱灾画成已发生的现实结果。 | `draft-02-0003`；影印页35 |

- 已对照影印34–35页核定首批3段经文、段界与形貌；正文、郭注、白话和英文分存。电子快照不改写，䳋渠末句的来源页由快照35页校正为实际34页，差异见`data/xishan-edition-review.json`。
- 新增8张独立卡：钱来、松果、太华3座山；羬羊、䳋渠、太华肥𧔥3项异兽；濩水和作为承接水域的渭2项水文。松、洗石与铜仍留在相应山段或水文，不虚构独立物种。新卡和3段阅读均从03章起可见，不增加地图坐标。
- 本批90幅插画任务，已审90幅；原图、完整提示词及复核记录见`frontend/artwork-source/xishan/generation.json`。每幅仅在复核通过后导出完整、预览和卡片WebP。
- 后续配图采用“先读原文特征 → 保证缩略图可辨 → 用木刻造型强化特征”的顺序；没有特殊器官记载的对象用姿态与表面纹样表现，纹样明确为艺术解释。
- 第二批新增小华、符禺、石脆3段与15张独立卡：3山、㸲牛、赤鷩、葱聾、鴖、萆荔、文茎、两种條、符禺之水、灌水、禺水、流赭。符禺与石脆的條分别记录，渭保留松果、符禺两段来源。第二批经文已核对影印35–37页；小华段注文缺字保留待核标记。
- 第三批新增英山、竹山、浮山3段与18张独立卡。英山肥遗鸟与太华肥𧔥蛇分卡，㸲牛及羬羊的复用插画注明别段依据；英山禺水与石脆同名水域不强行合并。竹山人鱼四脚来自郭注，丹水东南流的南字经影印38页补入阅读引文，原始缺字图快照保留。浮山无水文，不补造河流；盼木、薰草独立记录。
- 后续批次已接入羭次、时山、西山经南山和大时。槖𩇯人面独足、猛豹熊状的正文与郭注边界分别保留；时山无草木。大时涔水按郭注音潜转写Qian、北注渭，清水南注汉，两水不合并；榖字小注的电子快照缺收已有说明。
- 后续继续核对剩余山段；具体接续点见本地交接文档，剩余候选仍为待核。未增加数据库，未改动现有地图章节；浏览器验收结果以交接文档最新记录为准。

## 来源分层与全部记录

| ID | 条目 | 分类 | 可达状态 | 原始出处声明 |
| --- | --- | --- | --- | --- |
| `beast-shengsheng` | 狌狌 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-lushu` | 鹿蜀 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-jiuweihu` | 九尾狐 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-chiru` | 赤鱬 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-boyi` | 猼訑 | 《山海经》 | 常规入口 | 《南山经》 |
| `beast-xuangui` | 旋龟 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-gudiao` | 蛊雕 | 《山海经》 | 常规入口 | 《南山经》 |
| `beast-qiongqi-hainei` | 穷奇（海内北经） | 《山海经》 | 常规入口 | 《海内北经》 |
| `beast-zhuyan` | 朱厌 | 《山海经》 | 常规入口 | 《西山经》 |
| `beast-yingzhao` | 英招 | 《山海经》 | 常规入口 | 《西山经》 |
| `beast-wenyaoyu` | 文鳐鱼 | 《山海经》 | 常规入口 | 《西山经》 |
| `beast-qiangliang` | 彊良（强良） | 《山海经》 | 常规入口 | 《大荒北经》 |
| `beast-zhulong` | 烛龙 | 《山海经》 | 常规入口 | 《大荒北经》 |
| `beast-xiangliu` | 相柳 | 《山海经》 | 常规入口 | 《大荒北经》 |
| `beast-kaiming` | 开明兽 | 《山海经》 | 常规入口 | 《海内西经》 |
| `beast-phoenix` | 凤皇 | 《山海经》 | 常规入口 | 《南山经》 |
| `beast-guanguan` | 灌灌 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-nanshan-lu` | 鯥 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-nanshan-lei` | 𩔗 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-nanshan-changfu` | 𪁺𩿧 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-nanshan-lili` | 狸力 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-nanshan-zhu` | 鴸 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-nanshan-changyou` | 长右 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-nanshan-huahuai` | 猾褢 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-nanshan-zhi` | 彘 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-nanshan-huan-xun` | 䍺 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-nanshan-quru` | 瞿如 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-nanshan-hujiao` | 虎蛟 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-nanshan-zhuan` | 鱄鱼 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-nanshan-yulingqiu` | 𪃍 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-nanshan-yuanchu` | 鵷鶵 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-qianyang` | 羬羊 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-tongqu` | 䳋渠 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-feiyi-taihua` | 肥𧔥（太华山） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-chibie` | 赤鷩 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-conglong` | 葱聾 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-min` | 鴖 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-bangyu-ying` | 䰷鱼 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-qianyang-ying` | 羬羊（英山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-feiyi-ying` | 肥遗（英山鸟） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-renyu-zhushan` | 人鱼（竹山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-haozhi-zhushan` | 毫彘 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-xiao-yuci` | 囂（羭次兽） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-tuofei-yuci` | 槖𩇯 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-mengbao-nanshan` | 猛豹（西山经南山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-shijiu-nanshan` | 尸鳩（西山经南山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-xishan-xi-bozhong` | 犀（嶓冡段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-xishan-si-bozhong` | 兕（嶓冡段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-xishan-bear-bozhong` | 熊（嶓冡段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-xishan-pi-bozhong` | 羆（嶓冡段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `bird-xishan-baihan-bozhong` | 白翰（嶓冡段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `bird-xishan-chibie-bozhong` | 赤鷩（嶓冡段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-xibian-tiandi` | 谿邊（天帝山） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-li-tiandi` | 櫟（天帝山鸟） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-yingru-gaotu` | 𤣎如（皐塗段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-shusi-gaotu` | 數斯（皐塗段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-min-huangshan` | 𤛎（黄山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-yingmu-huangshan` | 鸚䳇（黄山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-xishan-maoniu-cuishan` | 旄牛（翠山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-xishan-ling-cuishan` | 麢（翠山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-xishan-she-cuishan` | 麝（翠山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `bird-xishan-lei-cuishan` | 鸓（翠山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-white-snake-taimao` | 白蛇（㤗冐段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-yingmu-shuli` | 鸚䳇（數歴段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-xishan-tiger-nvchuang` | 虎（女牀段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-xishan-leopard-nvchuang` | 豹（女牀段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-xishan-xi-nvchuang` | 犀（女牀段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-xishan-si-nvchuang` | 兕（女牀段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-luan-nvchuang` | 鸞鳥（女牀段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-xishan-zuoniu-lutai` | 㸲牛（鹿臺段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-qianyang-lutai` | 羬羊（鹿臺段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-xishan-baihao-lutai` | 白豪（鹿臺段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-fuxi-lutai` | 鳬徯（鹿臺段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-zhuyan-xiaoci` | 朱厭（小次段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-xishan-zuoniu-daci` | 㸲牛（大次段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-xishan-lingyang-daci` | 麢羊（大次段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-xishan-xi-quyang` | 犀（𢇨陽段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-xishan-si-quyang` | 兕（𢇨陽段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-xishan-tiger-quyang` | 虎（𢇨陽段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-xishan-zhuo-quyang` | 犳（𢇨陽段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-xishan-zuoniu-quyang` | 㸲牛（𢇨陽段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-xishan-xi-zhongshou` | 犀（衆獸段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-xishan-si-zhongshou` | 兕（衆獸段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-xishan-mi-xihuang` | 麋（西皇段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-xishan-deer-xihuang` | 鹿（西皇段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-xishan-zuoniu-xihuang` | 㸲牛（西皇段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `bird-xishan-luoluo-laishan` | 羅羅（萊山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-jufu-chongwu` | 舉父（崇吾段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `bird-xishan-manman-chongwu` | 蠻蠻（崇吾段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `bird-xishan-birds-mi-zhong` | 竒鳥（峚鍾泽间） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-beasts-mi-zhong` | 怪獸（峚鍾泽间） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-fish-mi-zhong` | 竒魚（峚鍾泽间） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `bird-xishan-qinpi-e-zhongshan` | 大鶚（欽䲹所化） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `bird-xishan-gu-jun-zhongshan` | 鵕鳥（皷所化） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-wenyao-taiqi` | 文鰩魚（㤗噐段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-luomu-huaijiang` | 蠃母（槐江水中） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `bird-xishan-ying-huaijiang` | 鷹（槐江北望） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `bird-xishan-zhan-huaijiang` | 鸇（槐江北望） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-luwu` | 陸吾 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-tulou` | 土螻 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-qinyuan` | 欽原 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `bird-xishan-chun-kunlun` | 鶉鳥 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-strange-kunlun` | 怪鳥獸（崑崙段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-huayu-leyou` | 滑魚 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-jiao-yushan` | 狡 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `bird-xishan-shengyu-yushan` | 胜遇 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-beasts-changliu` | 文尾兽（長留段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `bird-xishan-birds-changliu` | 文首鸟（長留段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-zheng` | 狰 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-bifang` | 畢方 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-tian-gou` | 天狗 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `bird-xishan-bluebirds-sanwei` | 三青鳥（三危段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-aoyu-sanwei` | 𢕟𢓨 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `bird-xishan-chi-sanwei` | 鴟（三危段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-jishes-guishan3` | 積蛇 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dijiang` | 帝江 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-guan` | 讙 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `bird-xishan-qiyu-yiwang` | 鵸䳜 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-deer-shangshen` | 白鹿（上申段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `bird-xishan-danghu-shangshen` | 當扈 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-snakes-zhuci` | 衆蛇（諸次段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-wolf-yushan4` | 白狼（盂山） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-tiger-yushan4` | 白虎（盂山） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `bird-xishan-pheasant-yushan4` | 白雉（盂山） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `bird-xishan-zhai-yushan4` | 白翟（盂山） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-zuoniu-baiyu` | 㸲牛（白於段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-qianyang-baiyu` | 羬羊（白於段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `bird-xishan-xiao-baiyu` | 鴞（白於段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-manman-gangwei` | 蠻蠻（鼠身鳖首） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-white-yingdi` | 白鸟兽（英鞮段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-ranyi-yingdi` | 冉遺之魚 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-bo` | 駮 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-qiongqi-xishan` | 窮竒（西山经） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-luoyu` | 蠃魚 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-tiger-niaoshu` | 白虎（鳥鼠段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-saoyu-niaoshu` | 鰠魚 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-rupi-niaoshu` | 𩶯魮之魚 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-turtle-yanzi` | 龜（崦嵫阳） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-xishan-shuhu-yanzi` | 孰湖 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `bird-xishan-unnamed-yanzi` | 未名鸟（崦嵫末段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-huayu-qiuru` | 滑魚（求如） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-shuima-qiuru` | 水馬（求如） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-huanshu-daishan` | 䑏䟽（帶山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-qitu-daishan` | 鵸䳜（帶山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-youyu-daishan` | 儵魚（帶山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-heluo-qiaoming` | 何羅之魚 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-menghuai-qiaoming` | 孟槐 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-xixi-zhuoguang` | 鰼鰼之魚 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-lingyang-zhuoguang` | 麢羊（涿光） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-fan-zhuoguang` | 蕃（涿光） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-tuotuo-guoshan` | 橐駝（虢山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-yu-guoshan` | 寓（虢山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-ershu-danxun` | 耳䑕 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-mengji-shizhe` | 孟極 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-youan-bianchun` | 幽鴳 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-zuzi-manlian` | 足訾 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-jiao-manlian` | 鵁 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-zhu-jian` | 諸犍 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-baiye-danzhang` | 白鵺 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-nafu-guanti` | 那父 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-songsi-guanti` | 竦斯 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-maoniu-panhou` | 旄牛（潘侯） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-changshe-daxian` | 長蛇（大咸） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-chigui-dunhong` | 赤鮭（敦薨） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-si-dunhong` | 兕（敦薨） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-maoniu-dunhong` | 旄牛（敦薨） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-shijiu-dunhong` | 鳲鳩（敦薨） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-yayu-shaoxian` | 窫窳（少咸） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-peipei-shaoxian` | 䰽䰽之魚 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-zao-yufa` | 䲃魚 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-shanhui-yufa` | 山𤟤 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-zhuhuai-beiyue` | 諸懐 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-yi-beiyue` | 鮨魚 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-feiyi-hunxi` | 肥遺（渾夕蛇） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-yema-bicha` | 野马（羆差郭注） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-ma-beixian` | 马（北鮮） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-ma-dishan` | 马（隄山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-yao-dishan` | 狕 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-longgui-dishan` | 龍龜（隄山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-lv-xianyong` | 閭（縣雍） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-mi-xianyong` | 麋（縣雍） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-white-di-xianyong` | 白翟（縣雍） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-white-you-xianyong` | 白䳑（縣雍） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-ci-xianyong` | 鮆魚（縣雍） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-boma-duntou` | 𩣡馬（敦頭） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-paoxiao-gouwu` | 狍鴞 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-dugu-beixiao` | 獨𤞞 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-banmao-beixiao` | 𪄀𪃑 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-juji-liangqu` | 居暨 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-xiao-liangqu` | 囂（梁渠鸟） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-ma-huguan` | 马（湖灌） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-shan-huguan` | 䱇（湖灌） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-strange-snakes-huan` | 怪蛇（洹山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-hui-guishan` | 䮝（歸山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-fen-guishan` | 䴅（歸山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-renyu-longhou` | 人魚（龍侯） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-tianma-macheng` | 天馬（馬成） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-quju-macheng` | 鶌鶋 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-feishu-tianchi` | 飛䑕（天池） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-linghu-yangshan` | 領胡 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-xiangshe-yangshan` | 𧰼蛇（陽山鸟） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-xianfu-yangshan` | 𩹴父之魚 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-suanyu-jingshan` | 酸與（景山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-feiyi-pengpi` | 肥遺之蛇（彭毗） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-guxi-xiaohou` | 鴣𪄶（小侯） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-huangniao-xuanyuan` | 黄鳥（軒轅） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-white-snakes-shenqun` | 白蛇（神囷） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-flying-insects-shenqun` | 飛蟲（神囷） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-jingwei` | 精衛 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-huomin-xiushan` | 鱯黽（繡山物名异说） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-dongdong-taixi` | 䍶䍶（泰戱） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-tuotuo-raoshan` | 槖駝（饒山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-liuli-raoshan` | 鶹歷（饒山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-shiyu-raoshan` | 師魚（饒山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-yuan-ganshan` | 獂（乾山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-pi-lunshan` | 羆（倫山麋状兽） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-puyi-jieshi` | 蒲夷之魚（碣石） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-beishan-redhead-snake-mufeng` | 赤首白身大蛇（末段） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-yongyong-suzhu` | 鱅鱅之魚 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-huoshi-leishan` | 活師（藟山） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-congcong-xunzhuang` | 從從 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-zishu-xunzhuang` | 䖪䑕 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-zhen-xunzhuang` | 箴魚（栒状） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-gan-fantiao` | 鱤魚（番條） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-kanyu-chai` | 堪㐨之魚 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-kuafu-like-chai` | 夸父状彘毛兽（犲山未名） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-tiaoyong-dushan` | 䖺䗤 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-tongtong-taishan` | 狪狪 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-zilei-zhu` | 茈羸（竹山） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-lingling-kongsang-east` | 軨軨（东次二） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-shen-yigao` | 蜃（嶧皐） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-yao-yigao` | 珧（嶧皐） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-zhubie-geshan-head` | 珠蟞魚（葛山之首） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-qiuyu-yue` | 犰狳（餘峩） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-large-snake` | 大蛇（东山文本索引） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-zhunou-gengshan` | 朱獳 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-lihu-luqi` | 𪁐鶘（盧其） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-bibi-gufeng` | 獙獙（姑逢） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-longzhi-fuli` | 蠪姪 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-youyou-zhenshan` | 峳峳 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-jiegou-zhenshan` | 絜鈎 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-yuanhu-shihu` | 妴胡 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-qin-zhugou` | 𥧌魚（諸鈎） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-zhan-mengzi` | 鱣（孟子） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-wei-mengzi` | 鮪（孟子） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-xigui-qizhong` | 蠵龜（深澤） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-gege-qizhong` | 鮯鮯之魚 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-jingjing-muyu` | 精精（踇隅） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-xieju-beihao` | 猲狙 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-qique-beihao` | 鬿雀 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-qiu-maoshan` | 鱃魚（东山文本索引） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-zi-dongshi` | 茈魚（東始） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-bo-nvzheng` | 薄魚（女烝） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dangkang` | 当康 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-dongshan-hua-zitong` | 䱻魚（子桐） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-heyu` | 合窳 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-fei` | 蜚 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-zhongshan-nuo-gancao` | 㔮（甘棗） | 《山海经》 | 常规入口 | 《山海经·中山经》（《四部丛刊》景明成化本，郭璞传） |
| `beast-zhongshan-hao-quzhu` | 豪魚（渠豬） | 《山海经》 | 常规入口 | 《山海经·中山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-qingqiu` | 青丘之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-kunlun` | 昆仑之墟 | 《山海经》 | 常规入口 | 《海内西经》 |
| `place-yushan` | 玉山 | 《山海经》 | 常规入口 | 《西山经》 |
| `place-east-ranges` | 东山经山列 | 《山海经》 | 常规入口 | 《东山经》 |
| `place-south-ranges` | 南山经山列 | 《山海经》 | 常规入口 | 《南山经》 |
| `place-west-ranges` | 西山经山列 | 《山海经》 | 常规入口 | 《西山经》 |
| `place-north-ranges` | 北山经山列 | 《山海经》 | 常规入口 | 《北山经》 |
| `place-heichi` | 黑齿国（方位参照） | 《山海经》 | 常规入口 | 《海外东经》 |
| `place-fusang` | 汤谷／扶桑 | 《山海经》 | 常规入口 | 《海外东经》 |
| `place-chishui` | 赤水 | 《山海经》 | 常规入口 | 《大荒北经》 |
| `place-zhangwei` | 章尾山 | 《山海经》 | 常规入口 | 《大荒北经》 |
| `place-zhaoyao` | 招摇之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-niuyang` | 杻阳之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-fajiu` | 發鳩之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `domain-kunlun` | 昆仑 · 帝之下都 | 《山海经》 | 常规入口 | 《海内西经》 |
| `domain-yushan` | 玉山 · 西王母所居 | 《山海经》 | 常规入口 | 《西山经》 |
| `domain-zhangwei` | 章尾山 · 烛龙所居 | 《山海经》 | 常规入口 | 《大荒北经》 |
| `plant-zhuyu` | 祝余 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-migu` | 迷谷 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-liji` | 丽𪊨之水 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-guai` | 怪水 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xianyi` | 宪翼之水 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-ying-qingqiu` | 英水 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-jiyi` | 即翼之泽 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-yupei` | 育沛 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-nanshan-fang` | 汸水 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-nanshan-yu-receiver` | 淯 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-nanshan-ying-gui` | 英水 · 柜山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-nanshan-chishui-gui` | 赤水 · 柜山段 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-nanshan-tiao` | 苕水 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-nanshan-juqu` | 具区 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-nanshan-zhupi-fuyu` | 诸毗 · 浮玉段 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-nanshan-shu` | 䦠水 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-nanshan-hushao-receiver` | 虖勺 · 成山流入对象 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-nanshan-shao` | 勺水 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-nanshan-ju` | 湨 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-nanshan-lietu` | 列涂 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-nanshan-xun` | 洵水 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-nanshan-yan-marsh` | 阏之泽 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-nanshan-pang` | 滂水 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-nanshan-lu` | 鹿水 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-nanshan-zegeng` | 泽更之水 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-nanshan-yin` | 泿水 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-nanshan-dan` | 丹水 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-nanshan-bohai-south` | 㴾海 · 南山经 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-nanshan-fan` | 汎水 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-nanshan-hei` | 黑水 · 鸡山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-nanshan-zuo` | 佐水 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-nanshan-yan` | 棪木 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-nanshan-baigao` | 白䓘 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-nanshan-west-sea` | 西海 · 南山经 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-nanshan-east-sea` | 东海 · 南山经 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-huo` | 濩水 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-wei` | 渭（西山经） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-bili` | 萆荔 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-wenjing` | 文茎 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-tiao-fuyu` | 條（符禺山） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-fuyu` | 符禺之水 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-tiao-shicui` | 條（石脆山） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-guan` | 灌水 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-yu-shicui` | 禺水（石脆山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-liuzhe` | 流赭 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-yu-ying` | 禺水（英山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-zhao-ying` | 招水（英山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-huangguan` | 黄雚 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-zhu` | 竹水 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-dan-zhushan` | 丹水（竹山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-luo-zhushan` | 洛水（竹山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-shuiyu-zhushan` | 水玉（竹山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-panmu` | 盼木 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-xuncao` | 薰草 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-qi-yuci` | 漆水（羭次段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-yingyuan-yuci` | 嬰垣之玉 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-zhu-shishan` | 逐水（时山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-shuiyu-shishan` | 水玉（时山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-dan-nanshan` | 丹水（西山经南山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-dansu-nanshan` | 丹粟（西山经南山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-qian-dashi` | 涔水（大时段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-qing-dashi` | 清水（大时段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-han-dashi` | 汉水（西山经首列） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-silver-dashi` | 银（大时段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-white-jade-dashi` | 白玉（大时段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-mian-bozhong` | 沔（嶓冡段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-xiao-bozhong` | 囂水（嶓冡段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-tang-bozhong` | 汤水（嶓冡段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-taozhi-bozhong` | 桃枝（嶓冡段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-gouduan-bozhong` | 鈎端（嶓冡段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-gurong-bozhong` | 蓇蓉（嶓冡段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-duheng-tiandi` | 杜衡（天帝山） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-se-gaotu` | 薔水（皐塗段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-zhuzi-gaotu` | 诸资之水（皐塗段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-tu-gaotu` | 塗水（皐塗段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-jihuo-gaotu` | 集获之水（皐塗段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-dansu-gaotu` | 丹粟（皐塗段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-silver-gaotu` | 银（皐塗段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-gold-gaotu` | 黄金（皐塗段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-gui-gaotu` | 桂木（皐塗段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-yu-gaotu` | 礜（皐塗段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-wutiao-gaotu` | 無條（皐塗段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-zhujian-huangshan` | 竹箭（黄山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-pan-huangshan` | 盼水（黄山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-chi-huangshan` | 赤水（西山经） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-jade-huangshan` | 玉（黄山水文段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-zong-cuishan` | 㯶（翠山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-nan-cuishan` | 枏（翠山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-zhujian-cuishan` | 竹箭（翠山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-gold-cuishan` | 黄金（翠山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-jade-cuishan` | 玉（翠山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-westsea-guishan` | 西海（西山经） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-jade-guishan` | 玉（騩山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-qi-guishan` | 淒水（騩山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-caishi-guishan` | 采石（騩山水文段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-gold-guishan` | 黄金（騩山水文段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-dansu-guishan` | 丹粟（騩山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-copper-qianshan` | 铜（鈐山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-jade-qianshan` | 玉（鈐山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-niu-qianshan` | 杻（鈐山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-jiang-qianshan` | 橿（鈐山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-jin-taimao` | 金（㤗冐段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-iron-taimao` | 铁（㤗冐段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-yu-taimao` | 浴水（㤗冐段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-he-taimao` | 河（西山经） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-zaoyu-taimao` | 藻玉（㤗冐段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-gold-shuli` | 黄金（數歴段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-silver-shuli` | 银（數歴段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-niu-shuli` | 杻（數歴段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-jiang-shuli` | 橿（數歴段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-chu-shuli` | 楚水（數歴段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-pearl-shuli` | 珠（數歴水文段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-silver-gaoshan` | 银（髙山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-qingbi-gaoshan` | 青碧（髙山下） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-xionghuang-gaoshan` | 雄黄（髙山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-zong-gaoshan` | 㯶（髙山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-bamboo-gaoshan` | 竹（髙山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-jing-gaoshan` | 涇水（西山经次二列） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-qingshi-gaoshan` | 磬石（髙山水文段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-qingbi-water-gaoshan` | 青碧（髙山水文段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-red-copper-nvchuang` | 赤铜（女牀段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-shinie-nvchuang` | 石𣵀（女牀段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-gold-longshou` | 黄金（龍首山阳面） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-iron-longshou` | 鐡（龍首山阴面） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-tiao-longshou` | 苕水（龍首山） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-fine-jade-longshou` | 羙玉（龍首山水文） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-white-jade-lutai` | 白玉（鹿臺山上） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-silver-lutai` | 銀（鹿臺山下） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-qingshi-niaowei` | 磬石（鳥危山阳面） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-tan-niaowei` | 檀（鳥危山阴面） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-chu-niaowei` | 楮（鳥危山阴面） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-nvchuang-niaowei` | 女牀（鳥危段·所指未詳） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-niaowei` | 鳥危之水 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-dansu-niaowei` | 丹粟（鳥危段水文） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-white-jade-xiaoci` | 白玉（小次山上） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-red-copper-xiaoci` | 赤銅（小次山下） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-e-daci` | 堊（大次山阳面） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-bi-daci` | 碧（大次山阴面） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-jin-xunwu` | 金（薰吳段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-jade-xunwu` | 玉（薰吳段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-ji-quyang` | 稷（𢇨陽段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-nan-quyang` | 柟（𢇨陽段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-yuzhang-quyang` | 豫章（𢇨陽段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-tufu-zhongshou` | 㻬琈之玉（衆獸山上） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-tan-zhongshou` | 檀（衆獸山下） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-chu-zhongshou` | 楮（衆獸山下） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-gold-zhongshou` | 黄金（衆獸山下） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-jin-huangren` | 金（皇人山上） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-jade-huangren` | 玉（皇人山上） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-qingxionghuang-huangren` | 青雄黄（皇人山下） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-huang-huangren` | 皇水（皇人段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-dansu-huangren` | 丹粟（皇人段水文） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-gold-zhonghuang` | 黄金（中皇山上） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-huitang-zhonghuang` | 蕙棠（中皇山下） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-jin-xihuang` | 金（西皇山阳面） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-iron-xihuang` | 鐡（西皇山阴面） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-tan-laishan` | 檀（萊山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-chu-laishan` | 楮（萊山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-yaoze-chongwu` | 䍃之澤（崇吾段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-yanyuan-chongwu` | 䗡淵（崇吾段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-unnamed-chongwu` | 未名木（崇吾段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-ci-changsha` | 泚水（長沙段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-you-changsha` | 泑水（西山经） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-qingxionghuang-changsha` | 青雄黄（長沙段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-youze-buzhou` | 泑澤（不周段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-jia-guo-buzhou` | 嘉果（不周段·未命名） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-danmu-mishan` | 丹木（峚山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-dan-mishan` | 丹水（峚山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-jize-mishan` | 稷澤（峚山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-white-jade-mishan` | 白玉（峚山丹水） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-yugao-mishan` | 玉膏（峚山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-xuanyu-mishan` | 𤣥玉（峚山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-yurong-mishan` | 玉榮（峚山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-jinyu-mishan` | 瑾瑜之玉（峚山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-wetlands-mi-zhong` | 泽地（峚至鍾） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-guan-taiqi` | 𮗚水（㤗噐段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-eastsea-taiqi` | 東海（㤗噐段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-qiushi-huaijiang` | 丘時之水（槐江段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-qingxionghuang-huaijiang` | 青雄黃（槐江山上） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-langgan-huaijiang` | 藏琅玕（槐江段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-gold-above-huaijiang` | 黄金（槐江山上） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-jade-above-huaijiang` | 玉（槐江山上） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-dansu-huaijiang` | 丹粟（槐江阳面） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-shaded-goods-huaijiang` | 采黄金銀（槐江阴面） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-daze-huaijiang` | 大澤（槐江西望） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-jade-daze-huaijiang` | 玉（槐江西望大澤） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-yaomu-ruo-huaijiang` | 榣木之有若（槐江西望） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-flowing-huaijiang` | 滛水（槐江东望） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-shatang-kunlun` | 沙棠 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-pin-kunlun` | 薲草 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-he-kunlun` | 河水（崑崙段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-chi-kunlun` | 赤水（崑崙段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-fantian-kunlun` | 汜天之水 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-yang-kunlun` | 洋水（崑崙段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-choutu-kunlun` | 醜塗之水 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-hei-kunlun` | 黑水（崑崙段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-tao-leyou` | 桃水 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-jize-leyou` | 稷澤（樂游段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-jade-leyou` | 白玉（樂游段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-jade-luomushan` | 玉（蠃母山上） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-stone-luomushan` | 青石（蠃母山下） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-xun-xuanyuan` | 洵水 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-hei-xuanyuan` | 黑水（軒轅段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-dansu-xuanyuan` | 丹粟（洵水段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-xionghuang-xuanyuan` | 青雄黄（洵水段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-he-jishi` | 河水（積石段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-jade-changliu` | 文玉石 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-yaobi-zhange` | 瑶碧 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-zhuoyu-yinshan3` | 濁浴之水 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-fan-yinshan3` | 蕃澤 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-shell-yinshan3` | 文貝 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-zong-futang` | 㯶（符愓段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-nan-futang` | 柟（符愓段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-gold-futang` | 金（符愓山下） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-jade-futang` | 玉（符愓山下） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-jade-guishan3` | 玉（西次三经騩山） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-gold-tianshan` | 金（天山） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-jade-tianshan` | 玉（天山） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-xionghuang-tianshan` | 青雄黄（天山） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-ying-tianshan` | 英水 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-yingduan-youshan` | 嬰短之玉 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-jinyu-youshan` | 瑾瑜之玉（泑山阳） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-xionghuang-youshan` | 青雄黄（泑山阴） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-gold-yiwang` | 金（翼望段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-jade-yiwang` | 玉（翼望段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-gu-yinshan4` | 榖（西次四经隂山） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-mao-yinshan4` | 茆（隂山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-fan-yinshan4` | 蕃（隂山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-yin-yinshan4` | 隂水 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-luo-yinshan4` | 洛（西次四经首段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-zicao-laoshan` | 茈草（勞山） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-ruo-laoshan` | 弱水（勞山） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-luo-laoshan` | 洛（勞山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-er-bafu` | 洱水 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-luo-bafu` | 洛（罷父段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-zibi-bafu` | 茈碧 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-gu-shenshan` | 榖（申山上） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-zuo-shenshan` | 柞（申山上） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-niu-shenshan` | 杻（申山下） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-jiang-shenshan` | 橿（申山下） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-gold-shenshan` | 金（申山阳） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-jade-shenshan` | 玉（申山阳） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-qu-shenshan` | 區水 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-he-shenshan` | 河（申山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-sang-niaoshan` | 桑（鳥山上） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-chu-niaoshan` | 楮（鳥山下） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-iron-niaoshan` | 鐡（鳥山阴） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-jade-niaoshan` | 玊（鳥山阳） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-ru-niaoshan` | 辱水 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-he-niaoshan` | 河（鳥山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-stone-shangshen` | 硌石 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-zhen-shangshen` | 榛（上申下） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-hu-shangshen` | 楛（上申下） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-tang-shangshen` | 湯水 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-he-shangshen` | 河（上申段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-zhuci-zhuci` | 諸次之水 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-he-zhuci` | 河（諸次段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-lacquer-haoshan` | 漆（號山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-zong-haoshan` | 㯶（號山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-yao-haoshan` | 葯 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-xian-haoshan` | 䖀 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-xiongqiong-haoshan` | 芎藭 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-qin-haoshan` | 汵石 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-duan-haoshan` | 端水 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-he-haoshan` | 河（號山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-iron-yushan4` | 鐡（盂山阴） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-copper-yushan4` | 銅（盂山阳） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-sheng-yushan4` | 生水 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-he-yushan4` | 河（盂山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-pine-baiyu` | 松（白於上） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-cypress-baiyu` | 柏（白於上） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-li-baiyu` | 櫟（白於下） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-tan-baiyu` | 檀（白於下） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-luo-baiyu` | 洛水（白於阳） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-wei-baiyu` | 渭（白於段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-jia-baiyu` | 夾水 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-sheng-baiyu` | 生水（白於段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-shen-shenshou` | 申水 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-jade-shenshou` | 白玉（申首段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-jing-jinggu` | 涇水（涇谷段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-wei-jinggu` | 渭（涇谷段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-metal-jinggu` | 白金（涇谷） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-jade-jinggu` | 白玉（涇谷） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-qi-gangshan` | 柒木 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-tufuyu-gangshan` | 㻬琈之玉（剛山） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-gang-gangshan` | 剛水 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-wei-gangshan` | 渭（剛山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-luo-gangwei` | 洛水（剛山尾） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-he-gangwei` | 河（剛山尾） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-mu-yingdi` | 𣾰木 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-gold-yingdi` | 金（英鞮下） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-jade-yingdi` | 玉（英鞮下） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-wan-yingdi` | 涴水 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-lingyang-yingdi` | 𨹧羊之澤 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-jade-sun-zhongqu` | 玉（中曲阳） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-xionghuang-zhongqu` | 雄黄（中曲阴） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-jade-shade-zhongqu` | 白玉（中曲阴） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-gold-zhongqu` | 金（中曲阴） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-huai-zhongqu` | 櫰木 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-meng-guishan4` | 𪷟水 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-yang-guishan4` | 洋水（邽山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-shell-guishan4` | 黄貝 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-jade-niaoshu` | 白玉（鳥鼠段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-wei-niaoshu` | 渭水（鳥鼠段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-he-niaoshu` | 河（鳥鼠段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-lan-niaoshu` | 濫水 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-han-niaoshu` | 漢水（鳥鼠段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-xishan-dan-yanzi` | 丹木（崦嵫段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-jade-yanzi` | 玉（崦嵫阴） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-tiao-yanzi` | 苕水（崦嵫） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-xishan-sea-yanzi` | 海（崦嵫段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-xishan-whetstones-yanzi` | 砥礪 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-ji-danhu` | 机木 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-huacao-danhu` | 華草（單狐） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-feng-danhu` | 漨水（單狐） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-you-danhu` | 泑水（北山经） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-pishi-danhu` | 芘石（單狐水文） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-wenshi-danhu` | 文石（單狐水文） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-copper-qiuru` | 铜（求如） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-qiuru` | 玉（求如） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-hua-qiuru` | 滑水（求如） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-zhupi-qiuru` | 諸毗之水（北山经） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-daishan` | 玉（帶山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-qingbi-daishan` | 青碧（帶山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-peng-daishan` | 彭水（帶山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-pihu-daishan` | 芘湖之水（帶山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-qiao-qiaoming` | 譙水（譙明） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-qingxionghuang-qiaoming` | 青雄黄（譙明） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-xiao-zhuoguang` | 囂水（涿光） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-pine-zhuoguang` | 松（涿光） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-bai-zhuoguang` | 栢（涿光） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-zong-zhuoguang` | 㯶（涿光） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-jiang-zhuoguang` | 橿（涿光） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-qi-guoshan` | 漆（虢山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-tong-guoshan` | 桐（虢山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-ju-guoshan` | 椐（虢山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-guoshan` | 玉（虢山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-iron-guoshan` | 铁（虢山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-yi-guoshan` | 伊水（虢山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-guowei` | 玉（虢山之尾） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-yu-guowei` | 魚水（虢山之尾） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-wenbei-guowei` | 文貝（虢山之尾） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-chu-danxun` | 樗（丹熏） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-bai-danxun` | 柏（丹熏） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-jiu-danxun` | 韭（丹熏） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-xie-danxun` | 薤（丹熏） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-danhuo-danxun` | 丹雘（丹熏） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-xun-danxun` | 熏水（丹熏） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-tang-danxun` | 棠水（丹熏） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-yaobi-shizhe` | 瑶碧（石者） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-ci-shizhe` | 泚水（石者） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-cong-bianchun` | 葱（邊春） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-kui-bianchun` | 葵（邊春） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-jiu-bianchun` | 韭（邊春） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-tao-bianchun` | 桃（邊春） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-li-bianchun` | 李（邊春） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-gang` | 杠水（北山经） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-youze` | 泑澤（北山经） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-li-danzhang` | 櫟水（單張） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-chu-guanti` | 樗（灌題） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-zhe-guanti` | 柘（灌題） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-sand-guanti` | 流沙（灌題） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-whetstone-guanti` | 砥（灌題） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-jianghan-guanti` | 匠韓之水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-magnetic-guanti` | 磁石（灌題水文） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-pine-panhou` | 松（潘侯） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-bai-panhou` | 栢（潘侯） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-zhen-panhou` | 榛（潘侯） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-hu-panhou` | 楛（潘侯） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-panhou` | 玉（潘侯） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-iron-panhou` | 铁（潘侯） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-bian-panhou` | 邊水（潘侯） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-lize-panhou` | 櫟澤（潘侯） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-daxian` | 玉（大咸） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-zong-dunhong` | 㯶（敦薨） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-nan-dunhong` | 柟（敦薨） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-zicao-dunhong` | 茈草（敦薨） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-dunhong` | 敦薨之水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-qingbi-shaoxian` | 青碧（少咸） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-dun-shaoxian` | 敦水（少咸） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-yanmen-shaoxian` | 鴈門之水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-huaize-yufa` | 瀤澤之水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-taize` | 㤗澤（北山经） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-zhi-beiyue` | 枳（北嶽） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-ji-beiyue` | 𣗥（北嶽） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-gang-beiyue` | 刚木（北嶽） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-zhuhuai-beiyue` | 諸懐之水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-xiao-beiyue-hunxi` | 囂水（北嶽—渾夕） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-copper-hunxi` | 铜（渾夕） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-hunxi` | 玉（渾夕） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-sea-hunxi` | 海（渾夕水文） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-cong-beidan` | 葱（北單） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-jiu-beidan` | 韭（北單） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-xian-beixian` | 鮮水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-tuwu-beixian` | 涂吾之水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-di-dishan` | 隄水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-guancen` | 玉（管涔） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-fen-guancen` | 汾水（管涔） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-shaoyang` | 玉（少陽） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-red-silver-shaoyang` | 赤銀 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-suan-shaoyang` | 酸水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-ochre-shaoyang` | 羙赭（少陽） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-xianyong` | 玉（縣雍） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-copper-xianyong` | 铜（縣雍） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-jin-xianyong` | 晉水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-qingbi-huqi` | 青碧（狐岐） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-sheng-huqi` | 勝水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-dark-jade-huqi` | 蒼玉（狐岐） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-wei-baisha` | 鮪水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-white-jade-baisha` | 白玉（白沙） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-kuang` | 狂水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-fu-kuang` | 浮水（狂山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-fine-jade-kuang` | 羙玉（狂山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-copper-zhuyu` | 铜（諸餘） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-zhuyu` | 玉（諸餘） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-pine-zhuyu` | 松（諸餘） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-bai-zhuyu` | 栢（諸餘） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-zhuyu` | 諸餘之水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-mao` | 旄水（諸餘—敦頭） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-gold-duntou` | 金（敦頭） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-duntou` | 玉（敦頭） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-yinze-duntou` | 印澤 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-gouwu` | 玉（鉤吾） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-copper-gouwu` | 铜（鉤吾） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-bi-beixiao` | 碧（北囂） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-beixiao` | 玉（北囂） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-cen-beixiao` | 涔水（北囂） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-qiongze-beixiao` | 卭澤 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-gold-liangqu` | 金（梁渠） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-liangqu` | 玉（梁渠） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-xiu-liangqu` | 脩水（梁渠） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-yanmen-liangqu` | 鴈門（梁渠水名） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-huguan` | 玉（湖灌） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-bi-huguan` | 碧（湖灌） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-huguan` | 湖灌之水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-sea-huguan` | 海（湖灌） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-redgrain-huguan` | 赤理无名木（湖灌） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-gold-huan` | 金（洹山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-huan` | 玉（洹山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-sansang-huan` | 三桑（洹山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-fruit-trees-huan` | 百果树（洹山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-gold-dunti` | 金（敦題） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-dunti` | 玉（敦題） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-north-sea-dunti` | 北海（敦題） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-gold-guishan` | 金（歸山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-guishan` | 玉（歸山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-bi-guishan` | 碧（歸山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-gold-longhou` | 金（龍侯） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-longhou` | 玉（龍侯） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-juejue-longhou` | 决决之水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-wenstone-macheng` | 文石（馬成） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-gold-macheng` | 金（馬成） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-macheng` | 玉（馬成） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-xianshan` | 玉（咸山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-copper-xianshan` | 铜（咸山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-tiaojian-xianshan` | 條菅之水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-changze-xianshan` | 長澤（咸山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-pine-xianshan` | 松（咸山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-bai-xianshan` | 栢（咸山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-zi-xianshan` | 茈草（咸山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-qisuan-xianshan` | 噐酸（未详物产） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-wenstone-tianchi` | 文石（天池） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-yellow-e-tianchi` | 黄堊（天池） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-sheng-tianchi` | 澠水（天池） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-yangshan` | 玉（陽山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-gold-yangshan` | 金（陽山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-copper-yangshan` | 铜（陽山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-liu-yangshan` | 留水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-dark-jade-benwen` | 蒼玉（賁聞） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-yellow-e-benwen` | 黄堊（賁聞） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-nie-stone-benwen` | 𣵀石（賁聞） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-stones-wangwu` | 石（王屋） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-lian-wangwu` | 㶌水（王屋） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-jiaoshan` | 玉（教山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-gold-fawan` | 金（發丸） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-fawan` | 玉（發丸） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-jiao-jiaoshan` | 教水（乾河） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-ochre-jingshan` | 赭（景山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-jingshan` | 玉（景山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-yanfan-jingshan` | 𬐱販之澤（景山南望） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-shaoze-jingshan` | 少澤（景山北望） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-zhuyu-jingshan` | 藷藇（景山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-qinjiao-jingshan` | 秦椒（景山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-dark-jade-mengmen` | 蒼玉（孟門） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-gold-mengmen` | 金（孟門） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-yellow-e-mengmen` | 黄堊（孟門） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-nie-mengmen` | 𣵀石（孟門） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-fine-jade-pingshan` | 羙玉（平山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-ping-pingshan` | 平水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-fine-jade-jingshan-east` | 羙玉（京山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-red-copper-jingshan-east` | 赤铜（京山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-xuansu-jingshan-east` | 𤣥䃤（京山黑砥） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-lacquer-jingshan-east` | 漆木（京山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-bamboo-jingshan-east` | 竹（京山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-gao-jingshan-east` | 髙水（京山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-gold-chongwei` | 金（虫尾） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-chongwei` | 玉（虫尾） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-qingbi-chongwei` | 青碧（虫尾） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-bamboo-chongwei` | 竹（虫尾） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-dan-chongwei` | 丹水（虫尾） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-bo-chongwei` | 薄水（虫尾） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-huangze-chongwei` | 黄澤（虫尾、小侯） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-gold-pengpi` | 金（彭毗） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-pengpi` | 玉（彭毗） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-zaolin-pengpi` | 蚤林之水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-fei-pengpi` | 肥水（彭毗） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-chuang-pengpi` | 牀水（肥水所注） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-mingzhang-xiaohou` | 明漳之水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-gold-taitou` | 金（泰頭） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-taitou` | 玉（泰頭） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-arrow-bamboo-taitou` | 竹箭（泰頭） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-gong-taitou` | 共水（泰頭） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-huchi-taitou` | 虖池／虖沱（北山经文本索引） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-copper-xuanyuan` | 铜（軒轅） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-bamboo-xuanyuan` | 竹（軒轅） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-gold-yeli` | 金（謁戾） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-yeli` | 玉（謁戾） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-pine-yeli` | 松（謁戾） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-bai-yeli` | 栢（謁戾） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-qin-yeli` | 沁水（謁戾、泰戱文本索引） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-danlin-yeli` | 丹林之水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-yinghou-yeli` | 嬰侯之水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-fan-yeli` | 汜水（嬰侯所注） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-gold-juru` | 金（沮洳） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-juru` | 玉（沮洳） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-qi-juru` | 濝水（沮洳） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-wenstone-shenqun` | 文石（神囷） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-huang-shenqun` | 黄水（神囷） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-huan-shenqun` | 洹水（黄水所注） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-fu-shenqun` | 滏水（神囷、錫山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-ou-shenqun` | 歐水（滏水所注） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-zhe-fajiu` | 柘木（發鳩） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-donghai-fajiu` | 東海（精衛叙事） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-zhang-fajiu` | 漳水、濁漳（發鳩、少山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-wood-fajiu` | 木（精衛所衔） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-stones-fajiu` | 石（精衛所衔） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-gold-shaoshan` | 金（少山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-shaoshan` | 玉（少山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-copper-shaoshan` | 铜（少山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-qingzhang-shaoshan` | 清漳之水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-xishan-north` | 玉（錫山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-whetstone-xishan-north` | 砥（錫山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-niushou-xishan-north` | 牛首之水（錫山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-fine-jade-jingshan-after-xi` | 羙玉（錫山北景山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-jing-after-xi` | 景水（錫山北景山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-haize-jingshan-after-xi` | 海澤（景水所注） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-tishou` | 玉（題首） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-stones-tishou` | 石（題首） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-xiushan` | 玉（繡山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-qingbi-xiushan` | 青碧（繡山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-xun-xiushan` | 栒（繡山木） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-shaoyao-xiushan` | 芍藥（繡山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-qiongqiong-xiushan` | 芎窮（繡山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-wei-xiushan` | 洧水（繡山、柘山文本索引） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-yang-songshan` | 陽水（松山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-gold-dunyu` | 金（敦與） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-dunyu` | 玉（敦與） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-suo-dunyu` | 溹水（敦與） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-tailu-dunyu` | 泰陸之水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-zhi-dunyu` | 泜水（敦與） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-peng-dunyu` | 彭水（敦與受水名） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-huai-dunyu` | 槐水（敦與） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-zhize-dunyu` | 泜澤（槐水所注） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-gold-zheshan` | 金（柘山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-zheshan` | 玉（柘山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-iron-zheshan` | 铁（柘山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-liju-zheshan` | 歷聚之水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-green-jade-weilong` | 碧玉（維龍） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-gold-weilong` | 金（維龍） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-iron-weilong` | 铁（維龍） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-fei-weilong` | 肥水（維龍） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-gaoze-weilong` | 皐澤（維龍） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-changtie-weilong` | 敞鐡之水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-daze-weilong` | 大澤（敞鐡所注） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-leishi-weilong` | 礨石（維龍） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-shiyu-baima` | 石玉（白馬） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-iron-baima` | 鐡（白馬） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-red-copper-baima` | 赤铜（白馬） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-muma-baima` | 木馬之水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-kongsang-north` | 空桑之水（北山经） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-gold-taixi` | 金（泰戱） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-taixi` | 玉（泰戱） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-lou-taixi` | 漊水（泰戱所注） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-yenu-taixi` | 液女之水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-gold-shishan` | 金（石山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-shishan` | 玉（石山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-huohuo-shishan` | 濩濩之水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-xianyu-shishan` | 鮮于之水（石山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-gaotu-tongrong` | 皐涂之水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-louye-tongrong` | 漊液水（童戎受水名） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-zong-gaoshi` | 㯶（髙是木） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-tiao-gaoshi` | 條草（髙是） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-zi-gaoshi` | 滋水（髙是） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-kou-gaoshi` | 𣸦水（髙是） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-fine-jade-lushan` | 羙玉（陸山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-tan-lushan` | 𨜰水（陸山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-ban-yishan` | 般水（沂山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-yingstone-yanshan` | 嬰石（燕山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-yan-yanshan` | 燕水（燕山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-yaobi-raoshan` | 瑶碧（饒山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-liguo-raoshan` | 歷虢之水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-gold-ganshan` | 金（乾山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-ganshan` | 玉（乾山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-iron-ganshan` | 鐡（乾山） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-lun-lunshan` | 倫水 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-jieshi` | 玉（碣石） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-qingbi-jieshi` | 青碧（碣石） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-sheng-jieshi` | 繩水（碣石） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-didu` | 玉（帝都） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-gold-didu` | 金（帝都） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-taize-didu` | 泰澤（帝都水行） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-yu-youdu-mufeng` | 浴水（幽都相邻记述） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-beishan-he` | 河（北山经） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-shi` | 食水（东山文本索引） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-sea` | 海（东山水文文本索引） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-jade-leishan` | 玉（藟山） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-gold-leishan` | 金（藟山） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-hu` | 湖水（藟山、栒状文本索引） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-gold-xunzhuang` | 金（栒状） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-jade-xunzhuang` | 玉（栒状） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-qingbistone-xunzhuang` | 青碧石（栒状） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-zhi-xunzhuang` | 𣲵水（栒状） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-sand-fantiao` | 沙（番條） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-jian-fantiao` | 減水（番條） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-dongshan-qi-guer` | 漆（姑兒） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-dongshan-sang-guer` | 桑（姑兒） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-dongshan-zhe-guer` | 柘（姑兒） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-guer` | 姑兒之水 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-jade-gaoshi-east` | 玉（髙氏山上） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-gold-zhusheng` | 金（諸繩水文） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-jade-zhusheng` | 玉（諸繩水文） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-zhusheng` | 諸繩之水 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-ze-gaoshi` | 澤（髙氏受水体） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-zhenstone-gaoshi` | 箴石（髙氏） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-dongshan-sang-yue` | 桑（嶽山） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-dongshan-chu-yue` | 樗（嶽山） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-gold-luo` | 金（濼水文） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-jade-luo` | 玉（濼水文） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-luo` | 濼水 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-ze-yue` | 澤（嶽山受水体） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-unnamed-chai` | 水（犲山下） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-gold-du` | 金（獨山） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-jade-du` | 玉（獨山） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-fine-stone-du` | 羙石（獨山） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-motu` | 末塗之水 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-mian` | 沔（末塗受水体） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-jade-tai` | 玉（泰山） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-gold-tai` | 金（泰山） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-water-jade-huan` | 水玉（環水文） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-huan` | 環水 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-jiang` | 江（泰山、竹山文本索引） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-yaobi-zhu` | 瑶碧（竹山） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-ji-zhu` | 激水（竹山） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-qutan` | 娶檀之水 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-min-marsh` | 湣澤 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-dongshan-gu-caoxi` | 榖（曹夕） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-gold-yigao` | 金（嶧皐） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-jade-yigao` | 玉（嶧皐） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-white-earth-yigao` | 白堊（嶧皐） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-yigao` | 嶧皐之水 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-jinv` | 激女之水 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-dili-geshan-tail` | 砥礪（葛山之尾） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-li-geshan-head` | 澧水（葛山之首） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-yu-marsh` | 余澤（澧水受水体） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-zayu` | 雜余之水 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-huang-yue` | 黄水（雜余受水体） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-dongshan-zi-yue` | 梓（餘峩） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-dongshan-nan-yue` | 柟（餘峩） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-dongshan-jing-yue` | 荆（餘峩） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-dongshan-qi-yue` | 𦬊（餘峩） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-unnamed-dufu` | 水（杜父未名） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-shuibi-geng` | 水碧（耿山） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-sand-luqi` | 沙（盧其） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-stone-luqi` | 石（盧其） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-sha-luqi` | 沙水（盧其） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-cen` | 涔水 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-unnamed-gushe` | 水（姑射未名） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-stone-north-gushe` | 石（北姑射） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-unnamed-south-gushe` | 水（南姑射未名） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-bi-bishan` | 碧（碧山） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-water-jade-bishan` | 水玉（碧山） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-gold-weishi` | 金（維氏） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-jade-weishi` | 玉（維氏） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-yuan-weishi` | 原水（維氏） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-sha-marsh` | 沙澤（原水受水体） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-gold-gufeng` | 金（姑逢） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-jade-gufeng` | 玉（姑逢） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-gold-fuli` | 金（鳬麗） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-jade-fuli` | 玉（鳬麗） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-zhenstone-fuli` | 箴石（鳬麗） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-zhen` | 䃌水 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-hu-marsh` | 湖澤（䃌山东望） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-gold-shihu` | 金（尸胡） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-jade-shihu` | 玉（尸胡） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-dongshan-ji-shihu` | 𣗥（尸胡） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-dongshan-peach-qi` | 桃（岐山） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-dongshan-plum-qi` | 李（岐山） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-sand-zhugou` | 沙（諸鈎） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-stone-zhugou` | 石（諸鈎） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-sand-zhongfu` | 沙（中父） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-sand-hushe` | 沙（胡射） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-stone-hushe` | 石（胡射） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-dongshan-zi-mengzi` | 梓（孟子） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-dongshan-tong-mengzi` | 桐（孟子） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-dongshan-peach-mengzi` | 桃（孟子） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-dongshan-plum-mengzi` | 李（孟子） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-dongshan-junpu-mengzi` | 菌蒲（孟子） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-biyang` | 碧陽水（孟子） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-jade-qizhong` | 玉（跂踵） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-shen-marsh` | 深澤（跂踵） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-gold-muyu` | 金（踇隅） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-jade-muyu` | 玉（踇隅） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-ochre-muyu` | 赭（踇隅） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-you-sea` | 幼海（無皐南望） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-north-sea` | 北海（北號所临） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-dongshan-unnamed-tree-beihao` | 木（北號未名） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-cangti` | 蒼體之水 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-zhan-water` | 展水 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-cang-jade-dongshi` | 蒼玉（東始） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-dongshan-qi-tree-dongshi` | 𦬊木（東始） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-ci-dongshi` | 泚水（東始） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-fine-shell-dongshi` | 羙貝（東始水文） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-shigao` | 石膏水（女烝） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-ge-water` | 鬲水 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-gold-qinshan` | 金（欽山） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-jade-qinshan` | 玉（欽山） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-shi-qinshan` | 師水（欽山） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-gao-marsh` | 皐澤（師水受水体） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-patterned-shell-qin` | 文貝（欽山水文） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-zitong` | 子桐之水 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-yuru-marsh` | 餘如之澤 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-gold-yanshan` | 金（剡山） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-jade-yanshan` | 玉（剡山） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-gold-taishan-range4` | 金（太山） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-jade-taishan-range4` | 玉（太山） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-dongshan-zhenwood-tai4` | 楨木（太山） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-gou-tai4` | 鈎水（太山） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-dongshan-lao-water` | 勞水 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-zhongshan-gong-gancao` | 共水（甘棗） | 《山海经》 | 常规入口 | 《山海经·中山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-zhongshan-he` | 河（中山首列文本索引） | 《山海经》 | 常规入口 | 《山海经·中山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-zhongshan-niu-gancao` | 杻木（甘棗） | 《山海经》 | 常规入口 | 《山海经·中山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-zhongshan-tuo-gancao` | 蘀（甘棗） | 《山海经》 | 常规入口 | 《山海经·中山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-zhongshan-jiang-lier` | 橿（歴兒） | 《山海经》 | 常规入口 | 《山海经·中山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-zhongshan-li-lier` | 櫔木（歴兒） | 《山海经》 | 常规入口 | 《山海经·中山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-zhongshan-bamboo-quzhu` | 竹（渠豬） | 《山海经》 | 常规入口 | 《山海经·中山经》（《四部丛刊》景明成化本，郭璞传） |
| `water-zhongshan-quzhu` | 渠豬之水 | 《山海经》 | 常规入口 | 《山海经·中山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-zhaoyao` | 招摇之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-tangting` | 堂庭之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-yuanyi` | 猨翼之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-niuyang` | 杻阳之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-di` | 祗山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-danyuan` | 亶爰之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-jishan` | 基山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-qingqiu` | 青丘之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-jiwei` | 箕尾之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-range1` | 䧿山总述与祭祀 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-gui` | 柜山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-changyou` | 长右之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-yaoguang` | 尧光之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-yu` | 羽山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-qufu` | 瞿父之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-gouyu` | 句余之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-fuyu` | 浮玉之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-cheng` | 成山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-kuaiji` | 会稽之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-yi` | 夷山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-pugou` | 仆勾之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-xun` | 洵山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-hushao` | 虖勺之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-quwu` | 区吴之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-xianyin` | 咸阴之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-luwu` | 鹿吴之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-qiwu` | 漆吴之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-range2` | 南次二经总述与祭祀 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-tianyu` | 天虞之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-daoguo` | 祷过之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-danxue` | 丹穴之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-fashuang` | 发爽之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-maowei` | 旄山之尾 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-feitou` | 非山之首 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-yangjia` | 阳夹之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-guanxiang` | 灌湘之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-ji` | 鸡山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-lingqiu` | 令丘之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-lunzhe` | 仑者之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-yugao` | 禺槀之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-nanyu` | 南禺之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-range3` | 南次三经总述与祭祀 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-nanshan-total` | 南山经篇末总计 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-qianlai` | 钱来之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-songguo` | 松果之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-taihua` | 太华之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-xiaohua` | 小华之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-fuyu` | 符禺之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-shicui` | 石脆之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-ying` | 英山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-zhushan` | 竹山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-fushan` | 浮山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-yuci` | 羭次之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-shishan` | 时山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-nanshan-west` | 南山（西山经） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-dashi` | 大时之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-bozhong` | 嶓冡之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-tiandi` | 天帝之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-gaotu` | 皐塗之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-huangshan` | 黄山（西山经） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-cuishan` | 翠山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-guishan` | 騩山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-range1-summary` | 西山首列总括与祭礼 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-qianshan` | 鈐山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-taimao` | 㤗冐之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-shuli` | 數歴之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-gaoshan` | 髙山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-nvchuang` | 女牀之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-longshou` | 龍首之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-lutai` | 鹿臺之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-niaowei` | 鳥危之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-xiaoci` | 小次之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-daci` | 大次之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-xunwu` | 薰吳之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-quyang` | 𢇨陽之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-zhongshou` | 衆獸之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-huangren` | 皇人之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-zhonghuang` | 中皇之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-xihuang` | 西皇之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-laishan` | 萊山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-range2-summary` | 西次二经总括与祭礼 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-chongwu` | 崇吾之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-changsha` | 長沙之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-buzhou` | 不周之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-mishan` | 峚山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-zhongshan` | 鍾山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-taiqi` | 㤗噐之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-huaijiang` | 槐江之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-kunlun` | 崑崙之丘 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-leyou` | 樂游之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-luomushan` | 蠃母之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-yushan` | 玉山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-xuanyuan` | 軒轅之丘 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-jishi` | 積石之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-changliu` | 長留之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-zhange` | 章莪之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-yinshan3` | 隂山（西次三经） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-futang` | 符愓之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-sanwei` | 三危之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-guishan3` | 騩山（西次三经） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-tianshan` | 天山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-youshan` | 泑山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-yiwang` | 翼望之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-range3-summary` | 西次三经总括与祠礼 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-yinshan4` | 隂山（西次四经） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-laoshan` | 勞山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-bafu` | 罷父之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-shenshan` | 申山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-niaoshan` | 鳥山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-shangshen` | 上申之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-zhuci` | 諸次之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-haoshan` | 號山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-yushan4` | 盂山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-baiyu` | 白於之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-shenshou` | 申首之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-jinggu` | 涇谷之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-gangshan` | 剛山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-gangwei` | 剛山之尾 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-yingdi` | 英鞮之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-zhongqu` | 中曲之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-guishan4` | 邽山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-niaoshu` | 鳥鼠同穴之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-yanzi` | 崦嵫之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-range4-summary` | 西次四经总括与祠礼 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-xishan-western-total` | 西山经篇末总计 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-danhu` | 單狐之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-qiuru` | 求如之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-daishan` | 帶山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-qiaoming` | 譙明之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-zhuoguang` | 涿光之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-guoshan` | 虢山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-guowei` | 虢山之尾 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-danxun` | 丹熏之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-shizhe` | 石者之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-bianchun` | 邊春之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-manlian` | 蔓聮之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-danzhang` | 單張之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-guanti` | 灌題之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-panhou` | 潘侯之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-xiaoxian` | 小咸之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-daxian` | 大咸之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-dunhong` | 敦薨之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-shaoxian` | 少咸之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-yufa` | 獄法之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-beiyue` | 北嶽之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-hunxi` | 渾夕之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-beidan` | 北單之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-bicha` | 羆差之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-beixian` | 北鮮之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-dishan` | 隄山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-range1-summary` | 北山经首列总括与祭礼 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-guancen` | 管涔之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-shaoyang` | 少陽之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-xianyong` | 縣雍之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-huqi` | 狐岐之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-baisha` | 白沙山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-ershi` | 爾是之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-kuang` | 狂山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-zhuyu` | 諸餘之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-duntou` | 敦頭之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-gouwu` | 鉤吾之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-beixiao` | 北囂之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-liangqu` | 梁渠之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-guguan` | 姑灌之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-huguan` | 湖灌之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-huan` | 洹山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-dunti` | 敦題之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-range2-summary` | 北次二经总括与祭礼 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-taihang` | 太行之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-longhou` | 龍侯之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-macheng` | 馬成之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-xianshan` | 咸山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-tianchi` | 天池之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-yangshan` | 陽山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-benwen` | 賁聞之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-wangwu` | 王屋之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-jiaoshan` | 教山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-jingshan` | 景山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-mengmen` | 孟門之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-pingshan` | 平山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-jingshan-east` | 京山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-chongwei` | 虫尾之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-pengpi` | 彭毗之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-xiaohou` | 小侯之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-taitou` | 泰頭之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-xuanyuan` | 軒轅之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-yeli` | 謁戾之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-juru` | 沮洳之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-shenqun` | 神囷之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-fajiu` | 發鳩之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-shaoshan` | 少山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-xishan-north` | 錫山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-jingshan-after-xi` | 景山（錫山北） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-tishou` | 題首之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-xiushan` | 繡山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-songshan` | 松山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-dunyu` | 敦與之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-zheshan` | 柘山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-weilong` | 維龍之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-baima` | 白馬之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-kongsang-north` | 空桑之山（北山经） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-taixi` | 泰戱之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-shishan` | 石山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-tongrong` | 童戎之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-gaoshi` | 髙是之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-lushan` | 陸山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-yishan` | 沂山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-yanshan` | 燕山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-raoshan` | 饒山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-ganshan` | 乾山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-lunshan` | 倫山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-jieshi` | 碣石之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-yanmenshan` | 鴈門之山（北水行） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-taize-didu` | 泰澤水行與帝都之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-mufeng` | 錞于母逢之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-range3-summary` | 北次三经总括与祭礼 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-beishan-book-total` | 北山经篇末总计与数字核对 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-suzhu` | 樕𧑤之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-leishan` | 藟山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-xunzhuang` | 栒状之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-boqi` | 勃亝之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-fantiao` | 番條之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-guer` | 姑兒之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-gaoshi-east` | 髙氏之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-yueshan` | 嶽山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-chaishan` | 犲山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-dushan` | 獨山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-taishan-range1` | 泰山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-zhushan` | 竹山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-range1-summary` | 首列总括与祭礼 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-kongsang-east` | 空桑之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-caoxi` | 曹夕之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-yigao` | 嶧皐之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-geshan-tail` | 葛山之尾 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-geshan-head` | 葛山之首 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-yue` | 餘峩之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-dufu` | 杜父之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-gengshan` | 耿山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-luqi` | 盧其之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-gushe` | 姑射之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-north-gushe` | 北姑射之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-south-gushe` | 南姑射之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-bishan` | 碧山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-weishi` | 維氏之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-gufeng` | 姑逢之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-fuli` | 鳬麗之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-zhenshan` | 䃌山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-range2-summary` | 次二总括与祭礼 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-shihu` | 尸胡之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-qishan` | 岐山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-zhugou` | 諸鈎之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-zhongfu` | 中父之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-hushe` | 胡射之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-mengzi` | 孟子之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-qizhong` | 跂踵之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-muyu` | 踇隅之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-wugao` | 無皐之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-range3-summary` | 次三总括与祭礼 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-beihao` | 北號之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-maoshan` | 旄山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-dongshi` | 東始之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-nvzheng` | 女烝之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-qinshan` | 欽山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-zitong` | 子桐之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-yanshan` | 剡山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-taishan-range4` | 太山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-range4-summary` | 次四总括 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-dongshan-book-total` | 东山经篇末总计 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-zhongshan-r01-gancao` | 甘棗之山 | 《山海经》 | 常规入口 | 《山海经·中山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-zhongshan-r01-lier` | 歴兒之山 | 《山海经》 | 常规入口 | 《山海经·中山经》（《四部丛刊》景明成化本，郭璞传） |
| `passage-zhongshan-r01-quzhu` | 渠豬之山 | 《山海经》 | 常规入口 | 《山海经·中山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-tangting` | 堂庭之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-yuanyi` | 猨翼之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-di` | 祗山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-danyuan` | 亶爰之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-jishan` | 基山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-jiwei` | 箕尾之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-gui` | 柜山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-changyou` | 长右之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-yaoguang` | 尧光之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-yu` | 羽山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-qufu` | 瞿父之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-gouyu` | 句余之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-fuyu` | 浮玉之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-cheng` | 成山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-kuaiji` | 会稽之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-yi` | 夷山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-pugou` | 仆勾之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-xun` | 洵山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-hushao` | 虖勺之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-quwu` | 区吴之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-xianyin` | 咸阴之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-luwu` | 鹿吴之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-qiwu` | 漆吴之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-tianyu` | 天虞之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-daoguo` | 祷过之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-danxue` | 丹穴之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-fashuang` | 发爽之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-maowei` | 旄山之尾 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-feitou` | 非山之首 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-yangjia` | 阳夹之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-guanxiang` | 灌湘之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-ji` | 鸡山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-lingqiu` | 令丘之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-lunzhe` | 仑者之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-yugao` | 禺槀之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-nanyu` | 南禺之山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `valley-nanshan-yuyi` | 育遗 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `valley-nanshan-zhonggu` | 中谷 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `wind-nanshan-kai` | 凯风 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `wind-nanshan-tiao` | 条风 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-reference-liuhuang` | 流黄 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-reference-zhupi` | 诸毗 · 柜山段 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-nanshan-reference-qiushan` | 丘山 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-nanshan-white-ape` | 白猿 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-nanshan-fu` | 蝮虫 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-nanshan-ji-fish` | 鮆鱼 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-nanshan-piluo` | 芘蠃 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-nanshan-xi` | 犀 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-nanshan-si` | 兕 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-nanshan-elephant` | 象 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-nanshan-1` | 䧿山诸神 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-nanshan-1` | 䧿山祭礼 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-nanshan-2` | 南次二经诸神 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-nanshan-2` | 南次二经祭礼 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-nanshan-3` | 南次三经诸神 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-nanshan-3` | 南次三经祭礼 | 《山海经》 | 常规入口 | 《山海经·南山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-qianlai` | 钱来之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-songguo` | 松果之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-taihua` | 太华之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-xiaohua` | 小华之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-xishan-zuoniu` | 㸲牛（小华山） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-fuyu` | 符禺之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-shicui` | 石脆之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-ying` | 英山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-xishan-zuoniu-ying` | 㸲牛（英山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-zhushan` | 竹山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-fushan` | 浮山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-yuci` | 羭次之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-shishan` | 时山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-nanshan-west` | 南山（西山经） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-dashi` | 大时之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-bozhong` | 嶓冡之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-tiandi` | 天帝之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-gaotu` | 皐塗之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-huangshan` | 黄山（西山经） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-cuishan` | 翠山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-guishan` | 騩山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-xishan-hua-range1` | 华山冢与太牢祠礼 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-xishan-yu-range1` | 羭山燭礼与玉器 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-xishan-seventeen-range1` | 其余十七山祠礼 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-qianshan` | 鈐山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-taimao` | 㤗冐之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-shuli` | 數歴之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-gaoshan` | 髙山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-nvchuang` | 女牀之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-longshou` | 龍首之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-lutai` | 鹿臺之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-niaowei` | 鳥危之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-xiaoci` | 小次之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-daci` | 大次之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-xunwu` | 薰吳之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-quyang` | 𢇨陽之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-zhongshou` | 衆獸之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-huangren` | 皇人之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-zhonghuang` | 中皇之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-xihuang` | 西皇之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-laishan` | 萊山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-xishan-horse-range2` | 十神·人靣馬身（西次二经） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-xishan-ox-range2` | 七神·人靣牛身（西次二经） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-xishan-shaolao-range2` | 少牢与白菅之席（西次二经） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-xishan-rooster-range2` | 十軰神雄鷄之祠（西次二经） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-chongwu` | 崇吾之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-zhongsui-chongwu` | 冡遂（崇吾段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-tuan-shou-qiu-chongwu` | 帝之摶獸之丘（崇吾段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-changsha` | 長沙之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-buzhou` | 不周之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-zhupi-buzhou` | 諸毗之山（西山经） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-yuechong-buzhou` | 嶽崇之山（不周段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-mishan` | 峚山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-xishan-huangdi-mishan` | 黃帝（峚山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-xishan-heaven-earth-mishan` | 天地鬼神（峚山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-zhongshan` | 鍾山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-xishan-gu-zhongshan` | 皷（鍾山龙身） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-xishan-qinpi-zhongshan` | 欽䲹（鍾山原身） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-xishan-baojiang-zhongshan` | 葆江（鍾山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-xishan-di-zhongshan` | 帝（鍾山段·未具名） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-kunlun-yang-zhongshan` | 崑崙之陽（鍾山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-yaoya-zhongshan` | 𡺯崖（鍾山之东） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-taiqi` | 㤗噐之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-liusha` | 流沙（㤗噐段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-huaijiang` | 槐江之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-pingpu-huaijiang` | 帝之平圃（槐江段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-xishan-yingzhao-huaijiang` | 英招（槐江段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-xishan-houji-huaijiang` | 后稷（槐江西望） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-xishan-lilun-huaijiang` | 槐鬼離侖（槐江北望） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-danshan-huaijiang` | 怛山（槐江东望） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-xishan-youqiong-huaijiang` | 有窮鬼（槐江东望） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-xishan-ox-eight-huaijiang` | 未名天神（槐江末段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-kunlun` | 崑崙之丘 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-wuda-kunlun` | 無逹 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-dayu-kunlun` | 大杅 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-leyou` | 樂游之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-luomushan` | 蠃母之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-xishan-changcheng-luomushan` | 長乗 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-yushan` | 玉山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-xishan-xiwangmu-yushan` | 西王母（玉山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-xuanyuan` | 軒轅之丘 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-jishi` | 積石之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-gate-jishi` | 石門（積石段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-changliu` | 長留之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-xishan-shaohao-changliu` | 白帝少昊 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-xishan-weishi-changliu` | 員神磈氏 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-zhange` | 章莪之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-yinshan3` | 隂山（西次三经） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-futang` | 符愓之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-xishan-jiangyi-futang` | 江疑 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-sanwei` | 三危之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-guishan3` | 騩山（西次三经） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-xishan-qitong-guishan3` | 𦒿童 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-tianshan` | 天山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-tang-tianshan` | 湯谷（天山段） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-youshan` | 泑山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-xishan-rushou-youshan` | 蓐𭣣 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-xishan-hongguang-youshan` | 紅光 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-yiwang` | 翼望之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-xishan-sheep-range3-summary` | 羊身人面神（西次三经） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-xishan-rite-range3-summary` | 吉玉稷米祠礼 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-yinshan4` | 隂山（西次四经） | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-laoshan` | 勞山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-bafu` | 罷父之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-shenshan` | 申山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-niaoshan` | 鳥山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-shangshen` | 上申之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-zhuci` | 諸次之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-haoshan` | 號山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-yushan4` | 盂山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-baiyu` | 白於之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-shenshou` | 申首之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-jinggu` | 涇谷之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-gangshan` | 剛山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-xishan-chi-gangshan` | 神𩳁 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-gangwei` | 剛山之尾 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-yingdi` | 英鞮之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-zhongqu` | 中曲之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-guishan4` | 邽山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-niaoshu` | 鳥鼠同穴之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-xishan-yanzi` | 崦嵫之山 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-xishan-rite-range4-summary` | 白鸡稻米白管祠礼 | 《山海经》 | 常规入口 | 《山海经·西山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-danhu` | 單狐之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-qiuru` | 求如之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-zhupi-qiuru` | 諸毗山（北山郭注） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-daishan` | 帶山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-qiaoming` | 譙明之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-zhuoguang` | 涿光之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-guoshan` | 虢山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-guowei` | 虢山之尾 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-danxun` | 丹熏之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-shizhe` | 石者之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-bianchun` | 邊春之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-manlian` | 蔓聮之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-danzhang` | 單張之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-guanti` | 灌題之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-panhou` | 潘侯之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-xiaoxian` | 小咸之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-daxian` | 大咸之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-dunhong` | 敦薨之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-kunlun-dunhong` | 崑崙（敦薨水文） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-shaoxian` | 少咸之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-yanmen-shaoxian` | 鴈門山（郭注） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-yufa` | 獄法之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-beiyue` | 北嶽之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-hunxi` | 渾夕之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-beidan` | 北單之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-bicha` | 羆差之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-beixian` | 北鮮之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-dishan` | 隄山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-beishan-range1-summary` | 北山经首列总括与祭礼 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-beishan-human-serpent-range1-summary` | 首列山神（人面蛇身） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-beishan-offerings-range1-summary` | 首列牲祭与瘗埋 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-beishan-gui-range1-summary` | 珪（首列祭玉） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-beishan-raw-food-range1-summary` | 山北生食记述 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-guancen` | 管涔之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-shaoyang` | 少陽之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-xianyong` | 縣雍之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-huqi` | 狐岐之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-baisha` | 白沙山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-ershi` | 爾是之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-kuang` | 狂山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-zhuyu` | 諸餘之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-duntou` | 敦頭之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-gouwu` | 鉤吾之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-beixiao` | 北囂之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-liangqu` | 梁渠之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-guguan` | 姑灌之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-huguan` | 湖灌之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-huan` | 洹山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-liusha-huan` | 流沙（洹山行程） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-dunti` | 敦題之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-beishan-range2-summary` | 北次二经总括与祭礼 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-beishan-human-serpent-range2-summary` | 次二山神（蛇身人面） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-beishan-animal-burial-range2` | 次二牲祭瘗埋 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-beishan-jade-casting-range2` | 次二投玉不糈 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-beishan-bi-range2` | 璧（次二祭玉） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-beishan-gui-range2` | 珪（次二祭玉） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-taihang` | 太行之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-guishan` | 歸山（太行之首） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-longhou` | 龍侯之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-macheng` | 馬成之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-xianshan` | 咸山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-tianchi` | 天池之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-yangshan` | 陽山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-benwen` | 賁聞之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-wangwu` | 王屋之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-jiaoshan` | 教山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-fawan` | 發丸之山（两山记述） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-jingshan` | 景山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-mengmen` | 孟門之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-pingshan` | 平山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-jingshan-east` | 京山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-chongwei` | 虫尾之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-pengpi` | 彭毗之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-xiaohou` | 小侯之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-taitou` | 泰頭之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-xuanyuan` | 軒轅之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-yeli` | 謁戾之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-danlin-forest-yeli` | 丹林（謁戾东林） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-juru` | 沮洳之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-shenqun` | 神囷之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-western-mountains-fajiu` | 西山（精衛取材叙事） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-shaoshan` | 少山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-xishan-north` | 錫山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-jingshan-after-xi` | 景山（錫山北） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-tishou` | 題首之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-xiushan` | 繡山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-songshan` | 松山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-dunyu` | 敦與之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-zheshan` | 柘山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-weilong` | 維龍之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-baima` | 白馬之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-kongsang-north` | 空桑之山（北山经） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-taixi` | 泰戱之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-shishan` | 石山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-tongrong` | 童戎之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-gaoshi` | 髙是之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-lushan` | 陸山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-yishan` | 沂山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-yanshan` | 燕山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-raoshan` | 饒山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-ganshan` | 乾山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-lunshan` | 倫山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-jieshi` | 碣石之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-yanmenshan` | 鴈門之山（北水行） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-taize-didu` | 泰澤水行與帝都之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-didu` | 帝都之山（泰澤中） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-mufeng` | 錞于母逢之山 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-jihao-mufeng` | 鷄號之山（北望） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-beishan-youdu-mufeng` | 幽都之山（西望） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `wind-beishan-li-mufeng` | 如䬅之风（末段） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-beishan-range3-summary` | 北次三经总括与祭礼 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-beishan-horse-human-range3` | 次三二十神（馬身人面） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-beishan-pig-jade-range3` | 次三十四神（彘身載玉） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-beishan-pig-eight-snake-range3` | 次三十神（彘身八足蛇尾） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-beishan-zaozhi-burial-range3` | 次三馬身神藻茝瘗礼 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-beishan-jade-not-buried-range3` | 次三載玉神祭玉不瘗 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-beishan-bi-burial-range3` | 次三八足神一璧瘗礼 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-beishan-grain-no-fire-range3` | 次三四十四神稌糈与不火食 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-zao-range3` | 藻（次三祭物） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-zhi-range3` | 茝（次三祭物） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-beishan-tu-range3` | 稌（次三祭米） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-jade-carried-range3` | 玉（次三神所載） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-beishan-bi-range3` | 璧（次三瘗礼） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-beishan-rice-range3` | 糈米（次三祭物） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-beishan-book-total` | 北山经篇末总计与数字核对 | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-beishan-mountains-book-total` | 八十七山（北经原报总数） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-beishan-distance-book-total` | 二萬三千二百三十里（原报总程） | 《山海经》 | 常规入口 | 《山海经·北山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-suzhu` | 樕𧑤之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-qianmei-suzhu` | 乾昧之山（北临） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-leishan` | 藟山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-xunzhuang` | 栒状之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-boqi` | 勃亝之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-fantiao` | 番條之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-guer` | 姑兒之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-gaoshi-east` | 髙氏之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-yueshan` | 嶽山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-chaishan` | 犲山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-dushan` | 獨山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-taishan-range1` | 泰山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-zhushan` | 竹山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-dongshan-range1-summary` | 首列总括与祭礼 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-dongshan-human-dragon-range1` | 人身龍首神（东山首列） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-dongshan-fur-offering-range1` | 祠毛用一犬（首列祭礼） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-dongshan-fish-er-range1` | 祈䎶用魚（首列祭礼） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-kongsang-east` | 空桑之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-juwu` | 沮呉（空桑东望） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-shaling` | 沙𨹧（空桑南望） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-caoxi` | 曹夕之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-yigao` | 嶧皐之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-geshan-tail` | 葛山之尾 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-geshan-head` | 葛山之首 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-yue` | 餘峩之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-dongshan-zhong-yue` | 螽（餘峩灾异） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-dongshan-huang-insects-yue` | 蝗（餘峩灾异） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-dufu` | 杜父之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-gengshan` | 耿山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-luqi` | 盧其之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-gushe` | 姑射之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-north-gushe` | 北姑射之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-south-gushe` | 南姑射之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-bishan` | 碧山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-weishi` | 維氏之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-gufeng` | 姑逢之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-fuli` | 鳬麗之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-zhenshan` | 䃌山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-dongshan-range2-summary` | 次二总括与祭礼 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-dongshan-humanface-antlers-range2` | 兽身人面载觡神（东次二） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-dongshan-chicken-range2` | 祠毛一鷄（次二祭礼） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-dongshan-bi-burial-range2` | 一璧瘞（次二祭礼） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-shihu` | 尸胡之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-xiang-shihu` | 𦍙山（尸湖北望） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-qishan` | 岐山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-dongshan-tiger-qi` | 虎（岐山泛称） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-zhugou` | 諸鈎之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-zhongfu` | 中父之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-hushe` | 胡射之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-mengzi` | 孟子之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-dongshan-mi-mengzi` | 麋（孟子泛称） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-dongshan-lu-mengzi` | 鹿（孟子泛称） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-qizhong` | 跂踵之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-muyu` | 踇隅之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-wugao` | 無皐之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-dongshan-fu-wood-wugao` | 榑木（無皐东望） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `wind-dongshan-wind-wugao` | 风（無皐） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-dongshan-range3-summary` | 次三总括与祭礼 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `deity-dongshan-human-ramhorn-range3` | 人身羊角神（东次三） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-dongshan-ram-offering-range3` | 一牡羊（次三祭礼） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `material-dongshan-millet-range3` | 𮮐（次三祭米） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-beihao` | 北號之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-maoshan` | 旄山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-dongshi` | 東始之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-nvzheng` | 女烝之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-qinshan` | 欽山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-zitong` | 子桐之山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-yanshan` | 剡山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-dongshan-insects-yanshan` | 蟲（合窳食性泛称） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `animal-dongshan-snakes-yanshan` | 蛇（合窳食性泛称） | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-dongshan-taishan-range4` | 太山 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-dongshan-range4-summary` | 次四总括 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `rite-dongshan-book-total` | 东山经篇末总计 | 《山海经》 | 常规入口 | 《山海经·东山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-zhongshan-r01-gancao` | 甘棗之山 | 《山海经》 | 常规入口 | 《山海经·中山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-zhongshan-r01-lier` | 歴兒之山 | 《山海经》 | 常规入口 | 《山海经·中山经》（《四部丛刊》景明成化本，郭璞传） |
| `plant-zhongshan-jian-comparison-lier` | 揀（櫔实比拟） | 《山海经》 | 常规入口 | 《山海经·中山经》（《四部丛刊》景明成化本，郭璞传） |
| `place-zhongshan-r01-quzhu` | 渠豬之山 | 《山海经》 | 常规入口 | 《山海经·中山经》（《四部丛刊》景明成化本，郭璞传） |
| `01-01` | 盘古开天 | 其他古籍 | 常规入口 | 《三五历纪》（三国·吴·徐整），佚文见《艺文类聚》卷一引、《太平御览》卷二引 |
| `01-02` | 女娲造人 | 其他古籍 | 常规入口 | 《风俗通义·皇霸》卷一（东汉·应劭），见王利器《风俗通义校注》 |
| `01-03` | 女娲补天 | 其他古籍 | 非默认条目 | 《淮南子·览冥训》（西汉·刘安），高诱注 |
| `01-04` | 共工怒触不周山 | 其他古籍 | 非默认条目 | 《淮南子·天文训》（西汉·刘安），高诱注 |
| `02-01` | 伏羲画卦 | 其他古籍 | 常规入口 | 《周易·系辞下》（《十三经注疏》本） |
| `02-02` | 女娲伏羲兄妹婚 | 其他古籍 | 非默认条目 | 《风俗通义》（东汉·应劭）；《独异志》（唐·李冗）卷下 |
| `02-03` | 神农尝百草 | 其他古籍 | 常规入口 | 《淮南子·修务训》（西汉·刘安），高诱注 |
| `02-04` | 燧人取火 | 其他古籍 | 常规入口 | 《韩非子·五蠹》（战国·韩非），王先慎《韩非子集解》 |
| `02-05` | 有巢构木 | 其他古籍 | 常规入口 | 《韩非子·五蠹》（战国·韩非），王先慎《韩非子集解》 |
| `03-01` | 阪泉之战 | 其他古籍 | 常规入口 | 《史记·五帝本纪》（西汉·司马迁），三家注 |
| `03-02` | 涿鹿之战 | 其他古籍 | 常规入口 | 《史记·五帝本纪》（西汉·司马迁），三家注 |
| `03-03` | 刑天舞干戚 | 《山海经》 | 常规入口 | 《山海经·海外西经》（郭璞注本） |
| `03-04` | 精卫填海 | 《山海经》 | 常规入口 | 《山海经·北山经》（郭璞注本） |
| `03-05` | 夸父逐日 | 《山海经》 | 常规入口 | 《山海经·海外北经》（郭璞注本）；又见《大荒北经》 |
| `04-01` | 共工与颛顼争帝 | 其他古籍 | 常规入口 | 《淮南子·天文训》（西汉·刘安），高诱注 |
| `04-02` | 大羿射日 | 其他古籍 | 常规入口 | 《淮南子·本经训》（西汉·刘安），高诱注 |
| `04-03` | 嫦娥奔月 | 其他古籍 | 常规入口 | 《淮南子·览冥训》（西汉·刘安），高诱注 |
| `04-04` | 鲧窃息壤 | 《山海经》 | 常规入口 | 《山海经·海内经》（郭璞注本） |
| `04-05` | 尧禅舜 | 其他古籍 | 常规入口 | 《论语·尧曰》第二十篇第一章 |
| `05-01` | 大禹治水 | 其他古籍 | 常规入口 | 《尚书·禹贡》（《十三经注疏》本） |
| `05-02` | 禹杀相柳 | 《山海经》 | 常规入口 | 《山海经·海外北经》；另见《大荒北经》相繇条 |
| `05-03` | 禹娶涂山女 | 其他古籍 | 常规入口 | 《尚书·益稷》（《十三经注疏》本） |
| `05-04` | 启母化石 | 其他古籍 | 常规入口 | 《汉书·武帝纪》颜师古注引《淮南子》（今本《淮南子》无此文） |
| `06-01` | 后羿代夏 | 其他古籍 | 常规入口 | 《左传·襄公四年》（《十三经注疏》本） |
| `06-02` | 寒浞之乱 | 其他古籍 | 常规入口 | 《左传·襄公四年》（《十三经注疏》本） |
| `06-03` | 少康中兴 | 其他古籍 | 常规入口 | 《左传·哀公元年》（《十三经注疏》本） |
| `06-04` | 成汤囚夏台 | 其他古籍 | 常规入口 | 《史记·夏本纪》（西汉·司马迁），三家注 |
| `06-05` | 伊尹空桑 | 其他古籍 | 常规入口 | 《吕氏春秋·本味》（战国·吕不韦），高诱注 |
| `07-03` | 升昆仑观黄帝之宫 | 其他古籍 | 常规入口 | 《穆天子传》卷二（郭璞注本） |
| `07-01` | 穆天子见西王母 | 其他古籍 | 常规入口 | 《穆天子传》卷三（郭璞注本） |
| `07-02` | 瑶池宴 | 其他古籍 | 常规入口 | 《穆天子传》卷三（郭璞注本） |
| `07-04` | 纪迹弇山 | 其他古籍 | 常规入口 | 《穆天子传》卷三（郭璞注本） |
| `08-01` | 海外诸国 | 《山海经》 | 未开放 | 《山海经》海外南/西/北/东经（郭璞注本） |
| `08-02` | 大荒异兽 | 《山海经》 | 未开放 | 《山海经》大荒东/南/西/北经（郭璞注本） |
| `08-03` | 昆仑之丘 | 《山海经》 | 未开放 | 《山海经·西山经》（郭璞注本） |
| `08-04` | 归墟五山 | 其他古籍 | 未开放 | 《列子·汤问》（战国·列御寇），张湛注 |
| `08-05` | 扶桑 | 《山海经》 | 未开放 | 《山海经·海外东经》（郭璞注本） |
| `08-06` | 烛龙 | 《山海经》 | 未开放 | 《山海经·海外北经》（郭璞注本）；又见《大荒北经》 |
| `08-07` | 西王母（早期形态） | 《山海经》 | 未开放 | 《山海经·西山经》（郭璞注本） |
| `01-03-a` | 炼石补天 | 其他古籍 | 常规入口 | 《淮南子·览冥训》（西汉·刘安），高诱注 |
| `01-03-b` | 断鳌立极 | 其他古籍 | 常规入口 | 《淮南子·览冥训》（西汉·刘安），高诱注 |
| `01-03-c` | 杀黑龙济冀州 | 其他古籍 | 常规入口 | 《淮南子·览冥训》（西汉·刘安），高诱注 |
| `01-03-d` | 积芦灰止水 | 其他古籍 | 常规入口 | 《淮南子·览冥训》（西汉·刘安），高诱注 |

## 南山经全篇阅读与全书待办清单

- 已保留2433个原始录文块与第26页4个补录块。清单逐项区分已说明、标题元信息和待核，候选实体匹配不算已核定关系。其他16篇仍待系统核对，西山经82段已有审核链接，本篇已连续覆盖正文；不将2437个录文块冒充2437段独立内容。
- 《南山经》43段连续覆盖正文：39个实际列名的山段、3个山列总述/祭祀段、1个篇末总计。中文白话、英文说明与英文释文同步，保留底本中文和注文；可从章节目录、搜索、收藏及续读进入。新段落不添加地图坐标。
- 第26页洵山、虖勺、区吴三段由影印补录；第21页“二千九百五十里”纠正电子录文漏“二”。猾褢等差异单列记录，祗山沿用底本写法；一个未确认图字仍显式保留待核标记，原电子快照不改写。
- 底本各列总数为10、17、14山，篇末写40山，逐项列名实际39段；三种口径分别保留，不据此补造山名。完整指正文段落说明齐备，不含全书实体穷尽、逐字多版本校勘或全量配图。
- 独立实体轮新增97卡：36座逐述山、3个参见地点、14项异兽、25项水域、2项植物、7项普通动物、2谷、2风、3组山神和3项祭礼。南山经共117项独立卡（不含总览），另有43段阅读器；覆盖ID及逐段关联见`data/nanshan-entity-coverage.json`，逐述山入口共39座。
- 首批和阅读器批已有9幅插画；最新独立实体轮共51幅任务，已审51幅，待补或待审0幅。仅已审图导出接入，水域等复用山景并标明场景示意；无成图的卡保留“插画待补”，不请求不存在的图片。权威提示词、状态和复核记录见`frontend/artwork-source/nanshan/entities-generation.json`。
- 文本接入、图片审阅与浏览器回归分别验收；最新轮的具体通过项和未运行项以根目录本地交接文档为准。下方历史验证不代表新增97卡轮已通过。

## 第一批补充内容：南山经三处（历史批次）

本批已接入11个新条目、6幅新图；同步完善青丘与狌狌、鹿蜀、旋龟、九尾狐、赤鱬。新山与自然条目从02章可见，灌灌从03章可见，关联阅读不推进章节。

| 地点 | 已有内容 | 首批新增/完善 | 原文关系与验收边界 |
| --- | --- | --- | --- |
| 招摇之山 | 狌狌异兽卡；南山经集合锚点 | 独立地点介绍、祝余、迷谷、丽𪊨之水与育沛 | 同一山段记载；区分草、木、水、物产，保留生僻字及音读待核项 |
| 杻阳之山 | 鹿蜀、旋龟异兽卡 | 独立地点介绍、怪水与宪翼之水、山阳山阴物产 | 旋龟在水中记载，不能简单改写成与鹿蜀相同陆上栖居；原文功效只作为古籍记述 |
| 青丘之山 | 青丘地点、九尾狐、赤鱬 | 新增灌灌、英水、即翼之泽，完善地点与分层关系 | 九尾狐与灌灌在山段，赤鱬在水中；不由同段共现推断捕食或因果 |

- 纠正旧报告：原有 `beast-guan` 为《西山经》讙；本批新增 `beast-guanguan` 为《南山经》灌灌，分别保留。
- 11个新ID：`place-zhaoyao`、`place-niuyang`、`plant-zhuyu`、`plant-migu`、`water-liji`、`water-guai`、`water-xianyi`、`water-ying-qingqiu`、`water-jiyi`、`material-yupei`、`beast-guanguan`。
- 校核依据：`data/reference-scans/nanshan/page-16.jpg`至`page-21.jpg`；扫描来源、哈希与定位见同目录`sources.json`。当前条目分别保存经文、郭注摘录、白话整理及出处定位；简体字和标点为编辑整理。
- 六幅图片：招摇、杻阳、青丘新版、祝余、迷谷、灌灌；均为内置image_gen生成并已接入。原图、提示词和核验记录在`frontend/artwork-source/nanshan/`。发布WebP含透明完整图、预览、缩略图；灌灌另有地图图标。育沛无具象图；五处水域复用场景并明示示意。
- 五项旧异兽图已逐项目视核验并沿用；狌狌的人面倾向属于图像解释，非经文明言。图像仅作艺术表达，不作古代动物学复原。

三处为首批编辑范围；其间山段已在后续43段阅读器和独立卡轮接入。叙述按“白话景象→原文→出处与边界”组织。任何古籍中的食用、佩用或治病功效均作为文本描述，不给现实使用建议。

## 本轮发现的待校问题

- `08-01`“海外诸国”和 `08-02`“大荒异兽”的 source_quote 实为项目汇总，不能当作连续经文引文。两项目前无网页章节入口；新增入口前须拆成逐篇、逐条原文。
- `08-06`所引“西北海之外，赤水之北，有章尾山”对应《大荒北经》，原出处首先列《海外北经》；开放前须明确主引篇和参见篇。
- 现有“郭璞注本”没有逐条精确到同一刊本。本轮选定的盘点基准不等于替换所有现有引文版本；简繁、异体、删节和文字差异均应逐条复核。
- 同名异篇、神域与地点、原文与郭注分别保留；尚不计算“全书完成百分比”。

## 全篇阅读验证（历史批次，2026-10-19）

- 本地通过：`build --base /mythmap/`、`verify:data`、`verify:publish`、`verify:cache`、盘点和全书清单`--check`；9幅南山经图的28个WebP版本保留透明通道，19个所需生僻字符由本地字体覆盖。
- Chromium、WebKit通过`verify:reader`：43段逐一打开、原文与目录、缺页补录、中文原名英文搜索、收藏/已读持久化、旧标记保留、续读、返回/刷新、关联阅读、3幅新场景实用与8种语言/视口组合；还覆盖地图图片加载中断。
- 本轮现有`verify:search`、`verify:discovery`在Chromium通过，WebKit复测通过；复测前曾暴露图片加载中断导致的OpenLayers图标尺寸异常，已改用已知尺寸缩放并增加中断测试。`verify:locale`在Chromium通过。
- 原47个地点/神域/异兽ID和原异兽开放章节保留。未运行Firefox、全故事长流程和数据库集成；远端CI尚未运行。未发布远端站点，检查结束后关闭测试端口。

## 首批三处验证记录（历史批次，2026-10-19）

- 本地通过：`build --base /mythmap/`、`verify:data`、`verify:cache`、`verify:publish`及本清单`--check`；6幅图的19个发布版本均保留透明通道。旧47个地点/神域/异兽ID全部保留，旧异兽开放章节未改变。
- Chromium、WebKit通过：`verify:nanshan`（11项、双语、搜索、关联往返、返回/刷新、收藏/已读、续读、8种语言/视口组合），以及`verify:search`、`verify:discovery`、`verify:design`、`verify:reading`、`verify:resume`。`verify:locale`本地Chromium通过。
- 本轮未运行Firefox、全故事时钟长流程及数据库集成检查；CI已纳入新条目检查，配置三浏览器运行，但尚未宣称远端CI通过。未发布远端站点。预览服务器在检查结束后关闭。

## 复现与更新

- `python data/build_nanshan_reader.py`：重建43段双语正文、出处和校核差异，保留既有独立条目。
- `python data/build_nanshan_entities.py`：在旧批次/阅读器构建之后运行，恢复最新实体、关系、图像状态和覆盖清单；不可将reader或首批构建器作为最后一步。
- `python data/build_source_inventory.py`（可加`--check`）：生成/检查十八篇原文块清单及明确的待核状态。
- `python data/prepare_zhongshan.py`（可加`--check`）：离线重建/检查中山212阶段准备计划、69影印哈希、标题字体预检；只规划，不增加网页阅读或配图。之后重建全书inventory/audit。
- `python data/build_zhongshan.py`：合并中山首三段/14双语卡并保留其他篇；已接入后不要再运行准备构建器覆盖进度。插画通过prepare-nanshan-artwork.py --chapter zhongshan导出，之后重建inventory/audit。
- `python data/build_nanshan.py`：合并本批中英文条目、图像指向与有引文依据的关系，保留其他记录。
- `python frontend/scripts/prepare-nanshan-artwork.py`：从保留的生成原图重建发布素材与素材清单。
- `python data/build_xishan.py`：合并西山经82段与508张双语卡，并记录影印页码和缺字图校正；在南山经构建器之后运行。
- `python data/build_dongshan.py`：合并东山全篇51段/237双语卡（含3张稳定旧卡接入），保留其他篇与东山既有稳定ID；东山插画通过prepare-nanshan-artwork.py --chapter dongshan导出，之后重建inventory/audit。
- `python data/build_beishan.py`：合并已核北山经全篇92段及507张双语卡（含复用諸犍、精衛、發鳩），保留其他篇目与旧ID；`python frontend/scripts/prepare-nanshan-artwork.py --chapter beishan`仅导出已审图。随后重建全书清单和本盘点。
- `python frontend/scripts/prepare-nanshan-artwork.py --chapter xishan`：仅导出已审核西山经插画。随后运行全书清单和本盘点构建器更新统计。
- `python data/audit_shanhaijing.py`：离线重建本清单和网页来源分类。
- `python data/audit_shanhaijing.py --check`：只检查快照结构、分类与清单是否和现有数据一致；CI运行该项。
- `python data/audit_shanhaijing.py --fetch`：显式重新获取十八卷录文，再重建；联网获取需要 requests、beautifulsoup4，离线检查仅需Python标准库。
- 影印页正文与注文分开保存。卷页固定修订链接不能锁定被嵌入页面的后续编辑，因此同时保留抓取日期、逐行快照及HTML SHA-256；更新后应审查差异。

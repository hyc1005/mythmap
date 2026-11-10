# 专题路线评估数据包（交给独立评估 agent）

基准：本地工作树，站点提交 `0b0b02c`（已推到 `main`）。本文件只放摘录，不放整份大文件；所有条目字段保持仓库原字形，不做繁简转换。标注“不存在”的项就是仓库里没有，不是估算。

给接收方的指令：

> 请只基于本文件与仓库现有文件评估，不要改代码。先核对第 0 节的性能前提是否成立，再按第 9 节的问题逐项回答。需要补数据时明确列出缺哪个文件/字段，不要猜。

## 0. 性能前提核对（先确认这些是否成立）

| 前提 | 仓库现状 | 结论 |
| --- | --- | --- |
| 不新增依赖 | `GuideRoutes.jsx` 只依赖 React、`useLocale`、`BlurRevealText`；无新包 | 成立 |
| 不新增运行时请求 | 路线数据是静态 JSON 导入；无 fetch | 成立 |
| 不新增 effect 或全局状态 | `GuideRoutes.jsx` 只有组件内 `useState(active)`；无 `useEffect`、无全局 store | 成立 |
| 路线只存 entryId + 编辑文字 | 当前字段只有 `entryId`、`label`，路线级 `title`、`intro` | 成立；未复制原文 |
| 同名/异形/范围词判断在构建期或验证脚本 | `form_group` 存在 `bestiary-metadata.json`；但详情并列区的“泛称组”提示用浏览器正则 `namesakeEntries.every(...)` 判断 | **部分不成立**：现有代码有一处浏览器内范围词判断（见 E 节），新增路线不应再增加这类判断 |
| 路线卡片不加图片 | `GuideRoutes.jsx` 只渲染文字按钮 | 成立 |
| 只渲染当前选中路线 | `active` 状态只渲染 `route` 一条 | 成立 |
| 增量只来自 `guide-routes.json` 文字 | 当前 JSON 2,079 B 原始 / 993 B gzip；组件代码很小但不单独计量 | 基本成立；无按功能记账 |

“25 KiB gzip 预算”在仓库里**没有强制脚本**：它只写在 `docs/README.md`（界面精修约定“新增JS/CSS gzip预算25KiB”）与 `docs/depth-roadmap.md` 第 4.4 节“gzip 增量实测并记录（预算 25 KiB）”。没有阈值常量、没有校验步骤，也没有“当前已用多少”的记账。因此无法给出“已用 X/25 KiB”，只能给可测增量。

## 1. A. 路线现状

### 1.1 `frontend/src/guide-routes.json`（全文，2,079 B）

```json
{
  "_note": "Curated thematic routes. Every stop must reference an existing bestiary entry id; the section is independent of the guided-tour playback state.",
  "routes": [
    {
      "id": "omens",
      "title": { "zh": "见则志", "en": "Omens and signs" },
      "intro": {
        "zh": "按原文的“见则/动则”串联灾异与吉兆，不改变各篇顺序。",
        "en": "Follows the text's own omen clauses across disasters and auspicious signs."
      },
      "stops": [
        { "entryId": "beast-bifang", "label": { "zh": "毕方 · 讹火", "en": "Bifang · fire" } },
        { "entryId": "beast-beishan-feiyi-hunxi", "label": { "zh": "浑夕肥遗 · 大旱", "en": "Feiyi of Hunxi · drought" } },
        { "entryId": "beast-nanshan-changyou", "label": { "zh": "长右 · 大水", "en": "Changyou · flood" } },
        { "entryId": "beast-zhuyan", "label": { "zh": "朱厌 · 大兵", "en": "Zhuyan · war" } },
        { "entryId": "beast-fei", "label": { "zh": "蜚 · 大疫", "en": "Fei · plague" } },
        { "entryId": "beast-dangkang", "label": { "zh": "当康 · 大穰", "en": "Dangkang · bountiful harvest" } }
      ]
    },
    {
      "id": "wards",
      "title": { "zh": "服佩辟邪", "en": "Wards and remedies" },
      "intro": {
        "zh": "只收原文写明“食之/佩之”功效的条目；䍺 等无功效记载者不入此路线。",
        "en": "Only accounts whose text states an effect after eating or wearing; accounts without one stay out."
      },
      "stops": [
        { "entryId": "beast-jiuweihu", "label": { "zh": "九尾狐 · 食者不蛊", "en": "Nine-tailed fox · no poison" } },
        { "entryId": "beast-boyi", "label": { "zh": "猼訑 · 佩之不畏", "en": "Boyi · worn, no fear" } },
        { "entryId": "beast-zhongshan-qinggeng-jinli11", "label": { "zh": "青耕 · 御疫", "en": "Qinggeng · plague ward" } },
        { "entryId": "beast-xishan-feiyi-ying", "label": { "zh": "英山肥遗 · 已疠、杀虫", "en": "Feiyi of Ying · illness, insects" } }
      ]
    }
  ]
}
```

### 1.2 `frontend/src/components/GuideRoutes.jsx`（全文，25 行）

```jsx
import { useState } from 'react';
import { useLocale } from '../i18n';
import BlurRevealText from './BlurRevealText';

export default function GuideRoutes({ routes, onOpen }) {
  const { t, locale } = useLocale();
  const [active, setActive] = useState(routes[0]?.id);
  const route = routes.find(item => item.id === active) || routes[0];
  if (!route) return null;
  return <section className="guide-routes" id="routes" aria-labelledby="routes-title">
    <div className="guide-routes-inner">
      <div className="guide-routes-heading">
        <h2 id="routes-title"><BlurRevealText text={t('专题巡山录')} revealKey={`routes:title:${locale}`} /></h2>
        <p><BlurRevealText text={t('按主题串联原文条目；不改变章节顺序，也不启动导览播放。')} revealKey={`routes:intro:${locale}`} variant="intro" /></p>
      </div>
      <div className="guide-route-tabs" role="group" aria-label={t('专题路线')}>
        {routes.map(item => <button type="button" key={item.id} aria-pressed={item.id === route.id} onClick={() => setActive(item.id)}>{item.title[locale] || item.title.zh}</button>)}
      </div>
      <p className="guide-route-intro">{route.intro?.[locale] || route.intro?.zh}</p>
      <ol className="guide-route-stops">{route.stops.map(stop => <li key={stop.entryId}>
        <button type="button" data-route-stop={stop.entryId} onClick={event => onOpen(stop.entryId, event)}>
          <b>{stop.label?.[locale] || stop.label?.zh}</b><small>{t('查看条目')}</small>
        </button>
      </li>)}</ol>
    </div>
  </section>;
}
```

### 1.3 `App.jsx` 相关片段

导入（静态，非懒加载）：

```jsx
import guideRoutes from './guide-routes.json' with { type: 'json' };
import GuideRoutes from './components/GuideRoutes';
```

`open` 的实现（路线只用到这一个入口）：

```jsx
const open = (id, trigger, sequence) => {
  setRestoreReading(null);
  setDetailReturnFocusKey(null);
  if (!selectedId) setDetailParentId(null);
  setPanel(null);
  if (!selectedId) detailPageScroll.current = [window.scrollX, window.scrollY];
  if (!selectedId) detailTrigger.current = trigger || null;
  if (sequence || !selectedId) setDetailSequence(sequence || null);
  setSelectedId(id);
};
```

挂载位置（异兽谱之后、读图与依据之前）：

```jsx
<Bestiary world={world} onOpen={open} reading={reading} />
<GuideRoutes routes={guideRoutes.routes} onOpen={(id, event) => open(id, event?.currentTarget)} />
<section className="reading-notes" id="reading-notes" ...>
```

导航入口：

```jsx
<a href="#routes">{t("专题巡山录")}</a>
```

### 1.4 路线相关 CSS（`frontend/src/styles/atlas-layout.css`，14 条规则）

```css
.guide-routes { padding: 40px clamp(18px, 4vw, 68px) 52px; border-top: 1px solid #b9a47c; background: #e9dec5; }
.guide-routes-inner { max-width: 1100px; margin: 0 auto; }
.guide-routes-heading h2 { margin: 0; font-size: 24px; }
.guide-routes-heading p { margin: 8px 0 0; color: var(--soft-ink); }
.guide-route-tabs { display: flex; flex-wrap: wrap; gap: 8px; margin: 18px 0 10px; }
.guide-route-tabs button { min-height: 44px; padding: 8px 14px; border: 1px solid var(--edge); background: transparent; color: var(--ink); font: inherit; cursor: pointer; }
.guide-route-tabs button[aria-pressed="true"] { border-color: var(--verm); color: var(--verm); }
.guide-route-intro { margin: 0 0 14px; font-size: 14px; color: var(--soft-ink); }
.guide-route-stops { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; margin: 0; padding: 0; list-style: none; }
.guide-route-stops button { display: block; width: 100%; min-height: 44px; padding: 10px 12px; border: 1px solid var(--edge); background: transparent; color: var(--ink); font: inherit; text-align: left; cursor: pointer; }
.guide-route-stops button:hover { border-color: var(--verm); }
.guide-route-stops b { display: block; font-weight: 600; }
.guide-route-stops small { display: block; margin-top: 4px; color: var(--soft-ink); }
@media (max-width: 640px) { .guide-routes { padding: 28px 16px 40px; } }
```

## 2. B. 性能基线

### 2.1 当前构建的 JS/CSS 产物（`dist/assets`，raw / gzip level 9）

| 文件 | raw | gzip |
| --- | ---: | ---: |
| `app-entry-BsGcpCaI.js` | 8,989,067 | 986,170 |
| `PanguOpening-CVcBpMpU.js` | 295,651 | 91,436 |
| `react-DTr1cmSM.js` | 222,411 | 68,878 |
| `openlayers-eFvmRjDT.js` | 284,875 | 82,080 |
| `index-CM3-Ta1U.js` | 74,715 | 27,169 |
| `StoryAnimation-D8HjdQHZ.js` | 21,396 | 8,625 |
| `KuafuJourney-DKyG2PMP.js` | 10,862 | 4,944 |
| `index-B7phFPiW.js` | 4,780 | 2,246 |
| `playback-C3sHHhMA.js` | 171 | 152 |
| `app-entry-Ct05sRTc.css` | 110,477 | 25,561 |

补充单文件 gzip：

- `frontend/src/guide-routes.json`：2,079 B 原始 / 993 B gzip。
- `frontend/src/bestiary-metadata.json`：205,914 B / 22,822 B gzip。
- `frontend/public/data/myth-world.json`：5,940,955 B / 540,080 B gzip。

### 2.2 加载方式

- `frontend/src/main.jsx`：开屏结束后 `const { mountApp } = await import('./app-entry');`，所以 `app-entry` 是**动态导入**，但导入后一次性加载。
- `App.jsx` 静态导入 `guideRoutes`、`mythWorld`、`bestiary`、`GuideRoutes`、`DetailDrawer`，因此路线 JSON 与组件都在 `app-entry` 里，**没有单独 chunk、没有懒加载**。
- 路线区块随 App 挂载渲染在 DOM 中，但位于地图、异兽谱之后，**不在首屏视口内**。
- `bestiary-metadata.json` 由 `bestiary.js` 静态导入，随 `app-entry` 加载；不是按需请求。

### 2.3 预算

**不存在**强制 25 KiB 的脚本或常量。预算只作为文档约定存在：

- `docs/README.md`：“新增JS/CSS gzip预算25KiB；按既有双语六尺寸、两浏览器设计与业务检查验收”。
- `docs/depth-roadmap.md` 第 4.4 节：“gzip 增量实测并记录（预算 25 KiB）”。

仓库没有按功能记录 gzip 增量，所以“已用多少”**不存在**。可测的路线文字增量目前是 993 B gzip（两条路线合计）。

## 3. C. 候选站点数据摘录

字段按要求：`id, display_name, group_key, book_key, form_group, basis, review_status, quote, commentary_quote, description, context_place_id, related_entry_ids, artwork`。`artwork` 为 `false` 表示无插画；`artwork_path` 保留原路径。

```json
[
 {
  "id": "beast-xishan-feiyi-ying",
  "display_name": { "zh": "肥遗", "en": "Feiyi" },
  "group_key": "肥遗", "book_key": "西山经", "form_group": "bird",
  "basis": "text", "review_status": "reviewed",
  "quote": "有鳥焉其状如鶉黄身而赤喙其名曰肥遺食之已癘可以殺蟲",
  "commentary_quote": "癘疫病也；或曰惡創韓子曰癘人憐主",
  "description": "英山肥遗是鸟，形如鹑，黄身、赤喙。它与太华山六足四翼的肥𧔥蛇分别保留稳定ID、形貌和原文；不因名称相近而合成一种异兽。食用功效仅作为古籍记述。",
  "context_place_id": "place-xishan-ying",
  "related_entry_ids": ["passage-xishan-ying"],
  "artwork": true, "artwork_path": "xishan/bird-feiyi-ying-v1.webp"
 },
 {
  "id": "beast-beishan-feiyi-hunxi",
  "display_name": { "zh": "肥遗", "en": "Feiyi" },
  "group_key": "肥遗", "book_key": "北山经", "form_group": "serpent",
  "basis": "text", "review_status": "reviewed",
  "quote": "有蛇一首兩身名曰肥遺見則其國大旱",
  "commentary_quote": "𬋩子曰涸水之精名曰蟡一頭而两身其状如蛇長八尺以其名呼之可使取魚龜亦此𩔗",
  "description": "肥遺一首两身，旱灾为古述；不与西山六足四翼蛇或英山鸟混形，郭注蟡等另存。",
  "context_place_id": "place-beishan-hunxi",
  "related_entry_ids": ["passage-beishan-hunxi"],
  "artwork": true, "artwork_path": "beishan/snake-feiyi-hunxi-v1.webp"
 },
 {
  "id": "beast-xishan-xiao-yuci",
  "display_name": { "zh": "嚣", "en": "Xiao" },
  "group_key": "嚣", "book_key": "西山经", "form_group": "beast",
  "basis": "text", "review_status": "reviewed",
  "quote": "有獸焉其狀如禺而長臂善投其名曰囂",
  "commentary_quote": "亦在畏獸𦘕中似猕猴投擲也",
  "description": "囂形如禺，长臂、善投。郭注另以猕猴与投掷解释。配图突出两条长臂，手中小石仅为表现善投的艺术选择，不添加投掷目标、武器或攻击故事；与他篇同名字物分开。",
  "context_place_id": "place-xishan-yuci",
  "related_entry_ids": ["passage-xishan-yuci"],
  "artwork": true, "artwork_path": "xishan/creature-xiao-yuci-v1.webp"
 },
 {
  "id": "beast-beishan-xiao-liangqu",
  "display_name": { "zh": "嚣", "en": "Xiao" },
  "group_key": "嚣", "book_key": "北山经", "form_group": "bird",
  "basis": "text", "review_status": "unresolved",
  "quote": "有鳥焉其状如夸父四翼一目犬尾名曰囂其音如鵲食之已腹痛可以止衕",
  "commentary_quote": "或作舉父；治洞下也音洞",
  "description": "囂如夸父、四翼一目犬尾，但夸父主体比拟及舉父异文未定，留占位，不借西山猿体或别处鸟形；食用为古述。",
  "context_place_id": "place-beishan-liangqu",
  "related_entry_ids": ["passage-beishan-liangqu"],
  "artwork": false, "artwork_path": null
 },
 {
  "id": "bird-xishan-manman-chongwu",
  "display_name": { "zh": "蛮蛮", "en": "Manman" },
  "group_key": "蛮蛮", "book_key": "西山经", "form_group": "bird",
  "basis": "text", "review_status": "reviewed",
  "quote": "有鳥焉其状如鳬而一翼一目相得乃飛名曰蠻蠻見則天下大水",
  "commentary_quote": "比翼鳥也色青赤不比不能飛爾雅作鶼鶼鳥也",
  "description": "蠻蠻形如鳬，却只有一翼一目，须相得才能飞，见则天下大水为古籍灾异。青赤色、比翼鸟与尔雅鶼鶼的说明来自郭注，不混成正文，也不鉴定为现实鸟种。",
  "context_place_id": "place-xishan-chongwu",
  "related_entry_ids": ["passage-xishan-chongwu"],
  "artwork": true, "artwork_path": "xishan/bird-manman-chongwu-v1.webp"
 },
 {
  "id": "beast-xishan-manman-gangwei",
  "display_name": { "zh": "蛮蛮", "en": "Manman" },
  "group_key": "蛮蛮", "book_key": "西山经", "form_group": "beast",
  "basis": "text", "review_status": "reviewed",
  "quote": "其中多蠻蠻其状鼠身而鼈首其音如吠犬",
  "commentary_quote": "",
  "description": "鼠身鳖首、犬吠音，是水中对象，不与崇吾独翼鸟共图。",
  "context_place_id": "place-xishan-gangwei",
  "related_entry_ids": ["passage-xishan-gangwei"],
  "artwork": true, "artwork_path": "xishan/beast-manman-gangwei-v1.webp"
 },
 {
  "id": "beast-xishan-huayu-leyou",
  "display_name": { "zh": "滑鱼", "en": "Huayu" },
  "group_key": "滑鱼", "book_key": "西山经", "form_group": "serpent",
  "basis": "text", "review_status": "reviewed",
  "quote": "其中多滑魚其状如蛇而四足是食魚",
  "commentary_quote": "",
  "description": "蛇状四足、食鱼；无鱼头鱼鳍的明文，不因鱼名补鳍。",
  "context_place_id": "place-xishan-leyou",
  "related_entry_ids": ["passage-xishan-leyou"],
  "artwork": true, "artwork_path": "xishan/beast-huayu-leyou-v1.webp"
 },
 {
  "id": "beast-beishan-huayu-qiuru",
  "display_name": { "zh": "滑鱼", "en": "Huayu" },
  "group_key": "滑鱼", "book_key": "北山经", "form_group": "fish",
  "basis": "text", "review_status": "reviewed",
  "quote": "其中多滑魚其状如鱓赤背其音如梧食之已疣",
  "commentary_quote": "鱓魚似蛇音善；如人相枝梧聲；音吾子之吾；疣贅也",
  "description": "求如水文中的滑魚形如鱓、背赤，声音比作梧，食用治疣为古籍说法。郭注释鱓似蛇，声音如人相枝梧，并另注梧音；不借西山同名滑魚的蛇状四足。",
  "context_place_id": "place-beishan-qiuru",
  "related_entry_ids": ["passage-beishan-qiuru", "water-beishan-hua-qiuru"],
  "artwork": true, "artwork_path": "beishan/creature-huayu-qiuru-v1.webp"
 },
 {
  "id": "beast-zhongshan-feiyu-niushou",
  "display_name": { "zh": "飞鱼", "en": "Feiyu" },
  "group_key": "飞鱼", "book_key": "中山经", "form_group": "fish",
  "basis": "text", "review_status": "reviewed",
  "quote": "是多飛魚其狀如鮒魚食之已痔衕",
  "commentary_quote": "",
  "description": "飞鱼本段仅如鲋，鱼体四鳍细节、体色姿态为艺术解释，不因飞名添翼，不借豚状赤文。",
  "context_place_id": "place-zhongshan-r01-niushou",
  "related_entry_ids": ["passage-zhongshan-r01-niushou", "water-zhongshan-lao-niushou"],
  "artwork": true, "artwork_path": "zhongshan/fish-feiyu-niushou-v1.webp"
 },
 {
  "id": "beast-zhongshan-feiyu-gui",
  "display_name": { "zh": "飞鱼", "en": "Feiyu" },
  "group_key": "飞鱼", "book_key": "中山经", "form_group": "beast",
  "basis": "text", "review_status": "reviewed",
  "quote": "其中多飛魚其狀如豚而赤文服之不畏雷可以禦兵",
  "commentary_quote": "",
  "description": "豚状赤文据文，四裂蹄、红斑纹样与底色卷尾站姿为解释；不以鱼/飞名添鳍翼，不借牛首鱼图。",
  "context_place_id": "place-zhongshan-r03-gui",
  "related_entry_ids": ["passage-zhongshan-r03-gui", "water-zhongshan-zhenghui-gui"],
  "artwork": true, "artwork_path": "zhongshan/creature-feiyu-gui-v1.webp"
 },
 {
  "id": "beast-qiongqi-xishan",
  "display_name": { "zh": "穷奇", "en": "Qiongqi" },
  "group_key": "穷奇", "book_key": "西山经", "form_group": "beast",
  "basis": "text", "review_status": "reviewed",
  "quote": "其上有獸焉其状如牛蝟毛名曰窮竒音如獋狗是食人",
  "commentary_quote": "或云似虎蝟毛有翼銘曰窮竒之獸厥形甚醜馳逐妖邪莫不奔走是以一名號曰神狗",
  "description": "正文牛状蝟毛、犬吼音、食人；虎状有翼仅郭注异说，不合图。",
  "context_place_id": "place-xishan-guishan4",
  "related_entry_ids": ["passage-xishan-guishan4"],
  "artwork": true, "artwork_path": "beasts/beast-qiongqi-xishan.webp"
 },
 {
  "id": "beast-qiongqi-hainei",
  "display_name": { "zh": "穷奇", "en": "Qiongqi" },
  "group_key": "穷奇", "book_key": "海内北经", "form_group": "beast",
  "basis": "text", "review_status": "reviewed",
  "quote": "穷奇状如虎，有翼，食人从首始，所食被发。",
  "commentary_quote": null,
  "description": "状如虎而有翼，食人；与《西山经》同名异形条目分开收录。",
  "context_place_id": null,
  "related_entry_ids": [],
  "artwork": true, "artwork_path": "beasts/beast-qiongqi-hainei.webp"
 }
]
```

见则志其余 6 站（补齐同字段）：

```json
[
 {
  "id": "beast-bifang", "display_name": { "zh": "毕方", "en": "Bifang" },
  "group_key": "毕方", "book_key": "西山经", "form_group": "bird",
  "basis": "text", "review_status": "reviewed",
  "quote": "有鳥焉其状如鶴一足赤文青質而白喙名曰畢方其鳴自呌也見則其邑有譌火",
  "commentary_quote": "譌亦妖訛字",
  "description": "鹤状一足，赤文青质白喙，鸣自叫；不添第二足或火焰器官。",
  "context_place_id": "place-xishan-zhange",
  "related_entry_ids": ["passage-xishan-zhange"],
  "artwork": true, "artwork_path": "beasts/beast-bifang.png"
 },
 {
  "id": "beast-nanshan-changyou", "display_name": { "zh": "长右", "en": "Changyou" },
  "group_key": "长右", "book_key": "南山经", "form_group": "beast",
  "basis": "text", "review_status": "reviewed",
  "quote": "有獸焉其状如禺而四耳其名長右其音如吟見則郡縣大水",
  "commentary_quote": "〔影印页23〕以山出此獸因以名之\n〔影印页23〕如人呻吟聲",
  "description": "长右山中之兽像禺而有四耳，鸣声如吟。原文以它的出现联系大水，不据此描写它主动引洪水。",
  "context_place_id": "place-nanshan-changyou",
  "related_entry_ids": ["passage-nanshan-changyou"],
  "artwork": true, "artwork_path": "nanshan/creature-changyou-v1.webp"
 },
 {
  "id": "beast-zhuyan", "display_name": { "zh": "朱厌", "en": "Zhuyan" },
  "group_key": "朱厌", "book_key": "西山经", "form_group": "beast",
  "basis": "text", "review_status": "reviewed",
  "quote": "其状如禺而白首赤足，名曰朱厌，见则大兵。",
  "commentary_quote": null,
  "description": "猿状白首赤足，见则有兵。",
  "context_place_id": null,
  "related_entry_ids": [],
  "artwork": true, "artwork_path": "beasts/beast-zhuyan.png"
 },
 {
  "id": "beast-fei", "display_name": { "zh": "蜚", "en": "Fei" },
  "group_key": "蜚", "book_key": "东山经", "form_group": "beast",
  "basis": "text", "review_status": "reviewed",
  "quote": "有獸焉其状如牛而白首一目而蛇尾其名曰蜚行水則竭行草則死見則天下大疫",
  "commentary_quote": "音如翡翠之翡；言其體含災氣也其銘曰蜚之；為名體似無害所經枯竭甚於鴆厲萬物斯懼思爾遐逝",
  "description": "蜚牛状白首、一目蛇尾；图中四裂蹄、双牛角、单目中置、蛇样尾鳞和深色躯为解释。蛇尾端不加蛇首或额外眼，稳定ID沿用。水竭草死疫兆与跨行铭文为古述。",
  "context_place_id": "place-dongshan-taishan-range4",
  "related_entry_ids": ["passage-dongshan-taishan-range4"],
  "artwork": true, "artwork_path": "dongshan/creature-fei-taishan-v1.webp"
 },
 {
  "id": "beast-dangkang", "display_name": { "zh": "当康", "en": "Dangkang" },
  "group_key": "当康", "book_key": "东山经", "form_group": "beast",
  "basis": "text", "review_status": "reviewed",
  "quote": "有獸焉其狀如豚而有牙其名曰當康其鳴自叫見則天下大穰",
  "commentary_quote": "",
  "description": "當康豚状有牙、鸣自叫，丰穰兆为古述。保留稳定ID及经复核旧图；四足、牙数、背毛配色及站姿为艺术解释，不把夸张牙数当原文。",
  "context_place_id": "place-dongshan-qinshan",
  "related_entry_ids": ["passage-dongshan-qinshan"],
  "artwork": true, "artwork_path": "beasts/beast-dangkang.webp"
 }
]
```

服佩辟邪其余 4 站：

```json
[
 {
  "id": "beast-jiuweihu", "display_name": { "zh": "九尾狐", "en": "Nine-tailed Fox" },
  "group_key": "九尾狐", "book_key": "南山经", "form_group": "beast",
  "basis": "text", "review_status": "reviewed",
  "quote": "有兽焉，其状如狐而九尾，其音如婴儿，能食人，食者不蛊。",
  "commentary_quote": null,
  "description": "青丘山有狐状而九尾的兽，声音像婴儿。经文随后写灌灌与英水；这些是同一山段相次记下的鸟兽与流水，不据此补出它们之间的捕食或因果关系。",
  "context_place_id": "place-qingqiu",
  "related_entry_ids": [],
  "artwork": true, "artwork_path": "beasts/beast-jiuweihu.webp"
 },
 {
  "id": "beast-boyi", "display_name": { "zh": "猼訑", "en": "Boyi" },
  "group_key": "猼訑", "book_key": "南山经", "form_group": "beast",
  "basis": "text", "review_status": "reviewed",
  "quote": "其状如羊而九尾四耳，其目在背，其名曰猼訑，佩之不畏。",
  "commentary_quote": null,
  "description": "羊状九尾四耳，眼睛在背上。",
  "context_place_id": "place-nanshan-jishan",
  "related_entry_ids": [],
  "artwork": true, "artwork_path": "beasts/beast-boyi.webp"
 },
 {
  "id": "beast-zhongshan-qinggeng-jinli11", "display_name": { "zh": "青耕", "en": "Qinggeng" },
  "group_key": "青耕", "book_key": "中山经", "form_group": "bird",
  "basis": "text", "review_status": "reviewed",
  "quote": "有鳥焉其狀如鵲青身白喙白目白尾名曰青耕可以禦疫其鳴自呌",
  "commentary_quote": "",
  "description": "鹊状青身白喙白目白尾据正文；羽纹双足姿态为艺术解释，不画医药符号或声称功效。",
  "context_place_id": "place-zhongshan-r11-jinli",
  "related_entry_ids": ["passage-zhongshan-r11-jinli"],
  "artwork": true, "artwork_path": "zhongshan/bird-qinggeng-jinli-v1.webp"
 },
 {
  "id": "beast-xishan-feiyi-ying", "display_name": { "zh": "肥遗", "en": "Feiyi" },
  "group_key": "肥遗", "book_key": "西山经", "form_group": "bird",
  "basis": "text", "review_status": "reviewed",
  "quote": "有鳥焉其状如鶉黄身而赤喙其名曰肥遺食之已癘可以殺蟲",
  "commentary_quote": "癘疫病也；或曰惡創韓子曰癘人憐主",
  "description": "英山肥遗是鸟，形如鹑，黄身、赤喙。它与太华山六足四翼的肥𧔥蛇分别保留稳定ID、形貌和原文；不因名称相近而合成一种异兽。食用功效仅作为古籍记述。",
  "context_place_id": "place-xishan-ying",
  "related_entry_ids": ["passage-xishan-ying"],
  "artwork": true, "artwork_path": "xishan/bird-feiyi-ying-v1.webp"
 }
]
```

## 4. D. 标签数据

### 4.1 schema

顶层：

```json
{
  "_note": "Derived effect/omen tags from the full text; entry status is auto (unreviewed) or reviewed (editorial spot-check). Derivatives only, never rewrites the source.",
  "_normalisation": "禦→御 見→见 動→动 訛→讹 靣→面 蟲→虫 殺→杀 癘→疠 國→国 縣→县 獸→兽 鳥→鸟 則→则 寧→宁 饑→饥 風→风 蠱→蛊",
  "_excluded": "可以為× (usage, e.g. 旋龜可以為底) is not tagged; 食之/佩之 without a stated effect is not tagged.",
  "entries": { "<entryId>": "EntryRecord" }
}
```

`EntryRecord`：

```json
{
  "status": "auto | reviewed",
  "basis": "text | commentary | comparison",
  "effect": ["Tag"],
  "omen": ["Tag"],
  "reviewed_at": "2026-11-09",
  "review_method": "editorial spot-check"
}
```

`Tag`：

```json
{
  "tag": "cure_disease | ward_fire | flood | drought | ...",
  "match": "原始匹配片段（归一并简体后的结果）",
  "evidence": "含上下文的摘句（归一后的结果）",
  "source": "quote | commentary_quote | description"
}
```

注意：`match` / `evidence` 经过 `_normalisation` 归一，字形可能与 `quote` 原字形不同；条目原文仍以 `myth-world.json` 为准。

### 4.2 五条完整样例

```json
{
 "beast-beishan-baiye-danzhang": {
  "status": "reviewed", "basis": "text",
  "effect": [{ "tag": "cure_disease", "match": "食之已嗌痛", "evidence": "白翼黄足名曰白鵺食之已嗌痛可以已痸", "source": "quote" }],
  "omen": [], "reviewed_at": "2026-11-09", "review_method": "editorial spot-check"
 },
 "beast-beishan-feiyi-hunxi": {
  "status": "reviewed", "basis": "text", "effect": [],
  "omen": [{ "tag": "drought", "match": "见则其国大旱", "evidence": "一首兩身名曰肥遺见则其国大旱", "source": "quote" }],
  "reviewed_at": "2026-11-09", "review_method": "editorial spot-check"
 },
 "beast-bifang": {
  "status": "reviewed", "basis": "text", "effect": [],
  "omen": [{ "tag": "fire", "match": "见则其邑有譌火", "evidence": "曰畢方其鳴自呌也见则其邑有譌火", "source": "quote" }],
  "reviewed_at": "2026-11-09", "review_method": "editorial spot-check"
 },
 "beast-zhongshan-qinggeng-jinli11": {
  "status": "reviewed", "basis": "text",
  "effect": [{ "tag": "ward_plague", "match": "可以御疫", "evidence": "白目白尾名曰青耕可以御疫其鳴自呌", "source": "quote" }],
  "omen": [], "reviewed_at": "2026-11-09", "review_method": "editorial spot-check"
 },
 "beast-xishan-fuxi-lutai": {
  "status": "reviewed", "basis": "text", "effect": [],
  "omen": [
   { "tag": "war", "match": "见则有兵", "evidence": "曰鳬徯其名自呌也见则有兵", "source": "quote" },
   { "tag": "war", "match": "见则有兵是经文的兵事征兆记述", "evidence": "字与其自呌相连。见则有兵是经文的兵事征兆记述；不新增手臂、兵", "source": "description" }
  ],
  "reviewed_at": "2026-11-09", "review_method": "editorial spot-check"
 }
}
```

## 5. E. 抽屉与同名机制

### 5.1 `bestiary.js` 同名查询（按 `group_key`）

```js
export function bestiaryNamesakes(world, id, locale = 'zh') {
  const selected = metadata[id];
  if (!selected) return [];
  return bestiaryEntries(world, locale)
    .filter(entry => entry.role === selected.role && entry.groupKey === selected.group_key)
    .sort((a, b) => (Number(notability[b.id]) || 0) - (Number(notability[a.id]) || 0));
}
```

### 5.2 `DetailDrawer.jsx` 同名下拉与并列

```jsx
const [parallelOpen, setParallelOpen] = useState(false);
useEffect(() => { setParallelOpen(false); }, [selected.id]);
...
<nav className="detail-related detail-namesakes" aria-label={t('同名记载')}>
  <select aria-label={t('同名记载')} value={selected.id}
    onChange={event => { pendingFocus.current = 'namesakes'; onRelated(event.target.value, readingPosition(), 'namesakes'); }}>
    {namesakeEntries.map(item => <option key={item.id} value={item.id}>{item.displayName} · {item.provenance}</option>)}
  </select>
  <button type="button" className="detail-parallel-toggle" aria-expanded={parallelOpen} aria-controls="detail-parallel"
    onClick={() => setParallelOpen(value => !value)}>{t(parallelOpen ? '收起并列校读' : '并列校读')}</button>
  {parallelOpen && <div className="detail-parallel" id="detail-parallel" data-parallel-count={namesakeEntries.length}>
    {namesakeEntries.every(entry => /^(其)?[中陰隂陽阳獸兽]?多|^是多/.test((entry.quote || '').trim())) && <p className="detail-parallel-generic">{t('本组多为泛称罗列，并列仅作索引。')}</p>}
    ...
  </div>}
</nav>
```

注意最后一行 `namesakeEntries.every(...)` 是**浏览器内**的范围词判断，属于第 0 节标注的“部分不成立”。新增路线若需要判断“泛称/同名异形”，应在构建期或验证脚本预计算，不要复制这个正则。

### 5.3 能否打开时预选同名条目？

- **通常不需要改**：每个同名条目都有自己的 `entryId`，路由站点点开时直接传目标 id，抽屉的 `selected` 就是它，同名下拉自然显示它。
- **如果要一打开就展开“并列校读”**：当前没有这个入口。`parallelOpen` 初始为 `false`，且 `selected.id` 变化时重置。最小改动：
  1. `open(id, trigger, sequence, options)` 增加可选 `options.parallel`；
  2. `DetailDrawer` 接收 `initialParallel`；
  3. 在 `selected.id` 的 effect 中 `setParallelOpen(Boolean(initialParallel))`，并在需要时展开 `.detail-evidence`（现有 `applyPosition` 只按阅读位置开折叠区）。
- 不改数据结构，也不改同名查询。

## 6. F. 验证脚本

### 6.1 `verify-bestiary.mjs` 路线相关断言

```js
const EFFECT_TAGS = ['ward_fire', 'ward_war', 'ward_evil', 'ward_plague', 'cure_disease', 'travel', 'calm', 'nourish'];
const OMEN_TAGS = ['flood', 'drought', 'war', 'famine', 'plague', 'fire', 'wind', 'bountiful', 'peace', 'other_omen'];
...
for (const route of guideRoutes.routes) {
  assert.ok(route.id && route.title?.zh && route.title?.en && route.intro?.zh && route.intro?.en, `${route.id}: bilingual title and intro`);
  assert.ok(!/[\u3400-\u9fff]/.test(route.title.en + route.intro.en), `${route.id}: English route copy`);
  assert.equal(new Set(route.stops.map(stop => stop.entryId)).size, route.stops.length, `${route.id}: unique stops`);
  for (const stop of route.stops) {
    assert.ok(metadata[stop.entryId], `${route.id}: route stop ${stop.entryId} exists`);
    assert.ok(stop.label?.zh && stop.label?.en && !/[\u3400-\u9fff]/.test(stop.label.en), `${route.id}/${stop.entryId}: bilingual label`);
  }
}
...
await routesPage.locator('#routes').scrollIntoViewIfNeeded();
assert.equal(await routesPage.locator('.guide-route-tabs button').count(), guideRoutes.routes.length);
const firstStop = guideRoutes.routes[0].stops[0];
await routesPage.locator(`[data-route-stop="${firstStop.entryId}"]`).click();
await routesPage.locator(`.detail-drawer[data-entry-id="${firstStop.entryId}"]`).waitFor();
assert.equal(await routesPage.locator('.world-layout').getAttribute('data-timeline-playing'), 'false', 'Routes do not start the guided tour');
```

### 6.2 构建期预计算的先例

存在，且是项目常态：

- `data/build_semantic_tags.py`：从 `myth-world.json` 抽标签，写 `frontend/src/bestiary-semantic-tags.json`。
- `data/build_nanshan.py`、`build_xishan.py`、`build_beishan.py`、`build_dongshan.py`、`build_zhongshan.py` 及 `*_completion.py`：生成 `myth-world.json` 的篇目数据。
- `data/build_myth_atlas.py`、`build_geography_basemap.py`、`audit_shanhaijing.py`、`english_review.py`：生成/校验派生数据。
- `frontend/scripts/assets/prepare-*`：处理发布图像。

因此“同名异形/范围词”检查适合放在构建脚本或 `verify-bestiary`/`verify-data`，不应放进路线组件。

## 7. G. 祭礼（形态 D）的数据

### 7.1 `text_entities` 中 `kind: "rite"`

总数 **94**，按篇目（按 id 前缀统计）：

| 篇目 | rite 条数 |
| --- | ---: |
| 南山经 | 3 |
| 西山经 | 7 |
| 北山经 | 18 |
| 东山经 | 10 |
| 中山经 | 56 |
| 合计 | 94 |

说明：94 条包含“列末总括”“单项祭品/祭玉”等细分条目，不等于 94 个独立祭礼。每条都有 `id`、`name`、`kind: "rite"`、`quote`；大多数没有 `description`/`artwork`。

代表条目（id / 名称 / 篇目 / 数量或性质）：

```json
[
 { "id": "rite-nanshan-1", "name": "䧿山祭礼", "book": "南山经", "note": "十山总括，鸟身龙首神" },
 { "id": "rite-nanshan-2", "name": "南次二经祭礼", "book": "南山经", "note": "十七山总括，龙身鸟首神" },
 { "id": "rite-nanshan-3", "name": "南次三经祭礼", "book": "南山经", "note": "十四山总括，龙身人面神" },
 { "id": "rite-xishan-hua-range1", "name": "华山冢与太牢祠礼", "book": "西山经", "note": "华山冢太牢" },
 { "id": "rite-xishan-yu-range1", "name": "羭山燭礼与玉器", "book": "西山经", "note": "羭山神，百犧、百瑜、百珪百璧" },
 { "id": "rite-beishan-range1-summary", "name": "北山经首列总括与祭礼", "book": "北山经", "note": "二十五山，人面蛇身" },
 { "id": "rite-dongshan-range1-summary", "name": "首列总括与祭礼", "book": "东山经", "note": "十二山，人身龙首，犬与鱼" },
 { "id": "rite-zhongshan-r01-summary", "name": "次1总括与祭礼", "book": "中山经", "note": "十五山，太牢、吉玉、桑封" },
 { "id": "rite-zhongshan-r07-summary", "name": "次7总括与祭礼", "book": "中山经", "note": "十九山，十六神豕身人面" },
 { "id": "rite-zhongshan-r12-summary", "name": "次12总括与祭礼", "book": "中山经", "note": "十五山，鸟身龙首" }
]
```

### 7.2 山神形貌条目（`kind: "deity"`）

共 21 条有“鸟身/龙身/人面/兽身/豕身/马身/彘身”等形貌总述，按篇目：

| 篇目 | id | 形貌 |
| --- | --- | --- |
| 南山经 | `deity-nanshan-1` | 鸟身而龙首 |
| 南山经 | `deity-nanshan-2` | 龙身而鸟首 |
| 南山经 | `deity-nanshan-3` | 龙身而人面 |
| 西山经 | `deity-xishan-horse-range2` | 人面马身（十神） |
| 西山经 | `deity-xishan-sheep-range3-summary` | 羊身人面 |
| 北山经 | `deity-beishan-human-serpent-range1-summary` | 人面蛇身 |
| 北山经 | `deity-beishan-human-serpent-range2-summary` | 蛇身人面 |
| 北山经 | `deity-beishan-horse-human-range3` | 马身人面（二十神） |
| 北山经 | `deity-beishan-pig-jade-range3` | 彘身载玉（十四神） |
| 北山经 | `deity-beishan-pig-eight-snake-range3` | 彘身八足蛇尾（十神） |
| 东山经 | `deity-dongshan-human-dragon-range1` | 人身龙首 |
| 东山经 | `deity-dongshan-humanface-antlers-range2` | 兽身人面载觡 |
| 东山经 | `deity-dongshan-human-ramhorn-range3` | 人身羊角 |
| 中山经 | `deity-zhongshan-humanbird-range2` | 人面鸟身 |
| 中山经 | `deity-zhongshan-humanbeast-range4` | 人面兽身 |
| 中山经 | `deity-zhongshan-humanpig-range7` | 豕身人面（十六神） |
| 中山经 | `deity-zhongshan-humanbird-summary8` | 鸟身人面 |
| 中山经 | `deity-zhongshan-horsedragon-summary09` | 马身龙首 |
| 中山经 | `deity-zhongshan-human-dragon-summary10` | 龙身人面 |
| 中山经 | `deity-zhongshan-humanhead-pig-summary11` | 彘身人首 |
| 中山经 | `deity-zhongshan-dragonhead-bird-summary12` | 鸟身龙首 |

两条完整记录：

```json
[
 {
  "id": "deity-nanshan-1",
  "name": "䧿山诸神",
  "kind": "deity",
  "quote": "凡䧿山之首自招揺之山以至箕尾之山凡十山二千九百五十里其神狀皆鳥身而龍首其祠之禮毛用一璋玉瘞糈用稌米一壁稻米白菅為席",
  "commentary_quote": "〔影印页22〕言擇牲取其毛色也周官曰陽杞用騂牲之毛；半圭為璋瘞埋\n〔影印页22〕也；糈祀神之米名先吕反今江東音所一音壻稌稌稻也他覩反糈或作疏非也\n〔影印页22〕菅茅属也音間",
  "description": "本列山神的共同形貌为鸟身龙首。这是山列总述，没有给出各神的独立名字。",
  "related_entry_ids": ["passage-nanshan-range1"],
  "artwork": "nanshan/deity-1-v1.webp"
 },
 {
  "id": "deity-zhongshan-humanbird-summary8",
  "name": "次八山神（鸟身人面）",
  "kind": "deity",
  "quote": "其神狀皆鳥身而人面",
  "commentary_quote": "",
  "description": "鸟身人面据正文，图为完整鸟躯配人面，不画成人身长翼；鸟种、双足、翼尾布局、年龄、配色和姿态为艺术解释。",
  "related_entry_ids": ["passage-zhongshan-r08-summary", "rite-zhongshan-r08-summary"],
  "artwork": "zhongshan/deity-humanbird-range8-v1.webp"
 }
]
```

## 8. H. 文字规范与现状

### 8.1 现有英文标签/简介样例

- 路线标题：`Omens and signs` / `Wards and remedies`
- 路线简介：`Follows the text's own omen clauses across disasters and auspicious signs.`；`Only accounts whose text states an effect after eating or wearing; accounts without one stay out.`
- 详情折叠：`Variant readings and evidence`；`Sources and notes`；`Identity traditions`
- 标签：`Same-name accounts`；`Morphology evidence`；`Effects and omens`；`Comparison account`
- 按钮：`Filter by this effect`；`Filter by this omen`；`View same-name accounts`

### 8.2 英文文风约定

`docs/review-guide.md` **不存在**英文文风段落；它只讲复审口径。项目里明确的英文范围与声明在 `docs/editorial-review.md`：

> 完成模型辅助审校：逐条阅读974组界面中英文本、45条形貌焦点记录的英文说明及引文、36条当前已有英文的故事条目。对整个3166条内容字典做结构、空值、中文泄漏、明显占位词及拼写模式检查。其余条目的语义与古文释读未全部逐句审校；7条未暴露故事无英文条目，本次不扩展内容接入范围。

> 古籍食疗、灾异和护兵记载均保留为古人所述。正文、郭注与编辑说明的层次不合并。现行页面继续声明英文由模型生成，未声称已完成专业审校。

页面声明见 `README.zh-CN.md`：`英文译文由模型生成，未声明已完成专业审校。`

### 8.3 `docs/depth-roadmap.md` 第 4.4 节现状

- 目标：专题巡山录先做 2–3 条，入口独立，不复用“开始游历”的入口与状态机。
- 实现：区块 `#routes` 位于异兽谱之后、读图与依据之前；两条路线 10 个点位；点位只打开条目，不启动导览。
- 未解决：路线仍像“按标签筛出的序列”；第 5 项复审记录写明“路线与筛选/征兆的区别仍未解决”。

### 8.4 第 8 节复审现状

- 第 1 项 effect/omen 标签：已抽查通过，95 条 `reviewed`。
- 第 2 项枚举边界：确认保留（`fire` 归 omen；`bountiful` 独立；`ward_evil` 吸收“杀虫”）。
- 第 3 项泛称组：确认保留现状。
- 第 4 项异说归属：5 条 `comparison` 保留；启母仍为 `commentary`；帝之二女改称“身份异说”。
- 第 5 项路线内容：两条路线保留；差异化待定。
- 第 6 项免责文案：待定。

## 9. 请评估回答的问题

1. 第 0 节哪些前提不成立？路线方案必须怎么改才能回到约束内？
2. 现有两条路线是否值得保留？如果保留，先改哪一条？
3. 五种候选形态（论点、对照、空间、祭礼、问题链）各自的数据充足性、组件改动、编辑成本、风险。
4. 对照站能否只用一个按钮实现？需要 `initialParallel` 还是别的机制？
5. 祭礼形态能否凑出 4–6 站？用哪些 rite/deity id？
6. 增量 gzip 的实测口径：以什么为基线、量什么文件、如何记录？
7. 给出一个最小实现顺序与验证断言清单，不要先做分支或自动播放。

## 10. 不存在项汇总

- 25 KiB gzip 的强制脚本/阈值常量：不存在。
- 路线按功能记账的 gzip 用量：不存在。
- `guide-routes` 的懒加载或独立 chunk：不存在。
- 打开抽屉时预选/自动展开并列校读的入口：不存在（需最小改动）。
- `docs/review-guide.md` 的英文文风段落：不存在。
- 路线卡片图片：不存在。

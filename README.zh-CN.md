# 山海寻踪

**[English](./README.md)** | **中文版**

一卷山海，七章神话。以纸本版画风格呈现中国古代神话，通过地图、动画和异兽插画，探索《山海经》中的世界。

**[在线体验 →](https://hyc1005.github.io/mythmap/)** · [GitHub 仓库](https://github.com/hyc1005/mythmap)

## 可以看什么

- **神话地图**：从盘古开天序章出发，浏览七章故事、地点与神域。
- **故事动画**：支持播放、暂停、重播和全屏展示。
- **异兽谱**：浏览 32 项异兽，按名称、形貌或篇目查找。
- **原文出处**：点击地图地点或异兽卡片，查看描述和所引篇章。

打开网页即可体验，支持电脑和手机。图面表达篇目方位与叙事关系，不表示真实距离或精确年代；插画是依据原文的艺术解释。

---

## 开发与维护

以下内容供本地运行、部署和数据维护使用。

### 技术与目录

前端使用 React 19、Vite 6、OpenLayers 10，动画使用 Remotion 4。在线版由 GitHub Actions 构建、GitHub Pages 托管，使用内置数据，无需后端或数据库。

| 目录 | 用途 |
| --- | --- |
| `frontend/src/` | 应用入口、共享状态与工具 |
| `frontend/src/components/` | 地图、图鉴、搜索及阅读面板 |
| `frontend/src/animations/`、`frontend/src/styles/` | 故事渲染与页面样式 |
| `frontend/public/data/` | 网站数据与发布素材 |
| `frontend/artwork-source/` | 插画原图与备用素材 |
| `frontend/scripts/` | 布局与叙事验证 |
| `backend-java/` | 可选 Java API |
| `backend/`、`database/` | 旧版 FastAPI/PostGIS 原型与数据库工具 |
| `data/`、`docs/` | 数据维护工具与项目资料 |

### 本地运行

需要 Node.js 22 或更新的兼容版本。在 `frontend/` 目录执行：

```bash
npm ci
npm run dev -- --host 127.0.0.1
```

打开 [本地开发页面](http://127.0.0.1:5173/#world)。开发模式会尝试访问可选 API，未启动时自动使用内置数据。

可选 Java API 需要 JDK 17 或以上，在 `backend-java/` 运行 `run.ps1`，默认端口为 8081。生产版默认不请求 API；外部 API 配置见 `frontend/.env.example`，`VITE_API_BASE_URL` 会公开到构建产物中。

### 构建与验证

在 `frontend/` 目录构建，并通过统一入口启动验证。测试使用动态端口，正常结束、失败或中断时关闭本次创建的预览进程，并复查端口释放：

```bash
npm run build -- --base /mythmap/
node scripts/with-preview.mjs --base /mythmap/ -- node scripts/verify-design.mjs
node scripts/with-preview.mjs --base /mythmap/ -- node scripts/verify-guided-tour.mjs
node scripts/with-preview.mjs --base /mythmap/ -- node scripts/verify-reading.mjs
node scripts/with-preview.mjs --base /mythmap/ -- node scripts/verify-resume.mjs
node scripts/with-preview.mjs --base /mythmap/ -- node scripts/verify-search.mjs
node scripts/with-preview.mjs --base /mythmap/ -- node scripts/verify-narrative.mjs
```

人工预览使用 `npm run preview:managed -- --base /mythmap/`，固定监听 127.0.0.1:4183；端口被占用时直接报错，不终止已有进程。浏览结束按 Ctrl+C 关闭。不要在验证期间重新构建同一个 `dist/`。

`verify:design` 覆盖双语六种视口、手机面板焦点和滚动锁定、正文对比度、六类插画样本、播放状态和 PNG 纸色。`verify:layout` 检查五种视口的动画、全屏和详情，`verify:narrative` 另检查完整叙事、素材和时间轴。截图保存在 `output/qa/`。本机 Firefox 若无法启动，须单独报告；CI 保留三种浏览器检查。

发布前复查电脑与手机上的动画、地图全屏、异兽搜索、详情关闭和出处链接，并确认刷新正常、图片无 404。

### GitHub Pages 部署

工作流位于 `.github/workflows/deploy-pages.yml`。在仓库 **Settings → Pages** 中选择 **GitHub Actions**；推送到 `main` 的前端或工作流修改会自动构建并发布。文档修改不会触发网页部署。

工作流自动处理 Pages 子路径，完成数据、缓存、后端、双语、探索、失败恢复、阅读、搜索与完整叙事检查后，发布同一份已验证的 `frontend/dist/`，无需手动提交构建产物。部署结果可在仓库 Actions 页面查看；回退使用 `git revert` 后推送。

### 数据与插画维护

- 主要数据位于 `frontend/public/data/`：`myth-world.json` 及 `atlas/` 下的 `catalog.json`、`story-animations.json`、`kuafu-journey.json`。
- 出处与素材核对使用 `atlas/review.json`、`atlas/artwork-manifest.json`；原图保存在 `frontend/artwork-source/`。
- `data/build_myth_atlas.py` 仅输出旧版数据到 `output/legacy-atlas/`，禁止覆盖网站审核数据。
- 可选静态地图由 `data/render_myth_atlas.py` 生成，需要 Pillow、pyproj 和指定的 Windows 字体，输出到 `output/atlas/`。
- 旧版 API、数据库与导入工具的说明见各目录 README。

`node_modules/`、`frontend/dist/`、`output/` 和本地环境配置均由 Git 忽略。

维护验证：新增 `npm run verify:repairs` 覆盖 Chromium、Firefox、WebKit 的失败恢复、详情焦点、定位和语言状态保留；首次需安装三种 Playwright 浏览器。减少动态效果模式统一逐幕手动推进。发布等待全部必要检查通过，并直接部署已验证产物。

手动切换章节保持静态；选择故事动画后才播放。连续游历按本章目录顺序播放可用动画，文字章节等待点击继续。手机提供“故事近景／本章全图”，切换视野保留播放进度。

条目详情支持手动标记已读、收藏及前后切换；长文末尾可选择“读完，下一条”。异兽谱可按阅读状态筛选，“本章条目”中的“我的收藏”汇总跨章节收藏。标记仅保存在当前浏览器，分享链接不包含这些私人状态；浏览器存储不可用时仅保留本页会话。

“继续上次阅读”恢复最近条目和段落位置；刷新正在阅读的同一条目也会恢复。插画和字体加载后再定位，支持展开的英文页中文原文。普通条目／分享链接从头打开，标记与续读信息保存在不同的浏览器本地记录中。

顶部“搜索”统一检索故事、异兽、出处、地点与神域；支持中文原名及当前语言文本，出处结果关联可阅读的条目。搜索面板会暂停背景动画，关闭后继续。相柳九首补绘与三张地图专用小图标通过 `src/refined-artwork.json` 接入，原图与完整生图提示词保留于 `artwork-source/woodcut-refinement/`；运行 `python scripts/prepare-refined-artwork.py` 可重新输出发布版本。

本地交接文档不进入 Git。验收产物、构建目录和浏览器缓存不作为发布源文件；插画原图继续版本管理以便复现，生图记录仅保留仓库相对路径。

### 真实地理基础视图

探索主区域默认“木刻叙事”，通过“真实地理”切换，沿用同一章节导航和全屏容器。真实地理使用连续的 OpenStreetMap 在线瓦片，保留可见署名，沿用 OSM 的边界与地名表达。“全国总览”包含大陆、台湾、海南和南海相关区域；“查看本事件地点”明确定位筛选结果。切换事件只更换关联标记，不自动移动镜头。

28项既有考证候选和盘古、精卫的4条地方传说关联继续保留；地点表示传承或考证关联，不证明神话事件发生，无定位依据时不补造坐标。保留事件内查询、分类符号、出处与版本对照、经纬度、比例尺、两点球面测距和筛选结果 GeoJSON 导出。两种模式分别保留镜头；本次页面会话中保留地理查询与对照选择。进入地理暂停故事，返回保留进度。章节提示持续1200毫秒，暂停被遮住的故事；无地点事件显示2500毫秒“暂无记录”，资料区保留说明。

继续支持 GitHub Pages，无需后端或密钥；在线底图需要网络，瓦片失败时显示错误和重试，不使用旧区域裁剪图代替完整地图。遵循 [OSM 瓦片使用政策](https://operations.osmfoundation.org/policies/tiles/)，使用浏览器缓存，不批量下载或预取。旧 Natural Earth 资产和 `scripts/prepare-geography.py` 保留供复现，已不作为当前底图或自动回退。

构建后通过 `node scripts/with-preview.mjs --base /mythmap/ -- node scripts/verify-geography.mjs` 验证，`verify-map-frame.mjs` 同样通过包装入口运行。地理自动化测试模拟瓦片，不请求公共 OSM 服务；生成的相关截图仅用于布局验收，不代表真实地理影像。CI保留三浏览器检查。

故事动画基础速度统一为旧版的1.3倍，按钮1×/2×相对于新基础速度。`src/playback.js` 管理基础倍率；`npm run verify:playback-speed` 验证三类时钟。地方传说增量和试点证据保存在 `src/geography-associations.json`，与旧候选合并时保留原ID和坐标，待核验资料不冒充已核对出处。

地理视图提供“对照本事件资料”：选择两条同事件记录，对照关联说明、类别、核验状态、原文摘录、出处和坐标精度；桌面双栏、手机纵排。对照使用本事件全部资料，不受地点搜索影响，切换模式后保留选择，切换事件时重置；不对地点排名，也不编造故事异文。

地理视图现有32条关联记录（28条旧候选、4条地方传说）。资料对照提供可追溯摘要及解释边界，标明来源机构、发布时间（已知时）、核对日期、段落定位和核对范围；搜索索引片段与网页正文分别标注，共享引文不作为独立故事版本证据。没有完整异文时只说明传承关联。

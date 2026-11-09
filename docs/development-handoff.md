# 开发交接：水墨开篇与阅读交互

更新：2026-11-07。本文件随仓库提交，供其他 agent 接续；根目录被忽略的本地交接文档保留历史。

## 当前状态与授权

- 本轮 UI 提交为 `c6bb559`，已推送 `codex/actions-speedup`。用户随后明确授权“合并且部署”，已快进合并并推送 main；之前“不合并 main、不部署”的安排已被本次授权替代。
- 首轮 main 发布 [42348028931](https://github.com/hyc1005/mythmap/actions/runs/42348028931) 构建成功，但素材审计因浅检出缺少 `git:447d823...` 等历史证据而失败（git show 退出 128）。已恢复 narrative 审计任务的 `fetch-depth: 0`；构建与浏览器的轻量检出不变，所有校验及 deploy 的 needs 门槛保留。修复提交后继续完整 main 发布。
- `39a4d8e` 的重跑在 `pages-main` 并发组排队约 20 分钟仍未开始，已取消，该提交没有运行结果。`625f118` 让叙事与引导用例经 `?splash=0` 进入、放宽章节时钟余量后重新推送。
- [42351743119](https://github.com/hyc1005/mythmap/actions/runs/42351743119) 首轮 24 成功、1 失败：`fetch-depth: 0` 让素材审计通过，浏览器任务只剩 `webkit / atlas` 在 `verify-resume.mjs:138` 等待 `.detail-drawer` 超时。三次重跑分别失败于同一处、`verify-design.mjs` 的 `page.goto: WebKit encountered an internal error`、再次 `verify-resume.mjs:138`；第 4 次重跑通过，deploy 于 08:57:45Z 成功，Pages 部署 SHA 为 `625f118`。同脚本在本机 WebKit 连续 3 次、每次约 33 秒均通过，属于 CI 上的 WebKit 不稳定，不是本轮改动引入；旧交接记录的同类 WebKit 超时仍未定根因。
- 2026-11-09 的 `9ca927a`（影片返回、默认排序、Open Graph、CI 拆分）与 `e075f38`（测试兼容修复）已发布：[42537656721](https://github.com/hyc1005/mythmap/actions/runs/42537656721)。首轮 `webkit / southern-cards` 单 Job 卡住约 60 分钟，取消整轮后只重跑该 Job，10 分钟通过；最终 26 个 Job 全绿，部署 `e075f38`（00:59Z）。排序改动曾让三个 atlas Job 同时失败，原因是测试假设首屏条目；已改为搜索定位与集合比对，不再依赖编辑顺序。
- 本轮开始前已有 `CHANGELOG.md`、`docs/editorial-review.md`、`frontend/src/assets/shanhai-mark.svg` 修改。保留这些内容；不要覆盖或无差别提交与本轮无关的改动。
- 古籍译注审校继续暂停。本机 `gh` 不在 PATH，常见安装位置也未找到；已用公开 GitHub REST API 读取最近 50 次运行及最新运行的 Jobs API，并用 `git ls-remote --heads origin` 核对远端分支。必需状态设置 API 返回 401，不能据此认定 main 没有分支保护。
- 远端基线：`main` 为 `e075f38`，部署同为 `e075f38`（00:59Z），与本地一致；`codex/actions-speedup` 为 `c6bb559`。2026-11-07/08 的失败运行 [42348028931](https://github.com/hyc1005/mythmap/actions/runs/42348028931) 与 [42351743119](https://github.com/hyc1005/mythmap/actions/runs/42351743119) 已处理完毕：前者暴露浅检出缺历史（后续以 `fetch-depth: 0` 修复）与四项浏览器用例，后者在第 4 次尝试通过并首次部署开屏版本；失败明细与修复见下方“CI 稳定性”。
- 临时输出、`output/`、`node_modules/`、`frontend/dist/` 和根目录本地交接不提交。过程文件删除前仍需先询问用户“可以删了吗？”。

## 已实施与主要入口

| 范围 | 文件与行为 |
| --- | --- |
| 启动与策略 | `frontend/index.html` 保留纸色 dialog 和进入按钮，初始不显示静态四字；`src/main.jsx` 是轻量入口；原 React 挂载位于 `src/app-entry.jsx` |
| 开屏 | `src/splash/index.js`、`createInk.js`、`stage.html`、`stage.css` 从 v12 独立原型迁移；动态加载、Shadow DOM 隔离，默认 low，结束淡出。正式构建不依赖本地 `output/` 或绝对路径 |
| 重播与衔接 | `App.jsx` 品牌发出 `splash:replay`；入口发出 `splash:start` / `splash:done`。同页重播，不重新挂载 App；保留焦点返回；新手引导在开屏关闭后挂载 |
| 导航字体 | `src/assets/shanhai-nav.woff2` 是现有 `public/fonts/shanhai-title.woff2` 的导航文字子集，约 7.5KB；`styles/atlas-layout.css` 定义导航字体，现有 Noto Serif SC OFL 随站点发布 |
| 文字显现 | `components/BlurRevealText.jsx` 的 `REVEAL_EASING_MS = 1200`；支持 `text` 或 `children`、`as`。读图全文使用一个 `as="div"` 文本块，五段不再各自独立显现；按钮/输入/状态提示保持清晰 |
| 正文覆盖 | `App.jsx`、`DetailDrawer.jsx`、`ChapterEntries.jsx`、`GlobalSearch.jsx`、`GeographicEvidence.jsx`、`GeographyComparison.jsx` 补齐正文与引文。保留查找、选文、阅读位置恢复、打印、减少动态效果时清晰可读 |
| 折叠 | `RevealDetails` 保留原生 details/summary；280ms 高度过渡和箭头旋转，支持键盘、快速反向、减少动态效果；不依赖第三方动画库 |
| 标签切换 | `components/PaperTabs.jsx` + `paper-interactions.css`：240ms 朱砂滑动选中块；用于地图模式、异兽/神灵和语言，保留原按钮及 `aria-pressed`，不改变地图或筛选语义 |
| 开篇影像 | `public/opening-film.html` 为自包含宣传片（2.82 MB，内嵌 5 PNG/5 WebP 角色帧），不进入首屏；唯一入口是页脚藏书印 `.bookplate-link`。左上角返回链接与「跳过」/Esc 都回上一页，HUD 只留「重播」「声音」 |
| 默认排序 | `src/bestiary-notability.json` 是人工维护的知名度权重，`bestiary.js` 的默认列表先按权重、再按原顺序；搜索仍先看匹配度。文件独立于生成数据，可直接编辑 |
| 社交预览 | `index.html` 声明 Open Graph / Twitter Card；`public/og-image.webp` 为 1200×630 裁切图，经 `publish-files.mjs` 白名单发布 |
| 深度路线 | `docs/depth-roadmap.md` 是评审稿：记录数据基线、三处修正与四个顺位，明确不做项；仅文档，未实施 |
| 浏览器标题 | 站点标题固定为 `山海寻踪`（英文 `Shanhai Atlas`），不再附带副标题；`verify-locale` 的 `startsWith('Shanhai Atlas')` 仍成立 |

策略：`?splash=1` 强制演示；`?splash=0` / `?nosplash` 跳过；带其他查询或 hash 的深链跳过自动播放。标记键为 `localStorage['shanhai-splash:v12:seen']`。减少动态效果始终跳过自动播放；主动点击品牌时可看静态降级。跳过或播放结束写入标记。开屏对话框内任意点击等同于「进入网站」；按钮、Esc、重播、加载中与淡出中的重复触发由既有幂等保护挡住，`verify-splash.mjs` 覆盖这些路径。

本轮借鉴 [Bencho Text blur](https://bencho.dev/blocks/text-blur)、[FAQ accordion](https://bencho.dev/blocks/faq-accordion)、[Tab bar](https://bencho.dev/blocks/tab-bar) 的交互方式，没有复制 Pro 源码，没有新增 `framer-motion` / `lucide-react` / Tailwind 依赖。原生实现沿用项目许可；流体源码保留 Pavel Dobryakov MIT 头，题字来自 Ma Shan Zheng（OFL）。

## CI 稳定性：WebKit 偶发失败与单次重试

- 现象：`webkit / atlas` 在 2026-11-07 至 11-08 的 5 次运行里 5 次失败，但位置每次不同：`verify-resume.mjs:138` 等 `.detail-drawer`（2 次）、`verify-design.mjs` 的 `page.goto: WebKit encountered an internal error`（1 次）、`verify-exploration.mjs:296` 等 `.artwork-fallback`（1 次）。同一脚本在本机 WebKit 连续通过，重跑后也能通过，没有出现可复现的应用侧断言失败。
- 判断：属于 CI 上 WebKit 进程的偶发崩溃或超时，不是某个断言稳定失败；11-05/11-06 的交接记录里已有同类未定根因的超时。
- 处理：浏览器步骤对每个脚本先跑一次，失败后在新浏览器中原样重试一次；第二次仍失败则 Job 失败。重试不跳过断言、不降低发布门槛，`::warning::` 会在日志中标出被重试的脚本，失败诊断附件仍按原逻辑上传。2026-11-09 起 `webkit / atlas` 再拆成两个 Job（前 5 个脚本 / 后 6 个脚本），单 Job 约 10–13 分钟，减少长跑压力；两个 Job 都使用 `atlas` 的轻量检出 profile，名字与 shard 区分。另有一个独立长尾：`webkit / southern-cards` 偶发跑到 60 分钟以上（正常 15–25 分钟），处理方式是取消整轮后仅重跑该 Job，通常 10 分钟内通过。
- 边界：重试只处理瞬态问题。若同一脚本连续两次失败，应按真实回归排查，不要继续加大重试次数或跳过脚本。

## 本地预览与验证

以下命令在 `frontend/` 执行。先完成 build，再运行浏览器验证；不要在验证尚未结束时重建同一个 dist。

```powershell
npm run build -- --base /mythmap/ --logLevel error
node node_modules/vite/bin/vite.js preview --host 127.0.0.1 --port 4187 --strictPort --base /mythmap/
```

首页：`http://127.0.0.1:4187/mythmap/?splash=0`；强制开屏：`http://127.0.0.1:4187/mythmap/?splash=1`。预览端口只在原本进程仍运行时可用。

```powershell
$env:ATLAS_URL='http://127.0.0.1:4187/mythmap/'
$env:ATLAS_BROWSERS='chromium,webkit'
node scripts/verify-blur-global.mjs
node scripts/verify-blur-detail.mjs
npm run verify:paper
npm run verify:publish
npm run verify:data
```

界面改动可先运行 `$env:ATLAS_LOCALE_SCOPE='ui'; node scripts/verify-locale.mjs`，仍检查四尺寸、八章节、双语切换/持久化、筛选及故事播放器；仅省去逐一打开全部独立条目的抽屉遍历。完整模式使用 `$env:ATLAS_LOCALE_SCOPE=''; node scripts/verify-locale.mjs`，默认行为与 CI 完整检查保持一致。

验证状态：

- 前一轮全局模糊验证：Chromium 双语六尺寸、详情双语手机/桌面、WebKit 手机/桌面全文显现、中文/英文地理资料与对照检查已通过；此前时长为 1.5 秒。
- 2026-11-09 线上复核：标题为「山海寻踪」，`og:image` 指向 `/mythmap/og-image.webp`；异兽谱默认前六为九尾狐/相柳/开明兽/凤皇/毕方/穷奇；藏书印进入影片后，「跳过」回到站点原页；无页面错误。本地对应 `verify-splash`（Chromium/WebKit）、`verify-bestiary`、`verify-reading`（Chromium/WebKit）、`verify-exploration`（Chromium/WebKit）与 `verify-design`（Chromium）全部通过。
- 2026-11-07 本批最终生产构建通过；`verify:paper` 的 Chromium/WebKit × 手机/桌面四例通过：滑动选中位置与字体/语言变化同步、异兽筛选、折叠开关、键盘操作、快速反向、减少动态效果，以及全文 1.2 秒显现。
- `verify-blur-global.mjs` 的 Chromium 双语六尺寸 12 例通过；`verify-blur-detail.mjs` 的 Chromium 双语手机/桌面四例完整复跑通过。首次详情运行曾在“继续阅读保留位置”断言失败，随后完整复跑未复现，未修改位置恢复算法，也未将首次失败归因于并发或宣称根因已修复。
- `verify-onboarding.mjs` 的 Chromium 双语四尺寸通过；最终开屏同页重播/Esc/App 不重挂载复查通过。
- `verify:publish`、`verify:data`、`verify-assets.py` 通过；补登记导航字体后最终素材审计为 2033 文件、1850 来源指针、1177 派生关系，errors 为空。`git diff --check` 通过。
- `verify:locale`：旧测试仍按太阳总位移超过 5 个 SVG 单位断言，而本轮开始前的 SVG 已调整为最多 3 单位；保留现有 SVG，测试改为核对当前幅度内确实运动。完整模式首次运行遍历完桌面故事、神灵及异兽后，发现语言持久化断言在新异步入口尚未挂载 App 时就检查 HTML 默认语言；已补 App/语言就绪等待，保留原持久化断言。最终 `ATLAS_LOCALE_SCOPE=ui` 已全部通过：1440×1000、390×844、320×700、844×390 的八章节、双语切换/持久化、搜索/筛选与布局，以及英文序章和六个故事的播放、暂停、来源详情。完整逐条模式未在同步修正后完整复跑，不将其写成全量通过。
- 开屏前期检查通过：正常完成、提前进入/Esc、重复同页重播、首访/回访/深链/减少动态效果、WebGL 不可用、contextlost、主包下载失败重试；本轮已另行复查新交互下同页重播、Esc 和 App 实例保留。
- 本地截图保留在被忽略的 `output/ink-splash-lab/integration-preview/`，不将单次模拟器结果称为真机帧率验证。

新增字体的 OFL 沿用已发布的 `public/fonts/noto-serif-sc-LICENSE.txt`；开屏题字的 Ma Shan Zheng 原作者与完整 OFL 已嵌入 `stage.html` 的 SVG metadata，流体 MIT 头保留。`verify-paper-interactions.mjs` 输出的 `paper-header-*`、`paper-bestiary-*`、`paper-disclosure-*` 是本批新交互截图。

导航字库目前裁入“山海寻踪地图异兽谱读图与依据搜索中文”；已验证所需字形均存在。以后新增导航中文时从表中母字库重新裁出子集，并更新素材清单的字节数和摘要；英文沿用现有 Lora/Source Sans 字库。

上传准备另将 7,512 字节导航字体的 SHA-256、母字库来源与许可边界补入 `docs/assets-inventory.tsv`，同步更新 ASSETS 的当前字体数与文件数；不要用历史审计批次的 2032 条覆盖新增登记。补登记后的 2033 条素材审计已通过。

## 上传前接续顺序

1. 先看 `git status --short`、本文件和 CHANGELOG，核对本轮新增文件都被纳入候选范围，尤其 `app-entry.jsx`、`splash/`、字体、`PaperTabs.jsx` 和样式。
2. 用户已授权将本批代码及文档提交并推送当前开发分支；后续先核对远端提交结果。保留既有文档与 SVG 修改，不重置工作树，不自动切到 main，不把构建产物和截图提交。
3. 运行最终构建、相关浏览器回归、数据和发布资源检查；如素材审计发现品牌 SVG 摘要变化，核对来源与改动后登记，不跳过断言或把待核写成通过。`verify:paper` 是新增本地回归入口，当前工作流尚未加入该脚本，不将“本地通过”写成“CI 已覆盖”。
4. 上传前重新读取最近运行与 Jobs API，并检查必需状态设置；既有失败 Jobs 的 URL 及失败步骤见上文。此次没有修改工作流，没有触发远端重跑。
5. 本次推送目标已明确为当前开发分支。后续合并或发布前仍需核对 CI、必需状态和未完成的验收；本地预览通过不等于 CI/线上验收通过。

尚未处理：约 8.94MB raw 的 App 主包及静态数据拆分、Safari/iOS 和低端 Android 真机性能、同页 GPU/滤镜开销的系统采样；首访约十多秒的动画等待仍需用户体验判断。不要恢复已暂停的译注工作，也不要将旧 CI 失败宣称为本轮已修复。

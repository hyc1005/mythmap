# 山海寻踪 MythMap

以木刻地图、故事动画、插画和双语阅读呈现《山海经》及其他古籍中的中国神话；七个故事章节与真实地理资料分别组织，并保留出处关联。

**[打开在线地图](https://hyc1005.github.io/mythmap/)** · [English](README.md) | **中文版**

## 当前内容

- 五山经阅读已接入：南山43段、西山82段、北山92段、东山51段、中山212段，共 **480段**。其余海经十三篇不在本轮已完成范围内，完整范围及待核状态见自动生成的[内容盘点](docs/content-coverage.md)。
- 异兽谱索引 **312条异兽、72条神灵**：短名显示、同名独立记载、六类形貌，以及篇目／特征／已读收藏组合筛选；每批显示24组名称，47条保留形貌待核标记。
- 中英文故事播放、连续游历、全站搜索、已读收藏和续读恢复；真实地理资料单列传承关联、考证候选与核验状态。

保留原名、经文、稳定ID和出处链接。英文说明与译文为项目整理，插画为艺术解释；叙事图坐标和现代地点关联均不证明古代事件发生位置。

## 仓库导航

| 路径 | 职责 |
| --- | --- |
| [frontend/](frontend/) | React/Vite网站，Pages只部署其构建产物 |
| [frontend/src/](frontend/src/) | 界面、共享状态、双语与异兽展示元数据 |
| [frontend/public/data/](frontend/public/data/) | 已审网站数据、影印页和发布插画版本 |
| [frontend/artwork-source/](frontend/artwork-source/) | 原图、提示词及复现记录 |
| [frontend/scripts/](frontend/scripts/README.md) | 浏览器验收和预览；`assets/`存素材工具，`fonts/`存字体工具 |
| [data/](data/README.md) | 各篇构建器、核查记录、原文清单 |
| [docs/](docs/README.md) | 文档索引、API约定、内容盘点与历史课程材料 |
| [backend-java/](backend-java/run.ps1) | 开发代理使用的可选本地`/api/world`服务 |
| [backend/](backend/README.md)、[database/](database/README.md) | 独立FastAPI/PostGIS原型、测试与导入工具 |
| `.github/workflows/` | 自动验收和Pages部署 |
| `output/` | Git忽略的本地QA、诊断与过程文件 |

在线静态页面无需后端或数据库；两个可选服务与网页发布分开维护。

## 本地开发

需要Node.js 22或更新的兼容版本。

```bash
cd frontend
npm ci
npm run dev -- --host 127.0.0.1
```

打开[127.0.0.1:5173](http://127.0.0.1:5173/)。开发模式尝试8081端口的Java API，未启动时使用内置数据。可选API需JDK 17以上，运行`backend-java/run.ps1`；生产默认使用内置数据，只有显式配置`VITE_API_BASE_URL`才请求外部API，该配置会公开在构建产物中。

真实地理底图使用天地图**浏览器端应用**Key，在被忽略的`frontend/.env.local`配置`VITE_TIANDITU_KEY`。服务商域名白名单填写`hyc1005.github.io,127.0.0.1`。底图不可用时仍可阅读和查询本地资料。

## 构建与验证

在`frontend/`目录执行：

```bash
npx playwright install chromium webkit
npm run build -- --base /mythmap/
npm run verify:data
npm run verify:cache
npm run verify:publish
node scripts/with-preview.mjs --base /mythmap/ -- node scripts/verify-bestiary.mjs
node scripts/with-preview.mjs --base /mythmap/ -- node scripts/verify-design.mjs
```

阅读、搜索、叙事和各山经的验收入口见[脚本索引](frontend/scripts/README.md)。统一预览工具使用空闲端口，完成或失败后关闭自己创建的进程；人工预览运行`npm run preview:managed -- --base /mythmap/`，结束按Ctrl+C。验证期间不要重新构建同一份`dist/`。截图保存在`output/qa/`；日常验证使用Chromium、WebKit，Firefox不在已支持验收范围内。

## 自动部署

仓库Settings → Pages选择**GitHub Actions**，并配置Actions secret **TIANDITU_BROWSER_KEY**。推送到`main`的前端、数据、后端／数据库或工作流修改会运行[deploy-pages.yml](.github/workflows/deploy-pages.yml)；纯文档修改不触发发布，也可手动运行。

所有必要检查通过后，部署同一份已验收产物。不要提交`dist/`、依赖、本地环境配置或QA输出；回退使用`git revert`后推送。

## 数据与素材维护

各篇构建器与核查依据见[data/README.md](data/README.md)，插画和字体工具见[脚本索引](frontend/scripts/README.md)，数据边界见[API约定](docs/API_CONTRACT.md)。短名与分类集中在`frontend/src/bestiary-metadata.json`，独立于生成的经文数据。

历史课程材料保存在[docs/coursework/](docs/coursework/)。原图和影印页继续版本管理，用于出处核验和复现；发布清单已排除重复原图。本地交接文档与过程文件由Git忽略。

清理原则：仅删除确认不再被运行代码、构建、测试或资料复现调用的文件。已移除旧中山初始化与Natural Earth底图生成链；当前构建器、完整验收、来源快照和原图保留。历史课程材料供查阅，不作为运行入口。

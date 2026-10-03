# 山海寻踪：中国古代神话传说地图

React + Vite + OpenLayers 的纸本版画神话图谱，包含盘古序章与七章叙事、七段启用动画、异兽谱、神域和原文详情。图面表达篇目方位与叙事关系，不表示真实距离或神话事件的精确年代。

## 当前工程结构

```text
webgisfinal/
├─ frontend/
│  ├─ src/                  当前页面、地图、动画组件及唯一主样式
│  ├─ public/data/          网站实际使用的图谱数据与素材
│  ├─ artwork-source/       插画原图、修复前备份及静态导出输入
│  ├─ scripts/              叙事与全屏布局验证
│  ├─ package.json
│  ├─ package-lock.json
│  └─ vite.config.js
├─ backend-java/            可选的 /api/world 服务
├─ backend/                 旧版 FastAPI / PostGIS 接口及其测试
├─ database/                旧版数据库模型与导入工具
├─ data/                    来源快照、数据构建与静态地图导出工具
├─ docs/                    API、课程报告与当前演示流程
├─ README.md                启动、GitHub 上传与 Demo 部署步骤
└─ 山海寻踪_WebGIS_交接文档.md  当前状态、已知问题与后续建议
```

`node_modules/`、`frontend/dist/`、`output/`、环境配置和缓存由 Git 忽略。运行验证时生成的截图位于 `output/qa/`；可选静态地图导出写入 `output/atlas/`，不再放进网站发布目录。

旧版 API、数据库和数据维护工具有独立用途，保留在工程中。**当前网页 Demo 只部署 frontend，不需要这些服务。**

## 本地启动和复查

使用 Node.js 22.x 或更新的兼容版本。首次运行，在 `frontend/` 目录执行：

```powershell
rtk npm ci
rtk npm run dev -- --host 127.0.0.1
```

打开 http://127.0.0.1:5173/#world 。本地开发会尝试可选 Java API；不可用时使用已内置的同版本数据。

需要 Java API 时，在 `backend-java/` 执行 `run.ps1`，要求 JDK 17 或以上。它默认监听 127.0.0.1:8081，Vite 开发服务器将 /api 转发至该端口。旧 FastAPI 的启动方法见 `backend/README.md`。

在 `frontend/` 执行：

```powershell
rtk npm run build
rtk npm run preview -- --host 127.0.0.1 --port 4173
```

打开 http://127.0.0.1:4173/#world 检查生产版。静态生产版默认不请求 API。可选的 `VITE_API_BASE_URL` 配置见 `frontend/.env.example`；它是构建时公开的 API 地址，不能放密码或密钥。演示部署留空即可。

另开终端，在 `frontend/` 运行：

```powershell
rtk npm run verify:layout
rtk npm run verify:narrative
```

`verify:layout` 检查五种视口、七段动画、原生/模拟全屏、图层/工具/预览/详情、不重叠以及动画与反复悬浮时地图尺寸稳定。`verify:narrative` 还包含旧有叙事、素材加载与时间轴回归；运行时间较长，其最新通过范围与未完成项必须以交接文档为准。

检查生产预览时，在项目根目录的新 PowerShell 终端设置目标地址，然后运行验证：

```powershell
$env:ATLAS_URL = 'http://127.0.0.1:4173'
rtk npm --prefix frontend run verify:layout
```

`vite preview` 用于本地复查生产产物；正式 Demo 由静态托管平台提供服务。[Vite 部署文档](https://vite.dev/guide/static-deploy.html)

## GitHub 仓库与 Demo 部署

公开仓库：[hyc1005/mythmap](https://github.com/hyc1005/mythmap)。
Demo 地址：[山海寻踪](https://hyc1005.github.io/mythmap/)（已发布）。

使用 **GitHub Actions 构建、GitHub Pages 托管**。不需要 Vercel、Java API、数据库或额外服务器。工作流位于 `.github/workflows/deploy-pages.yml`，平台使用普通 npm，无需安装 RTK。

### 首次发布配置

1. 仓库 Settings → Pages → Build and deployment → Source 选择 **GitHub Actions**，本仓库已设置。
2. main 分支上传前端和 workflow 后，Actions 自动执行 Node.js 22、npm ci、Vite build、上传 frontend/dist、发布 Pages。
3. workflow 根据 Pages 的 base_path 构建；asset-url.js 同步处理运行时 /data 素材地址，支持 /mythmap/ 项目子路径。
4. Actions → Build and deploy GitHub Pages 查看运行结果，成功后打开上方 Demo。失败时检查具体步骤日志；不手动修改 dist。
5. 当前静态 Demo 无需设置 Secrets 或 API 环境变量；部署使用 GitHub 提供的短期 GITHUB_TOKEN 与 OIDC 权限。

流程依据 [Vite 的 Pages 指南](https://vite.dev/guide/static-deploy.html#github-pages) 和 [GitHub 自定义 Pages 工作流](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)。

### 后续修改与发布

在项目根目录运行：

```powershell
rtk git status
rtk git diff
rtk git add frontend .github README.md 山海寻踪_WebGIS_交接文档.md
rtk git commit -m "Describe the change"
rtk git push origin main
```

origin 已指向 https://github.com/hyc1005/mythmap.git，提交者已设为 hyc1005。不要重复添加 origin。只有 frontend 或部署 workflow 的变更自动触发发布；文档修改不触发重复构建。也可在 Actions 页面用 Run workflow 手动发布 main。

需要回退网页时，对出问题的提交执行 git revert 并推送 main，Actions 会重新发布；不要强制推送重写已上传历史。

### 发布前本地检查与上线验收

在 frontend 目录执行 `rtk npm run build -- --base /mythmap/` 和 `rtk npm run preview -- --host 127.0.0.1 --port 4173 --base /mythmap/`，检查 http://127.0.0.1:4173/mythmap/ 。将 ATLAS_URL 设为该地址再运行 verify:layout，避免用根路径预览模拟子路径部署。

- 用未登录浏览器确认 Demo 可访问、刷新成功，图片没有 404。
- 依次打开七段动画，检查播放、暂停、重播与 1×/2×。
- 全屏中连续悬浮地点，检查地图和底栏稳定；打开详情、用 Tab/Shift+Tab、关闭，再切章和退出全屏。
- 开启异兽与神域、展开地图工具，检查桌面、手机竖屏和窄横屏。
- 检查异兽谱搜索、导航锚点、底部说明和原文链接。
- 当前生产版直接使用内置数据。配置外部 API 时额外检查 HTTPS、CORS 和完整数据结构。

最新验收范围与待改进项见交接文档；完整叙事长测试尚不能登记为全部通过。

## 数据与美术维护

- 当前运行时数据：`frontend/public/data/myth-world.json`、`atlas/catalog.json`、`atlas/story-animations.json`、`atlas/kuafu-journey.json`。
- 出处与复核：`atlas/review.json` 和 `atlas/artwork-manifest.json`。
- 图像原图与备用版本位于 `frontend/artwork-source/`；这些文件有复现或恢复用途，不放入 public。
- 旧静态地图可从项目根目录运行 `rtk proxy python data/render_myth_atlas.py` 生成。需要 Pillow、pyproj 和脚本指定的 Windows 字体；结果进入 output/atlas。这类地理参考汇总图不替代实时示意地图。
- `data/build_myth_atlas.py` 是早期数据构建工具，运行可能覆盖当前人工审核快照。修改数据前核对交接文档、来源和 Git 差异，避免把已停用叙事重新带回页面。
- 旧 PostGIS 功能及导入步骤保留在 `backend/`、`database/`、`data/README.md`；当前 Demo 不依赖它们。

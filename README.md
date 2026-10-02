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

## 上传 GitHub 的详细步骤

本地仓库已初始化为 `main`，提交者已按本次授权设为 hyc1005。当前没有指定远程仓库，因此本地提交与远程上传分开完成。

1. 登录 GitHub，点击 New repository。仓库名可用 `shanhai-map`；公开或私有按自己的发布意愿选择。
2. 创建**空仓库**，不勾选初始化 README、.gitignore 或 License，避免与本地初始提交产生不同历史。
3. 在仓库页面复制 HTTPS 地址。以下地址只是以用户名 hyc1005 和仓库名 shanhai-map 为例；如实际名称不同，替换后执行。
4. 在项目根目录运行：

```powershell
rtk git status
rtk git remote add origin https://github.com/hyc1005/shanhai-map.git
rtk git remote -v
rtk git push -u origin main
```

首次推送通常会启动 Git Credential Manager 的浏览器登录。按浏览器提示登录 GitHub；不要把访问令牌写进远程地址、前端变量或代码。

5. 刷新 GitHub 仓库，确认 src、public、package-lock.json、README 和交接文档已上传，node_modules、dist、output、.env 未上传。
6. 若已有 origin，先核对 `rtk git remote -v`；需要换地址时使用 `rtk git remote set-url origin 实际仓库地址`。不要重复添加同名远程。

这些步骤按 [GitHub 本地代码上传指南](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github) 整理。

## 部署可分享的 Demo：GitHub + Vercel

当前项目图片路径从 /data 开始，适合部署在网站根路径。推荐先将代码上传 GitHub，再用 Vercel 导入仓库；无需为当前 Demo 配置 Java、数据库或服务器。

1. 用 GitHub 账号登录 Vercel，选择 Add New → Project。
2. 导入刚上传的仓库，并只授权目标仓库。
3. 设置以下构建项：

| 设置项 | 值 |
|---|---|
| Production Branch | main |
| Framework Preset | Vite |
| Root Directory | frontend |
| Install Command | npm ci |
| Build Command | npm run build |
| Output Directory | dist |
| Node.js Version | 22.x 或兼容的更新版本 |
| 环境变量 | 当前静态 Demo 不需要 |

平台构建环境使用普通 npm，不需要安装本机的 RTK。上述路径相对于 Root Directory，因此 Output Directory 填 `dist`，不是 `frontend/dist`。

4. 点击 Deploy，确认安装与构建成功。失败时先检查 Root Directory 和 lockfile；不要把开发服务器当作部署入口。
5. 打开生成的 HTTPS 域名及 /#world，进行下面的上线验收。
6. 验收后，将 Demo 地址填入 GitHub 仓库 About → Website；在 README 首段补上实际地址。
7. 后续推送 main 会触发生产部署；其他分支可用于预览。需要回退时在 Vercel 选先前通过验收的部署恢复生产版本，再修正代码。

构建与自动部署规则见 [Vite 的 Vercel 指南](https://vite.dev/guide/static-deploy.html#vercel)；子目录设置见 [Vercel 项目配置](https://vercel.com/docs/project-configuration)。

### 上线验收

- 用未登录的浏览器窗口确认 Demo 可访问、刷新成功，图像没有 404。
- 依次打开盘古、女娲、燧人、夸父、精卫、大羿和大禹，确认播放、暂停、重播与 1×/2×。
- 全屏中连续悬浮地图地点，确认地图和底栏不跳动；打开/关闭详情，再切章和退出全屏。
- 开启异兽与神域，展开地图工具，检查横屏、手机竖屏及窄横屏的按钮与人物。
- 检查异兽谱搜索、导航锚点、底部读图说明和原文链接。
- 当前无需 /api 服务；生产构建默认直接使用内置数据。若配置外部 API，额外检查 HTTPS 和 CORS。

### 若改用 GitHub Pages

用户站点 `https://用户名.github.io/` 或自定义域名可使用根路径部署。项目站点 `https://用户名.github.io/仓库名/` 还需要统一处理 Vite base 和代码/JSON 中从 /data 开始的素材路径；**仅设置 base 不足以修复当前这些运行时 URL**。当前代码尚未做子路径适配。选择项目 Pages 时先完成该改动，再按 [Vite 的 GitHub Pages 指南](https://vite.dev/guide/static-deploy.html#github-pages) 建立构建部署 workflow。

## 数据与美术维护

- 当前运行时数据：`frontend/public/data/myth-world.json`、`atlas/catalog.json`、`atlas/story-animations.json`、`atlas/kuafu-journey.json`。
- 出处与复核：`atlas/review.json` 和 `atlas/artwork-manifest.json`。
- 图像原图与备用版本位于 `frontend/artwork-source/`；这些文件有复现或恢复用途，不放入 public。
- 旧静态地图可从项目根目录运行 `rtk proxy python data/render_myth_atlas.py` 生成。需要 Pillow、pyproj 和脚本指定的 Windows 字体；结果进入 output/atlas。这类地理参考汇总图不替代实时示意地图。
- `data/build_myth_atlas.py` 是早期数据构建工具，运行可能覆盖当前人工审核快照。修改数据前核对交接文档、来源和 Git 差异，避免把已停用叙事重新带回页面。
- 旧 PostGIS 功能及导入步骤保留在 `backend/`、`database/`、`data/README.md`；当前 Demo 不依赖它们。

# 山海寻踪 · 静态部署包

这个包只包含**已验证的静态站点**，不需要 Node、数据库、API 或后端服务。

## 目录

```text
site/                 # 构建产物（index.html、assets/、data/、字体、宣传片）
一键部署.cmd          # Windows 双击入口
一键部署.command      # macOS 双击入口
一键部署.sh           # Linux 双击入口
Deploy.ps1            # Windows 检查与启动脚本
deploy.sh             # Linux / macOS 检查与启动脚本
SHA256SUMS            # site/ 全文件摘要
README.md             # 本说明
```

## 一键部署

### Windows：双击

双击 **`一键部署.cmd`**。默认在 `http://127.0.0.1:8080/` 启动并打开浏览器；端口可选：

```text
一键部署.cmd 8090
```

首次运行会检查 PowerShell、Python 3、必需文件、SHA256SUMS、端口，然后要求确认。关闭窗口或按 `Ctrl+C` 停止。

### macOS / Linux：双击或终端

- macOS：双击 **`一键部署.command`**。
- Linux：双击 **`一键部署.sh`**（文件管理器需允许运行），或：

```bash
chmod +x deploy.sh
./deploy.sh serve          # 默认 8080
./deploy.sh serve 8090     # 可选端口
```

### 复制到静态站点目录

```powershell
powershell -ExecutionPolicy Bypass -File .\Deploy.ps1 -Mode copy -Target D:\www\mythmap
```

```bash
./deploy.sh copy /var/www/mythmap
```

首次运行会检查 Python 3、必需文件、SHA256SUMS、端口/目标目录，然后要求确认。`FORCE=1` / `-Force` 可跳过确认。

## 检查了什么

- 环境：PowerShell 5.1+ 或 bash + Python 3。
- 完整性：`site/index.html`、`site/opening-film.html`、`site/data/myth-world.json`、`site/assets` 存在；`SHA256SUMS` 全量匹配。
- 目标：端口未被占用；复制目标可写且为空（否则需 `-Force`/`FORCE=1`）。
- 确认：显示站点大小和校验文件数，人工确认后才启动/复制。

没有自动安装依赖、没有联网上传、没有修改系统配置。

## 托管说明

这是 `base=/` 的静态构建，适合放在域名根目录或子目录的根路径。若放在 `https://example.com/mythmap/` 这类子路径，需要重新用 `--base /mythmap/` 构建；当前正式站由 GitHub Actions 从源码构建并部署，不走这个包。

若托管在 Nginx，最小配置：

```nginx
location / {
  root /var/www/mythmap;
  try_files $uri $uri/ /index.html;
}
```

`site/` 内是构建产物；不要把它提交回源码仓库。

在仓库根目录运行 `powershell -ExecutionPolicy Bypass -File deploy/make-package.ps1` 可用 Python 3 创建部署 ZIP。默认输出到 `output/deploy/static-日期-提交号/`。再次打包时可用 `-OutputDirectory` 指定新目录。

## 回滚

保留上一版 `site/` 目录或压缩包，替换后重启静态服务即可。这是纯静态包，没有数据库迁移。

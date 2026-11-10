# 山海寻踪 · 静态部署包

这个包只包含**已验证的静态站点**，不需要 Node、数据库、API 或后端服务。

## 目录

```text
site/                 # 构建产物（index.html、assets/、data/、字体、宣传片）
Deploy.ps1            # Windows 一键部署
deploy.sh             # Linux / macOS 一键部署
SHA256SUMS            # site/ 全文件摘要
README.md             # 本说明
```

## 一键部署

### Windows

```powershell
# 本地启动，浏览器打开 http://127.0.0.1:8080/
powershell -ExecutionPolicy Bypass -File .\Deploy.ps1

# 复制到静态站点目录（Nginx/IIS/任意静态托管）
powershell -ExecutionPolicy Bypass -File .\Deploy.ps1 -Mode copy -Target D:\www\mythmap
```

首次运行会检查 PowerShell、Python 3、必需文件、SHA256SUMS、端口/目标目录，然后要求确认。加 `-Force` 可跳过确认（自动化用）。

### Linux / macOS

```bash
chmod +x deploy.sh
./deploy.sh serve 8080
./deploy.sh copy 8080 /var/www/mythmap
```

首次运行会检查 Python 3、必需文件、SHA256SUMS、端口/目标目录，然后要求确认。`FORCE=1` 可跳过确认。

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

## 回滚

保留上一版 `site/` 目录或压缩包，替换后重启静态服务即可。这是纯静态包，没有数据库迁移。

# 数据维护入口

当前网页数据位于`frontend/public/data/`，此目录保存构建器、影印依据与审核清单，不是网页发布目录。原始经文、稳定ID、来源关联和图片审核记录需要一并保留。

## 当前山经构建器

所有命令从仓库根目录运行；只在需要更新相应内容时运行构建器。

| 篇目 | 主入口 | 核查记录 |
| --- | --- | --- |
| 南山经43段 | `build_nanshan.py`、`build_nanshan_reader.py`、`build_nanshan_entities.py` | `nanshan-edition-review.json`、`nanshan-entity-coverage.json` |
| 西山经82段 | `build_xishan.py` | `xishan-edition-review.json` |
| 北山经92段 | `build_beishan.py` | `beishan-edition-review.json` |
| 东山经51段 | `build_dongshan.py` | `dongshan-edition-review.json` |
| 中山经212段 | `build_zhongshan.py` | `zhongshan-edition-review.json` |

南山reader或首批构建器运行后，需要用`build_nanshan_entities.py`恢复最终实体与关系。其他篇的`*_completion.py`、`*_range*.py`、`*_batch.py`、`zhongshan_stages*.py`及`zhongshan_next30.py`仍被主构建器导入，是内容模块，不是可以删除的旧脚本。

## 来源与生成清单

- `shanhaijing-reference.json`：保留的十八篇录文快照。
- `reference-scans/`：影印页、页码和来源哈希。
- `build_source_inventory.py`：构建`shanhaijing-inventory.json`，保留未接入和待核状态。
- `audit_shanhaijing.py`：生成[内容盘点](../docs/content-coverage.md)及前端来源分类。内容盘点是生成文件，不手工编辑。
- 短名、同名组和形貌位于`frontend/src/bestiary-metadata.json`；生成经文不会覆盖它们。

仅检查、不重建：

```bash
python data/build_source_inventory.py --check
python data/audit_shanhaijing.py --check
```

素材和字体生成已分到[frontend/scripts/assets/与fonts/](../frontend/scripts/README.md)。

## 历史图谱复现

- `build_myth_atlas.py`只输出`output/legacy-atlas/`，拒绝覆盖已审网页数据；`render_myth_atlas.py`用于复现旧版静态图。

五山经共480段阅读已接入；海经十三篇仍有缺口，当前实现不等于十八篇逐字校勘完成。每次内容更新后运行上述清单检查和对应浏览器验收。

已停用的中山初始计划工具和Natural Earth底图生成链已移除；当前中山维护入口是`build_zhongshan.py`，底图配置是`frontend/src/geography-map-config.js`。旧版本可从Git历史恢复。

古籍英文引文的后续修订集中于`english_review.py`，绑定原文并由上述主构建器及南山阅读/实体补全构建器应用。运行`python data/english_review.py`核对现行66条译文和中文依据；更新原文时须同步复核译文。


## 轻量检出与原图分发

普通界面开发可跳过大部分原图和影印二进制；元数据、来源记录和网页资源全部保留。需要 Python 3.10+、Git 和 Node.js 22。

```bash
git clone --filter=blob:none --no-checkout https://github.com/hyc1005/mythmap.git mythmap-lite
cd mythmap-lite
git sparse-checkout set --no-cone '/*' '!/frontend/artwork-source/**/*.png' '!/frontend/artwork-source/**/*.webp' '!/data/reference-scans/**/*.jpg'
git checkout main
python data/light_checkout.py --profile core
npm --prefix frontend ci
npm --prefix frontend run verify:data
npm --prefix frontend run build -- --base /mythmap/
npm --prefix frontend run verify:publish
```

`core`保留默认数据校验依赖的五张母图。按测试选择`central-current`（中山）、`northern`（北山）或`narrative`（叙事）会补齐相应原图和影印；其余 CI 套件可使用同名 profile。`--dry-run`只显示选择。不在已有修改的素材工作区切换 profile。完整来源审计、重新生成插画或影印校对前，运行`git sparse-checkout disable`恢复完整检出；`verify:assets`仍须完整素材与完整 Git 历史。

原图及影印的可选分发包索引为`data/asset-bundles.json`。ZIP按原目录分组，每组可独立下载；文件级与包级 SHA-256、来源提交和 Release 地址均在索引中。分发不改变[素材许可边界](../ASSETS.md)。

```bash
# 示例：仅恢复北山原画；去掉 --group 则处理全部分组
python data/asset_packages.py download --catalog data/asset-bundles.json --archives output/asset-packages --group art-beishan
python data/asset_packages.py restore --catalog data/asset-bundles.json --archives output/asset-packages --group art-beishan
python data/asset_packages.py check --catalog data/asset-bundles.json --group art-beishan
```

`download`拒绝覆盖不同的既有下载，校验失败时保留`.download`供检查；`restore`先验证全部所选包与现有文件，再只补缺失文件，拒绝覆盖本地差异。恢复不改变 sparse 规则；后续切换 profile 可能再次移除被排除的已跟踪文件。长期编辑原图宜使用完整检出。`check`核对已恢复的原路径文件，JSON采用LF摘要。

维护新版本时先完整审计，再用`pack --output <新目录> --tag <新版本> --source-commit <已核验提交>`生成包、`verify`检查包，并在独立轻量检出中恢复后执行完整素材审计。核对上传摘要后才能发布；固定版本包不能覆盖。原图仍保留在主仓库，不重写 Git 历史。

# 图谱维护数据与工具

网站直接使用 `frontend/public/data/myth-world.json` 和 `atlas/` 下的审核数据；运行网站不需要 Python 或数据库。

- `myth-atlas-inputs/`：保留的图谱记录与现代地理参考，供维护和考据使用。
- `build_myth_atlas.py`：生成目录、图层及审核记录。可能覆盖人工修订，运行前核对来源和 Git 差异；不会自动重建当前网页的 `myth-world.json`。
- `render_myth_atlas.py`：可选静态地图输出，需要 Pillow、pyproj 和脚本指定的 Windows 字体，结果保存在 `output/atlas/`。

序章及七章次序是叙事编排，不表示精确年代。现代地理参考不代表上古复原；原文、现代解释与插画说明需分别保留。

旧 FastAPI/PostGIS 种子数据及工具已从精简分支移除，可从仓库原版历史查阅。当前数据格式及网页运行方式以根目录 README 为准。

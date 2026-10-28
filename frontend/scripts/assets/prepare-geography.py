import hashlib
import io
import json
import urllib.request
import zipfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageChops

root = Path(__file__).resolve().parents[3]
archive = root / 'output/geography-source/SR_50M.zip'
url = 'https://naturalearth.s3.amazonaws.com/50m_raster/SR_50M.zip'
archive.parent.mkdir(parents=True, exist_ok=True)
if not archive.exists():
    with urllib.request.urlopen(url, timeout=60) as response:
        archive.write_bytes(response.read())
with zipfile.ZipFile(archive) as files:
    raster = Image.open(io.BytesIO(files.read('SR_50M.tif')))
    affine = [float(value) for value in files.read('SR_50M.tfw').decode().split()]
    assert raster.mode == 'L' and affine[1:3] == [0, 0]
    dx, _, _, dy, cx, cy = affine
    west, north = cx - dx / 2, cy - dy / 2
    extent = [65, 15, 140, 55]
    box = tuple(round(value) for value in ((extent[0] - west) / dx, (extent[3] - north) / dy,
                                          (extent[2] - west) / dx, (extent[1] - north) / dy))
    shade = raster.crop(box)
mask = Image.new('L', shade.size)
draw = ImageDraw.Draw(mask)
land = json.loads((root / 'frontend/public/data/atlas/land.geojson').read_text(encoding='utf-8'))
def pixel(point):
    return ((point[0] - extent[0]) / (extent[2] - extent[0]) * shade.width,
            (extent[3] - point[1]) / (extent[3] - extent[1]) * shade.height)
for feature in land['features']:
    geometry = feature['geometry']
    polygons = [geometry['coordinates']] if geometry['type'] == 'Polygon' else geometry['coordinates']
    for rings in polygons:
        for index, ring in enumerate(rings):
            draw.polygon([pixel(point) for point in ring], fill=255 if index == 0 else 0)
alpha = shade.point(lambda value: round((255 - value) * .32))
alpha = ImageChops.multiply(alpha, mask)
image = Image.new('RGBA', shade.size, (77, 60, 40))
image.putalpha(alpha)
target = root / 'frontend/public/data/geography/relief.webp'
target.parent.mkdir(parents=True, exist_ok=True)
image.save(target, 'WEBP', quality=86, method=6)
manifest = {
    'path': '/data/geography/relief.webp', 'projection': 'EPSG:4326', 'extent': extent,
    'dimensions': list(image.size), 'bytes': target.stat().st_size,
    'source': 'Natural Earth SR_50M 3.2.0; regional crop masked by Natural Earth 1:110m land',
    'source_url': url, 'source_sha256': hashlib.sha256(archive.read_bytes()).hexdigest(),
    'license_url': 'https://www.naturalearthdata.com/about/terms-of-use/',
    'note': 'Modern regional relief reference; not ancient terrain reconstruction or a measurable elevation model.',
}
(root / 'data/archive/geography-basemap.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
print('Prepared georeferenced relief:', image.size, target.stat().st_size, 'bytes')

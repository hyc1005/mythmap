"""Render deterministic geography and Chinese labels around reviewed ImageGen artwork."""
from __future__ import annotations

import json
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from pyproj import Transformer

ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / 'frontend/public/data/atlas'
ARTWORK = ROOT / 'frontend/artwork-source/atlas-illustrations'
EXPORT = ROOT / 'output/atlas'
SIZE = (2560, 1800)
MAP = (70, 210, 1790, 1220)
PAPER = '#f6efde'
INK = '#314a43'
GOLD = '#97773f'
RED = '#a75138'
FONT = 'C:/Windows/Fonts/msyh.ttc'
SERIF = 'C:/Windows/Fonts/simsun.ttc'
projection = Transformer.from_crs(4326, 3857, always_xy=True)
west, south = projection.transform(72, 17)
east, north = projection.transform(137, 55)
scale = min((MAP[2]-MAP[0])/(east-west), (MAP[3]-MAP[1])/(north-south))
x0 = MAP[0] + ((MAP[2]-MAP[0]) - (east-west)*scale)/2
y0 = MAP[1] + ((MAP[3]-MAP[1]) - (north-south)*scale)/2


def font(size, serif=False):
    return ImageFont.truetype(SERIF if serif else FONT, size)


def xy(lon, lat):
    x, y = projection.transform(lon, lat)
    return (x0+(x-west)*scale, y0+(north-y)*scale)


def geo(draw, geometry, fill=None, stroke=None, width=2):
    kind, coords = geometry['type'], geometry.get('coordinates', [])
    if kind == 'GeometryCollection':
        for item in geometry['geometries']:
            geo(draw, item, fill, stroke, width)
    elif kind == 'Polygon':
        for i, ring in enumerate(coords):
            draw.polygon([xy(*p[:2]) for p in ring], fill=fill if i == 0 else '#e8efdf', outline=stroke, width=width)
    elif kind in ('MultiPolygon', 'MultiLineString'):
        for part in coords:
            geo(draw, {'type': 'Polygon' if kind == 'MultiPolygon' else 'LineString', 'coordinates': part}, fill, stroke, width)
    elif kind == 'LineString':
        if len(coords) > 1:
            draw.line([xy(*p[:2]) for p in coords], fill=stroke, width=width, joint='curve')


def text(draw, pos, value, size=24, color=INK, serif=False):
    draw.text(pos, value, fill=color, font=font(size, serif))


def wrapped(draw, pos, value, size=22, width=550, color=INK, max_lines=4):
    ft = font(size)
    lines, current = [], ''
    for ch in value:
        if ch == '\n' or draw.textlength(current + ch, font=ft) > width:
            lines.append(current)
            current = '' if ch == '\n' else ch
        else:
            current += ch
    if current:
        lines.append(current)
    for i, line in enumerate(lines[:max_lines]):
        if i == max_lines-1 and len(lines) > max_lines:
            line = line[:-1] + '…'
        text(draw, (pos[0], pos[1]+i*(size+12)), line, size, color)
    return min(len(lines), max_lines)*(size+12)


def fit_image(path, rect):
    im = Image.open(path).convert('RGBA')
    ratio = min((rect[2]-rect[0])/im.width, (rect[3]-rect[1])/im.height)
    im = im.resize((round(im.width*ratio), round(im.height*ratio)), Image.Resampling.LANCZOS)
    return im, (round(rect[0]+((rect[2]-rect[0])-im.width)/2), round(rect[1]+((rect[3]-rect[1])-im.height)/2))


def add_image(layer, path, rect):
    image, point = fit_image(path, rect)
    layer.alpha_composite(image, point)


def dashed(draw, a, b, fill=GOLD, width=3):
    length = math.dist(a, b)
    for start in range(0, int(length), 20):
        end = min(length, start+11)
        draw.line([(a[0]+(b[0]-a[0])*start/length, a[1]+(b[1]-a[1])*start/length),
                   (a[0]+(b[0]-a[0])*end/length, a[1]+(b[1]-a[1])*end/length)], fill=fill, width=width)


def render():
    catalog = json.loads((ATLAS/'catalog.json').read_text(encoding='utf-8'))
    output, layers = EXPORT/'maps', EXPORT/'layers'
    output.mkdir(parents=True, exist_ok=True)
    layers.mkdir(parents=True, exist_ok=True)
    base = Image.new('RGBA', SIZE, PAPER)
    d = ImageDraw.Draw(base)
    d.rectangle((26, 26, 2534, 1774), outline='#b39a66', width=3)
    d.rectangle((40, 40, 2520, 1760), outline='#ddcda6', width=1)
    d.rectangle(MAP, fill='#e8efdf', outline='#baa77c', width=2)
    for f in json.loads((ATLAS/'land.geojson').read_text(encoding='utf-8'))['features']:
        geo(d, f['geometry'], '#d8dfc7', '#849886', 2)
    for lon in range(80, 137, 10):
        a,b = xy(lon,17),xy(lon,55)
        d.line((a,b), fill='#bbc9b388',width=1)
        text(d,(a[0]-20,MAP[3]-26),str(lon)+'°E',15,'#899679')
    for lat in range(20, 55, 10):
        a,b = xy(72,lat),xy(137,lat)
        d.line((a,b),fill='#bbc9b388',width=1)
        text(d,(MAP[0]+8,a[1]-20),str(lat)+'°N',15,'#899679')
    for f in json.loads((ATLAS/'rivers.geojson').read_text(encoding='utf-8'))['features']:
        geo(d,f['geometry'],stroke='#7a9eae',width=4)
    for name, point in [('黄河（现代）',(108,38)),('长江（现代）',(112,29)),('海域',(129,30))]:
        text(d,xy(*point),name,24,'#6c9297',True)
    text(d,(MAP[2]-85,MAP[1]+28),'北',28,GOLD,True)
    text(d,(MAP[2]-73,MAP[1]+70),'↑',36,GOLD)
    text(d,(75,1690),'底图 Natural Earth 1:110m · 现代海岸与河流仅作参照；不表示上古地貌或历史疆域。',20,'#8a7e63')
    text(d,(75,1725),'现代候选参考位置 © OpenStreetMap contributors · ODbL；所有古代对应解释保留待核验状态。',18,'#988970')
    text(d,(1860,1725),'神话叙事图集 · 2026.09',20,GOLD,True)
    base.save(layers/'geographic-base.png')
    manifests = []
    for stage in catalog['stages']:
        sid = stage['id']
        art = Image.new('RGBA',SIZE)
        labels = Image.new('RGBA',SIZE)
        ld = ImageDraw.Draw(labels)
        chapter = [e for e in catalog['events'] if e['properties']['stage_id']==sid]
        cp = [c for c in catalog['candidates'] if c['properties']['stage_id']==sid and c['geometry']]
        text(ld,(78,67),'山海寻踪',28,GOLD,True)
        text(ld,(75,109),sid+'  '+stage['title'],58,INK,True)
        text(ld,(730,132),stage['subtitle'],28,GOLD,True)
        text(ld,(1840,91),'七章神话 · 共用地理骨架',26,GOLD,True)
        text(ld,(1840,136),'叙事次序为后人建构，并非古籍编年。',20,'#8d8065')
        illustration = ARTWORK/f'{sid}.png'
        if sid=='01':
            ImageDraw.Draw(art).rectangle(MAP, fill=PAPER, outline='#baa77c', width=2)
            add_image(art,illustration,MAP)
            ld.rounded_rectangle((180,1115,1670,1190),radius=10,fill='#f8f0dedf',outline='#c7ae7d',width=1)
            text(ld,(210,1138),'创世天地示意 · 无经纬度 · 四则神话分别呈现，不合并为因果链',27,'#765c3b',True)
        else:
            add_image(art,ARTWORK/'divine.png',(1840,220,2480,650))
            text(ld,(1840,675),'天外神域 · 固定云层',30,INK,True)
            wrapped(ld,(1840,730),'昆仑、玉山西王母、烛龙、扶桑、归墟与海外。神域布局为象征构图，不对应经纬度和真实距离。',22,610,'#7d735d',4)
            text(ld,(1840,915),'● 现代候选区域参考点',22,GOLD)
            text(ld,(1840,955),'┄ 候选解释连接，非实际道路',22,GOLD)
            wrapped(ld,(1840,1020),'图中点位来自报告所列候选解释的现代地名查询。参考区域中心不等于古代事件发生点。',22,610,'#7d735d',4)
            for route in catalog['routes']:
                if route['properties']['stage_id']==sid:
                    a,b=[xy(*p) for p in route['geometry']['coordinates']]
                    dashed(ld,a,b)
        if sid=='01':
            text(ld,(1840,255),'天地初开',38,INK,True)
            wrapped(ld,(1840,335),'盘古开天文献晚出；女娲造人、女娲补天与共工触山各有不同文本来源。画面按章节构图，保留各自独立叙事。',24,610,'#7d735d',6)
            text(ld,(1840,630),'图像与地理',30,GOLD,True)
            wrapped(ld,(1840,698),'创世章节不设置虚构地理落点。后续六章使用同一现代地理骨架，插图和文字标注独立保存。',24,610,'#7d735d',5)
            text(ld,(1840,925),'七阶段时间演进',28,GOLD,True)
            wrapped(ld,(1840,990),'创世 → 三皇五氏 → 炎黄 → 五帝后期 → 禹夏 → 夏商之际 → 周穆王西巡',23,610,'#7d735d',4)
        occupied=[]
        for c in cp:
            p=c['properties']; x,y=xy(*c['geometry']['coordinates'])
            label=p['entity_id']+' '+p['label']
            tw=int(ld.textlength(label,font=font(20)))+20
            desired=(x+15,y-28)
            found=None
            for offset in [0,35,-35,70,-70,105,-105,140,-140,175,-175]:
                lx=max(MAP[0]+35,min(MAP[2]-tw-15,desired[0])); ly=max(MAP[1]+10,min(MAP[3]-40,desired[1]+offset))
                rect=(lx,ly,lx+tw,ly+32)
                if all(rect[2]<r[0] or rect[0]>r[2] or rect[3]<r[1] or rect[1]>r[3] for r in occupied):
                    found=rect;break
            rect=found or (desired[0],desired[1],desired[0]+tw,desired[1]+32)
            occupied.append(rect)
            ld.line(((x,y),(rect[0],rect[1]+16)),fill='#bca575',width=2)
            ld.ellipse((x-7,y-7,x+7,y+7),fill=RED,outline='#fff5df',width=2)
            ld.rounded_rectangle(rect,radius=5,fill='#fff7e9ed',outline='#bba478',width=1)
            text(ld,(rect[0]+10,rect[1]+3),label,20,'#785334')
        if sid=='02':
            ld.rounded_rectangle((430,590,1370,735),radius=14,fill='#f8f2dfec',outline='#c1b287',width=2)
            text(ld,(485,620),'本章人物无可支持的具体地理落点',32,GOLD,True)
            text(ld,(485,678),'共用底图提供空间参照，故事见下方叙事插画与条目。',21,'#858166')
        ld.line((70,1250,2480,1250),fill='#c6b78f',width=2)
        add_image(art,illustration,(70,1280,690,1690))
        text(ld,(745,1276),'本章叙事与文献索引',28,GOLD,True)
        for n,e in enumerate(chapter):
            x=745+(n%2)*850; y=1330+(n//2)*109
            p=e['properties']
            text(ld,(x,y),e['id']+'  '+p['name'],26,INK,True)
            wrapped(ld,(x,y+42),p['source_text'],18,795,'#8c8068',2)
        text(ld,(1840,1180),f'{len(chapter)} 条叙事 · {len(cp)} 个可展示候选',22,GOLD)
        art.save(layers/f'{sid}-illustrations.png')
        labels.save(layers/f'{sid}-labels.png')
        result=Image.alpha_composite(Image.alpha_composite(base,art),labels).convert('RGB')
        result.save(output/f'{sid}.png',optimize=True)
        result.resize((640,450),Image.Resampling.LANCZOS).save(output/f'{sid}-preview.jpg',quality=86)
        manifests.append({'stage_id':sid,'map':f'maps/{sid}.png','size':list(SIZE),'projection':'EPSG:3857',
                          'extent':[72,17,137,55], 'map_pixel_rect':list(MAP),'layers':['layers/geographic-base.png',f'layers/{sid}-illustrations.png',f'layers/{sid}-labels.png'],
                          'entity_ids':[e['id'] for e in chapter], 'candidate_ids':[c['id'] for c in cp],
                          'illustration_asset':f'frontend/artwork-source/atlas-illustrations/{sid}.png', 'geography_is_modern_reference':True})
        print('Rendered',sid,flush=True)
    (EXPORT/'render-manifest.json').write_text(json.dumps({'revision_id':catalog['revision_id'],'stages':manifests},ensure_ascii=False,indent=2),encoding='utf-8')
    sheet=Image.new('RGB',(1280,1800),PAPER)
    for n,stage in enumerate(catalog['stages']):
        thumb=Image.open(output/f'{stage["id"]}-preview.jpg')
        sheet.paste(thumb,((n%2)*640,(n//2)*450))
    sheet.save(output/'contact-sheet.jpg',quality=90)


if __name__=='__main__':
    render()

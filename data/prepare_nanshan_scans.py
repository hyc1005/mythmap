"""Retain the full volume-one facsimile references; downloads are explicit."""
import hashlib
import json
from pathlib import Path
import requests
from bs4 import BeautifulSoup

root = Path(__file__).resolve().parents[1]
folder = root / 'data/reference-scans/nanshan'
records = json.loads((folder / 'sources.json').read_text(encoding='utf-8'))
session = requests.Session()
session.headers['User-Agent'] = 'ShanhaiAtlasContentAudit/1.0 (local research with attribution)'
for page in range(16, 33):
    if any(row['page'] == page for row in records):
        continue
    url = f'https://zh.wikisource.org/wiki/Page:Sibu_Congkan0465-郭璞-山海經-2-1.djvu/{page}'
    response = session.get(url, timeout=40)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    image_url = 'https:' + next(img['src'] for img in soup.find_all('img') if f'page{page}-1280px' in img.get('src', ''))
    target = folder / f'page-{page}.jpg'
    if not target.exists():
        image = session.get(image_url, timeout=60)
        image.raise_for_status()
        target.write_bytes(image.content)
    records.append({'page': page, 'url': url, 'image_url': image_url, 'local_path': target.relative_to(root).as_posix(), 'sha256': hashlib.sha256(target.read_bytes()).hexdigest()})
    (folder / 'sources.json').write_text(json.dumps(sorted(records, key=lambda r: r['page']), ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('Retained scan', page, flush=True)

"""Retain completed built-in generations and their prompt provenance."""
import json
import shutil
import sys
from pathlib import Path

folder=Path(__file__).resolve().parents[1]/'frontend/artwork-source/nanshan'
manifest=folder/'entities-generation.json'
data=json.loads(manifest.read_text(encoding='utf-8'))
results={r['name']:r for r in json.loads(sys.argv[1]) if r['status']=='generated'}
for asset in data['assets']:
    if asset['name'] not in results:continue
    result=results[asset['name']]
    target=folder/(asset['name']+'-v1.png')
    if not target.exists():shutil.copy2(result['path'],target)
    asset['original_path']=result['path']
    if asset['status']!='reviewed':asset['status']='generated_pending_review'
manifest.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Retained generated originals:',len(results))

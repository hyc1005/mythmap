"""Inventory every captured source block, with separate confirmed and candidate links."""
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def read(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))

def build(check=False):
    snapshot = read('data/shanhaijing-reference.json')
    world = read('frontend/public/data/myth-world.json')
    passages = world['passages']
    western_review_path = ROOT / 'data/xishan-edition-review.json'
    western_review = read(western_review_path) if western_review_path.exists() else {}
    page_corrections = western_review.get('source_unit_page_corrections', {})
    heading_ids = {'source-01-0001', 'source-01-0002', *western_review.get('heading_unit_ids', [])}
    northern_review_path = ROOT / 'data/beishan-edition-review.json'
    if northern_review_path.exists():
        northern_review = read(northern_review_path)
        page_corrections = {**page_corrections, **northern_review.get('source_unit_page_corrections', {})}
        heading_ids.update(northern_review.get('heading_unit_ids', []))
    eastern_review_path = ROOT / 'data/dongshan-edition-review.json'
    if eastern_review_path.exists():
        eastern_review = read('data/dongshan-edition-review.json')
        page_corrections = {**page_corrections, **eastern_review.get('source_unit_page_corrections', {})}
        heading_ids.update(eastern_review.get('heading_unit_ids', []))
    confirmed = {}
    for passage in passages:
        for id in passage['source_unit_ids']:
            confirmed.setdefault(id, []).append(passage['id'])
    all_entries = [item for group in ['beasts','places','domains','natural_features','text_entities'] for item in world[group]]
    units, drafts = [], []
    for chapter in snapshot['chapters']:
        for number,line in enumerate(chapter['lines'],1):
            id = f'source-{chapter["number"]:02}-{number:04}'
            candidates = [entry['id'] for entry in all_entries if chapter['title'] in entry['source'] and entry['name'] in line['text']]
            linked = confirmed.get(id, [])
            units.append({'id':id, 'chapter':chapter['number'], 'source_url':chapter['revision_url'],
                'page_url':'https://zh.wikisource.org/wiki/'+line['page'], 'page_quality':line['page_quality'],
                'text':line['text'], 'commentary':line['annotations'], 'text_sha256':hashlib.sha256(line['text'].encode()).hexdigest(),
                'status':'explained_in_reader' if linked else 'heading_metadata' if id in heading_ids else 'pending_review',
                'confirmed_passage_ids':linked, 'candidate_entry_ids':candidates,
                'objects':sorted({subject for p in passages if p['id'] in linked for subject in p['subjects']}),
                'relationship_review':'passage_context_only' if linked else 'pending',
                'segmentation':'captured_source_block; reviewed semantic passages are linked separately'})
            if id in page_corrections:
                units[-1]['captured_page_url'] = units[-1]['page_url']
                units[-1]['page_url'] = units[-1]['page_url'].rsplit('/', 1)[0] + '/' + str(page_corrections[id])
        if chapter['number'] != 1:
            chapter_units = [u for u in units if u['chapter'] == chapter['number']]
            text = ''.join(u['text'] for u in chapter_units)
            starts = {0, *[m.start() for m in re.finditer(r'(?:又?[東西南北]{1,2}[一二三四五六七八九十百千萬]+里|凡[東西南北中海外內荒次一二三四五六七八九十山經之首]{2,}|有國(?:名曰|曰)|有山(?:名曰|曰)|有[神人獸鳥](?:名曰|曰))', text)]}
            bounds = sorted(starts) + [len(text)]
            offsets, cursor = [], 0
            for unit in chapter_units:
                offsets.append((cursor,cursor+len(unit['text']),unit)); cursor += len(unit['text'])
            for i,(start,end) in enumerate(zip(bounds,bounds[1:]),1):
                if start == end:
                    continue
                section = text[start:end]
                refs = [u for a,b,u in offsets if a<end and b>start or a==b and start<=a<end or a==b==end==len(text)]
                drafts.append({'id':f'draft-{chapter["number"]:02}-{i:04}', 'chapter':chapter['number'],
                    'source_span':[start,end], 'source_unit_ids':[u['id'] for u in refs],
                    'source_pages':list(dict.fromkeys(u['page_url'] for u in refs)), 'text':section,
                    'candidate_entry_ids':sorted({id for u in refs for id in u['candidate_entry_ids']}),
                    'relationship_excerpts':[section[max(0,m.start()-12):min(len(section),m.end()+18)] for m in re.finditer('流注|出焉|注于|所居|所生',section)],
                    'status':'pending_review','segmentation':'structural_candidate; boundaries and entities require manual review'})
                content_refs = [u for u in refs if u['status'] != 'heading_metadata']
                if content_refs and all(u['confirmed_passage_ids'] for u in content_refs):
                    drafts[-1]['status'] = 'reviewed_in_reader'
                    drafts[-1]['confirmed_passage_ids'] = sorted({p for u in content_refs for p in u['confirmed_passage_ids']})
                    drafts[-1]['segmentation'] = 'reviewed semantic passage linked; heading metadata excluded from reader'
    review = read('data/nanshan-edition-review.json')
    for number,(text,note) in enumerate(review['supplement'],1):
        id=f'scan-01-26-{number:02}'
        units.append({'id':id,'chapter':1,'page_url':'https://zh.wikisource.org/wiki/Page:Sibu_Congkan0465-郭璞-山海經-2-1.djvu/26',
            'text':text,'commentary':[note] if note else [],'status':'explained_in_reader','confirmed_passage_ids':confirmed[id],
            'objects':sorted({s for p in passages if p['id'] in confirmed[id] for s in p['subjects']}),'candidate_entry_ids':[],
            'relationship_review':'passage_context_only','segmentation':'manually restored from scan'})
    value={'version':1,'edition':snapshot['edition'],'snapshot_sha256':hashlib.sha256((ROOT/'data/shanhaijing-reference.json').read_bytes()).hexdigest(),
        'limits':f'全书清单逐项保留电子录文块及待核状态，不把录文换行当作已核定语义段。南山经43段、西山经{sum(p.get("source_book")==2 for p in passages)}段、北山经{sum(p.get("source_book")==3 for p in passages)}段已核；其余结构候选的边界、实体和关系仍待人工核定。候选匹配与关系摘录不构成已核定关联，也不作全书完成率分母。',
        'chapters':[{'number':c['number'],'title':c['title'],'source_blocks':sum(u['chapter']==c['number'] for u in units),
            'explained_blocks':sum(u['chapter']==c['number'] and u['status']=='explained_in_reader' for u in units),
            'semantic_passages':sum(p['region']==c['title'] for p in passages),
            'candidate_passages':sum(p['chapter']==c['number'] for p in drafts),
            'pending_candidate_passages':sum(p['chapter']==c['number'] and p['status']=='pending_review' for p in drafts),
            'semantic_review':'reviewed' if all(u['confirmed_passage_ids'] or u['status']=='heading_metadata' for u in units if u['chapter']==c['number']) else 'partial' if any(p['region']==c['title'] for p in passages) else 'pending'} for c in snapshot['chapters']],
        'units':units, 'candidate_passages':drafts}
    path=ROOT/'data/shanhaijing-inventory.json'
    output=json.dumps(value,ensure_ascii=False,indent=2)+'\n'
    if check:
        assert path.read_text(encoding='utf-8')==output,'Source inventory stale'
    else:
        path.write_text(output,encoding='utf-8')
    assert len({u['id'] for u in units})==len(units)
    assert all(u['confirmed_passage_ids'] or u['status']=='heading_metadata' for u in units if u['chapter']==1)
    assert all(u['id'] in {id for p in drafts for id in p['source_unit_ids']} for u in units if u['chapter']!=1)
    print('Inventory:',len(units),'source blocks;',len(passages),'reviewed passages;',sum(p['status']=='pending_review' for p in drafts),'pending structural drafts')

if __name__=='__main__':
    args=argparse.ArgumentParser(); args.add_argument('--check',action='store_true'); build(args.parse_args().check)

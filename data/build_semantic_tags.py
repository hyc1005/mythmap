"""Extract effect / omen tags from the full text of every bestiary account.

Output: frontend/src/bestiary-semantic-tags.json  (derived, not hand-edited)
Status: auto-extracted, pending editorial review; the UI must label it as such.

Rules follow docs/depth-roadmap.md 4.2:
- read quote / commentary_quote / description, never only classification.evidence
- normalise traditional / variant characters before matching
- keep the matched snippet as evidence, do not rewrite the source text
- separate 可以已/可以御 (effects) from 可以为 (usage, not tagged here)
- tag each field separately so commentary text is not glued onto the passage
"""

import io
import json
import re

ROOT = r'D:\testfileplace\gpttry02\webgisfinal'
WORLD = ROOT + r'\frontend\public\data\myth-world.json'
META = ROOT + r'\frontend\src\bestiary-metadata.json'
OUT = ROOT + r'\frontend\src\bestiary-semantic-tags.json'

VARIANT = str.maketrans({
    '禦': '御', '見': '见', '動': '动', '訛': '讹', '靣': '面', '蟲': '虫',
    '殺': '杀', '癘': '疠', '國': '国', '縣': '县', '獸': '兽', '鳥': '鸟',
    '則': '则', '寧': '宁', '饑': '饥', '風': '风', '蠱': '蛊',
})

FIELDS = ('quote', 'commentary_quote', 'description')

EFFECT_RULES = [
    ('ward_fire', re.compile(r'可以御火')),
    ('ward_war', re.compile(r'可以御兵')),
    ('ward_plague', re.compile(r'可以御疫')),
    ('ward_evil', re.compile(r'不蛊')),
    ('ward_evil', re.compile(r'可以御凶')),
    ('ward_evil', re.compile(r'可以杀虫')),
    ('cure_disease', re.compile(r'食[之者]已([\u4e00-\u9fff]{1,3}?)(?=可以|[，。；、]|$)')),
    ('calm', re.compile(r'(?:佩|食)之不畏')),
    ('calm', re.compile(r'不惑|不眯|已忧')),
    ('travel', re.compile(r'善走')),
    ('nourish', re.compile(r'不饥')),
]

OMEN_MARK = re.compile(r'(见则|动则)([^。；，、\n]{1,16})')
OMEN_RULES = [
    ('flood', ('大水',)),
    ('drought', ('大旱',)),
    ('war', ('大兵', '有兵')),
    ('plague', ('大疫',)),
    ('bountiful', ('大穰',)),
    ('peace', ('安宁',)),
    ('famine', ('大饥',)),
    ('fire', ('火',)),
    ('wind', ('大风', '风')),
    ('other_omen', ('土功', '放士', '大繇')),
]


def snippet(text, start, end, pad=8):
    return text[max(0, start - pad):min(len(text), end + pad)].strip()


def extract(text):
    canonical = text.translate(VARIANT)
    effects, omens = [], []

    for tag, pattern in EFFECT_RULES:
        for match in pattern.finditer(canonical):
            effects.append({
                'tag': tag,
                'match': match.group(0),
                'evidence': snippet(canonical, match.start(), match.end()),
            })

    for mark in OMEN_MARK.finditer(canonical):
        clause = mark.group(2).strip()
        if not clause:
            continue
        for tag, words in OMEN_RULES:
            if any(word in clause for word in words):
                omens.append({'tag': tag, 'match': (mark.group(1) + clause), 'evidence': snippet(canonical, mark.start(), mark.end())})
                break
        else:
            omens.append({'tag': 'other_omen', 'match': (mark.group(1) + clause), 'evidence': snippet(canonical, mark.start(), mark.end())})

    return effects, omens


def dedupe(items):
    seen, result = set(), []
    for item in items:
        key = (item['tag'], item['match'])
        if key in seen:
            continue
        seen.add(key)
        result.append(item)
    return sorted(result, key=lambda item: (item['tag'], item['match']))


def main():
    world = json.load(io.open(WORLD, encoding='utf-8'))
    meta = json.load(io.open(META, encoding='utf-8'))
    items = world['beasts'] + [item for item in world.get('text_entities', []) if item.get('kind') == 'deity']

    entries = {}
    for item in items:
        record = meta.get(item['id'])
        if not record:
            continue
        effects, omens = [], []
        for field in FIELDS:
            text = str(item.get(field) or '')
            if not text:
                continue
            field_effects, field_omens = extract(text)
            for tag in field_effects:
                tag['source'] = field
            for tag in field_omens:
                tag['source'] = field
            effects.extend(field_effects)
            omens.extend(field_omens)
        effects, omens = dedupe(effects), dedupe(omens)
        if not effects and not omens:
            continue
        entries[item['id']] = {
            'status': 'auto',
            'basis': record.get('classification', {}).get('basis', 'text'),
            'effect': effects,
            'omen': omens,
        }

    output = {
        '_note': 'Auto-extracted effect/omen tags from the full text; pending editorial review. Derivatives only, never rewrites the source.',
        '_normalisation': '禦→御 見→见 動→动 訛→讹 靣→面 蟲→虫 殺→杀 癘→疠 國→国 縣→县 獸→兽 鳥→鸟 則→则 寧→宁 饑→饥 風→风 蠱→蛊',
        '_excluded': '可以為× (usage, e.g. 旋龜可以為底) is not tagged; 食之/佩之 without a stated effect is not tagged.',
        'entries': dict(sorted(entries.items())),
    }

    io.open(OUT, 'w', encoding='utf-8', newline='\n').write(json.dumps(output, ensure_ascii=False, indent=2) + '\n')

    print('entries with tags: %d / %d' % (len(entries), len(items)))
    print('entries with effect tags: %d' % sum(1 for record in entries.values() if record['effect']))
    print('entries with omen tags: %d' % sum(1 for record in entries.values() if record['omen']))
    print('output bytes: %d' % len(io.open(OUT, 'rb').read()))


if __name__ == '__main__':
    main()

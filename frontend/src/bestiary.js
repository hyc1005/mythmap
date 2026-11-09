import morphologyReviews from './bestiary-morphology-review.json' with { type: 'json' };
import metadata from './bestiary-metadata.json' with { type: 'json' };
import notability from './bestiary-notability.json' with { type: 'json' };
import semanticTags from './bestiary-semantic-tags.json' with { type: 'json' };

export const BESTIARY_INITIAL = 12;
export const BESTIARY_BATCH = 24;
export const FORM_LABELS = {
  beast: { zh: '兽形', en: 'Beast form' }, bird: { zh: '鸟形', en: 'Bird form' },
  fish: { zh: '鱼形', en: 'Fish form' }, serpent: { zh: '蛇龟形', en: 'Serpent / turtle form' },
  insect: { zh: '虫形', en: 'Insect form' }, other: { zh: '其他／未详', en: 'Other / unspecified' },
};
export const FEATURE_LABELS = {
  human_face: { zh: '人面', en: 'Human face' }, many_heads: { zh: '多首', en: 'Multiple heads' },
  many_tails: { zh: '多尾', en: 'Multiple tails' }, winged: { zh: '有翼', en: 'Winged' },
  four_wings: { zh: '四翼', en: 'Four wings' }, one_eye: { zh: '独眼', en: 'One eye' },
  one_leg: { zh: '独足', en: 'One leg' }, many_legs: { zh: '多足', en: 'Many legs' },
  horned: { zh: '有角', en: 'Horned' }, scales: { zh: '鳞甲', en: 'Scales / armour' },
};
export const EFFECT_LABELS = {
  ward_fire: { zh: '御火', en: 'Fire ward' }, ward_war: { zh: '御兵', en: 'War ward' },
  ward_evil: { zh: '御凶', en: 'Evil ward' }, ward_plague: { zh: '御疫', en: 'Plague ward' },
  cure_disease: { zh: '已疾', en: 'Cures illness' }, travel: { zh: '善走', en: 'Swift travel' },
  calm: { zh: '不畏', en: 'Calms fear' }, nourish: { zh: '不饥', en: 'Prevents hunger' },
};
export const OMEN_LABELS = {
  flood: { zh: '大水', en: 'Flood' }, drought: { zh: '大旱', en: 'Drought' }, war: { zh: '大兵', en: 'War' },
  famine: { zh: '大饥', en: 'Famine' }, plague: { zh: '大疫', en: 'Plague' }, fire: { zh: '火灾', en: 'Fire' },
  wind: { zh: '大风', en: 'Great wind' }, bountiful: { zh: '大穰', en: 'Bountiful harvest' },
  peace: { zh: '安宁', en: 'Peace' }, other_omen: { zh: '其他征兆', en: 'Other omen' },
};

export function semanticTagsFor(id) {
  return semanticTags.entries[id] || null;
}

export function notabilityFor(id) {
  return Number(notability[id]) || 0;
}

export function sharedSemanticTags(a, b) {
  const left = semanticTagsFor(a), right = semanticTagsFor(b);
  if (!left || !right) return 0;
  const tags = new Set([...left.effect, ...left.omen].map(tag => tag.tag));
  return [...right.effect, ...right.omen].filter(tag => tags.has(tag.tag)).length;
}
const normalize = value => String(value || '').normalize('NFKC').toLocaleLowerCase().replace(/\s+/g, ' ').trim();

export function bestiaryEntry(item, locale = 'zh') {
  const value = metadata[item.id];
  if (!value) return null;
  return { ...item, displayName: value.display_name[locale], shortNames: Object.values(value.display_name),
    nameAliases: [...new Set([item.name, item.originalName, ...(item.aliases || []), ...Object.values(value.display_name)].filter(Boolean))],
    qualifier: value.qualifier[locale], bookKey: value.book_key, groupKey: value.group_key, role: value.role,
    formGroup: value.form_group, featureTags: value.feature_tags, classification: value.classification };
}

export function bestiaryEntries(world, locale = 'zh') {
  const places = new Map(world.places.map(item => [item.id, item]));
  return [...world.beasts, ...(world.text_entities || []).filter(item => item.kind === 'deity')].map(item => {
    const entry = bestiaryEntry(item, locale);
    if (!entry) return null;
    return { ...entry, provenance: [...new Set([item.region, entry.qualifier || places.get(item.context_place_id)?.name].filter(Boolean))].join(' · ') };
  }).filter(Boolean);
}

export function bestiarySearchFields(entry) {
  return [entry.nameAliases, entry.provenance, entry.description, entry.quote, entry.originalQuote,
    entry.source, entry.region, Object.values(FORM_LABELS[entry.formGroup]),
    entry.featureTags.flatMap(tag => Object.values(FEATURE_LABELS[tag]))].flat(Infinity).filter(Boolean);
}

export function filterBestiary(entries, { role = 'beast', book = '', form = '', feature = '', reading = '', query = '', effect = '', omen = '' } = {}, marks = { read: [], favorites: [] }) {
  const value = normalize(query), terms = value.split(' ').filter(Boolean);
  return entries.filter(item => (!role || item.role === role) && (!book || item.bookKey === book)
    && (!form || item.formGroup === form) && (!feature || item.featureTags.includes(feature))
    && (!effect || semanticTags.entries[item.id]?.effect.some(tag => tag.tag === effect))
    && (!omen || semanticTags.entries[item.id]?.omen.some(tag => tag.tag === omen))
    && (!reading || reading === 'read' && marks.read.includes(item.id) || reading === 'unread' && !marks.read.includes(item.id) || reading === 'favorites' && marks.favorites.includes(item.id))
    && terms.every(term => normalize(bestiarySearchFields(item).join(' ')).includes(term)))
    .map((entry, order) => ({ entry, order, score: Number(notability[entry.id]) || 0, rank: !value ? 0 : entry.shortNames.some(name => normalize(name) === value) ? 0
      : entry.nameAliases.some(name => normalize(name) === value) ? 1 : entry.nameAliases.some(name => normalize(name).includes(value)) ? 2 : 3 }))
    .sort((a, b) => a.rank - b.rank || b.score - a.score || a.order - b.order).map(item => item.entry);
}

export function groupBestiary(entries) {
  const groups = new Map();
  for (const entry of entries) {
    const key = `${entry.role}:${entry.groupKey}`;
    if (!groups.has(key)) groups.set(key, { key, entries: [] });
    groups.get(key).entries.push(entry);
  }
  return [...groups.values()];
}

export function bestiaryNamesakes(world, id, locale = 'zh') {
  const selected = metadata[id];
  if (!selected) return [];
  return bestiaryEntries(world, locale)
    .filter(entry => entry.role === selected.role && entry.groupKey === selected.group_key)
    .sort((a, b) => (Number(notability[b.id]) || 0) - (Number(notability[a.id]) || 0));
}

export function comparisonEntries(world, id, locale = 'zh') {
  const selected = metadata[id];
  if (!selected) return [];
  const items = [...world.beasts, ...(world.text_entities || [])];
  const source = items.find(item => item.id === id);
  const passages = new Set(source?.source_passage_ids || []);
  if (!passages.size) return [];
  return items
    .filter(item => item.id !== id && metadata[item.id]?.classification?.basis === 'comparison')
    .filter(item => (item.source_passage_ids || []).some(passage => passages.has(passage)))
    .map(item => bestiaryEntry(item, locale))
    .filter(Boolean);
}

const reviewLabels = {
  described: ['形貌有据', 'Form described'], partial: ['比拟未详', 'Comparison unclear'], ambiguous: ['物名有异说', 'Name disputed'],
  commentary: ['郭注另述', 'Commentary account'], collective: ['集体称谓', 'Collective designation'],
  name_only: ['仅列名称', 'Name only'], not_recorded: ['本段未记形貌', 'Form unstated here'],
  transformation: ['仅记变化', 'Transformation only'], comparison: ['比较引文未记形貌', 'Form unstated in comparison'],
};
export function morphologyReview(id, locale = 'zh') {
  const review = morphologyReviews[id];
  return review ? { ...review, label: reviewLabels[review.status][locale === 'en' ? 1 : 0], note: review.note[locale] } : null;
}

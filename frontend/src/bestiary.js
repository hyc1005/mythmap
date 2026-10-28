import metadata from './bestiary-metadata.json' with { type: 'json' };

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

export function filterBestiary(entries, { role = 'beast', book = '', form = '', feature = '', reading = '', query = '' } = {}, marks = { read: [], favorites: [] }) {
  const value = normalize(query), terms = value.split(' ').filter(Boolean);
  return entries.filter(item => (!role || item.role === role) && (!book || item.bookKey === book)
    && (!form || item.formGroup === form) && (!feature || item.featureTags.includes(feature))
    && (!reading || reading === 'read' && marks.read.includes(item.id) || reading === 'unread' && !marks.read.includes(item.id) || reading === 'favorites' && marks.favorites.includes(item.id))
    && terms.every(term => normalize(bestiarySearchFields(item).join(' ')).includes(term)))
    .map((entry, order) => ({ entry, order, rank: !value ? 0 : entry.shortNames.some(name => normalize(name) === value) ? 0
      : entry.nameAliases.some(name => normalize(name) === value) ? 1 : entry.nameAliases.some(name => normalize(name).includes(value)) ? 2 : 3 }))
    .sort((a, b) => a.rank - b.rank || a.order - b.order).map(item => item.entry);
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

import { bestiaryEntry, bestiarySearchFields } from './bestiary.js';
import { storySummary } from './story-summaries.js';
import { associationLabel, geographicReferences } from './geography.js';
import { contentOrigin } from './content-provenance.js';

const normalize = value => String(value || '').normalize('NFKC').toLocaleLowerCase().replace(/\s+/g, ' ').trim();
const strings = values => values.flat(Infinity).filter(value => typeof value === 'string' && value.trim());

export function searchIndex(world, catalog, originalWorld, originalCatalog, locale = 'zh', translate = value => value) {
  const records = [];
  const events = catalog.events.filter(item => world.stages.some(stage => stage.id === item.properties.stage_id));
  const add = (record, fields) => records.push({ ...record, origin: record.origin || contentOrigin(record), fields: strings(fields), text: normalize(strings([record.name, record.alias, record.nameAliases, record.shortNames, fields]).join(' ')), order: records.length });
  for (const [group, kind] of [['beasts', 'beast'], ['places', 'place'], ['domains', 'place']]) {
    for (const item of world[group]) {
      const original = originalWorld[group].find(entry => entry.id === item.id) || item;
      const presentation = kind === 'beast' ? bestiaryEntry(item, locale) : null;
      add({ key: item.id, id: item.id, kind, name: presentation?.displayName || item.name, alias: original.name, nameAliases: presentation?.nameAliases, shortNames: presentation?.shortNames, source: item.source, chapter: item.reveal_chapter }, [item.name, presentation ? bestiarySearchFields(presentation) : [], item.aliases, original.aliases, item.description, item.quote, item.source, item.region, original.description, original.quote, original.source, kind === 'beast' ? '山海经 Shanhaijing Classic of Mountains and Seas' : '']);
    }
  }
  for (const item of events) {
    const value = item.properties, original = originalCatalog.events.find(entry => entry.id === item.id)?.properties || value;
    const summaries = [...new Set([storySummary(item.id, locale), storySummary(item.id, 'zh')].filter(Boolean))];
    add({ key: item.id, id: item.id, kind: 'story', name: value.name, alias: original.name, source: value.source_text, chapter: value.stage_id, summaries, summaryLocale: locale }, [summaries, value.source_quote, value.source_text, value.commentary, value.tags, value.people, original.source_quote, original.source_text, original.tags, original.people]);
  }
  for (const item of world.natural_features || []) {
    const original = originalWorld.natural_features?.find(entry => entry.id === item.id) || item;
    add({ key: item.id, id: item.id, kind: item.kind, name: item.name, alias: original.name, source: item.source, chapter: item.reveal_chapter },
      [item.description, item.quote, item.source, item.source_locator, original.name, original.description, original.quote]);
  }
  for (const item of world.passages || []) {
    const original = originalWorld.passages?.find(entry => entry.id === item.id) || item;
    add({ key: item.id, id: item.id, kind: 'passage', name: item.name, alias: original.name, source: item.source, chapter: item.reveal_chapter },
      [item.description, item.quote, item.source, original.name, original.description, original.quote, original.subjects]);
  }
  for (const item of world.text_entities || []) {
    const original = originalWorld.text_entities?.find(entry => entry.id === item.id) || item;
    const presentation = bestiaryEntry(item, locale);
    add({ key: item.id, id: item.id, kind: item.kind, name: presentation?.displayName || item.name, alias: original.name, nameAliases: presentation?.nameAliases, shortNames: presentation?.shortNames, source: item.source, chapter: item.reveal_chapter },
      [item.name, presentation ? bestiarySearchFields(presentation) : [], item.description, item.quote, item.source, original.name, original.description, original.quote]);
  }
  const originalReferences = new Map(geographicReferences(originalCatalog).map(record => [record.id, record.properties]));
  for (const record of geographicReferences(catalog)) {
    const value = record.properties;
    const original = originalReferences.get(record.id) || value;
    const event = events.find(item => item.id === value.entity_id);
    if (!event || ['archive', 'group'].includes(event.properties.presentation)) continue;
    const originalEvent = originalCatalog.events.find(item => item.id === event.id);
    const account = locale === 'en' ? value.basis_note_en || translate(value.basis_note || value.reason || '') : value.basis_note || value.reason;
    add({ key: `geography:${record.id}`, id: event.id, origin: contentOrigin(record), referenceId: record.id, kind: 'geography', name: translate(value.label), alias: original.label,
      chapter: event.properties.stage_id, source: translate(associationLabel(record)), entryName: event.properties.name },
    [account, value.basis_note, value.basis_note_en, value.reason, value.account?.summary, value.account?.summary_en, original.basis_note,
      event.properties.name, originalEvent?.properties.name, translate(value.label), original.label, translate(associationLabel(record)), associationLabel(record)]);
  }
  for (const source of catalog.sources) {
    const linked = events.filter(item => item.properties.source_ids?.includes(source.id));
    if (!linked.length) continue;
    const original = originalCatalog.sources.find(item => item.id === source.id) || source;
    add({ key: `source:${source.id}`, id: linked[0].id, origin: contentOrigin(`source:${source.id}`), kind: 'source', name: source.title, alias: original.title, entryName: linked.slice(0, 3).map(item => item.properties.name).join(' / '), entryCount: linked.length, entryIds: linked.map(item => item.id) }, [source.quote, source.commentary, source.modern_source, original.quote, original.commentary, original.modern_source, linked.map(item => item.properties.name)]);
  }
  const books = new Map();
  for (const item of [...world.beasts, ...world.places, ...world.domains, ...(world.natural_features || [])]) {
    if (!item.source) continue;
    if (!books.has(item.source)) books.set(item.source, []);
    books.get(item.source).push(item);
  }
  for (const [title, items] of books) {
    const originals = items.map(item => [...originalWorld.beasts, ...originalWorld.places, ...originalWorld.domains, ...(originalWorld.natural_features || [])].find(entry => entry.id === item.id)).filter(Boolean);
    add({ key: `book:${title}`, id: items[0].id, kind: 'source', name: title, alias: originals[0]?.source, entryName: items.slice(0, 3).map(item => item.name).join(' / '), entryCount: items.length, entryIds: items.map(item => item.id) }, [title, items.map(item => [item.name, item.description, item.quote]), originals.map(item => [item.name, item.source, item.description, item.quote]), '山海经 Shanhaijing Classic of Mountains and Seas']);
  }
  return records;
}

export function searchEntries(index, query, kind = 'all') {
  const value = normalize(query), terms = value.split(' ').filter(Boolean);
  if (!value && kind === 'all') return [];
  return index.filter(item => (kind === 'all' || item.kind === kind) && terms.every(term => item.text.includes(term)))
    .map(item => {
      const titles = [item.name, ...(item.shortNames || [])].map(normalize);
      const aliases = [item.alias, ...(item.nameAliases || [])].filter(Boolean).map(normalize);
      const rank = titles.includes(value) ? 0 : aliases.includes(value) ? 1 : [...titles, ...aliases].some(name => name.startsWith(value)) ? 2 : [...titles, ...aliases].some(name => name.includes(value)) ? 3 : 4;
      const field = item.fields.find(text => terms.some(term => normalize(text).includes(term))) || item.fields[0] || '';
      const match = terms.map(term => normalize(field).indexOf(term)).find(position => position >= 0) || 0;
      const start = Math.max(0, match - 35);
      const summary = item.summaries?.includes(field);
      return { ...item, rank, snippetKind: summary ? 'summary' : 'text', snippetLanguage: summary ? field === item.summaries[0] ? item.summaryLocale : 'zh' : undefined,
        snippet: `${start ? '…' : ''}${field.slice(start, start + 140)}${field.length > start + 140 ? '…' : ''}` };
    }).sort((a, b) => a.rank - b.rank || a.order - b.order);
}
export function highlightTerms(text, query) {
  const terms = [...new Set(normalize(query).split(' ').filter(Boolean))].sort((a, b) => b.length - a.length);
  if (!terms.length) return [{ text, matched: false }];
  const pattern = new RegExp(`(${terms.map(term => term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|')})`, 'giu');
  return text.split(pattern).filter(Boolean).map(value => ({ text: value, matched: terms.includes(normalize(value)) }));
}

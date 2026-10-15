const normalize = value => String(value || '').normalize('NFKC').toLocaleLowerCase().replace(/\s+/g, ' ').trim();
const strings = values => values.flat(Infinity).filter(value => typeof value === 'string' && value.trim());

export function searchIndex(world, catalog, originalWorld, originalCatalog) {
  const records = [];
  const events = catalog.events.filter(item => world.stages.some(stage => stage.id === item.properties.stage_id));
  const add = (record, fields) => records.push({ ...record, fields: strings(fields), text: normalize(strings([record.name, record.alias, fields]).join(' ')), order: records.length });
  for (const [group, kind] of [['beasts', 'beast'], ['places', 'place'], ['domains', 'place']]) {
    for (const item of world[group]) {
      const original = originalWorld[group].find(entry => entry.id === item.id) || item;
      add({ key: item.id, id: item.id, kind, name: item.name, alias: original.name, source: item.source, chapter: item.reveal_chapter }, [item.description, item.quote, item.source, item.region, original.description, original.quote, original.source, kind === 'beast' ? '山海经 Shanhaijing Classic of Mountains and Seas' : '']);
    }
  }
  for (const item of events) {
    const value = item.properties, original = originalCatalog.events.find(entry => entry.id === item.id)?.properties || value;
    add({ key: item.id, id: item.id, kind: 'story', name: value.name, alias: original.name, source: value.source_text, chapter: value.stage_id }, [value.source_quote, value.source_text, value.commentary, value.tags, value.people, original.source_quote, original.source_text, original.tags, original.people]);
  }
  for (const source of catalog.sources) {
    const linked = events.filter(item => item.properties.source_ids?.includes(source.id));
    if (!linked.length) continue;
    const original = originalCatalog.sources.find(item => item.id === source.id) || source;
    add({ key: `source:${source.id}`, id: linked[0].id, kind: 'source', name: source.title, alias: original.title, entryName: linked.slice(0, 3).map(item => item.properties.name).join(' / '), entryCount: linked.length, entryIds: linked.map(item => item.id) }, [source.quote, source.commentary, source.modern_source, original.quote, original.commentary, original.modern_source, linked.map(item => item.properties.name)]);
  }
  const books = new Map();
  for (const item of [...world.beasts, ...world.places, ...world.domains]) {
    if (!item.source) continue;
    if (!books.has(item.source)) books.set(item.source, []);
    books.get(item.source).push(item);
  }
  for (const [title, items] of books) {
    const originals = items.map(item => [...originalWorld.beasts, ...originalWorld.places, ...originalWorld.domains].find(entry => entry.id === item.id)).filter(Boolean);
    add({ key: `book:${title}`, id: items[0].id, kind: 'source', name: title, alias: originals[0]?.source, entryName: items.slice(0, 3).map(item => item.name).join(' / '), entryCount: items.length, entryIds: items.map(item => item.id) }, [title, items.map(item => [item.name, item.description, item.quote]), originals.map(item => [item.name, item.source, item.description, item.quote]), '山海经 Shanhaijing Classic of Mountains and Seas']);
  }
  return records;
}

export function searchEntries(index, query, kind = 'all') {
  const value = normalize(query), terms = value.split(' ').filter(Boolean);
  if (!value && kind === 'all') return [];
  return index.filter(item => (kind === 'all' || item.kind === kind) && terms.every(term => item.text.includes(term)))
    .map(item => {
      const title = normalize(item.name), alias = normalize(item.alias);
      const rank = title === value || alias === value ? 0 : title.startsWith(value) || alias.startsWith(value) ? 1 : title.includes(value) || alias.includes(value) ? 2 : 3;
      const field = item.fields.find(text => terms.some(term => normalize(text).includes(term))) || item.fields[0] || '';
      const match = terms.map(term => normalize(field).indexOf(term)).find(position => position >= 0) || 0;
      const start = Math.max(0, match - 35);
      return { ...item, rank, snippet: `${start ? '…' : ''}${field.slice(start, start + 140)}${field.length > start + 140 ? '…' : ''}` };
    }).sort((a, b) => a.rank - b.rank || a.order - b.order);
}

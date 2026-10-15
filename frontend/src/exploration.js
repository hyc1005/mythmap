export function itemChapter(id, world, catalog) {
  const event = catalog.events.find(item => item.id === id);
  if (event) return world.stages.some(stage => stage.id === event.properties.stage_id) ? event.properties.stage_id : null;
  const item = [...world.beasts, ...world.places, ...world.domains].find(item => item.id === id);
  return item?.reveal_chapter || null;
}

export function readExploration(search, world, catalog) {
  const query = new URLSearchParams(search);
  const chapter = query.get('chapter');
  const requestedItem = query.get('item');
  const validChapter = !chapter || world.stages.some(stage => stage.id === chapter);
  const relatedChapter = validChapter && itemChapter(requestedItem, world, catalog);
  const chosenChapter = validChapter ? chapter || relatedChapter || '00' : '00';
  const stageIndex = Math.max(0, world.stages.findIndex(stage => stage.id === chosenChapter));
  const item = relatedChapter && (catalog.events.some(event => event.id === requestedItem)
    ? relatedChapter === chosenChapter : Number(relatedChapter) <= Number(chosenChapter)) ? requestedItem : null;
  return { stageIndex, item, shared: query.has('chapter') || query.has('item') };
}

export function explorationUrl(href, chapter, item, locale) {
  const url = new URL(href);
  url.searchParams.set('chapter', chapter);
  url.searchParams.set('lang', locale);
  if (item) url.searchParams.set('item', item);
  else url.searchParams.delete('item');
  url.hash = 'world';
  return url;
}

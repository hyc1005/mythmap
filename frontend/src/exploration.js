import { worldEntries } from './entries.js';

export function itemChapter(id, world, catalog) {
  const event = catalog.events.find(item => item.id === id);
  if (event) return world.stages.some(stage => stage.id === event.properties.stage_id) ? event.properties.stage_id : null;
  const item = worldEntries(world).find(item => item.id === id);
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
  const contextId = worldEntries(world).find(item => item.id === requestedItem)?.context_place_id;
  const contextChapter = contextId && itemChapter(contextId, world, catalog);
  const item = relatedChapter && (catalog.events.some(event => event.id === requestedItem)
    ? relatedChapter === chosenChapter : Number(relatedChapter) <= Number(chosenChapter) || contextChapter && Number(contextChapter) <= Number(chosenChapter)) ? requestedItem : null;
  return { stageIndex, item, shared: query.has('chapter') || query.has('item') };
}

export function readGeography(search, chapter, catalog, references) {
  const query = new URLSearchParams(search);
  const event = catalog.events.find(item => item.id === query.get('event') && item.properties.stage_id === chapter && !['archive', 'group'].includes(item.properties.presentation));
  const reference = event && references.find(item => item.id === query.get('reference') && item.properties.entity_id === event.id);
  return { open: query.get('mode') === 'geography', eventId: event?.id || null, referenceId: reference?.id || null };
}

export function explorationUrl(href, chapter, item, locale, geography = {}) {
  const url = new URL(href);
  url.searchParams.set('chapter', chapter);
  url.searchParams.set('lang', locale);
  if (item) url.searchParams.set('item', item);
  else url.searchParams.delete('item');
  for (const key of ['mode', 'event', 'reference']) url.searchParams.delete(key);
  if (geography.open) {
    url.searchParams.set('mode', 'geography');
    if (geography.eventId) url.searchParams.set('event', geography.eventId);
    if (geography.referenceId) url.searchParams.set('reference', geography.referenceId);
  }
  url.hash = 'world';
  return url;
}

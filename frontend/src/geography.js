import associations from './geography-associations.json' with { type: 'json' };

export function validReference(record) {
  const coordinates = record.geometry?.coordinates;
  return record.geometry?.type === 'Point' && Array.isArray(coordinates) && coordinates.length === 2
    && coordinates.every(Number.isFinite) && Math.abs(coordinates[0]) <= 180 && Math.abs(coordinates[1]) <= 90
    && record.properties?.verification_status === 'modern_reference_verified';
}

export function referenceCollection(records) {
  return { type: 'FeatureCollection', name: 'Event traditions and geographic hypotheses; not established historical sites',
    features: records.filter(validReference).map(record => ({ ...record, properties: { ...record.properties, reference_only: true } })) };
}

export function groupReferences(records) {
  const groups = new Map();
  for (const record of records) {
    const key = record.geometry.coordinates.join(',');
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(record);
  }
  return [...groups.values()];
}

export function unlocatedStories(catalog, chapter = '') {
  return geographicEvents(catalog).filter(event => (!chapter || event.properties.stage_id === chapter)
    && !geographicReferences(catalog).some(item => validReference(item) && item.properties.entity_id === event.id));
}

export function geographicEvents(catalog) {
  return catalog.stages.flatMap(stage => {
    const order = stage.event_ids || [];
    return catalog.events.filter(event => event.properties.stage_id === stage.id && !['archive', 'group'].includes(event.properties.presentation))
      .sort((a, b) => (order.includes(a.id) ? order.indexOf(a.id) : 999) - (order.includes(b.id) ? order.indexOf(b.id) : 999));
  });
}

export function defaultGeographicEvent(catalog, chapterId, currentEventId) {
  const events = geographicEvents(catalog);
  return events.find(event => event.id === currentEventId && event.properties.stage_id === chapterId)?.id
    || events.find(event => event.properties.stage_id === chapterId)?.id || events[0]?.id || '';
}

export function geographicReferences(catalog) {
  return [...catalog.candidates.map(record => ({ ...record, properties: {
    ...record.properties, association_type: 'research_hypothesis', location_precision: 'region_representative',
    evidence_status: 'pending', evidence: [], ...associations.evidence_updates[record.id],
  } })), ...associations.features].filter(validReference);
}

export const associationLabel = record => record.properties.association_type === 'local_tradition' ? '地方传说' : '地理考证';

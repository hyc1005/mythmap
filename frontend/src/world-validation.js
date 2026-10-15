function requireValue(condition, message) {
  if (!condition) throw new Error(`Invalid world: ${message}`);
}

const text = value => typeof value === 'string' && value.trim().length > 0;
const point = value => Array.isArray(value) && value.length === 2 && value.every(Number.isFinite)
  && value[0] >= 0 && value[0] <= 1200 && value[1] >= 0 && value[1] <= 800;

export function validateWorld(data, bundled) {
  requireValue(data && data.revision === bundled.revision, 'incompatible revision');
  requireValue(data.coordinate_system === 'diagram-units', 'coordinate system');
  const groups = ['stages', 'regions', 'terrain', 'places', 'relations', 'domains', 'beasts'];
  for (const key of groups) requireValue(Array.isArray(data[key]), `${key} must be an array`);
  requireValue(data.stages.length === bundled.stages.length && data.stages.every((stage, i) => stage?.id === bundled.stages[i].id), 'chapter order');
  const chapters = new Set(data.stages.map(stage => stage.id));
  const ids = new Set();
  for (const key of groups.filter(key => key !== 'relations')) {
    for (const record of data[key]) {
      requireValue(record && text(record.id) && !ids.has(record.id), `${key}: missing or duplicate id`);
      ids.add(record.id);
      if (key !== 'stages') requireValue(chapters.has(record.reveal_chapter), `${record.id}: reveal chapter`);
      if (['places', 'domains', 'beasts'].includes(key)) requireValue(text(record.name) && text(record.source), `${record.id}: name/source`);
      if (['places', 'terrain'].includes(key)) requireValue(point([record.x, record.y]), `${record.id}: coordinates`);
      if (key === 'places') requireValue(text(record.direction), `${record.id}: direction`);
      if (key === 'beasts') requireValue(text(record.description) && text(record.region), `${record.id}: description/region`);
      if (key === 'domains') requireValue(text(record.quote) && text(record.place_id), `${record.id}: quote/place`);
      if (key === 'regions') requireValue(text(record.label) && point(record.label_position), `${record.id}: label`);
      if (key === 'terrain') requireValue(['peak', 'ridge', 'sea-cloud', 'distant'].includes(record.kind) && Number.isFinite(record.width) && record.width > 0
        && Number.isFinite(record.opacity) && record.opacity >= 0 && record.opacity <= 1, `${record.id}: terrain style`);
      if (key === 'stages') {
        const e = record.extent;
        requireValue(text(record.title) && text(record.subtitle) && Array.isArray(e) && e.length === 4
          && point(e.slice(0, 2)) && point(e.slice(2)) && e[0] < e[2] && e[1] < e[3], `${record.id}: chapter extent`);
      }
    }
  }
  requireValue(text(data.stages[0].scene), 'prologue scene');
  const places = new Set(data.places.map(place => place.id));
  for (const item of [...data.beasts, ...data.domains]) if (item.place_id) requireValue(places.has(item.place_id), `${item.id}: unknown place`);
  for (const relation of data.relations) requireValue(relation && places.has(relation.from) && places.has(relation.to) && text(relation.label), 'relation endpoint/label');
  return data;
}

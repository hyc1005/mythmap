import origins from './content-provenance.json' with { type: 'json' };

export const originLabels = {
  shanhaijing: '《山海经》所载',
  other_classic: '其他古籍所载',
  mixed: '多书合引',
  local_tradition: '地方传说',
  modern_research: '地望考证',
  pending: '来源待核对',
};

export function contentOrigin(record) {
  if (record?.properties?.association_type) {
    return { family: record.properties.association_type === 'local_tradition' ? 'local_tradition' : 'modern_research' };
  }
  return record?.origin || origins[typeof record === 'string' ? record : record?.id] || { family: 'pending' };
}

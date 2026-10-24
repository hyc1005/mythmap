import { assetUrl } from './asset-url';

export function iconFor(record, variant = 'full') {
  const creature = /^(beast|animal|bird)-/.test(record.id || '') || ['beast', 'animal', 'deity', '兽', '鸟', '鱼', '蛇', '水族', '神异'].includes(record.kind);
  if (record.appearance_unknown || creature && !record.artwork) return assetUrl('/data/atlas/myth-icons/unknown-creature.webp', variant);
  return record.artwork ? assetUrl(record.artwork.startsWith('/') ? record.artwork : `/data/atlas/myth-icons/${record.artwork}`, variant) : null;
}

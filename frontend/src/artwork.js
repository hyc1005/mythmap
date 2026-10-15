import { assetUrl } from './asset-url';

export function iconFor(record, variant = 'full') {
  return record.artwork ? assetUrl(record.artwork.startsWith('/') ? record.artwork : `/data/atlas/myth-icons/${record.artwork}`, variant) : null;
}

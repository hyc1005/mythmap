export function assetUrl(path) {
  return path?.startsWith('/data/') ? `${import.meta.env.BASE_URL}${path.slice(1)}` : path;
}

export function iconFor(record) {
  return record.artwork ? assetUrl(record.artwork.startsWith('/') ? record.artwork : `/data/atlas/myth-icons/${record.artwork}`) : null;
}

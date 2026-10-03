export function assetUrl(path) {
  return path?.startsWith('/data/') ? `${import.meta.env.BASE_URL}${path.slice(1)}` : path;
}

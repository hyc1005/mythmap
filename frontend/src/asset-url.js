import optimizedAssets from './optimized-assets.json';
import previews from './preview-assets.json';
import refined from './refined-artwork.json';

export function assetUrl(path, variant = 'full') {
  const fallback = variant === 'map' ? 'card' : variant;
  const published = refined[path]?.[variant]?.path || refined[path]?.[fallback]?.path || previews[path]?.[fallback]?.path || refined[path]?.full?.path || optimizedAssets[path]?.path || path;
  return published?.startsWith('/data/') ? `${import.meta.env.BASE_URL}${published.slice(1)}` : published;
}

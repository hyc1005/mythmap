import { assetUrl } from './asset-url';
import optimizedAssets from './optimized-assets.json';
import previews from './preview-assets.json';
import refined from './refined-artwork.json';

const decodedImages = new Map();
const spriteSheets = new Map();
const SPRITE_CACHE_BUDGET = 24 * 1024 * 1024;
const IMAGE_CACHE_BUDGET = 32 * 1024 * 1024;
export const IMAGE_TIMEOUT_MS = 15000;
export const PREFETCH_BUDGET = 1500000;

function trimImages() {
  let bytes = [...decodedImages.values()].reduce((sum, entry) => sum + entry.bytes, 0);
  for (const [key, entry] of decodedImages) {
    if (bytes <= IMAGE_CACHE_BUDGET) break;
    if (!entry.bytes) continue;
    decodedImages.delete(key);
    bytes -= entry.bytes;
  }
}

function spriteBytes(value, seen = new Set()) {
  if (!value || typeof value !== 'object' || seen.has(value)) return 0;
  seen.add(value);
  if (typeof value.getImage === 'function') return spriteBytes(value.getImage(1), seen);
  if (typeof value.getContext === 'function' || typeof value.decode === 'function') {
    return (value.naturalWidth || value.width || 0) * (value.naturalHeight || value.height || 0) * 4;
  }
  return Object.values(value).reduce((sum, item) => sum + spriteBytes(item, seen), 0);
}

function trimSprites() {
  let bytes = [...spriteSheets.values()].reduce((sum, entry) => sum + entry.bytes, 0);
  for (const [key, entry] of spriteSheets) {
    if (bytes <= SPRITE_CACHE_BUDGET) break;
    if (!entry.bytes) continue;
    spriteSheets.delete(key);
    bytes -= entry.bytes;
  }
}

export function loadImage(path, timeoutMs = IMAGE_TIMEOUT_MS) {
  const url = assetUrl(path);
  if (decodedImages.has(url)) {
    const cached = decodedImages.get(url);
    decodedImages.delete(url);
    decodedImages.set(url, cached);
    return cached.promise;
  }
  if (!decodedImages.has(url)) {
    const entry = { promise: null, bytes: 0 };
    entry.promise = (async () => {
      const image = new Image();
      image.src = url;
      let timer;
      try {
        await Promise.race([image.decode(), new Promise((_, reject) => {
          timer = setTimeout(() => { image.src = ''; reject(new Error(`Image load timed out: ${url}`)); }, timeoutMs);
        })]);
      } finally { clearTimeout(timer); }
      entry.bytes = (image.naturalWidth || image.width || 0) * (image.naturalHeight || image.height || 0) * 4;
      trimImages();
      return image;
    })().catch(error => {
      if (decodedImages.get(url) === entry) decodedImages.delete(url);
      throw error;
    });
    decodedImages.set(url, entry);
  }
  return decodedImages.get(url).promise;
}

export function cachedSprites(key, load) {
  if (spriteSheets.has(key)) {
    const entry = spriteSheets.get(key);
    spriteSheets.delete(key); spriteSheets.set(key, entry);
    return entry.promise;
  }
  const entry = { bytes: 0, promise: null };
  entry.promise = Promise.resolve().then(load).then(value => {
    if (spriteSheets.get(key) === entry) { entry.bytes = spriteBytes(value); trimSprites(); }
    return value;
  }).catch(error => {
    if (spriteSheets.get(key) === entry) spriteSheets.delete(key);
    throw error;
  });
  spriteSheets.set(key, entry);
  return entry.promise;
}

export function chapterPrefetchPaths(chapter, world, catalog) {
  const index = world.stages.findIndex(stage => stage.id === chapter);
  const next = world.stages[index + 1];
  if (!next) return [];
  const paths = new Set(catalog.events.filter(event => event.properties.stage_id === next.id)
    .flatMap(event => event.properties.artworks || [event.properties.artwork])
    .filter(Boolean).map(path => path.startsWith('/') ? path : `/data/atlas/myth-icons/${path}`));
  let bytes = 0;
  return [...paths].map(path => refined[path]?.preview || previews[path]?.preview || optimizedAssets[path]).filter(Boolean)
    .filter(asset => {
      const size = asset.bytes ?? asset.optimized_bytes;
      if (!Number.isFinite(size) || bytes + size > PREFETCH_BUDGET) return false;
      bytes += size;
      return true;
    }).map(asset => asset.path);
}

export function prefetchNextChapter(chapter, world, catalog) {
  const paths = chapterPrefetchPaths(chapter, world, catalog);
  let cancelled = false;
  const timer = window.setTimeout(() => {
    if (navigator.connection?.saveData || ['slow-2g', '2g', '3g'].includes(navigator.connection?.effectiveType)) return;
    const queue = [...paths];
    const work = async () => {
      while (queue.length && !cancelled) {
        const path = queue.shift();
        try {
          const response = await fetch(assetUrl(path), { cache: 'force-cache', keepalive: true });
          if (response.ok) await response.arrayBuffer();
        } catch { /* Prefetch failure leaves on-demand loading available. */ }
      }
    };
    void work(); void work();
  }, 1200);
  return () => { window.clearTimeout(timer); cancelled = true; };
}

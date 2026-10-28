import { readFile, readdir } from 'node:fs/promises';
import { join } from 'node:path';

export async function publishingFiles(publicDir, manifestPath) {
  const optimized = JSON.parse(await readFile(manifestPath, 'utf8'));
  const refined = JSON.parse(await readFile(new URL('../src/refined-artwork.json', import.meta.url), 'utf8'));
  const files = new Set(['favicon.png', 'fonts/shanhai-title.woff2', 'fonts/shanhai-title-beishan.woff2', 'fonts/atlas-northern-extb.woff2', 'fonts/atlas-northern-tan.woff2', 'fonts/shanhai-title-dongshan.woff2', 'fonts/atlas-eastern-rare.woff2', 'fonts/shanhai-rare.woff2', 'data/atlas/land.geojson', 'data/atlas/rivers.geojson']);
  const collect = value => {
    if (typeof value === 'string' && value.startsWith('/data/')) files.add((refined[value]?.full?.path || optimized[value]?.path || value).slice(1));
    else if (Array.isArray(value)) value.forEach(collect);
    else if (value && typeof value === 'object') {
      for (const [key, item] of Object.entries(value)) {
        if (typeof item === 'string' && ['artwork', 'actor_art'].includes(key) && !item.startsWith('/')) collect(`/data/atlas/myth-icons/${item}`);
        else if (key === 'artworks' && Array.isArray(item)) item.forEach(path => collect(path.startsWith('/') ? path : `/data/atlas/myth-icons/${path}`));
        else collect(item);
      }
    }
  };
  files.add('fonts/shanhai-title-zhongshan.woff2');
  files.add('fonts/shanhai-bestiary.woff2');
  files.add('fonts/atlas-central-rare.woff2');
  files.add('fonts/atlas-central-exth.woff2');
  for (const file of ['data/myth-world.json', 'data/atlas/catalog.json', 'data/atlas/story-animations.json', 'data/atlas/kuafu-journey.json']) {
    files.add(file);
    collect(JSON.parse(await readFile(join(publicDir, file), 'utf8')));
  }
  const previews = JSON.parse(await readFile(new URL('../src/preview-assets.json', import.meta.url), 'utf8'));
  for (const [original, variants] of Object.entries(previews)) collect(refined[original]?.full ? refined[original] : variants);
  collect(refined);
  files.add(optimized.bookplate.path.slice(1));
  for (const name of ['peak', 'ridge', 'sea-cloud']) collect(`/data/atlas/myth-icons/terrain/${name}.webp`);
  collect('/data/atlas/myth-icons/terrain/distant.png');
  collect('/data/atlas/myth-paper.webp');
  for (const name of ['pangu-cloud-layer', 'pangu-earth-layer', 'pangu-supporting-figure']) collect(`/data/atlas/myth-icons/scenes/${name}.webp`);
  for (const file of await readdir(join(publicDir, 'fonts'))) if (/LICENSE/i.test(file)) files.add(`fonts/${file}`);
  return files;
}

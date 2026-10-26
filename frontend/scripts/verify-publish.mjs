import assert from 'node:assert/strict';
import { access, readdir, readFile, stat } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { publishingFiles } from './publish-files.mjs';

const frontend = new URL('../', import.meta.url);
const manifest = JSON.parse(await readFile(new URL('src/optimized-assets.json', frontend), 'utf8'));
const originals = new Set(Object.keys(manifest).filter(path => path.startsWith('/data/')).map(path => path.slice(1)));
const included = await publishingFiles(fileURLToPath(new URL('public/', frontend)), new URL('src/optimized-assets.json', frontend));
let retainedBytes = 0, excludedBytes = 0, files = 0;
async function check(directory, prefix = '') {
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const filename = prefix + entry.name;
    if (entry.isDirectory()) await check(new URL(entry.name + '/', directory), filename + '/');
    else if (entry.isFile()) {
      const source = new URL(entry.name, directory);
      const published = new URL('dist/' + filename, frontend);
      if (!included.has(filename)) {
        await assert.rejects(access(published), { code: 'ENOENT' }, `${filename}: unused source stays out of publishing output`);
        excludedBytes += (await stat(source)).size;
      } else {
        const size = (await stat(source)).size;
        assert.equal((await stat(published)).size, size, `${filename}: publishing asset matches source`);
        retainedBytes += size; files++;
      }
    }
  }
}
await check(new URL('public/', frontend));
await access(new URL('dist/index.html', frontend));
await access(new URL('dist/fonts/shanhai-title.woff2', frontend));
await access(new URL('dist/fonts/atlas-northern-tan.woff2', frontend));
await access(new URL('dist/fonts/shanhai-title-dongshan.woff2', frontend));
await access(new URL('dist/fonts/atlas-eastern-rare.woff2', frontend));
await access(new URL('dist/fonts/shanhai-title-zhongshan.woff2', frontend));
await access(new URL('dist/fonts/atlas-central-rare.woff2', frontend));
await access(new URL('dist/fonts/atlas-central-exth.woff2', frontend));
await access(new URL('dist/fonts/noto-serif-sc-LICENSE.txt', frontend));
console.log(`PASS: ${files} public assets (${(retainedBytes / 1e6).toFixed(1)} MB); ${(excludedBytes / 1e6).toFixed(1)} MB duplicate originals excluded, all sources retained.`);

import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { readFile } from 'node:fs/promises';
import { join } from 'node:path';
import { publishingFiles } from './scripts/publish-files.mjs';

function publishAssets() {
  let publicDir;
  return {
    name: 'publish-optimized-assets',
    apply: 'build',
    configResolved(config) { publicDir = config.publicDir; },
    async generateBundle() {
      const files = await publishingFiles(publicDir, new URL('./src/optimized-assets.json', import.meta.url));
      for (const filename of files) this.emitFile({ type: 'asset', fileName: filename, source: await readFile(join(publicDir, filename)) });
    },
  };
}

export default defineConfig({
  plugins: [react(), publishAssets()],
  server: { host: '0.0.0.0', proxy: { '/api': 'http://127.0.0.1:8081', '/health': 'http://127.0.0.1:8081' } },
  build: { copyPublicDir: false, rollupOptions: { output: { manualChunks: { openlayers: ['ol'], react: ['react', 'react-dom', 'react-dom/client'] } } } },
});

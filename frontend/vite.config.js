import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: { host: '0.0.0.0', proxy: { '/api': 'http://127.0.0.1:8081', '/health': 'http://127.0.0.1:8081' } },
  build: { rollupOptions: { output: { manualChunks: { openlayers: ['ol'] } } } },
});

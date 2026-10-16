import WMTS from 'ol/source/WMTS';
import WMTSTileGrid from 'ol/tilegrid/WMTS';
import TileState from 'ol/TileState';

export function createTiandituSource(layer, key, onError, signal) {
  const levels = Array.from({ length: 14 }, (_, index) => index + 1);
  return new WMTS({
    urls: Array.from({ length: 8 }, (_, index) => `https://t${index}.tianditu.gov.cn/${layer}_w/wmts?tk=${encodeURIComponent(key)}`),
    layer, matrixSet: 'w', style: 'default', format: 'tiles', projection: 'EPSG:3857', wrapX: true,
    attributions: '<a href="https://www.tianditu.gov.cn/" target="_blank" rel="noopener noreferrer">天地图 · 国家基础地理信息中心</a>',
    tileGrid: new WMTSTileGrid({ origin: [-20037508.342789244, 20037508.342789244],
      resolutions: levels.map(level => 156543.03392804097 / 2 ** level), matrixIds: levels.map(String), tileSize: 256 }),
    tileLoadFunction: async (tile, url) => {
      try {
        const response = await fetch(url, { signal });
        if (!response.ok || !response.headers.get('content-type')?.startsWith('image/')) {
          const body = await response.text();
          const auth = [401, 403].includes(response.status) || /30100\d|30101\d|非法key|无效key|授权|鉴权|白名单/i.test(body);
          let code;
          try { code = String(JSON.parse(body).code); } catch {}
          onError(auth ? 'auth' : layer, code);
          tile.setState(TileState.ERROR); return;
        }
        const objectUrl = URL.createObjectURL(await response.blob());
        try {
          const image = new Image(); image.src = objectUrl;
          await image.decode();
          if (!signal.aborted) tile.setImage(image);
        } finally { URL.revokeObjectURL(objectUrl); }
      } catch (error) {
        if (signal.aborted) return;
        onError(layer); tile.setState(TileState.ERROR);
      }
    },
  });
}

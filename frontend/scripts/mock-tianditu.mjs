export async function mockTianditu(context) {
  const state = { fail: false, auth: false, terrainFail: false, labelsFail: false, requests: 0, osmRequests: 0, layers: { ter: 0, cta: 0 }, hold: null };
  await context.route('https://tile.openstreetmap.org/**', route => { state.osmRequests++; return route.abort(); });
  await context.route(/^https:\/\/t[0-7]\.tianditu\.gov\.cn\/(ter|cta)_w\/wmts/, async route => {
    state.requests++;
    const layer = new URL(route.request().url()).pathname.split('/')[1].slice(0, 3);
    state.layers[layer]++;
    if (state.hold) await state.hold;
    const headers = { 'Access-Control-Allow-Origin': '*' };
    if (state.auth) return route.fulfill({ status: 403, headers, contentType: 'application/json', body: JSON.stringify({ code: state.auth === true ? 301001 : Number(state.auth), msg: 'invalid key or application type' }) });
    if (state.fail || layer === 'ter' && state.terrainFail || layer === 'cta' && state.labelsFail) return route.fulfill({ status: 503, headers, body: 'service unavailable' });
    return route.fulfill({ contentType: 'image/svg+xml', headers: { 'Access-Control-Allow-Origin': '*' },
      body: `<svg xmlns="http://www.w3.org/2000/svg" width="256" height="256">${layer === 'ter' ? '<rect width="256" height="256" fill="#dfe6dc"/><path d="M0 110L256 150M120 0L160 256" stroke="#c3cfbf" fill="none"/>' : '<text x="12" y="28" fill="#53634e" font-size="12">TEST LABEL</text>'}</svg>` });
  });
  return state;
}

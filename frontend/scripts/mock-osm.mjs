export async function mockOsm(context) {
  const state = { fail: false, requests: 0, hold: null };
  await context.route('https://tile.openstreetmap.org/**', async route => {
    state.requests++;
    if (state.hold) await state.hold;
    if (state.fail) return route.abort();
    return route.fulfill({ contentType: 'image/svg+xml', headers: { 'Access-Control-Allow-Origin': '*' },
      body: '<svg xmlns="http://www.w3.org/2000/svg" width="256" height="256"><rect width="256" height="256" fill="#dfe6dc"/><path d="M0 110L256 150M120 0L160 256" stroke="#c3cfbf" fill="none"/><text x="12" y="28" fill="#53634e" font-size="12">TEST TILE</text></svg>' });
  });
  return state;
}

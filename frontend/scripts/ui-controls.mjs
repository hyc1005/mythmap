async function setDetails(details, open) {
  await details.waitFor({ state: 'visible' });
  if (await details.evaluate(node => node.open) !== open) await details.locator(':scope > summary').click();
}

export async function openMapTools(page) { await setDetails(page.locator('.map-tools'), true); }
export async function closeMapTools(page) { await setDetails(page.locator('.map-tools'), false); }
export async function openBestiaryFilters(page) {
  const toggle = page.locator('.bestiary-extra-toggle:visible');
  if (await toggle.count() && await toggle.getAttribute('aria-expanded') === 'false') await toggle.click();
}
export async function openSourceLibrary(page) {
  const full = page.locator('.is-map-fullscreen');
  const scope = await full.count() ? full : page;
  const entries = scope.locator('.map-entry-list');
  if (await entries.count()) await setDetails(entries, true);
  await setDetails(scope.locator('.chapter-library:visible'), true);
}
export async function clickPlaybackControl(scope, name) {
  const button = scope.getByRole('button', { name, exact: true });
  const menu = scope.locator('.journey-more:visible');
  const opened = !await button.isVisible();
  if (opened) await setDetails(menu, true);
  await button.click();
  if (opened && await menu.count()) await setDetails(menu, false);
}

export async function waitForPrologueControls(page) {
  await page.locator('.pangu-player-controls').waitFor();
  await page.locator('html').evaluate(async () => {
    await Promise.allSettled([
      ...[...document.fonts].filter(font => font.status === 'loading').map(font => font.loaded),
      ...[...document.images].filter(image => image.loading !== 'lazy' && image.getClientRects().length).map(image => image.decode()),
    ]);
    await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
  }, undefined, { timeout: 30000 });
}

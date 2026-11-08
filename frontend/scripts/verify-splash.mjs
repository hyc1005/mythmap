import assert from 'node:assert/strict';
import { chromium, firefox, webkit } from 'playwright';

const base = process.env.ATLAS_URL;
if (!base) throw new Error('Run through with-preview.mjs');
const splash = page => page.locator('#splash-dialog');

for (const name of (process.env.ATLAS_BROWSERS || 'chromium,webkit').split(',')) {
  const browser = await ({ chromium, firefox, webkit }[name]).launch();
  try {
    const errors = [];
    const monitor = page => page.on('pageerror', error => errors.push(error.message));
    const openSplash = async (context, path = '') => {
      const page = await context.newPage();
      monitor(page);
      await page.goto(`${base}${path}`);
      await splash(page).waitFor({ state: 'visible', timeout: 15000 });
      assert.equal(await page.evaluate(() => document.documentElement.dataset.splash), 'active', 'Splash marks the document while it is open');
      return page;
    };
    const dismissGuide = async page => {
      if (await page.locator('.onboarding-skip').count()) await page.locator('.onboarding-skip').click();
    };

    const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });

    // 1. First visit: any click in the window ends the opening.
    const page = await openSplash(context);
    await page.mouse.click(640, 300);
    await splash(page).waitFor({ state: 'detached', timeout: 15000 });
    assert.equal(await page.evaluate(() => document.documentElement.dataset.splash), 'done', 'Click-anywhere marks the splash done');
    assert.ok(await page.evaluate(() => localStorage.getItem('shanhai-splash:v12:seen') === '1'), 'Click-anywhere records the seen marker');
    await page.locator('.brand-replay').waitFor();
    await dismissGuide(page);

    // 2. A corner click works the same as a centre click.
    await page.evaluate(() => { window.__splashMarker = 'kept'; document.body.dataset.splashMarker = 'kept'; });
    await page.locator('.brand-replay').click();
    await splash(page).waitFor({ state: 'visible', timeout: 15000 });
    await page.mouse.click(8, 8);
    await splash(page).waitFor({ state: 'detached', timeout: 15000 });
    assert.equal(await page.evaluate(() => window.__splashMarker), 'kept', 'Replay click does not remount the app');
    assert.equal(await page.locator('body').getAttribute('data-splash-marker'), 'kept');
    await page.close();

    // 3. The enter button and Escape keep working.
    const buttonPage = await openSplash(context, '?splash=1');
    await buttonPage.locator('#splash-enter').click();
    await splash(buttonPage).waitFor({ state: 'detached', timeout: 15000 });
    assert.equal(await buttonPage.evaluate(() => document.documentElement.dataset.splash), 'done', 'Enter button still closes the splash');
    await buttonPage.close();

    const escapePage = await openSplash(context, '?splash=1');
    await escapePage.keyboard.press('Escape');
    await splash(escapePage).waitFor({ state: 'detached', timeout: 15000 });
    assert.equal(await escapePage.evaluate(() => document.documentElement.dataset.splash), 'done', 'Escape still closes the splash');
    await escapePage.close();

    // 4. Explicit skip, deep links and reduced motion never open the dialog.
    for (const [label, path] of [['?splash=0', '?splash=0'], ['deep link', '?chapter=01&lang=zh']]) {
      const skipPage = await context.newPage();
      monitor(skipPage);
      await skipPage.goto(`${base}${path}`);
      await skipPage.locator('.brand-replay').waitFor();
      await skipPage.waitForTimeout(400);
      assert.equal(await splash(skipPage).count(), 0, `${label} skips the splash`);
      assert.equal(await skipPage.evaluate(() => document.documentElement.dataset.splash), 'done');
      await skipPage.close();
    }

    const reduced = await browser.newContext({ viewport: { width: 1280, height: 800 }, reducedMotion: 'reduce' });
    const reducedPage = await reduced.newPage();
    monitor(reducedPage);
    await reducedPage.goto(base);
    await reducedPage.locator('.brand-replay').waitFor();
    await reducedPage.waitForTimeout(400);
    assert.equal(await splash(reducedPage).count(), 0, 'Reduced motion skips the splash');
    await reduced.close();

    // 5. The bookplate is the only entry into the opening film.
    const filmPage = await context.newPage();
    monitor(filmPage);
    await filmPage.goto(`${base}?splash=0`);
    const bookplate = filmPage.locator('.bookplate-link');
    await bookplate.scrollIntoViewIfNeeded();
    const href = await bookplate.getAttribute('href');
    assert.ok(href && href.endsWith('opening-film.html'), 'The bookplate links to the opening film');
    await Promise.all([filmPage.waitForURL(/opening-film\.html$/, { timeout: 20000 }), bookplate.click()]);
    assert.equal(await filmPage.title(), '山海寻踪 · 开篇影像', 'The film keeps its own title');
    assert.equal(await filmPage.locator('a.back-home').getAttribute('href'), './', 'The film links back to the atlas');
    await filmPage.locator('#skipMin').click();
    await filmPage.locator('.bookplate-link').waitFor({ timeout: 20000 });
    assert.equal(await filmPage.locator('a.back-home').count(), 0, 'Skip returns to the atlas');
    await filmPage.close();

    await context.close();
    assert.deepEqual(errors, []);
    console.log(`PASS ${name}: click-anywhere skip, enter button, Escape, explicit skip, deep links, reduced motion and replay without remount`);
  } finally {
    await browser.close();
  }
}

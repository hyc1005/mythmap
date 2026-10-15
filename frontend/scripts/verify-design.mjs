import assert from 'node:assert/strict';
import { mkdir, readFile } from 'node:fs/promises';
import { chromium, firefox, webkit } from 'playwright';

const base = process.env.ATLAS_URL;
if (!base) throw new Error('Run through with-preview.mjs');
const output = new URL('../../output/qa/', import.meta.url);
await mkdir(output, { recursive: true });
const catalog = JSON.parse(await readFile(new URL('../public/data/atlas/catalog.json', import.meta.url), 'utf8'));
const chapterMarkers = catalog.events.filter(item => item.properties.stage_id === '03' && item.properties.map_visible).map(item => item.properties.layout_hint);
for (const name of (process.env.ATLAS_BROWSERS || 'chromium,webkit').split(',')) {
  const browser = await ({ chromium, firefox, webkit }[name]).launch();
  try {
    const page = await browser.newPage({ reducedMotion: 'reduce' });
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    for (const [width, height] of [[1440, 1000], [1024, 768], [768, 1024], [390, 844], [320, 700], [844, 390]]) {
      await page.setViewportSize({ width, height });
      for (const lang of ['zh', 'en']) {
        await page.goto(`${base}?chapter=03&lang=${lang}#world`);
        await page.locator('.myth-map-canvas canvas').first().waitFor();
        await page.evaluate(() => document.fonts.ready);
        await page.waitForTimeout(300);
        const dimensions = await page.evaluate(() => {
          const map = document.querySelector('.map-surface').getBoundingClientRect();
          const toolbar = document.querySelector('.explore-toolbar').getBoundingClientRect();
          const playback = document.querySelector('.explore-playback').getBoundingClientRect();
          return { map: { top: map.top, bottom: map.bottom, height: map.height }, toolbar: { bottom: toolbar.bottom }, playback: { top: playback.top }, overflow: document.documentElement.scrollWidth > innerWidth, columns: getComputedStyle(document.querySelector('.beast-grid')).gridTemplateColumns.split(' ').length };
        });
        assert.equal(await page.locator('[role=slider], .chapter-slider').count(), 0, 'Chapter slider removed');
        if (width > 768) assert.equal(await page.locator('.timeline-current button').count(), 2, 'Chapter navigation has only previous/next');
        assert.equal(dimensions.overflow, false, `${name} ${width} ${lang} body overflow`);
        assert.ok(dimensions.toolbar.bottom <= dimensions.map.top + 1, 'Toolbar outside map');
        assert.ok(dimensions.playback.top >= dimensions.map.bottom - 1, 'Playback outside map');
        if (width <= 768 && height > 480) assert.ok(dimensions.map.height >= height / 2, `Mobile map height ${dimensions.map.height}`);
        assert.equal(dimensions.columns, width <= 768 ? 2 : width <= 1100 ? 3 : 4);
        const mapView = JSON.parse(await page.locator('.myth-map-canvas').getAttribute('data-view'));
        for (const [x, y] of chapterMarkers) {
          const pixel = [mapView.size[0] / 2 + (x - mapView.center[0]) / mapView.resolution, mapView.size[1] / 2 - (y - mapView.center[1]) / mapView.resolution];
          assert.ok(pixel[0] >= 28 && pixel[0] <= mapView.size[0] - 28 && pixel[1] >= 28 && pixel[1] <= mapView.size[1] - 28, `${width}: chapter marker has edge space`);
        }
        const contrast = await page.evaluate(() => {
          const luminance = color => {
            const channels = color.match(/[\d.]+/g).slice(0, 3).map(Number).map(value => {
              const channel = value / 255;
              return channel <= .04045 ? channel / 12.92 : ((channel + .055) / 1.055) ** 2.4;
            });
            return channels[0] * .2126 + channels[1] * .7152 + channels[2] * .0722;
          };
          const background = luminance(getComputedStyle(document.querySelector('.myth-app')).backgroundColor);
          return ['.chapter-rail>p', '.beast-card>p', '.beast-card>small', '.reading-notes p', '.mobile-explore-nav button'].map(selector => {
            const node = document.querySelector(selector);
            const foreground = luminance(getComputedStyle(node).color);
            return { selector, ratio: (Math.max(background, foreground) + .05) / (Math.min(background, foreground) + .05) };
          });
        });
        for (const item of contrast) assert.ok(item.ratio >= 4.5, `${item.selector}: contrast ${item.ratio}`);
        if (width <= 768) {
          assert.ok(await page.locator('.begin-journey, .mobile-explore-nav button, .explore-toolbar button, .explore-toolbar select').evaluateAll(nodes => nodes.filter(node => node.checkVisibility()).every(node => {
            const box = node.getBoundingClientRect(); return box.width >= 44 && box.height >= 44;
          })), 'Primary mobile targets are at least 44px');
          assert.equal(await page.locator('.mobile-explore-nav button').count(), 2, 'One chapter and one entry panel');
          const trigger = page.locator('.mobile-explore-nav button').first();
          await trigger.click();
          const sheet = page.locator('.explore-sheet');
          await sheet.waitFor();
          assert.equal(await page.locator('#root').evaluate(node => node.inert), true);
          assert.equal(await page.evaluate(() => document.body.style.overflow), 'hidden');
          await page.keyboard.press('Shift+Tab');
          assert.ok(await sheet.evaluate(node => node.contains(document.activeElement)), 'Focus trapped');
          await page.keyboard.press('Escape');
          assert.equal(await page.locator('#root').evaluate(node => node.inert), false);
          assert.ok(await trigger.evaluate(node => node === document.activeElement), 'Focus restored');
          await trigger.click();
          await sheet.locator('.timeline-steps button').nth(4).click();
          assert.equal(await sheet.count(), 0);
          assert.match(page.url(), /chapter=04/);
          await page.locator('.mobile-explore-nav button').nth(1).click();
          await page.locator('.explore-sheet .story-entry').first().click();
          await page.locator('.detail-drawer').waitFor();
          assert.equal(await page.locator('#root').evaluate(node => node.inert), true, 'Source modal remains isolated after sheet');
          await page.locator('.drawer-close').click();
          assert.equal(await page.locator('#root').evaluate(node => node.inert), false);
        }
        if (name === 'chromium' && lang === 'zh') {
          await page.goto(`${base}?chapter=03&lang=zh#world`);
          await page.waitForTimeout(500);
          await page.screenshot({ path: new URL(`design-${width}x${height}.png`, output).pathname.replace(/^\/([A-Za-z]:)/, '$1'), fullPage: true });
        }
        console.log(`PASS ${name} ${width}x${height} ${lang}: layout, panels, sources`);
      }
    }
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto(`${base}?chapter=03&lang=zh#world`);
    await page.getByRole('combobox', { name: '选择地图故事动画' }).selectOption('03-05');
    await page.locator('.kuafu-journey').waitFor();
    assert.ok(await page.locator('.kuafu-journey').evaluate(node => Boolean(node.closest('.explore-playback'))));
    await page.getByRole('button', { name: '地图全屏', exact: true }).click();
    await page.locator('.is-map-fullscreen').waitFor();
    assert.ok(await page.locator('.kuafu-journey').evaluate(node => Boolean(node.closest('.fullscreen-dock'))));
    await page.locator('.map-entry-list > summary').click();
    const fullEntries = page.locator('.map-entry-list .chapter-entries');
    await fullEntries.locator('[data-entry-id="03-04"]').click();
    await page.locator('.detail-drawer').waitFor();
    await page.locator('.drawer-close').click();
    assert.equal(await page.locator('.is-map-fullscreen').count(), 1, 'Entry sources preserve fullscreen');
    const entryIds = await fullEntries.locator('[data-entry-id]').evaluateAll(nodes => nodes.map(node => node.dataset.entryId));
    assert.equal(new Set(entryIds).size, entryIds.length, 'Unified entries contain no duplicate stories');
    await page.locator('.map-entry-list > summary').click();
    await page.getByRole('button', { name: '退出地图全屏', exact: true }).click();
    await page.locator('.explore-playback .kuafu-journey').waitFor();
    await page.waitForFunction(() => {
      const canvas = document.querySelector('.myth-map-canvas');
      const view = JSON.parse(canvas.dataset.view), box = canvas.getBoundingClientRect();
      return Math.abs(view.size[0] - box.width) < 1 && Math.abs(view.size[1] - box.height) < 1;
    });
    const elapsed = await page.locator('.kuafu-journey').getAttribute('data-elapsed');
    const view = await page.locator('.myth-map-canvas').getAttribute('data-view');
    await page.locator('.mobile-explore-nav button').nth(1).click();
    await page.keyboard.press('Escape');
    assert.equal(await page.locator('.kuafu-journey').getAttribute('data-elapsed'), elapsed, 'Panel preserves manual progress');
    assert.equal(await page.locator('.myth-map-canvas').getAttribute('data-view'), view, 'Panel preserves camera');
    await page.setViewportSize({ width: 1440, height: 1000 });
    await page.goto(`${base}?chapter=03&lang=zh#world`);
    await page.locator('.timeline-steps [aria-current="step"]').press('Home');
    assert.equal(await page.locator('.world-layout').getAttribute('data-chapter'), '00');
    assert.ok(await page.locator('.timeline-current button').first().isDisabled());
    await page.locator('.timeline-steps [aria-current="step"]').press('End');
    assert.equal(await page.locator('.world-layout').getAttribute('data-chapter'), '07');
    assert.ok(await page.locator('.timeline-current button').last().isDisabled());
    await page.locator('.timeline-steps button').nth(3).click();
    await page.locator('.timeline-steps [aria-current="step"]').press('ArrowRight');
    assert.equal(await page.locator('.world-layout').getAttribute('data-chapter'), '04');
    await page.locator('.timeline-current button').first().click();
    assert.equal(await page.locator('.world-layout').getAttribute('data-chapter'), '03');
    assert.equal(await page.locator('.world-layout').getAttribute('data-timeline-playing'), 'false', 'Manual navigation leaves guided tour');
    await page.locator('.bestiary-toggle').click();
    for (const id of ['beast-wenyaoyu', 'beast-bifang', 'beast-xiangliu', 'beast-jiuweihu', 'beast-shengsheng', 'beast-bo']) {
      const card = page.locator(`[data-beast-id="${id}"]`);
      await card.scrollIntoViewIfNeeded();
      await page.waitForFunction(id => {
        const image = document.querySelector(`[data-beast-id="${id}"] img`);
        return image?.complete && image.naturalWidth > 0;
      }, id);
      await card.locator('img').evaluate(image => image.decode());
      assert.ok(await card.locator('img').evaluate(image => {
        const bounds = image.getBoundingClientRect(), art = image.closest('.beast-art').getBoundingClientRect();
        return bounds.left >= art.left + 10 && bounds.right <= art.right - 10 && bounds.top >= art.top + 10 && bounds.bottom <= art.bottom - 10 && getComputedStyle(image).objectFit === 'contain';
      }), `${id}: illustration has safe margins`);
      if (name === 'chromium') await card.screenshot({ path: new URL(`design-card-${id}.png`, output).pathname.replace(/^\/([A-Za-z]:)/, '$1') });
    }
    await page.locator('.map-fit').filter({ hasText: '存为本章 PNG' }).scrollIntoViewIfNeeded();
    await page.evaluate(() => {
      const original = HTMLCanvasElement.prototype.toDataURL;
      HTMLCanvasElement.prototype.toDataURL = function (...args) { const result = original.apply(this, args); window.reviewExport = result; return result; };
    });
    const download = page.waitForEvent('download');
    await page.getByRole('button', { name: '存为本章 PNG', exact: true }).click();
    await download;
    assert.ok(await page.evaluate(async () => {
      const image = new Image(); image.src = window.reviewExport; await image.decode();
      const canvas = document.createElement('canvas'); canvas.width = image.width; canvas.height = image.height;
      const context = canvas.getContext('2d'); context.drawImage(image, 0, 0);
      return [[1, 1], [image.width - 2, 1], [1, image.height - 2]].every(([x, y]) => context.getImageData(x, y, 1, 1).data[3] === 255);
    }), 'Reduced paper opacity retains opaque paper in PNG');
    assert.deepEqual(errors, []);
    console.log(`PASS ${name}: shared playback, fullscreen, camera, six art samples and PNG paper`);
  } finally { await browser.close(); }
}

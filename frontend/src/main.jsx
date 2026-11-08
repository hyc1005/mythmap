const query = new URLSearchParams(location.search);
const seenKey = 'shanhai-splash:v12:seen';
const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
let seen = false;
try { seen = localStorage.getItem(seenKey) === '1'; } catch {}
const deepLink = Boolean(location.hash || [...query.keys()].some(key => !['splash', 'nosplash'].includes(key)));
const shouldPlay = query.get('splash') !== '0' && !query.has('nosplash') && !reducedMotion
  && (query.get('splash') === '1' || (!seen && !deepLink && !navigator.connection?.saveData));
const dialog = document.getElementById('splash-dialog');
const stage = document.getElementById('splash-stage');
const placeholder = document.getElementById('splash-placeholder');
const enter = document.getElementById('splash-enter');
let engine, ended = false, appMounted = false, exiting = false, timer, returnFocus;

function openSplash() {
  ended = false;
  exiting = false;
  returnFocus = document.activeElement;
  placeholder.hidden = true;
  enter.disabled = false;
  enter.textContent = '进入网站';
  enter.onclick = finish;
  dialog.classList.remove('splash-leaving');
  document.body.append(dialog);
  document.documentElement.dataset.splash = 'active';
  document.documentElement.classList.add('splash-lock');
  window.dispatchEvent(new Event('splash:start'));
  dialog.showModal();
  enter.focus();
  timer = setTimeout(finish, 25000);
}

async function playSplash(modulePromise = import('./splash').catch(() => null)) {
  const splash = await modulePromise;
  if (exiting || ended) return;
  if (!splash) { finish(); return; }
  try {
    engine = splash.mountSplash(stage, finish);
    engine.play();
  } catch (error) {
    console.error('开屏初始化失败', error);
    finish();
  }
}

function closeSplash() {
  if (ended) return;
  ended = true;
  dialog.classList.add('splash-leaving');
  setTimeout(() => {
    engine?.destroy();
    engine = null;
    dialog.close();
    dialog.remove();
    document.documentElement.classList.remove('splash-lock');
    document.documentElement.dataset.splash = 'done';
    const focusTarget = returnFocus?.isConnected && returnFocus !== document.body
      ? returnFocus : document.querySelector('.brand-replay');
    focusTarget?.focus({ preventScroll: true });
    window.dispatchEvent(new Event('splash:done'));
  }, reducedMotion ? 0 : 650);
}

function finish() {
  if (ended || exiting) return;
  exiting = true;
  clearTimeout(timer);
  engine?.pause();
  try { localStorage.setItem(seenKey, '1'); } catch {}
  if (!appMounted) {
    placeholder.hidden = false;
    placeholder.textContent = '正在展开山海…';
    enter.disabled = true;
    enter.textContent = '正在进入';
    return;
  }
  closeSplash();
}

function showAppError() {
  clearTimeout(timer);
  engine?.destroy();
  placeholder.hidden = false;
  placeholder.textContent = '山海暂未展开，请重试';
  enter.disabled = false;
  enter.textContent = '重新加载';
  enter.onclick = () => location.reload();
}

async function boot() {
  if (shouldPlay) {
    openSplash();
  } else {
    document.documentElement.dataset.splash = 'done';
    dialog.remove();
  }
  const splashModule = shouldPlay ? import('./splash').catch(() => null) : null;
  try {
    const { mountApp } = await import('./app-entry');
    mountApp();
    await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
    appMounted = true;
  } catch (error) {
    console.error('主站加载失败', error);
    if (!dialog.isConnected) document.body.append(dialog);
    if (!dialog.open) dialog.showModal();
    showAppError();
    return;
  }
  if (!shouldPlay) return;
  if (exiting) { closeSplash(); return; }
  await playSplash(splashModule);
}

dialog.addEventListener('cancel', event => { event.preventDefault(); finish(); });
dialog.addEventListener('click', () => { if (dialog.open) finish(); });
window.addEventListener('splash:replay', () => {
  if (!appMounted || dialog.open) return;
  openSplash();
  playSplash();
});

boot();

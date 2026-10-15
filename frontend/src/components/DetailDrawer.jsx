import { useEffect, useMemo, useRef } from 'react';
import { useLocale, localize } from '../i18n';
import rawCatalog from '../../public/data/atlas/catalog.json';
import { iconFor } from '../artwork';
import ArtworkImage from './ArtworkImage';

function checkpoints(node) {
  const top = node.getBoundingClientRect().top;
  return [{ anchor: 'start', top: 0 }, ...[...node.querySelectorAll('[data-reading-anchor]')].map(element => ({ anchor: element.dataset.readingAnchor, top: element.getBoundingClientRect().top - top + node.scrollTop }))];
}

function capturePosition(node) {
  const points = checkpoints(node);
  const index = points.findLastIndex(point => point.top <= node.scrollTop + 1);
  const current = points[Math.max(0, index)], end = points[index + 1]?.top ?? node.scrollHeight;
  return { anchor: current.anchor, fraction: Math.max(0, Math.min(1, (node.scrollTop - current.top) / Math.max(1, end - current.top))), originalOpen: Boolean(node.querySelector('.original-text')?.open) };
}

function applyPosition(node, position) {
  const points = checkpoints(node);
  const anchor = position.anchor === 'original' && !node.querySelector('.original-text') ? 'quote' : position.anchor;
  const index = Math.max(0, points.findIndex(point => point.anchor === anchor));
  const current = points[index], end = points[index + 1]?.top ?? node.scrollHeight;
  node.scrollTo({ top: current.top + position.fraction * Math.max(1, end - current.top), behavior: 'instant' });
}

export default function DetailDrawer({ selected, onClose, onOpen, restoreReading, onSaveReading, readingChapter, resumeSaveFailed, relatedChapter, canLocate, onNavigate, onShare, shareStatus, reading, navigation }) {
  const { t, locale } = useLocale();
  const catalog = useMemo(() => localize(rawCatalog, locale), [locale]);
  const closeButton = useRef(null);
  const drawer = useRef(null);
  const heading = useRef(null);
  const previousButton = useRef(null);
  const nextButton = useRef(null);
  const pendingFocus = useRef(null);
  const lastEntry = useRef(null);
  const positionRecord = useRef(null);
  const sources = (selected.raw?.properties.source_ids || []).map(id => catalog.sources.find(source => source.id === id)).filter(Boolean);
  const links = [...new Map([
    ...(selected.url ? [{ url: selected.url, title: selected.source }] : []),
    ...sources.filter(source => source.url),
  ].map(source => [source.url, source])).values()];
  useEffect(() => {
    const node = drawer.current.closest('.detail-scrim');
    const previous = [document.documentElement.style.overflow, document.body.style.overflow];
    document.documentElement.style.overflow = 'hidden';
    document.body.style.overflow = 'hidden';
    const background = [];
    for (let current = node; current?.parentElement; current = current.parentElement) {
      for (const sibling of current.parentElement.children) {
        if (sibling !== current && !sibling.contains(node)) {
          background.push([sibling, sibling.inert]);
          sibling.inert = true;
        }
      }
    }
    return () => {
      document.documentElement.style.overflow = previous[0];
      document.body.style.overflow = previous[1];
      background.forEach(([element, inert]) => { element.inert = inert; });
    };
  }, []);
  useEffect(() => {
    const node = drawer.current;
    const localPosition = lastEntry.current === selected.id && positionRecord.current?.id === selected.id ? positionRecord.current.position : null;
    let requested = localPosition || (restoreReading?.id === selected.id ? restoreReading.position : null);
    lastEntry.current = selected.id;
    let restoring = Boolean(requested), cancelled = false, timer;
    node.dataset.readingRestoring = String(restoring);
    node.scrollTo({ top: 0, behavior: 'instant' });
    const button = pendingFocus.current === 'previous' ? previousButton.current : pendingFocus.current === 'next' ? nextButton.current : closeButton.current;
    (button && !button.disabled ? button : heading.current)?.focus({ preventScroll: true });
    pendingFocus.current = null;
    const snapshot = () => {
      if (restoring) return;
      positionRecord.current = { id: selected.id, chapter: readingChapter, position: capturePosition(node) };
    };
    const save = () => {
      window.clearTimeout(timer);
      if (restoring) return;
      snapshot(); onSaveReading(positionRecord.current);
    };
    const scroll = () => {
      if (restoring) return;
      snapshot(); window.clearTimeout(timer);
      timer = window.setTimeout(() => onSaveReading(positionRecord.current), 200);
    };
    const cancelRestore = () => {
      if (!restoring) return;
      requested = null; restoring = false; node.dataset.readingRestoring = 'false'; save();
    };
    const key = event => { if (['PageDown', 'PageUp', 'Home', 'End', 'ArrowDown', 'ArrowUp', ' '].includes(event.key)) cancelRestore(); };
    const visibility = () => { if (document.hidden) save(); };
    if (!restoring) save();
    else if (node.querySelector('.original-text')) node.querySelector('.original-text').open = requested.originalOpen;
    node.addEventListener('scroll', scroll, { passive: true });
    node.addEventListener('toggle', scroll, true);
    node.addEventListener('wheel', cancelRestore, { passive: true });
    node.addEventListener('touchmove', cancelRestore, { passive: true });
    node.addEventListener('keydown', key);
    window.addEventListener('pagehide', save);
    document.addEventListener('visibilitychange', visibility);
    const ready = async () => {
      await Promise.allSettled([document.fonts.ready, ...[...node.querySelectorAll('img')].map(img => img.decode())]);
      await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
      if (cancelled) return;
      if (requested) applyPosition(node, requested);
      restoring = false; node.dataset.readingRestoring = 'false'; save();
    };
    ready();
    return () => {
      cancelled = true; window.clearTimeout(timer);
      if (!restoring && positionRecord.current?.id === selected.id) onSaveReading(positionRecord.current);
      node.removeEventListener('scroll', scroll); node.removeEventListener('toggle', scroll, true);
      node.removeEventListener('wheel', cancelRestore); node.removeEventListener('touchmove', cancelRestore); node.removeEventListener('keydown', key);
      window.removeEventListener('pagehide', save); document.removeEventListener('visibilitychange', visibility);
    };
  }, [selected.id, locale]);
  const step = direction => {
    const item = navigation[direction];
    if (!item) return;
    pendingFocus.current = direction;
    onOpen(item.id);
  };
  const keepFocusInDrawer = event => {
    if (event.key !== 'Tab') return;
    const controls = [...drawer.current.querySelectorAll('button:not(:disabled), a[href], summary, input:not(:disabled), select:not(:disabled), textarea:not(:disabled), [tabindex="0"]')].filter(element => element.checkVisibility());
    const first = controls[0], last = controls.at(-1);
    if (event.shiftKey && (document.activeElement === first || document.activeElement === drawer.current)) {
      event.preventDefault(); last?.focus({ preventScroll: true });
    } else if (!event.shiftKey && (document.activeElement === last || document.activeElement === drawer.current)) {
      event.preventDefault(); first?.focus({ preventScroll: true });
    }
  };
  return <div className="detail-scrim" onClick={onClose}>
    <aside ref={drawer} className="detail-drawer" data-entry-id={selected.id} role="dialog" aria-modal="true" aria-label={selected.name} tabIndex={-1} onKeyDown={keepFocusInDrawer} onClick={event => event.stopPropagation()}>
      <div className="drawer-actions">
        <button ref={closeButton} className="drawer-close" onClick={onClose} aria-label={t("关闭")}>×</button></div>
      <span className="intro-overline">{selected.region || selected.source}</span>
      <h2 ref={heading} tabIndex={-1} data-reading-anchor="title">{selected.name}</h2>
      {navigation.total > 1 && <nav className="detail-entry-nav" aria-label={t('条目切换')}>
        <button ref={previousButton} type="button" disabled={!navigation.previous} onClick={() => step('previous')} aria-label={t('上一条')}><span>← {t('上一条')}</span><small>{navigation.previous?.name || t('已是第一条')}</small></button>
        <span className="detail-entry-position" aria-live="polite">{navigation.index + 1} / {navigation.total}</span>
        <button ref={nextButton} type="button" disabled={!navigation.next} onClick={() => step('next')} aria-label={t('下一条')}><span>{t('下一条')} →</span><small>{navigation.next?.name || t('已是最后一条')}</small></button>
      </nav>}
      <div className="detail-reading-actions" role="group" aria-label={t('阅读标记')}>
        <button type="button" aria-pressed={reading.read.includes(selected.id)} onClick={() => reading.toggleRead(selected.id)}>{t(reading.read.includes(selected.id) ? '已读 · 撤销' : '标为已读')}</button>
        <button type="button" aria-pressed={reading.favorites.includes(selected.id)} onClick={() => reading.toggleFavorite(selected.id)}>{t(reading.favorites.includes(selected.id) ? '已收藏 · 取消' : '收藏条目')}</button>
      </div>
      <p className="reading-storage-note" role="status">{t(reading.saveFailed ? '浏览器暂不能保存，标记仅在当前页面有效。' : '标记保存在此浏览器中。')}</p>
      {resumeSaveFailed && <p className="reading-storage-note" role="status">{t('阅读位置暂不能保存，关闭页面后将失效。')}</p>}
      {iconFor(selected) && <ArtworkImage key={selected.id} className="drawer-art" src={iconFor(selected)} alt={t(`${selected.name}版画插画`)} />}
      <div className="detail-exploration" data-reading-anchor="actions">
        {relatedChapter && <button type="button" onClick={() => onNavigate(relatedChapter)}>{t('相关章节')} · {relatedChapter}</button>}
        {relatedChapter && canLocate && <button type="button" onClick={() => onNavigate(relatedChapter, true)}>{t('在地图中查看')}</button>}
        <button type="button" onClick={onShare}>{t('复制探索链接')}</button>
        {shareStatus && <span role="status">{shareStatus.startsWith('http') ? <input aria-label={t('探索链接')} readOnly value={shareStatus} onFocus={event => event.target.select()} /> : t(shareStatus)}</span>}
      </div>
      {selected.kind !== 'story' && selected.description && <><h3 data-reading-anchor="description">{t('形态介绍')}</h3><p className="detail-description">{selected.description}</p></>}
      {(selected.quote || selected.kind === 'story') && <><h3 data-reading-anchor="quote">{t('原文')}</h3><blockquote>{selected.quote || selected.raw?.properties.source_quote || selected.description}</blockquote></>}
      {selected.reveal_chapter && <p className="detail-chapter">{t('第')}{selected.reveal_chapter}{t('章起可见（非诞生年代）')}</p>}
      {locale === 'en' && (selected.originalQuote || selected.raw?.properties.originalQuote) && <details className="original-text" data-reading-anchor="original"><summary>Chinese original</summary><blockquote lang="zh-CN">{selected.originalQuote || selected.raw.properties.originalQuote}</blockquote></details>}
      {selected.raw?.properties.parent_event_id && <nav className="story-siblings" aria-label={t("补天四幕")}>{catalog.events.filter(item => item.properties.parent_event_id === selected.raw.properties.parent_event_id).map(item => <button key={item.id} aria-current={item.id === selected.id ? 'true' : undefined} onClick={event => onOpen(item.id, event.currentTarget)}>{item.properties.name}</button>)}</nav>}
      <h3 data-reading-anchor="source">{t("原文出处")}</h3><p>{selected.source || selected.raw?.properties.source_text}</p>
      {links.map(source => <p key={source.url}><a className="source-link" href={source.url} target="_blank" rel="noreferrer">{t("打开所引篇章 ↗")}{links.length > 1 ? ` · ${source.title}` : ''}</a></p>)}
      {!links.length && <p>{t('暂无在线入口，请查阅所列书目。')}</p>}
      {selected.illustration_review && <p className="source-review">{t(selected.illustration_review)}</p>}
      {!!sources.length && <p className="source-review">{sources.some(source => source.verification_status === 'report_imported') ? t('来源状态：报告导入，待逐条复核') : t('来源状态：已进行文本摘录核对')}</p>}
      <h3 data-reading-anchor="location">{selected.kind === 'story' ? t("位置说明") : t("方位表达")}</h3>
      <p>{selected.direction || selected.raw?.properties.basis_note}</p>
      <h3 data-reading-anchor="notes">{t("项目说明")}</h3><p className="source-caution">{selected.kind === 'story' ? t("故事点为叙事锚点·示意，不表示真实地点、距离或未经原文支持的因果关系；插画中的器物与场景属于艺术解释。") : t("原文未明示的方位不以图面位置补出；淡墨山海纹样仅为装饰。")}</p>
      <button className="detail-finish-reading" type="button" onClick={() => {
        if (!reading.read.includes(selected.id)) reading.toggleRead(selected.id);
        if (navigation.next) step('next'); else onClose();
      }}>{t(navigation.next ? '读完，下一条 →' : '读完，关闭')}</button>
    </aside>
  </div>;
}

import { morphologyReview, FORM_LABELS } from '../bestiary';
import { useEffect, useLayoutEffect, useMemo, useRef, useState } from 'react';
import { useLocale, localize } from '../i18n';
import rawCatalog from '../../public/data/atlas/catalog.json';
import { iconFor } from '../artwork';
import ArtworkImage from './ArtworkImage';
import BlurRevealText, { RevealDetails } from './BlurRevealText';
import { storySummary } from '../story-summaries';
import ContentOrigin from './ContentOrigin';
import { entryTypes } from '../entries';

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

function highlightDiff(text, others) {
  if (!text || !others.length) return text;
  const shared = new Set();
  for (const other of others) for (const char of other) shared.add(char);
  const nodes = [];
  let buffer = '', unique = false;
  const flush = () => {
    if (!buffer) return;
    nodes.push(unique ? <mark key={nodes.length}>{buffer}</mark> : buffer);
    buffer = '';
  };
  for (const char of text) {
    const nextUnique = !shared.has(char) && char.trim() !== '';
    if (nextUnique !== unique) { flush(); unique = nextUnique; }
    buffer += char;
  }
  flush();
  return nodes;
}

export default function DetailDrawer({ placeReference, onOpenPlace, selected, namesakeEntries = [], comparisonEntries = [], placeContents = [], contextPlace, fromSearch, onClose, onOpen, restoreReading, returnFocusKey, onSaveReading, readingChapter, resumeSaveFailed, relatedChapter, canLocate, onNavigate, reading, navigation, animationId, onPlay, relatedItems, onRelated, parentEntry }) {
  const { t, locale } = useLocale();
  const catalog = useMemo(() => localize(rawCatalog, locale), [locale]);
  const [parallelOpen, setParallelOpen] = useState(false);
  useEffect(() => { setParallelOpen(false); }, [selected.id]);
  const closeButton = useRef(null);
  const drawer = useRef(null);
  const heading = useRef(null);
  const previousButton = useRef(null);
  const nextButton = useRef(null);
  const pendingFocus = useRef(null);
  const lastEntry = useRef(null);  const positionRecord = useRef(null);
  const sources = (selected.raw?.properties.source_ids || []).map(id => catalog.sources.find(source => source.id === id)).filter(Boolean);
  const links = [...new Map([
    ...(selected.url ? [{ url: selected.url, title: selected.source }] : []),
    ...sources.filter(source => source.url),
  ].map(source => [source.url, source])).values()];
  useLayoutEffect(() => {
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
    const button = pendingFocus.current === 'previous' ? previousButton.current : pendingFocus.current === 'next' ? nextButton.current : pendingFocus.current === 'namesakes' ? node.querySelector('.detail-namesakes select') : closeButton.current;
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
      // WebKit can leave FontFaceSet.ready pending after a font fails.
      await Promise.allSettled([
        ...[...document.fonts].filter(font => font.status === 'loading').map(font => font.loaded),
        ...[...node.querySelectorAll('img')].map(img => img.decode()),
      ]);
      await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
      if (cancelled) return;
      if (requested) applyPosition(node, requested);
      const returnControl = returnFocusKey === 'play' ? node.querySelector('.detail-play-story')
        : returnFocusKey === 'namesakes' ? node.querySelector('.detail-namesakes select')
        : [...node.querySelectorAll('[data-related-id]')].find(button => button.dataset.relatedId === returnFocusKey);
      returnControl?.focus({ preventScroll: true });
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
  const readingPosition = () => ({ id: selected.id, chapter: readingChapter, position: capturePosition(drawer.current) });
  const visibleRelated = relatedItems.filter(item => item.id !== contextPlace?.id && !placeContents.some(entry => entry.id === item.id));
  const morphology = morphologyReview(selected.id, locale);
  const descriptionTitle = { place: '此地记述', plant: '草木记述', water: '水域记述', material: '物产记述', passage: '白话整理', animal: '动物记载', valley: '谷地记述', wind: '风的记述', deity: '山神记述', rite: '祭礼记述' }[selected.kind] || '形态介绍';
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
        {parentEntry && <button type="button" className="return-related" onClick={onClose}>{t('← 返回')} · {parentEntry.name}</button>}
        {fromSearch && !parentEntry && <button type="button" className="return-search" onClick={onClose}>{t('← 返回搜索结果')}</button>}
        <button ref={closeButton} className="drawer-close" onClick={onClose} aria-label={t("关闭")}>×</button></div>
      <span className="intro-overline">{selected.region || selected.source}</span>
      <h2 ref={heading} tabIndex={-1} data-reading-anchor="title"><BlurRevealText text={selected.name} revealKey={`detail:${selected.id}:title:${locale}`} rootRef={drawer} /></h2>
      <ContentOrigin record={selected} />
      {namesakeEntries.length > 1 && <nav className="detail-related detail-namesakes" aria-label={t('同名记载')}>
        <h3><BlurRevealText revealKey="components/DetailDrawer.jsx:1" variant="inline" text={t('同名记载')} /> · {namesakeEntries.length}</h3><p><BlurRevealText variant="prose" revealKey={`detail:${selected.id}:prose-1:${locale}`} rootRef={drawer}>{t('同名仅作索引，各条出处独立。')}</BlurRevealText></p>
        <select aria-label={t('同名记载')} value={selected.id} onChange={event => { pendingFocus.current = 'namesakes'; onRelated(event.target.value, readingPosition(), 'namesakes'); }}>{namesakeEntries.map(item => <option key={item.id} value={item.id}>{item.displayName} · {item.provenance}</option>)}</select>
        <button type="button" className="detail-parallel-toggle" aria-expanded={parallelOpen} aria-controls="detail-parallel" onClick={() => setParallelOpen(value => !value)}>{t(parallelOpen ? '收起并列校读' : '并列校读')}</button>
        {parallelOpen && <div className="detail-parallel" id="detail-parallel" data-parallel-count={namesakeEntries.length}>{namesakeEntries.every(entry => /^(其)?[中陰隂陽阳獸兽]?多|^是多/.test((entry.quote || '').trim())) && <p className="detail-parallel-generic">{t('本组多为泛称罗列，并列仅作索引。')}</p>}{namesakeEntries.map(entry => {
          const others = namesakeEntries.filter(item => item.id !== entry.id).map(item => item.quote || '');
          const form = FORM_LABELS[entry.formGroup] || FORM_LABELS.other;
          return <article key={entry.id} className="detail-parallel-card" data-parallel-id={entry.id}>
            <h4>{entry.displayName}<small>{entry.bookKey ? t(entry.bookKey) : ''}{entry.bookKey ? ' · ' : ''}{t(form[locale] || form.zh)}</small></h4>
            <blockquote lang="zh-CN">{highlightDiff(entry.quote || entry.originalQuote || '', others)}</blockquote>
            {entry.classification?.review_status === 'unresolved' && <small className="detail-parallel-note">{t('形貌未记入正文，不作补写。')}</small>}
          </article>;
        })}</div>}
      </nav>}
      {!!comparisonEntries.length && <nav className="detail-related detail-comparisons" data-reading-anchor="comparisons" aria-label={t('异说校读')}>
        <h3>{t('异说校读')} · {comparisonEntries.length}</h3>
        <p>{t('同段另有比较记述，与正文分列，不作同名条目。')}</p>
        {comparisonEntries.map(item => <button type="button" key={item.id} data-related-id={item.id} onClick={() => onRelated(item.id, readingPosition())}>
          <b>{item.displayName}</b><small>{item.bookKey ? t(item.bookKey) : ''}{item.bookKey ? ' · ' : ''}{t('比较记述')}</small>
          {item.classification?.evidence && <small className="relation-quote" lang="zh-CN">{item.classification.evidence}</small>}
        </button>)}
      </nav>}
      {selected.kind === 'story' && storySummary(selected.id, locale) && <section className="story-summary" data-reading-anchor="summary" aria-label={t('故事梗概')}><h3><BlurRevealText text={t('故事梗概')} revealKey={`detail:${selected.id}:summary:${locale}`} variant="section" rootRef={drawer} /></h3><p><BlurRevealText variant="prose" revealKey={`detail:${selected.id}:prose-2:${locale}`} rootRef={drawer}>{storySummary(selected.id, locale)}</BlurRevealText></p><small>{t('项目整理 · 依据下列引文转述，非古籍原文。')}</small></section>}
      {selected.kind !== 'story' && selected.description && <><h3 data-reading-anchor="description"><BlurRevealText text={t(descriptionTitle)} revealKey={`detail:${selected.id}:description:${locale}`} variant="section" rootRef={drawer} /></h3><p className="detail-description"><BlurRevealText variant="prose" revealKey={`detail:${selected.id}:prose-3:${locale}`} rootRef={drawer}>{selected.description}</BlurRevealText></p></>}
      {morphology && <RevealDetails className="morphology-review" key={`morphology:${selected.id}`} data-morphology-status={morphology.status}>
        <summary><BlurRevealText variant="inline" revealKey="components/DetailDrawer.jsx:summary" text={t('形貌依据')} /> · {morphology.label}</summary><p><BlurRevealText variant="prose" revealKey={`detail:${selected.id}:prose-4:${locale}`} rootRef={drawer}>{morphology.note}</BlurRevealText></p><blockquote lang="zh-CN"><BlurRevealText variant="prose" revealKey={`detail:${selected.id}:prose-5:${locale}`} rootRef={drawer}>{morphology.evidence}</BlurRevealText></blockquote>
        <div className="morphology-sources">{morphology.source_urls.map((url, index) => <a key={url} href={url} target="_blank" rel="noopener noreferrer">{t('查看影印来源 ↗')} {index + 1}</a>)}</div>
      </RevealDetails>}
      {contextPlace && parentEntry?.id !== contextPlace.id && <button type="button" className="detail-context-place" data-related-id={contextPlace.id} onClick={() => onRelated(contextPlace.id, readingPosition())}>{t('查看关联地点')} · {contextPlace.name}</button>}
      {(selected.quote || selected.kind === 'story') && <><h3 data-reading-anchor="quote"><BlurRevealText revealKey="components/DetailDrawer.jsx:2" variant="inline" text={<>{t('原文')}</>} /></h3><blockquote><BlurRevealText variant="prose" revealKey={`detail:${selected.id}:prose-6:${locale}`} rootRef={drawer}>{selected.quote || selected.raw?.properties.source_quote || selected.description}</BlurRevealText></blockquote></>}
      {selected.reveal_chapter && <p className="detail-chapter"><BlurRevealText variant="prose" revealKey={`detail:${selected.id}:prose-7:${locale}`} rootRef={drawer}>{t('第')}{selected.reveal_chapter}{t('章起可见（非诞生年代）')}</BlurRevealText></p>}
      {locale === 'en' && (selected.originalQuote || selected.raw?.properties.originalQuote) && <RevealDetails className="original-text" data-reading-anchor="original"><summary>Chinese original</summary><blockquote lang="zh-CN"><BlurRevealText variant="prose" revealKey={`detail:${selected.id}:prose-8:${locale}`} rootRef={drawer}>{selected.originalQuote || selected.raw.properties.originalQuote}</BlurRevealText></blockquote></RevealDetails>}
      {(selected.originalCommentary || selected.commentary_quote) && <RevealDetails className="original-text commentary-section"><summary><BlurRevealText variant="inline" revealKey="components/DetailDrawer.jsx:summary" text={t(selected.kind === 'passage' ? '底本注文 · 按录文行保留' : '郭注摘录')} /></summary>{locale === 'en' && selected.originalCommentary && selected.commentary_quote && selected.commentary_quote !== selected.originalCommentary && <p lang="en"><BlurRevealText variant="prose" revealKey={`detail:${selected.id}:prose-9:${locale}`} rootRef={drawer}>{selected.commentary_quote}</BlurRevealText></p>}<blockquote lang="zh-CN"><BlurRevealText variant="prose" revealKey={`detail:${selected.id}:prose-10:${locale}`} rootRef={drawer}>{selected.originalCommentary || selected.commentary_quote}</BlurRevealText></blockquote></RevealDetails>}
      {selected.raw?.properties.parent_event_id && <nav className="story-siblings" aria-label={t("补天四幕")}>{catalog.events.filter(item => item.properties.parent_event_id === selected.raw.properties.parent_event_id).map(item => <button key={item.id} aria-current={item.id === selected.id ? 'true' : undefined} onClick={event => onOpen(item.id, event.currentTarget)}>{item.properties.name}</button>)}</nav>}
      {iconFor(selected) && <ArtworkImage key={selected.id} className="drawer-art" src={iconFor(selected)} alt={t(`${selected.name}版画插画`)} />}
      {selected.artwork_caption && iconFor(selected) && <p className="artwork-caption"><BlurRevealText variant="prose" revealKey={`detail:${selected.id}:prose-11:${locale}`} rootRef={drawer}>{selected.artwork_caption}</BlurRevealText></p>}
      {!!placeContents.length && <nav className="detail-place-contents detail-related" aria-label={t('此地所见')} data-reading-anchor="contents">
        <h3><BlurRevealText revealKey="components/DetailDrawer.jsx:3" variant="inline" text={<>{t('此地所见')}</>} /></h3><p><BlurRevealText variant="prose" revealKey={`detail:${selected.id}:prose-12:${locale}`} rootRef={drawer}>{t('按本段经文组织阅读，山中记载与水域记述分别呈现。')}</BlurRevealText></p>
        {['plant', 'water', 'beast', 'animal', 'valley', 'wind', 'deity', 'rite', 'material', 'place'].map(kind => {
          const entries = placeContents.filter(item => item.kind === kind);
          return entries.length ? <section key={kind}><h4><BlurRevealText revealKey="components/DetailDrawer.jsx:4" variant="inline" text={<>{t(entryTypes[kind])}</>} /></h4>{entries.map(item => <button type="button" key={item.id} data-related-id={item.id} onClick={() => onRelated(item.id, readingPosition())}><b><BlurRevealText revealKey="components/DetailDrawer.jsx:9" variant="inline" text={<>{item.name}</>} /></b><small>{t(item.kind === 'water' || item.relation_scope === 'water' || ['beast-xuangui', 'beast-chiru', 'material-yupei'].includes(item.id) ? '本段水域记述' : '本山段记载')}</small></button>)}</section> : null;
        })}
      </nav>}
      <div className="detail-exploration" data-reading-anchor="actions">
        {relatedChapter && <button type="button" onClick={() => onNavigate(relatedChapter)}>{t('相关章节')} · {relatedChapter}</button>}
        {relatedChapter && canLocate && <button type="button" onClick={() => onNavigate(relatedChapter, true)}>{t('在地图中查看')}</button>}
      </div>
      {placeReference && <button className="detail-open-place" type="button" onClick={onOpenPlace}>{t("查看真实地理资料")} · {t(placeReference.properties.label)}</button>}
      {animationId && <button className="detail-play-story" type="button" onClick={() => onPlay(readingPosition())}>{t('播放这个故事')}</button>}
      <h3 data-reading-anchor="source"><BlurRevealText revealKey="components/DetailDrawer.jsx:5" variant="inline" text={<>{t("原文出处")}</>} /></h3><p><BlurRevealText variant="prose" revealKey={`detail:${selected.id}:prose-13:${locale}`} rootRef={drawer}>{selected.source || selected.raw?.properties.source_text}</BlurRevealText></p>
      {selected.source_locator && <p className="source-review"><BlurRevealText variant="prose" revealKey={`detail:${selected.id}:prose-14:${locale}`} rootRef={drawer}>{selected.source_locator}</BlurRevealText></p>}
      {selected.source_pages?.length > 1 && <p className="source-pages"><BlurRevealText variant="prose" revealKey={`detail:${selected.id}:prose-15:${locale}`} rootRef={drawer}>{selected.source_pages.map((url, index) => <a key={url} href={url} target="_blank" rel="noreferrer">{t('影印页')} {Number(url.split('/').at(-1))}{index < selected.source_pages.length - 1 ? ' · ' : ''}</a>)}</BlurRevealText></p>}
      {links.map(source => <p key={source.url}><BlurRevealText variant="prose" revealKey={`detail:${selected.id}:prose-16:${locale}`} rootRef={drawer}><a className="source-link" href={source.url} target="_blank" rel="noreferrer">{t("打开所引篇章 ↗")}{links.length > 1 ? ` · ${source.title}` : ''}</a></BlurRevealText></p>)}
      {!links.length && <p><BlurRevealText variant="prose" revealKey={`detail:${selected.id}:prose-17:${locale}`} rootRef={drawer}>{t('暂无在线入口，请查阅所列书目。')}</BlurRevealText></p>}
      {selected.illustration_review && <p className="source-review"><BlurRevealText variant="prose" revealKey={`detail:${selected.id}:prose-18:${locale}`} rootRef={drawer}>{t(selected.illustration_review)}</BlurRevealText></p>}
      {!!sources.length && <p className="source-review"><BlurRevealText variant="prose" revealKey={`detail:${selected.id}:prose-19:${locale}`} rootRef={drawer}>{sources.some(source => source.verification_status === 'report_imported') ? t('来源状态：报告导入，待逐条复核') : t('来源状态：已进行文本摘录核对')}</BlurRevealText></p>}
      <h3 data-reading-anchor="location"><BlurRevealText revealKey="components/DetailDrawer.jsx:6" variant="inline" text={<>{selected.kind === 'story' ? t("位置说明") : t("方位表达")}</>} /></h3>
      <p><BlurRevealText variant="prose" revealKey={`detail:${selected.id}:prose-20:${locale}`} rootRef={drawer}>{selected.direction || selected.raw?.properties.basis_note}</BlurRevealText></p>
      <h3 data-reading-anchor="notes"><BlurRevealText revealKey="components/DetailDrawer.jsx:7" variant="inline" text={<>{t("项目说明")}</>} /></h3><p className="source-caution"><BlurRevealText variant="prose" revealKey={`detail:${selected.id}:prose-21:${locale}`} rootRef={drawer}>{selected.kind === 'story' ? t("故事点为叙事锚点·示意，不表示真实地点、距离或未经原文支持的因果关系；插画中的器物与场景属于艺术解释。") : t("原文未明示的方位不以图面位置补出；淡墨山海纹样仅为装饰。")}</BlurRevealText></p>
      {selected.editorial_note && <p className="source-caution"><BlurRevealText variant="prose" revealKey={`detail:${selected.id}:prose-22:${locale}`} rootRef={drawer}>{selected.editorial_note}</BlurRevealText></p>}
      {selected.content_note && <p className="source-caution"><BlurRevealText variant="prose" revealKey={`detail:${selected.id}:prose-23:${locale}`} rootRef={drawer}>{selected.content_note}</BlurRevealText></p>}
      {!!visibleRelated.length && <nav className="detail-related" data-reading-anchor="related" aria-label={t('相关条目')}><h3><BlurRevealText revealKey="components/DetailDrawer.jsx:8" variant="inline" text={<>{t('相关条目')}</>} /></h3><p><BlurRevealText variant="prose" revealKey={`detail:${selected.id}:prose-24:${locale}`} rootRef={drawer}>{t('按原文关联，故事、异兽和地点分别呈现。')}</BlurRevealText></p>{visibleRelated.map(item => <button type="button" key={item.id} data-related-id={item.id} onClick={() => onRelated(item.id, readingPosition())}><b><BlurRevealText revealKey="components/DetailDrawer.jsx:10" variant="inline" text={<>{item.name}</>} /></b><small>{t(item.relationLabel || item.entryType)} · {t(item.relationSource)}</small>{item.relationQuote && <small className="relation-quote" lang="zh-CN">{item.relationQuote}</small>}</button>)}</nav>}
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
      <button className="detail-finish-reading" type="button" onClick={() => {
        if (!reading.read.includes(selected.id)) reading.toggleRead(selected.id);
        if (navigation.next) step('next'); else onClose();
      }}>{t(navigation.next ? '读完，下一条 →' : '读完，关闭')}</button>
    </aside>
  </div>;
}

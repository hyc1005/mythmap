import { useEffect, useMemo, useRef, useState } from 'react';
import { useLocale } from '../i18n';
import { useReducedMotion } from '../motion';
import { iconFor } from '../artwork';
import ArtworkImage from './ArtworkImage';
import { ReadingMarks } from '../reading';
import { BESTIARY_INITIAL, BESTIARY_BATCH, FORM_LABELS, FEATURE_LABELS, bestiaryEntries, filterBestiary, groupBestiary } from '../bestiary';

const emptyFilters = { role: 'beast', query: '', book: '', form: '', feature: '', reading: '' };


function BeastArtwork({ src, seen, reduced }) {
  const slot = useRef(null);
  const [near, setNear] = useState(false), [inView, setInView] = useState(false);
  const [ready, setReady] = useState(false), [revealing, setRevealing] = useState(false);
  useEffect(() => {
    if (!src) return undefined;
    if (typeof IntersectionObserver !== 'function') { setNear(true); setInView(true); return undefined; }
    const nearby = new IntersectionObserver(records => setNear(records.some(record => record.isIntersecting)), { rootMargin: '600px 0px' });
    const viewport = new IntersectionObserver(records => setInView(records.some(record => record.isIntersecting)), { threshold: .01 });
    nearby.observe(slot.current); viewport.observe(slot.current);
    return () => { nearby.disconnect(); viewport.disconnect(); };
  }, [src]);
  useEffect(() => {
    if (!near) { setReady(false); setRevealing(false); return; }
    if (reduced) setRevealing(false);
    if (!ready || !inView || seen.has(src)) return;
    seen.add(src);
    if (typeof IntersectionObserver === 'function' && !reduced) setRevealing(true);
  }, [near, ready, inView, src, seen, reduced]);
  return <div className="beast-art" ref={slot} onAnimationEnd={() => setRevealing(false)} data-artwork-src={src}>{near && src && <ArtworkImage src={src} alt="" className={revealing ? 'artwork-reveal' : undefined} loading="lazy" interactive={false} onLoad={event => {
    const image = event.currentTarget;
    void image.decode().then(() => { if (image.isConnected) setReady(true); }, () => {});
  }} />}</div>;
}

export default function Bestiary({ world, onOpen, reading }) {
  const { t, locale } = useLocale();
  const reduced = useReducedMotion();
  const entries = useMemo(() => bestiaryEntries(world, locale), [world, locale]);
  const seenIllustrations = useRef(new Set());
  const [moreFilters, setMoreFilters] = useState(false);
  const [filters, setFilters] = useState(emptyFilters);
  const [limit, setLimit] = useState(BESTIARY_INITIAL);
  const hasFilter = Object.entries(filters).some(([key, value]) => key !== 'role' && value.trim());
  const change = patch => { setFilters(value => ({ ...value, ...patch })); setLimit(BESTIARY_INITIAL); };
  const reset = () => { setFilters({ ...emptyFilters, role: filters.role }); setLimit(BESTIARY_INITIAL); };
  const list = useMemo(() => filterBestiary(entries, filters, reading), [entries, filters, reading.read, reading.favorites]);
  const groups = useMemo(() => groupBestiary(list), [list]);
  const visible = groups.slice(0, limit);
  const ids = list.map(item => item.id);
  const counted = (count, zh, en) => `${count} ${locale === 'en' ? `${en}${count === 1 ? '' : 's'}` : zh}`;
  const count = (field, value) => filterBestiary(entries, { ...filters, [field]: value }, reading).length;
  const books = [...new Map(entries.filter(item => item.role === filters.role).map(item => [item.bookKey, item.region])).entries()];
  const card = entry => <button type="button" className="beast-card" data-beast-id={entry.id} data-form-group={entry.formGroup} key={entry.id} onClick={event => onOpen(entry.id, event.currentTarget, ids)}>
    <BeastArtwork key={entry.id} src={iconFor(entry, 'card')} seen={seenIllustrations.current} reduced={reduced} />
    <b>{entry.displayName}</b><small className="beast-provenance">{entry.provenance}</small>
    <span className="beast-tags"><span>{FORM_LABELS[entry.formGroup][locale]}</span>{entry.featureTags.map(tag => <span key={tag}>{FEATURE_LABELS[tag][locale]}</span>)}{entry.classification.basis !== 'text' && <span>{t(entry.classification.basis === 'comparison' ? '比较记述' : '郭注记述')}</span>}{entry.classification.review_status === 'unresolved' && <span>{t('形貌待核')}</span>}</span>
    <ReadingMarks reading={reading} id={entry.id} /><span className="beast-card-more">{t('查看形貌与出处 ↗')}</span>
  </button>;
  return <section className="best-page" id="creatures">
    <div className="best-page-heading"><h2>{t('山海经异兽谱')}</h2><p>{t('按原文形貌整理；同名组仅作索引，各条出处独立。')}</p></div>
    <div className="bestiary-roles" role="group" aria-label={t('异兽谱类型')}>
      {['beast', 'deity'].map(role => <button type="button" key={role} aria-pressed={filters.role === role} data-bestiary-role={role} onClick={() => { setFilters({ ...emptyFilters, role }); setLimit(BESTIARY_INITIAL); }}>{t(role === 'beast' ? '异兽' : '神灵')} · {entries.filter(item => item.role === role).length}</button>)}
    </div>
    <div className="bestiary-tools">
      <input type="search" maxLength={120} value={filters.query} onChange={event => change({ query: event.target.value })} placeholder={t('搜索异兽或形貌')} aria-label={t('搜索异兽')} />
      <select value={filters.book} onChange={event => change({ book: event.target.value })} aria-label={t('按篇目筛选')}><option value="">{t('全部篇目')} · {count('book', '')}</option>{books.map(([key, label]) => <option key={key} value={key}>{label} · {count('book', key)}</option>)}</select>
      <button className="bestiary-extra-toggle" type="button" aria-expanded={moreFilters} aria-controls="bestiary-extra-filters" onClick={() => setMoreFilters(value => !value)}>{t('更多筛选')}{[filters.form, filters.feature, filters.reading].filter(Boolean).length > 0 && ` · ${[filters.form, filters.feature, filters.reading].filter(Boolean).length}`}</button>
      <div className="bestiary-extra-filters" id="bestiary-extra-filters" data-expanded={moreFilters}>
      <select value={filters.form} onChange={event => change({ form: event.target.value })} aria-label={t('按形貌筛选')}><option value="">{t('全部形貌')} · {count('form', '')}</option>{Object.entries(FORM_LABELS).map(([key, label]) => <option key={key} value={key}>{label[locale]} · {count('form', key)}</option>)}</select>
      <select value={filters.feature} onChange={event => change({ feature: event.target.value })} aria-label={t('按特征筛选')}><option value="">{t('全部特征')} · {count('feature', '')}</option>{Object.entries(FEATURE_LABELS).map(([key, label]) => <option key={key} value={key}>{label[locale]} · {count('feature', key)}</option>)}</select>
      <select value={filters.reading} onChange={event => change({ reading: event.target.value })} aria-label={t('按阅读状态筛选')}><option value="">{t('全部阅读状态')}</option><option value="unread">{t('未读')} · {count('reading', 'unread')}</option><option value="read">{t('已读')} · {count('reading', 'read')}</option><option value="favorites">{t('已收藏')} · {count('reading', 'favorites')}</option></select>
      </div>
      {hasFilter && <button type="button" className="bestiary-reset" onClick={reset}>{t('清除筛选')}</button>}
    </div>
    <p className="bestiary-count" role="status">{counted(list.length, '条记载', 'account')} · {counted(groups.length, '组名称', 'name group')} · {t('已显示')} {counted(visible.length, '组', 'group')}</p>
    <div className="beast-grid" id="beast-cards">{visible.map(group => <article className="beast-group" data-group-key={group.key} key={group.key}>
      {card(group.entries[0])}
      {group.entries.length > 1 && <button type="button" className="beast-variants-toggle" aria-haspopup="dialog" onClick={event => onOpen(group.entries[0].id, event.currentTarget, ids)}>{t('查看同名记载')} · {group.entries.length}</button>}
    </article>)}</div>
    {!list.length && <p className="bestiary-empty">{t('没有找到匹配的异兽，请换一个名称或篇目。')}</p>}
    {groups.length > limit && <button type="button" className="bestiary-toggle" aria-controls="beast-cards" onClick={() => setLimit(value => value + BESTIARY_BATCH)}>{t('再显示')} {Math.min(BESTIARY_BATCH, groups.length - limit)} {t('组名称')} ↓</button>}
  </section>;
}

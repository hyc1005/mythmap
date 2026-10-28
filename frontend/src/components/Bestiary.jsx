import { useEffect, useMemo, useRef, useState } from 'react';
import { useLocale } from '../i18n';
import { iconFor } from '../artwork';
import ArtworkImage from './ArtworkImage';
import { ReadingMarks } from '../reading';
import { BESTIARY_BATCH, FORM_LABELS, FEATURE_LABELS, bestiaryEntries, filterBestiary, groupBestiary } from '../bestiary';

const emptyFilters = { role: 'beast', query: '', book: '', form: '', feature: '', reading: '' };

export default function Bestiary({ world, onOpen, reading }) {
  const { t, locale } = useLocale();
  const entries = useMemo(() => bestiaryEntries(world, locale), [world, locale]);
  const grid = useRef(null), seenCards = useRef(new Set());
  const [filters, setFilters] = useState(emptyFilters);
  const [limit, setLimit] = useState(BESTIARY_BATCH);
  const [expandedGroups, setExpandedGroups] = useState({});
  const hasFilter = Object.entries(filters).some(([key, value]) => key !== 'role' && value.trim());
  const change = patch => { setFilters(value => ({ ...value, ...patch })); setLimit(BESTIARY_BATCH); setExpandedGroups({}); };
  const reset = () => { setFilters({ ...emptyFilters, role: filters.role }); setLimit(BESTIARY_BATCH); setExpandedGroups({}); };
  const list = useMemo(() => filterBestiary(entries, filters, reading), [entries, filters, reading.read, reading.favorites]);
  const groups = useMemo(() => groupBestiary(list), [list]);
  const visible = groups.slice(0, limit);
  const ids = list.map(item => item.id);
  const counted = (count, zh, en) => `${count} ${locale === 'en' ? `${en}${count === 1 ? '' : 's'}` : zh}`;
  const count = (field, value) => filterBestiary(entries, { ...filters, [field]: value }, reading).length;
  const books = [...new Map(entries.filter(item => item.role === filters.role).map(item => [item.bookKey, item.region])).entries()];
  useEffect(() => {
    const observer = new IntersectionObserver(records => {
      records.forEach(({ target, isIntersecting }) => {
        if (!isIntersecting) return;
        if (!seenCards.current.has(target.dataset.beastId) && !hasFilter) target.classList.add('beast-enter');
        seenCards.current.add(target.dataset.beastId);
        observer.unobserve(target);
      });
    }, { threshold: .1 });
    grid.current.querySelectorAll('.beast-card').forEach(card => observer.observe(card));
    return () => observer.disconnect();
  }, [list, limit, expandedGroups, hasFilter]);
  const card = entry => <button type="button" className="beast-card" data-beast-id={entry.id} data-form-group={entry.formGroup} key={entry.id} onClick={event => onOpen(entry.id, event.currentTarget, ids)}>
    <div className="beast-art">{iconFor(entry) && <ArtworkImage src={iconFor(entry, 'card')} alt="" loading="lazy" interactive={false} />}</div>
    <b>{entry.displayName}</b><small className="beast-provenance">{entry.provenance}</small>
    <span className="beast-tags"><span>{FORM_LABELS[entry.formGroup][locale]}</span>{entry.featureTags.map(tag => <span key={tag}>{FEATURE_LABELS[tag][locale]}</span>)}{entry.classification.basis !== 'text' && <span>{t(entry.classification.basis === 'comparison' ? '比较记述' : '郭注记述')}</span>}{entry.classification.review_status === 'unresolved' && <span>{t('形貌待核')}</span>}</span>
    <ReadingMarks reading={reading} id={entry.id} /><p>{entry.description}</p><small>{entry.source}</small>
  </button>;
  return <section className="best-page" id="creatures">
    <div className="best-page-heading"><h2>{t('山海经异兽谱')}</h2><p>{t('按原文形貌整理；同名组仅作索引，各条出处独立。')}</p></div>
    <div className="bestiary-roles" role="group" aria-label={t('异兽谱类型')}>
      {['beast', 'deity'].map(role => <button type="button" key={role} aria-pressed={filters.role === role} data-bestiary-role={role} onClick={() => { setFilters({ ...emptyFilters, role }); setLimit(BESTIARY_BATCH); setExpandedGroups({}); }}>{t(role === 'beast' ? '异兽' : '神灵')} · {entries.filter(item => item.role === role).length}</button>)}
    </div>
    <div className="bestiary-tools">
      <input type="search" maxLength={120} value={filters.query} onChange={event => change({ query: event.target.value })} placeholder={t('搜索异兽或形貌')} aria-label={t('搜索异兽')} />
      <select value={filters.book} onChange={event => change({ book: event.target.value })} aria-label={t('按篇目筛选')}><option value="">{t('全部篇目')} · {count('book', '')}</option>{books.map(([key, label]) => <option key={key} value={key}>{label} · {count('book', key)}</option>)}</select>
      <select value={filters.form} onChange={event => change({ form: event.target.value })} aria-label={t('按形貌筛选')}><option value="">{t('全部形貌')} · {count('form', '')}</option>{Object.entries(FORM_LABELS).map(([key, label]) => <option key={key} value={key}>{label[locale]} · {count('form', key)}</option>)}</select>
      <select value={filters.feature} onChange={event => change({ feature: event.target.value })} aria-label={t('按特征筛选')}><option value="">{t('全部特征')} · {count('feature', '')}</option>{Object.entries(FEATURE_LABELS).map(([key, label]) => <option key={key} value={key}>{label[locale]} · {count('feature', key)}</option>)}</select>
      <select value={filters.reading} onChange={event => change({ reading: event.target.value })} aria-label={t('按阅读状态筛选')}><option value="">{t('全部阅读状态')}</option><option value="unread">{t('未读')} · {count('reading', 'unread')}</option><option value="read">{t('已读')} · {count('reading', 'read')}</option><option value="favorites">{t('已收藏')} · {count('reading', 'favorites')}</option></select>
      {hasFilter && <button type="button" className="bestiary-reset" onClick={reset}>{t('清除筛选')}</button>}
    </div>
    <p className="bestiary-count" role="status">{counted(list.length, '条记载', 'account')} · {counted(groups.length, '组名称', 'name group')} · {t('已显示')} {counted(visible.length, '组', 'group')}</p>
    <div className="beast-grid" id="beast-cards" ref={grid}>{visible.map(group => {
      const expanded = expandedGroups[group.key] ?? Boolean(filters.query.trim());
      const region = `beast-variants-${group.entries[0].id}`;
      return <article className="beast-group" data-group-key={group.key} key={group.key}>
        {card(group.entries[0])}
        {group.entries.length > 1 && <>
          <button type="button" className="beast-variants-toggle" aria-controls={region} aria-expanded={expanded} onClick={() => setExpandedGroups(value => ({ ...value, [group.key]: !expanded }))}>{t(expanded ? '收起同名记载' : '展开同名记载')} · {group.entries.length}</button>
          {expanded && <div className="beast-variants" id={region}>{group.entries.slice(1).map(card)}</div>}
        </>}
      </article>;
    })}</div>
    {!list.length && <p className="bestiary-empty">{t('没有找到匹配的异兽，请换一个名称或篇目。')}</p>}
    {groups.length > limit && <button type="button" className="bestiary-toggle" aria-controls="beast-cards" onClick={() => setLimit(value => value + BESTIARY_BATCH)}>{t('再显示')} {Math.min(BESTIARY_BATCH, groups.length - limit)} {t('组名称')} ↓</button>}
  </section>;
}

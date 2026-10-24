import { useEffect, useRef, useState } from 'react';
import { useLocale } from '../i18n';
import { iconFor } from '../artwork';
import ArtworkImage from './ArtworkImage';
import { ReadingMarks } from '../reading';

export default function Bestiary({ beasts, onOpen, reading }) {
  const { t, locale } = useLocale();
  const grid = useRef(null);
  const [columns, setColumns] = useState(2);
  const [expanded, setExpanded] = useState(false);
  const [search, setSearch] = useState('');
  const [bookFilter, setBookFilter] = useState('');
  const [readingFilter, setReadingFilter] = useState('');
  const seenCards = useRef(new Set());
  const hasFilter = Boolean(search.trim()) || bookFilter !== '' || readingFilter !== '';
  const list = beasts.filter(beast => (readingFilter === '' || readingFilter === 'read' && reading.read.includes(beast.id) || readingFilter === 'unread' && !reading.read.includes(beast.id) || readingFilter === 'favorites' && reading.favorites.includes(beast.id)) && (bookFilter === '' || beast.region === bookFilter) && (!search.trim() || `${beast.name} ${beast.originalName || ""} ${beast.region} ${beast.description}`.toLocaleLowerCase().includes(search.trim().toLocaleLowerCase())));
  const showAll = expanded || hasFilter;
  useEffect(() => {
    const measure = () => setColumns(getComputedStyle(grid.current).gridTemplateColumns.split(' ').length);
    const observer = new ResizeObserver(measure);
    observer.observe(grid.current);
    measure();
    return () => observer.disconnect();
  }, []);
  useEffect(() => {
    const cards = [...grid.current.querySelectorAll('.beast-card')];
    const observer = new IntersectionObserver(entries => {
      entries.forEach(({ target, isIntersecting }) => {
        if (!isIntersecting) return;
        if (!seenCards.current.has(target.dataset.beastId) && !hasFilter) target.classList.add('beast-enter');
        seenCards.current.add(target.dataset.beastId);
        observer.unobserve(target);
      });
    }, { threshold: .1 });
    cards.forEach(card => observer.observe(card));
    return () => observer.disconnect();
  }, [search, bookFilter, readingFilter, reading.read, reading.favorites, expanded, columns, locale]);
  useEffect(() => setExpanded(false), [search, bookFilter, readingFilter]);
  useEffect(() => { setBookFilter(''); }, [locale]);
  return <section className="best-page" id="creatures">
    <div className="best-page-heading"><h2>{t("山海经异兽谱")}</h2><p>{t("选编")} {beasts.length} {t("项异兽 · 同名异篇分开呈现")}</p></div>
    <div className="bestiary-tools"><input value={search} onChange={event => setSearch(event.target.value)} placeholder={t("搜索异兽或形貌")} aria-label={t("搜索异兽")} /><select value={bookFilter} onChange={event => setBookFilter(event.target.value)} aria-label={t("按篇目筛选")}><option value="">{t("全部篇目")}</option>{Array.from(new Set(beasts.map(item => item.region))).map(item => <option key={item}>{item}</option>)}</select><select value={readingFilter} onChange={event => setReadingFilter(event.target.value)} aria-label={t('按阅读状态筛选')}><option value="">{t('全部阅读状态')}</option><option value="unread">{t('未读')}</option><option value="read">{t('已读')}</option><option value="favorites">{t('已收藏')}</option></select><span>{list.length}{t("项索引 ·")}{showAll ? t("全部匹配条目") : t("首行预览")}</span></div>
    <div className="beast-grid" id="beast-cards" ref={grid} data-expanded={showAll}>{(showAll ? list : list.slice(0, columns)).map(beast => <button className="beast-card" data-beast-id={beast.id} key={beast.id} onClick={event => onOpen(beast.id, event.currentTarget, list.map(item => item.id))}><div className="beast-art">{iconFor(beast) && <ArtworkImage key={beast.id} src={iconFor(beast, 'card')} alt="" loading="lazy" interactive={false} />}</div><b>{beast.name}</b><ReadingMarks reading={reading} id={beast.id} /><p>{beast.description}</p><small>{beast.source}</small></button>)}</div>
    {!list.length && <p className="bestiary-empty">{t("没有找到匹配的异兽，请换一个名称或篇目。")}</p>}
    <button className="bestiary-toggle" aria-controls="beast-cards" aria-expanded={showAll} onClick={() => { if (hasFilter) { setSearch(''); setBookFilter(''); setReadingFilter(''); setExpanded(false); } else setExpanded(value => !value); }}>{hasFilter ? t("清除筛选并收起") : expanded ? t("收起异兽谱 ↑") : t(`展开全部 ${beasts.length} 项 ↓`)}</button>
  </section>;
}

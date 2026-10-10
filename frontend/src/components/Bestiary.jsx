import { useEffect, useRef, useState } from 'react';
import { iconFor } from '../asset-url';

export default function Bestiary({ beasts, onOpen }) {
  const grid = useRef(null);
  const [columns, setColumns] = useState(2);
  const [expanded, setExpanded] = useState(false);
  const [search, setSearch] = useState('');
  const [bookFilter, setBookFilter] = useState('全部篇目');
  const hasFilter = Boolean(search.trim()) || bookFilter !== '全部篇目';
  const list = beasts.filter(beast => (bookFilter === '全部篇目' || beast.region === bookFilter) && (!search.trim() || `${beast.name} ${beast.region} ${beast.description}`.includes(search.trim())));
  const showAll = expanded || hasFilter;
  useEffect(() => {
    const measure = () => setColumns(getComputedStyle(grid.current).gridTemplateColumns.split(' ').length);
    const observer = new ResizeObserver(measure);
    observer.observe(grid.current);
    measure();
    return () => observer.disconnect();
  }, []);
  useEffect(() => setExpanded(false), [search, bookFilter]);
  return <section className="best-page" id="creatures">
    <div className="best-page-heading"><h2>山海经异兽谱</h2><p>收录32项异兽 · 同名异篇分开呈现</p></div>
    <div className="bestiary-tools"><input value={search} onChange={event => setSearch(event.target.value)} placeholder="搜索异兽或形貌" aria-label="搜索异兽" /><select value={bookFilter} onChange={event => setBookFilter(event.target.value)} aria-label="按篇目筛选"><option>全部篇目</option>{Array.from(new Set(beasts.map(item => item.region))).map(item => <option key={item}>{item}</option>)}</select><span>{list.length} 项索引 · {showAll ? '全部匹配条目' : '首行预览'}</span></div>
    <div className="beast-grid" id="beast-cards" ref={grid} data-expanded={showAll}>{(showAll ? list : list.slice(0, columns)).map(beast => <button className="beast-card" key={beast.id} onClick={event => onOpen(beast.id, event.currentTarget)}><div className="beast-art">{iconFor(beast) ? <img src={iconFor(beast)} alt="" loading="lazy" /> : <div className="beast-placeholder" aria-hidden="true"><span>異</span><i>山海经</i></div>}<span>{beast.region}</span></div><b>{beast.name}</b><p>{beast.description}</p><small>{beast.source} · 第 {beast.reveal_chapter} 章起可见（非诞生年代）</small></button>)}</div>
    {!list.length && <p className="bestiary-empty">没有找到匹配的异兽，请换一个名称或篇目。</p>}
    <button className="bestiary-toggle" aria-controls="beast-cards" aria-expanded={showAll} onClick={() => { if (hasFilter) { setSearch(''); setBookFilter('全部篇目'); setExpanded(false); } else setExpanded(value => !value); }}>{hasFilter ? '清除筛选并收起' : expanded ? '收起异兽谱 ↑' : `展开全部 ${beasts.length} 项 ↓`}</button>
  </section>;
}

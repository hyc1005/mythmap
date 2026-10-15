import { useEffect, useMemo, useState } from 'react';
import { useLocale } from '../i18n';
import ExploreSheet from './ExploreSheet';
import { searchEntries, searchIndex } from '../search';
import originalWorld from '../../public/data/myth-world.json';
import originalCatalog from '../../public/data/atlas/catalog.json';

export default function GlobalSearch({ open, onClose, onChoose, returnFocus, world, catalog }) {
  const { t } = useLocale();
  const [query, setQuery] = useState('');
  const [kind, setKind] = useState('all');
  const [limit, setLimit] = useState(40);
  const index = useMemo(() => searchIndex(world, catalog, originalWorld, originalCatalog), [world, catalog]);
  const results = useMemo(() => searchEntries(index, query, kind), [index, query, kind]);
  useEffect(() => setLimit(40), [query, kind]);
  if (!open) return null;
  const labels = { story: '故事', beast: '异兽', source: '出处', place: '地点与神域' };
  const ids = [...new Set(results.filter(item => item.kind !== 'source').map(item => item.id))];
  return <ExploreSheet title={t('全站搜索')} onClose={onClose} returnFocus={returnFocus} initialFocus=".global-search-input" className="global-search-dialog">
    <div className="global-search-tools">
      <label>{t('搜索故事、异兽与出处')}<input className="global-search-input" type="search" maxLength={120} autoComplete="off" value={query} onChange={event => setQuery(event.target.value)} placeholder={t('输入名称、形貌或典籍')} /></label>
      <div><select aria-label={t('搜索范围')} value={kind} onChange={event => setKind(event.target.value)}><option value="all">{t('全部类型')}</option>{Object.entries(labels).map(([key, label]) => <option key={key} value={key}>{t(label)}</option>)}</select>{query && <button type="button" onClick={() => setQuery('')}>{t('清空搜索')}</button>}</div>
    </div>
    {!query.trim() && kind === 'all' ? <div className="search-suggestions"><p>{t('按名称、形貌或书目查找，也支持中文原名。')}</p>{['精卫', '九尾狐', '淮南子'].map(term => <button type="button" key={term} onClick={() => setQuery(term)}>{t(term)}</button>)}</div> : <>
      <p className="search-count" role="status">{t('找到条目')} · {results.length}</p>
      <div className="global-search-results">
        {results.slice(0, limit).map(item => <button className="search-result" type="button" key={item.key} data-result-kind={item.kind} data-result-id={item.id} onClick={() => onChoose(item.id, item.entryIds || ids)}><small>{t(labels[item.kind])}{item.chapter && ` · ${t('相关章节')} ${item.chapter}`}</small><b>{item.name}</b>{item.alias && item.alias !== item.name && <span lang="zh-CN">{item.alias}</span>}<p>{item.snippet}</p>{item.kind === 'source' ? <small>{t('关联条目')} · {item.entryName}{item.entryCount > 3 && ` … · ${item.entryCount}`}</small> : <small>{item.source}</small>}</button>)}
        {!results.length && <p>{t('未找到匹配条目，请缩短关键词或切换搜索范围。')}</p>}
        {results.length > limit && <button className="search-more" type="button" onClick={() => setLimit(value => value + 40)}>{t('显示更多结果')}</button>}
      </div>
    </>}
  </ExploreSheet>;
}

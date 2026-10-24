import { useEffect, useMemo, useRef } from 'react';
import { useLocale } from '../i18n';
import ExploreSheet from './ExploreSheet';
import ContentOrigin from './ContentOrigin';
import { highlightTerms, searchEntries, searchIndex } from '../search';
import originalWorld from '../../public/data/myth-world.json';
import originalCatalog from '../../public/data/atlas/catalog.json';

export default function GlobalSearch({ open, state, onStateChange, onClose, onChoose, returnFocus, world, catalog }) {
  const { t, locale } = useLocale();
  const { query, kind, limit } = state;
  const resultList = useRef(null), remembered = useRef(state), keywordInput = useRef(null);
  remembered.current = state;
  const update = patch => onStateChange({ ...state, ...patch });
  const setQuery = query => update({ query, limit: 40, scrollTop: 0, focusKey: null });
  const index = useMemo(() => searchIndex(world, catalog, originalWorld, originalCatalog, locale, t), [world, catalog, locale, t]);
  const results = useMemo(() => searchEntries(index, query, kind), [index, query, kind]);
  const otherResults = useMemo(() => kind !== 'all' && !results.length ? searchEntries(index, query, 'all') : [], [index, query, kind, results.length]);
  useEffect(() => {
    if (!open || !resultList.current) return;
    const saved = remembered.current;
    resultList.current.scrollTop = saved.scrollTop;
    [...resultList.current.querySelectorAll('[data-result-key]')].find(node => node.dataset.resultKey === saved.focusKey)?.focus({ preventScroll: true });
  }, [open]);
  if (!open) return null;
  const labels = { story: '故事', beast: '异兽', source: '出处', place: '地点与神域', plant: '草木', water: '水域', material: '物产', passage: '经文段落', animal: '动物记载', valley: '谷地', wind: '风的记述', deity: '山神', rite: '祭礼', geography: '现代地点资料' };
  const ids = [...new Set(results.filter(item => !['source', 'geography'].includes(item.kind)).map(item => item.id))];
  return <ExploreSheet title={t('全站搜索')} onClose={onClose} returnFocus={returnFocus} initialFocus=".global-search-input" className="global-search-dialog">
    <div className="global-search-tools">
      <label>{t('搜索故事、异兽与现代地点')}<input ref={keywordInput} className="global-search-input" type="search" maxLength={120} autoComplete="off" value={query} onChange={event => setQuery(event.target.value)} placeholder={t('输入故事、地名、形貌或典籍')} /></label>
      <div><select aria-label={t('搜索范围')} value={kind} onChange={event => update({ kind: event.target.value, limit: 40, scrollTop: 0, focusKey: null })}><option value="all">{t('全部类型')}</option>{Object.entries(labels).map(([key, label]) => <option key={key} value={key}>{t(label)}</option>)}</select>{query && <button type="button" onClick={() => setQuery('')}>{t('清空搜索')}</button>}</div>
    </div>
    {!query.trim() && kind === 'all' ? <div className="search-suggestions"><p>{t('按故事、现代地名、形貌或书目查找，也支持中文原名。')}</p>{['精卫', '九尾狐', '怀来县', '淮南子'].map(term => <button type="button" key={term} onClick={() => setQuery(term)}>{t(term)}</button>)}</div> : <>
      <p className="search-count" role="status">{t('找到条目')} · {results.length}</p>
      <div className="global-search-results" ref={resultList}>
        {results.slice(0, limit).map(item => <button className="search-result" type="button" key={item.key} data-result-key={item.key} data-result-kind={item.kind} data-result-id={item.id} data-reference-id={item.referenceId} onClick={() => onChoose(item.id, item.entryIds || ids, { ...state, scrollTop: resultList.current.scrollTop, focusKey: item.key }, item)}><small>{t(labels[item.kind])}{item.chapter && ` · ${t('相关章节')} ${item.chapter}`}</small><b>{item.name}</b><ContentOrigin record={item} />{item.alias && item.alias !== item.name && <span lang="zh-CN">{item.alias}</span>}{item.snippetKind === 'summary' && <small className="search-snippet-kind">{t(item.snippetLanguage === 'zh' && locale === 'en' ? '中文梗概' : '故事梗概')}</small>}<p lang={item.snippetLanguage === 'zh' ? 'zh-CN' : item.snippetLanguage}>{highlightTerms(item.snippet, query).map((part, index) => part.matched ? <mark key={index}>{part.text}</mark> : part.text)}</p>{item.kind === 'source' ? <small>{t('关联条目')} · {item.entryName}{item.entryCount > 3 && ` … · ${item.entryCount}`}</small> : <small>{item.source}{item.kind === 'geography' && ` · ${item.entryName}`}</small>}{item.kind === 'geography' && <small>{t('关联地点，不代表事件发生地。')}</small>}</button>)}
        {!results.length && <div className="search-empty">
          <p>{t('未找到匹配条目，请缩短关键词或切换搜索范围。')}</p>
          {kind !== 'all' && <button type="button" onClick={() => { update({ kind: 'all', limit: 40, scrollTop: 0, focusKey: null }); keywordInput.current?.focus(); }}>{otherResults.length ? `${t('在全部类型中查看结果')} · ${otherResults.length}` : t('搜索全部类型')}</button>}
          {query && <button type="button" onClick={() => { setQuery(''); keywordInput.current?.focus(); }}>{t('重新输入关键词')}</button>}
        </div>}
        {results.length > limit && <button className="search-more" type="button" onClick={() => update({ limit: limit + 40 })}>{t('显示更多结果')}</button>}
      </div>
    </>}
  </ExploreSheet>;
}

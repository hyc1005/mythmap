import { useLocale } from '../i18n';
import { ReadingMarks } from '../reading';
import ContentOrigin from './ContentOrigin';
import { entryTypes } from '../entries';

export default function ChapterEntries({ stories, records, naturalEntries = [], passageEntries = [], onOpen, reading, collectionItems }) {
  const { t } = useLocale();
  const storyIds = new Set(stories.map(item => item.id));
  const others = [...new Map([...records, ...naturalEntries].filter(record => !storyIds.has(record.id)).map(record => [record.id, record])).values()];
  const sequence = [...stories, ...others].map(item => item.id);
  const books = [
    { number: 1, title: '南山经 · 全篇阅读', ranges: ['䧿山', '南次二经', '南次三经'] },
    { number: 2, title: '西山经 · 分段阅读', ranges: ['华山山列 · 山段与总括', '西次二经 · 已核山段', '西次三经 · 已核山段', '西次四经 · 山段与总括', '西山经 · 篇末总计'] },
    { number: 3, title: '北山经 · 分段阅读', ranges: ['北山经首列 · 山段与总括', '北次二经 · 山段与总括', '北次三经 · 山段与总括', '北山经 · 篇末总计'] },
  ];
  const list = items => <ul>{items.map(record => <li key={record.id}><button type="button" className="map-entry-button" data-entry-id={record.id} onClick={event => onOpen(record.id, event.currentTarget, sequence)}><b>{record.name}</b><ContentOrigin record={record} /><small>{t(entryTypes[record.kind])}{record.source && ` · ${record.source}`}</small><ReadingMarks reading={reading} id={record.id} /></button></li>)}</ul>;
  return <div className="chapter-entries">
    {books.map(book => {
      const passages = passageEntries.filter(item => (item.source_book || 1) === book.number);
      return passages.length ? <details key={book.number} data-source-book={book.number} className="chapter-text-entries chapter-map-entries"><summary>{t(book.title)} · {passages.length}</summary><p className="entry-reading-hint">{t('按底本山段与总述排列，可任选一段阅读；独立对象仍在逐步建档。')}</p>{book.ranges.map((label, i) => <details key={i} className="passage-range"><summary>{t(label)}</summary><ul>{passages.filter(item => item.range === i + 1).map(item => <li key={item.id}><button type="button" className="map-entry-button" data-entry-id={item.id} onClick={event => onOpen(item.id, event.currentTarget, passages.map(entry => entry.id))}><b>{item.name}</b><small>{item.source_locator}</small><ReadingMarks reading={reading} id={item.id} /></button></li>)}</ul></details>)}</details> : null;
    })}
    <div className="chapter-story-list">{stories.map(item => <button type="button" className="story-entry" data-entry-id={item.id} key={item.id} onClick={event => onOpen(item.id, event.currentTarget, sequence)}><i aria-hidden="true">✦</i><span><b>{item.properties.name}</b><ContentOrigin record={item} /><small>{item.properties.source_text || item.properties.basis_note}</small><ReadingMarks reading={reading} id={item.id} /></span></button>)}</div>
    {!!others.length && <details className="chapter-map-entries"><summary>{t('本章其他条目')} · {others.length}</summary>{others.length <= 30 ? list(others) : Object.entries(entryTypes).map(([kind,label]) => {
      const items=others.filter(item=>item.kind===kind);
      return items.length ? <details className="entry-kind-group" key={kind}><summary>{t(label)} · {items.length}</summary>{list(items)}</details> : null;
    })}</details>}
    <details className="reading-collection chapter-map-entries"><summary>{t('我的收藏')} · {collectionItems.length}</summary>{collectionItems.length ? <ul>{collectionItems.map(item => <li key={item.id}><button type="button" className="map-entry-button" data-collection-id={item.id} onClick={event => onOpen(item.id, event.currentTarget, collectionItems.map(entry => entry.id))}><b>{item.name}</b><ContentOrigin record={item} /><small>{item.source}</small><ReadingMarks reading={reading} id={item.id} /></button></li>)}</ul> : <p className="entry-reading-hint">{t('在条目详情中收藏，即可在这里找回。')}</p>}</details>
    <p className="entry-reading-hint">{t('选择条目，阅读介绍、原文与出处。')}</p>
  </div>;
}

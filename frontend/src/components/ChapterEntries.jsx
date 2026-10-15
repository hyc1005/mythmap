import { useLocale } from '../i18n';
import { ReadingMarks } from '../reading';

export default function ChapterEntries({ stories, records, onOpen, reading, collectionItems }) {
  const { t } = useLocale();
  const storyIds = new Set(stories.map(item => item.id));
  const others = records.filter(record => !storyIds.has(record.id));
  const sequence = [...stories, ...others].map(item => item.id);
  return <div className="chapter-entries">
    <div className="chapter-story-list">{stories.map(item => <button type="button" className="story-entry" data-entry-id={item.id} key={item.id} onClick={event => onOpen(item.id, event.currentTarget, sequence)}><i aria-hidden="true">✦</i><span><b>{item.properties.name}</b><small>{item.properties.source_text || item.properties.basis_note}</small><ReadingMarks reading={reading} id={item.id} /></span></button>)}</div>
    {!!others.length && <details className="chapter-map-entries"><summary>{t('图中其他条目')} · {others.length}</summary><ul>{others.map(record => <li key={record.id}><button type="button" className="map-entry-button" data-entry-id={record.id} onClick={event => onOpen(record.id, event.currentTarget, sequence)}><b>{record.name}</b><small>{t({ story: '故事示意', place: '篇目地点', domain: '神域', beast: '异兽' }[record.kind])}{record.source && ` · ${record.source}`}</small><ReadingMarks reading={reading} id={record.id} /></button></li>)}</ul></details>}
    <details className="reading-collection chapter-map-entries"><summary>{t('我的收藏')} · {collectionItems.length}</summary>{collectionItems.length ? <ul>{collectionItems.map(item => <li key={item.id}><button type="button" className="map-entry-button" data-collection-id={item.id} onClick={event => onOpen(item.id, event.currentTarget, collectionItems.map(entry => entry.id))}><b>{item.name}</b><small>{item.source}</small><ReadingMarks reading={reading} id={item.id} /></button></li>)}</ul> : <p className="entry-reading-hint">{t('在条目详情中收藏，即可在这里找回。')}</p>}</details>
    <p className="entry-reading-hint">{t('选择条目，阅读介绍、原文与出处。')}</p>
  </div>;
}

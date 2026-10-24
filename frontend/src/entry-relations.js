import nanshanRelations from './nanshan-relations.json' with { type: 'json' };
import entityRelations from './nanshan-entity-relations.json' with { type: 'json' };
import xishanRelations from './xishan-relations.json' with { type: 'json' };

export const entryRelations = [
  { ids: ['03-04', 'beast-jingwei'], source: '《北山经》', quote: '女娃游于东海，溺而不返，故为精卫' },
  { ids: ['03-04', 'place-fajiu'], source: '《北山经》', quote: '发鸠之山，其上多柘木。有鸟焉' },
  { ids: ['beast-jingwei', 'place-fajiu'], source: '《北山经》', quote: '发鸠之山，有鸟焉，其状如乌，文首、白喙、赤足，名曰精卫。' },
  ...nanshanRelations,
  ...entityRelations,
  ...xishanRelations,
];

export function relatedEntries(id, index) {
  const explicit = entryRelations.filter(relation => relation.ids.includes(id)).map(relation => {
    const other = index.get(relation.ids.find(value => value !== id));
    return other && { ...other, relationSource: relation.source, relationLabel: relation.labels?.[relation.ids.indexOf(id)], relationQuote: relation.labels ? relation.quote : null };
  }).filter(Boolean);
  const passages = [...index.values()].filter(item => item.kind === 'passage' && item.related_entry_ids?.includes(id));
  const entries = (index.get(id)?.related_entry_ids || []).map(other => index.get(other)).filter(Boolean);
  return [...new Map([...explicit, ...passages, ...entries].map(item => [item.id, { relationSource: item.source_chapter, ...item }])).values()];
}

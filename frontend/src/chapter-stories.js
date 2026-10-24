export function chapterStoryIds(chapterId, catalog, animations, kuafu) {
  if (chapterId === '00') return ['00-opening'];
  const order = catalog.stages.find(stage => stage.id === chapterId)?.event_ids || [];
  const stories = animations.stories.filter(story => story.stage_id === chapterId && !['06-03', '07-journey'].includes(story.id));
  const ids = stories.map(story => ({ id: story.id, eventId: story.source_event_id || story.id }));
  if (kuafu.stage_id === chapterId) ids.push({ id: kuafu.event_id, eventId: kuafu.event_id });
  const rank = id => { const index = order.indexOf(id); return index < 0 ? Number.MAX_SAFE_INTEGER : index; };
  return ids.sort((a, b) => rank(a.eventId) - rank(b.eventId)).map(item => item.id);
}

export function animationForEvent(eventId, catalog, animations, kuafu) {
  const event = catalog.events.find(item => item.id === eventId);
  if (!event || ['archive', 'group'].includes(event.properties.presentation)) return null;
  const available = chapterStoryIds(event.properties.stage_id, catalog, animations, kuafu);
  if (event.properties.stage_id === '00') return '00-opening';
  if (eventId === kuafu.event_id && available.includes(eventId)) return eventId;
  return animations.stories.find(story => (story.source_event_id || story.id) === eventId && available.includes(story.id))?.id || null;
}

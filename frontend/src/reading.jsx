import { useCallback, useEffect, useState } from 'react';
import { useLocale } from './i18n';
import catalog from '../public/data/atlas/catalog.json';
import world from '../public/data/myth-world.json';
import { readExploration } from './exploration';
import { worldEntries } from './entries';

const storageKey = 'shanhai-reading-v1';
const validIds = new Set([...catalog.events, ...worldEntries(world)].map(item => item.id));
const resumeKey = 'shanhai-last-reading-v1';
const anchors = new Set(['start', 'title', 'summary', 'actions', 'description', 'quote', 'original', 'source', 'location', 'notes', 'related', 'contents']);

function parseResume(value) {
  try {
    const data = JSON.parse(value);
    if (data?.version !== 1 || !validIds.has(data.id) || !world.stages.some(stage => stage.id === data.chapter)) return null;
    const query = new URLSearchParams({ chapter: data.chapter, item: data.id });
    if (readExploration(query.toString(), world, catalog).item !== data.id) return null;
    const position = data.position;
    return { version: 1, id: data.id, chapter: data.chapter, position: {
      anchor: anchors.has(position?.anchor) ? position.anchor : 'start',
      fraction: Number.isFinite(position?.fraction) ? Math.max(0, Math.min(1, position.fraction)) : 0,
      originalOpen: position?.originalOpen === true,
    } };
  } catch { return null; }
}

export function useLastReading() {
  const [resume, setResume] = useState(() => {
    try { return parseResume(localStorage.getItem(resumeKey)); } catch { return null; }
  });
  const [saveFailed, setSaveFailed] = useState(false);
  const save = useCallback(record => {
    const next = parseResume(JSON.stringify({ version: 1, ...record }));
    if (!next) return;
    setResume(previous => JSON.stringify(previous) === JSON.stringify(next) ? previous : next);
    try { localStorage.setItem(resumeKey, JSON.stringify(next)); setSaveFailed(false); }
    catch { setSaveFailed(true); }
  }, []);
  useEffect(() => {
    const update = event => {
      if (event.key !== resumeKey && event.key !== null) return;
      try { if (event.storageArea === localStorage) setResume(parseResume(event.newValue)); } catch {}
    };
    window.addEventListener('storage', update);
    return () => window.removeEventListener('storage', update);
  }, []);
  return { resume, save, saveFailed };
}
const empty = () => ({ version: 1, read: [], favorites: [] });
function parse(value) {
  try {
    const data = JSON.parse(value);
    if (data?.version !== 1) return empty();
    const ids = list => Array.isArray(list) ? [...new Set(list.filter(id => validIds.has(id)))] : [];
    return { version: 1, read: ids(data.read), favorites: ids(data.favorites) };
  } catch { return empty(); }
}

export function useReading() {
  const [marks, setMarks] = useState(() => {
    try { return parse(localStorage.getItem(storageKey)); } catch { return empty(); }
  });
  const [saveFailed, setSaveFailed] = useState(false);
  useEffect(() => {
    try { localStorage.setItem(storageKey, JSON.stringify(marks)); setSaveFailed(false); }
    catch { setSaveFailed(true); }
  }, [marks]);
  useEffect(() => {
    const update = event => {
      if (event.key !== storageKey && event.key !== null) return;
      try { if (event.storageArea === localStorage) setMarks(parse(event.newValue)); } catch {}
    };
    window.addEventListener('storage', update);
    return () => window.removeEventListener('storage', update);
  }, []);
  const toggle = useCallback((field, id) => {
    if (!validIds.has(id)) return;
    setMarks(previous => ({ ...previous, [field]: previous[field].includes(id) ? previous[field].filter(item => item !== id) : [...previous[field], id] }));
  }, []);
  return { ...marks, saveFailed, toggleRead: id => toggle('read', id), toggleFavorite: id => toggle('favorites', id) };
}

export function ReadingMarks({ reading, id }) {
  const { t } = useLocale();
  const read = reading.read.includes(id), favorite = reading.favorites.includes(id);
  return (read || favorite) && <span className="reading-marks">{read && <span>{t('已读')}</span>}{favorite && <span>{t('已收藏')}</span>}</span>;
}

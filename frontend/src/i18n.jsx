import { createContext, useContext, useMemo, useState } from 'react';
import english from './locale-en.json';
import content from './locale-content-en.json';

const LocaleContext = createContext(null);
const replacements = Object.entries(english).sort((a, b) => b[0].length - a[0].length);
const textFields = new Set(['name', 'title', 'subtitle', 'label', 'quote', 'source_quote',
  'description', 'direction', 'place_basis', 'source', 'source_text', 'source_chapter',
  'region', 'location_label', 'basis_note', 'note', 'location_note']);

export function translate(text, locale) {
  if (locale !== 'en' || typeof text !== 'string') return text;
  if (english[text]) return english[text];
  return replacements.reduce((value, [from, to]) => value.split(from).join(to), text);
}

export function localize(data, locale) {
  if (locale !== 'en') return data;
  if (typeof data === 'string') return translate(data, locale);
  if (Array.isArray(data)) return data.map(value => localize(value, locale));
  if (!data || typeof data !== 'object') return data;
  const result = Object.fromEntries(Object.entries(data).map(([key, value]) => [key,
    typeof value === 'string' && !textFields.has(key) ? value : localize(value, locale)]));
  if (content[data.id]) {
    const fields = content[data.id];
    for (const key of Object.keys(fields)) {
      if (key in data) result[key] = fields[key];
    }
  }
  if (data.quote || data.source_quote) result.originalQuote = data.quote || data.source_quote;
  if (data.name) result.originalName = data.name;
  return result;
}

function initialLocale() {
  const query = new URLSearchParams(window.location.search).get('lang');
  if (query === 'en' || query === 'zh') return query;
  try { return localStorage.getItem('shanhai-language') === 'en' ? 'en' : 'zh'; }
  catch { return 'zh'; }
}

export function LocaleProvider({ children }) {
  const [locale, setLocaleState] = useState(initialLocale);
  const value = useMemo(() => ({
    locale,
    t: text => translate(text, locale),
    setLocale(next) {
      setLocaleState(next);
      try { localStorage.setItem('shanhai-language', next); } catch {}
      const url = new URL(window.location.href);
      url.searchParams.set('lang', next);
      window.history.replaceState(null, '', url);
    },
  }), [locale]);
  return <LocaleContext.Provider value={value}>{children}</LocaleContext.Provider>;
}

export const useLocale = () => useContext(LocaleContext);

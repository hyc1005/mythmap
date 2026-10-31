import { createContext, useContext, useEffect, useMemo, useState } from 'react';
import english from './locale-en.json';
import content from './locale-content-en.json';

const LocaleContext = createContext(null);
const replacements = Object.entries(english).sort((a, b) => b[0].length - a[0].length);
const asciiKeys = replacements.map(([from]) => from).filter(from => /^[\x00-\x7f]*$/.test(from));
const textFields = new Set(['name', 'title', 'subtitle', 'label', 'quote', 'source_quote', 'source_locator', 'editorial_note', 'content_note', 'artwork_caption',
  'description', 'direction', 'place_basis', 'source', 'source_text', 'source_chapter',
  'region', 'location_label', 'basis_note', 'note', 'location_note']);

export function translate(text, locale) {
  if (locale !== 'en' || typeof text !== 'string') return text;
  if (english[text]) return english[text];
  if (/^[\x00-\x7f]*$/.test(text) && !asciiKeys.some(from => text.includes(from))) return text;
  return replacements.reduce((value, [from, to]) => value.split(from).join(to), text);
}

export function localize(data, locale) {
  if (locale !== 'en') return data;
  if (typeof data === 'string') return translate(data, locale);
  if (Array.isArray(data)) return data.map(value => localize(value, locale));
  if (!data || typeof data !== 'object') return data;
  const fields = content[data.id];
  const result = Object.fromEntries(Object.entries(data).map(([key, value]) => [key,
    fields && Object.hasOwn(fields, key) ? fields[key]
      : key === 'aliases' || typeof value === 'string' && !textFields.has(key) ? value : localize(value, locale)]));
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
  useEffect(() => {
    const restore = () => {
      const next = initialLocale();
      setLocaleState(next);
      try { localStorage.setItem('shanhai-language', next); } catch {}
    };
    window.addEventListener('popstate', restore);
    return () => window.removeEventListener('popstate', restore);
  }, []);
  const value = useMemo(() => ({
    locale,
    t: text => translate(text, locale),
    setLocale(next) {
      setLocaleState(next);
      try { localStorage.setItem('shanhai-language', next); } catch {}
      const url = new URL(window.location.href);
      url.searchParams.set('lang', next);
      window.history.replaceState(window.history.state, '', url);
    },
  }), [locale]);
  return <LocaleContext.Provider value={value}>{children}</LocaleContext.Provider>;
}

export const useLocale = () => useContext(LocaleContext);

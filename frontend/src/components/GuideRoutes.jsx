import { useState } from 'react';
import { useLocale } from '../i18n';
import BlurRevealText from './BlurRevealText';

export default function GuideRoutes({ routes, onOpen }) {
  const { t, locale } = useLocale();
  const [active, setActive] = useState(routes[0]?.id);
  const route = routes.find(item => item.id === active) || routes[0];
  if (!route) return null;
  return <section className="guide-routes" id="routes" aria-labelledby="routes-title">
    <div className="guide-routes-heading">
      <h2 id="routes-title"><BlurRevealText text={t('专题巡山录')} revealKey={`routes:title:${locale}`} /></h2>
      <p><BlurRevealText text={t('按主题串联原文条目；不改变章节顺序，也不启动导览播放。')} revealKey={`routes:intro:${locale}`} variant="intro" /></p>
    </div>
    <div className="guide-route-tabs" role="group" aria-label={t('专题路线')}>
      {routes.map(item => <button type="button" key={item.id} aria-pressed={item.id === route.id} onClick={() => setActive(item.id)}>{item.title[locale] || item.title.zh}</button>)}
    </div>
    <p className="guide-route-intro">{route.intro?.[locale] || route.intro?.zh}</p>
    <ol className="guide-route-stops">{route.stops.map(stop => <li key={stop.entryId}>
      <button type="button" data-route-stop={stop.entryId} onClick={event => onOpen(stop.entryId, event)}>
        <b>{stop.label?.[locale] || stop.label?.zh}</b><small>{t('查看条目')}</small>
      </button>
    </li>)}</ol>
  </section>;
}

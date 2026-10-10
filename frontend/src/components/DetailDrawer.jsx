import { useEffect, useRef } from 'react';
import catalog from '../../public/data/atlas/catalog.json';
import { iconFor } from '../asset-url';

export default function DetailDrawer({ selected, onClose, onOpen, scrollTopRef }) {
  const closeButton = useRef(null);
  const drawer = useRef(null);
  useEffect(() => {
    drawer.current?.scrollTo(0, scrollTopRef.current);
    closeButton.current?.focus({ preventScroll: true });
    return () => { scrollTopRef.current = drawer.current?.scrollTop || 0; };
  }, [selected.id]);
  const keepFocusInDrawer = event => {
    if (event.key !== 'Tab') return;
    const controls = [...drawer.current.querySelectorAll('button:not(:disabled), a[href], input:not(:disabled), select:not(:disabled), textarea:not(:disabled), [tabindex="0"]')].filter(element => element.getClientRects().length);
    const first = controls[0], last = controls.at(-1);
    if (event.shiftKey && (document.activeElement === first || document.activeElement === drawer.current)) {
      event.preventDefault(); last?.focus({ preventScroll: true });
    } else if (!event.shiftKey && (document.activeElement === last || document.activeElement === drawer.current)) {
      event.preventDefault(); first?.focus({ preventScroll: true });
    }
  };
  return <div className="detail-scrim" onClick={onClose}>
    <aside ref={drawer} className="detail-drawer" role="dialog" aria-modal="true" aria-label={selected.name} tabIndex={-1} onKeyDown={keepFocusInDrawer} onClick={event => event.stopPropagation()}>
      <div className="drawer-actions">
        <button ref={closeButton} className="drawer-close" onClick={onClose} aria-label="关闭">×</button></div>
      <span className="intro-overline">{selected.region || selected.source}</span>
      <h2>{selected.name}</h2>
      {iconFor(selected) && <img className="drawer-art" src={iconFor(selected)} alt={`${selected.name}版画插画`} />}
      <blockquote>{selected.quote || selected.description || selected.raw?.properties.source_quote}</blockquote>
      {selected.raw?.properties.parent_event_id && <nav className="story-siblings" aria-label="补天四幕">{catalog.events.filter(item => item.properties.parent_event_id === selected.raw.properties.parent_event_id).map(item => <button key={item.id} aria-current={item.id === selected.id ? 'true' : undefined} onClick={event => onOpen(item.id, event.currentTarget)}>{item.properties.name}</button>)}</nav>}
      <h3>原文出处</h3><p>{selected.source || selected.raw?.properties.source_text}</p>
      {selected.url && <a className="source-link" href={selected.url} target="_blank" rel="noreferrer">打开所引篇章 ↗</a>}
      <h3>{selected.kind === 'story' ? '位置说明' : '方位表达'}</h3>
      <p>{selected.direction || selected.raw?.properties.basis_note}</p>
      <p className="source-caution">{selected.kind === 'story' ? '故事点为叙事锚点·示意，不表示真实地点、距离或未经原文支持的因果关系；插画中的器物与场景属于艺术解释。' : '原文未明示的方位不以图面位置补出；淡墨山海纹样仅为装饰。'}</p>
    </aside>
  </div>;
}

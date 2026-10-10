import { useRef } from 'react';

export default function Timeline({ stages, index, onSelect, playing, onPlay, containerRef }) {
  const slider = useRef(null);
  const lastIndex = stages.length - 1;
  const setFromPointer = event => {
    const rect = slider.current.getBoundingClientRect();
    const value = Math.round(Math.max(0, Math.min(1, (event.clientX - rect.left) / rect.width)) * (stages.length - 1));
    onSelect(value);
  };
  return <section ref={containerRef} className="myth-timeline" aria-label="序章与七章神话时间轴">
    <div className="timeline-current"><button onClick={() => onSelect(Math.max(0, index - 1))} disabled={!index}>‹</button><button onClick={onPlay} aria-label={playing ? '暂停' : '播放'}>{playing ? 'Ⅱ' : '▶'}</button><button onClick={() => onSelect(Math.min(stages.length - 1, index + 1))} disabled={index === stages.length - 1}>›</button><span><small>第 {stages[index].id} 章</small><b>{stages[index].title}</b></span></div>
    <div className="timeline-steps">{stages.map((stage, i) => <button key={stage.id} aria-current={index === i ? 'step' : undefined} onClick={() => onSelect(i)}><i>{stage.id}</i>{stage.title}</button>)}</div>
    <div className="chapter-slider" ref={slider} tabIndex={0} role="slider" aria-valuemin={0} aria-valuemax={lastIndex} aria-valuenow={index} aria-valuetext={`第 ${stages[index].id} 章 ${stages[index].title}`}
      onPointerDown={event => { if (event.button !== 0) return; event.currentTarget.setPointerCapture(event.pointerId); onSelect(index); setFromPointer(event); }}
      onPointerMove={event => { if (event.currentTarget.hasPointerCapture(event.pointerId)) setFromPointer(event); }}
      onPointerUp={event => { if (event.currentTarget.hasPointerCapture(event.pointerId)) { setFromPointer(event); event.currentTarget.releasePointerCapture(event.pointerId); } }}
      onPointerCancel={event => { if (event.currentTarget.hasPointerCapture(event.pointerId)) event.currentTarget.releasePointerCapture(event.pointerId); onSelect(index); }}
      onKeyDown={event => { const next = { ArrowRight: index + 1, ArrowUp: index + 1, ArrowLeft: index - 1, ArrowDown: index - 1, Home: 0, End: lastIndex }[event.key]; if (next !== undefined) { event.preventDefault(); onSelect(Math.max(0, Math.min(lastIndex, next))); } }}>
      <i style={{ width: `${index / lastIndex * 100}%` }} /><span style={{ left: `${index / lastIndex * 100}%` }} />
    </div>
  </section>;
}

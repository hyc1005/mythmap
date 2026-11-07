import { useLayoutEffect, useRef } from 'react';
import './paper-interactions.css';

export default function PaperTabs({ value, children, className = '', ...props }) {
  const ref = useRef(null);
  useLayoutEffect(() => {
    const group = ref.current;
    const update = () => {
      const selected = group.querySelector(':scope > button[aria-pressed="true"]');
      if (!selected || !selected.offsetWidth) {
        group.style.setProperty('--paper-tab-visible', '0');
        return;
      }
      group.style.setProperty('--paper-tab-x', `${selected.offsetLeft}px`);
      group.style.setProperty('--paper-tab-y', `${selected.offsetTop}px`);
      group.style.setProperty('--paper-tab-width', `${selected.offsetWidth}px`);
      group.style.setProperty('--paper-tab-height', `${selected.offsetHeight}px`);
      group.style.setProperty('--paper-tab-visible', '1');
    };
    update();
    const observer = new ResizeObserver(update);
    observer.observe(group);
    for (const button of group.querySelectorAll(':scope > button')) observer.observe(button);
    return () => observer.disconnect();
  }, [value, children]);
  return <div {...props} ref={ref} role="group" className={`paper-tabs ${className}`.trim()}>{children}</div>;
}

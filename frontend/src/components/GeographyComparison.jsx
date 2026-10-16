import { useLocale } from '../i18n';
import { associationLabel } from '../geography';
import GeographicEvidence from './GeographicEvidence';

export default function GeographyComparison({ records, ids, onChange, onClose }) {
  const { t } = useLocale();
  const paired = ids.map(id => records.find(item => item.id === id));
  const sharedSource = paired[0].properties.evidence.some(left => paired[1].properties.evidence.some(right => (left.source_group || left.url) === (right.source_group || right.url)));
  return <section id="geo-comparison" className="geo-comparison" aria-label={t('本事件资料对照')}>
    <div className="geo-compare-heading"><h3>{t('本事件资料对照')}</h3><button onClick={onClose}>{t('关闭对照')}</button></div>
    <p className="geo-note">{t('比较关联说明、出处和位置精度，不给地点排名。对照涵盖本事件全部条目，不受地点搜索影响。')}</p>
    {sharedSource && <p className="geo-note" data-shared-sources>{t('双方部分出处相同，不能把共享引文当作两个独立版本的证据。')}</p>}
    <div className="geo-compare-grid">{ids.map((id, index) => {
      const record = records.find(item => item.id === id);
      return <article key={index} data-comparison-id={id}>
        <label>{t(index === 0 ? '对照条目一' : '对照条目二')}<select aria-label={t(index === 0 ? '对照条目一' : '对照条目二')} value={id} onChange={event => onChange(index, event.target.value)}>
          {records.map(item => <option key={item.id} value={item.id} disabled={item.id === ids[1 - index]}>{t(item.properties.label)} · {t(associationLabel(item))}</option>)}
        </select></label>
        <h4>{t(record.properties.label)}</h4>
        <GeographicEvidence record={record} />
      </article>;
    })}</div>
  </section>;
}

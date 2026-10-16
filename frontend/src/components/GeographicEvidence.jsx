import { useLocale } from '../i18n';
import { associationLabel } from '../geography';

export default function GeographicEvidence({ record }) {
  const { t, locale } = useLocale();
  const info = record.properties;
  return <>
    <p>{t(associationLabel(record))} · {t('不证明事件发生')}</p>
    <p>{t(info.location_precision === 'county_representative' ? '县域代表点，非具体遗址或山顶' : '区域代表点，非精确事件位置')}</p>
    <p>{record.geometry.coordinates.map(number => number.toFixed(3)).join(', ')}° · {t('参考坐标，非事件发生点')}</p>
    <h4>{t('关联说明')}</h4>
    <p>{locale === 'zh' ? info.basis_note : info.basis_note_en || t('坐标核验与历史对应核验分别记录，不能相互替代。')}</p>
    {locale === 'en' && <details className="original-text"><summary>{t('中文位置说明')}</summary><p lang="zh-CN">{info.basis_note}</p></details>}
    <h4>{t('关联依据与核验')}</h4>
    <p>{t(info.evidence_status === 'source_checked' ? '关联资料已核对，历史发生位置未确证。' : '导入的考证候选，关联依据仍待逐条核验。')}</p>
    {info.evidence.map(evidence => <div key={evidence.url}>
      <a href={evidence.url} target="_blank" rel="noreferrer">{locale === 'en' ? evidence.title_en : evidence.title} · {evidence.checked_at}</a>
      {evidence.excerpt && <details className="original-text"><summary>{t('资料原文摘录')}</summary><blockquote lang="zh-CN">{evidence.excerpt}</blockquote></details>}
    </div>)}
    {!info.evidence.length && <p>{t('既有资料索引')} · {(info.source_ids || []).join(', ')}</p>}
    <h4>{t('现代坐标来源')}</h4>
    <a href={info.coordinate_source} target="_blank" rel="noreferrer">{t('坐标来源（OpenStreetMap）')}</a>
  </>;
}

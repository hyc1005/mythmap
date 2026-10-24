import { useLocale } from '../i18n';
import { associationLabel, referenceNarrative } from '../geography';
import ContentOrigin from './ContentOrigin';

export default function GeographicEvidence({ record }) {
  const { t, locale } = useLocale();
  const info = record.properties;
  return <>
    <section className="geo-place-story" aria-label={t('相关传说')}>
      <h4>{t(info.association_type === 'local_tradition' ? '流传在这里的故事' : '相关传说')}</h4>
      <ContentOrigin record={record} />
      <p>{referenceNarrative(record, locale)}</p>
    </section>
    <section className="geo-account" aria-label={t('资料侧重与不足')}>
      <h4>{t('资料侧重与不足')}</h4>
      <p className="geo-note">{t('故事与此地的关联，并不证明传说真实发生，也不能据此确定事件发生地点。')}</p>
      <b>{t(associationLabel(record))}{info.account && <> · {locale === 'en' ? info.account.focus_en : info.account.focus}</>}</b>
      <p>{info.account ? locale === 'en' ? info.account.summary_en : info.account.summary : locale === 'zh' ? info.basis_note : info.basis_note_en || t('现有资料将此地列为故事地望的考证候选，尚未核实历史对应。')}</p>
      {info.account ? <p><strong>{t('不能据此推断')}：</strong>{locale === 'en' ? info.account.limits_en : info.account.limits}</p>
        : <p>{t('以上叙述整理自相关故事，不作为当地独立传说版本；现有地点关联仍待逐条核验。')}</p>}
      <p className="geo-note">{t(info.location_precision === 'county_representative' ? '县域代表点，非具体遗址或山顶' : '区域代表点，非精确事件位置')}</p>
      <p className="geo-note">{t(info.evidence_status === 'source_checked' ? '已核对所列资料；核对范围见各出处，历史位置未确证。' : '导入的考证候选，关联依据仍待逐条核验。')}</p>
    </section>
    <details className="geo-evidence-section" data-evidence-section="quotes"><summary>{t('原文摘录')}</summary>
      {info.evidence.filter(evidence => evidence.excerpt).map(evidence => <div key={evidence.url}>
        <h4>{locale === 'en' ? evidence.title_en : evidence.title}</h4>
        <blockquote className="original-text" lang="zh-CN">{evidence.excerpt}</blockquote>
      </div>)}
      {!info.evidence.some(evidence => evidence.excerpt) && <p>{t('暂无可核对的原文摘录。')}</p>}
    </details>
    <details className="geo-evidence-section" data-evidence-section="sources"><summary>{t('出处与核验状态')}</summary>
      {info.account?.source_urls.map(url => {
        const evidence = info.evidence.find(item => item.url === url);
        return <a key={url} href={url} target="_blank" rel="noreferrer">{t('摘要依据')} · {locale === 'en' ? evidence.title_en : evidence.title}</a>;
      })}
      {info.evidence.map(evidence => <div key={evidence.url}>
        <a href={evidence.url} target="_blank" rel="noreferrer">{locale === 'en' ? evidence.title_en : evidence.title}</a>
        <p className="geo-source-meta">{t(evidence.publisher)}{evidence.published_on && <> · {t('发布')} {evidence.published_on}</>} · {t('核对')} {evidence.checked_at}</p>
        {evidence.locator && <p className="geo-source-meta">{t('定位')}：{locale === 'en' ? evidence.locator_en : evidence.locator}</p>}
        {evidence.review_scope && <p className="geo-source-meta">{t(evidence.review_scope === 'page_text' ? '核对范围：网页正文' : '核对范围：搜索索引片段，原页暂无法完整读取')}</p>}
      </div>)}
      {!info.evidence.length && <p>{t('既有资料索引')} · {(info.source_ids || []).join(', ')}</p>}
    </details>
    <details className="geo-evidence-section" data-evidence-section="coordinates"><summary>{t('坐标与精度依据')}</summary>
      <p>{record.geometry.coordinates.map(number => number.toFixed(3)).join(', ')}° · {t('参考坐标，非事件发生点')}</p>
      <p>{t(info.location_precision === 'county_representative' ? '县域代表点，非具体遗址或山顶' : '区域代表点，非精确事件位置')}</p>
      <a href={info.coordinate_source} target="_blank" rel="noreferrer">{t('坐标来源（OpenStreetMap）')}</a>
    </details>
  </>;
}

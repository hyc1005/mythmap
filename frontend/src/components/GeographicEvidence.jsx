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
    {info.account ? <section className="geo-account" aria-label={t('资料侧重与不足')}>
      <h4>{t('资料侧重与不足')}</h4>
      <b>{locale === 'en' ? info.account.focus_en : info.account.focus}</b>
      <p>{locale === 'en' ? info.account.summary_en : info.account.summary}</p>
      <p><strong>{t('不能据此推断')}：</strong>{locale === 'en' ? info.account.limits_en : info.account.limits}</p>
      {info.account.source_urls.map(url => {
        const evidence = info.evidence.find(item => item.url === url);
        return <a key={url} href={url} target="_blank" rel="noreferrer">{t('摘要依据')} · {locale === 'en' ? evidence.title_en : evidence.title}</a>;
      })}
    </section> : <p className="geo-note">{t('尚无足以整理故事异文的核验资料，不补写版本差异。')}</p>}
    <h4>{t('关联依据与核验')}</h4>
    <p>{t(info.evidence_status === 'source_checked' ? '已核对所列资料；核对范围见各出处，历史位置未确证。' : '导入的考证候选，关联依据仍待逐条核验。')}</p>
    {info.evidence.map(evidence => <div key={evidence.url}>
      <a href={evidence.url} target="_blank" rel="noreferrer">{locale === 'en' ? evidence.title_en : evidence.title}</a>
      <p className="geo-source-meta">{t(evidence.publisher)}{evidence.published_on && <> · {t('发布')} {evidence.published_on}</>} · {t('核对')} {evidence.checked_at}</p>
      {evidence.locator && <p className="geo-source-meta">{t('定位')}：{locale === 'en' ? evidence.locator_en : evidence.locator}</p>}
      {evidence.review_scope && <p className="geo-source-meta">{t(evidence.review_scope === 'page_text' ? '核对范围：网页正文' : '核对范围：搜索索引片段，原页暂无法完整读取')}</p>}
      {evidence.excerpt && <details className="original-text"><summary>{t('资料原文摘录')}</summary><blockquote lang="zh-CN">{evidence.excerpt}</blockquote></details>}
    </div>)}
    {!info.evidence.length && <p>{t('既有资料索引')} · {(info.source_ids || []).join(', ')}</p>}
    <h4>{t('现代坐标来源')}</h4>
    <a href={info.coordinate_source} target="_blank" rel="noreferrer">{t('坐标来源（OpenStreetMap）')}</a>
  </>;
}

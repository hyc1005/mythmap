import { useLocale } from '../i18n';
import { contentOrigin, originLabels } from '../content-provenance';

export default function ContentOrigin({ record }) {
  const { t } = useLocale();
  const origin = contentOrigin(record);
  return <small className="content-origin" data-origin={origin.family}>{t(originLabels[origin.family] || originLabels.pending)}</small>;
}

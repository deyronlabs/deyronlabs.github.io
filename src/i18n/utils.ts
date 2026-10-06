import { ui, type UiKey, type Dict } from './ui';
import { DEFAULT_LANG, ENABLED_LANGS, type Lang } from '../site';

export function useTranslations(lang: Lang) {
  return function t<K extends UiKey>(key: K): Dict[K] {
    return (ui[lang]?.[key] ?? ui[DEFAULT_LANG][key]) as Dict[K];
  };
}

/** Pentru getStaticPaths: doar limbile publicate. */
export const langPaths = () => ENABLED_LANGS.map((lang) => ({ params: { lang } }));

export function formatDate(date: Date, lang: Lang, style: 'long' | 'short' = 'long'): string {
  const opts: Intl.DateTimeFormatOptions =
    style === 'long'
      ? { day: 'numeric', month: 'long', year: 'numeric', timeZone: 'UTC' }
      : { day: 'numeric', month: 'short', timeZone: 'UTC' };
  return new Intl.DateTimeFormat(lang, opts).format(date);
}

export const isoDate = (d: Date) => d.toISOString();

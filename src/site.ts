// Setări globale ale site-ului. Fișier fără dependențe, ca să poată fi testat separat.

export const LOCALES = ['en', 'es'] as const;
export type Lang = (typeof LOCALES)[number];

export const DEFAULT_LANG: Lang = 'en';

// Limbile publicate acum. Pentru lansarea în spaniolă: adaugă 'es' aici
// (traducerile interfeței sunt deja în src/i18n/ui.ts).
export const ENABLED_LANGS: Lang[] = ['en'];

export const OG_LOCALE: Record<Lang, string> = { en: 'en_US', es: 'es_ES' };

export const SITE = {
  url: 'https://deyronlabs.com',
  name: 'Deyron Labs',
  authorName: 'Deyron Labs Editorial Desk',
  contactEmail: 'contact@deyronlabs.com',
  collabEmail: 'collab@deyronlabs.com',
  ogImage: '/og-default.png',
  themeColor: '#1a1a1a',
};

// Verifică aceste adrese înainte de lansare (handle-ul presupus: deyronlabs).
export const SOCIALS = [
  { name: 'YouTube', url: 'https://www.youtube.com/@deyronlabs' },
  { name: 'X', url: 'https://x.com/deyronlabs' },
  { name: 'Instagram', url: 'https://www.instagram.com/deyronlabs' },
  { name: 'TikTok', url: 'https://www.tiktok.com/@deyronlabs' },
  { name: 'Facebook', url: 'https://www.facebook.com/deyronlabs' },
];

export const absUrl = (path: string): string => new URL(path, SITE.url).toString();

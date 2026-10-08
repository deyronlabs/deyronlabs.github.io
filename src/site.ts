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

// Pagina de susținere (donații voluntare). Nu intră în SOCIALS, ca să nu apară în schema sameAs.
export const SUPPORT = {
  kofiUrl: 'https://ko-fi.com/deyronlabs',
};

// Newsletter „The Lab Report” (beehiiv, plan gratuit). Abonarea se face pe pagina găzduită de beehiiv:
// pe site nu se încarcă niciun script sau formular de la ei, doar un link.
export const NEWSLETTER = {
  name: 'The Lab Report',
  url: 'https://deyronlabs.beehiiv.com/',
};

// Adresele conturilor oficiale (confirmate de proprietar).
export const SOCIALS = [
  { name: 'YouTube', icon: 'youtube', url: 'https://www.youtube.com/@deyronlabs' },
  { name: 'X', icon: 'x', url: 'https://x.com/deyronlabs' },
  { name: 'Instagram', icon: 'instagram', url: 'https://www.instagram.com/deyronlabs/' },
  { name: 'TikTok', icon: 'tiktok', url: 'https://www.tiktok.com/@deyronlabs' },
  { name: 'Facebook', icon: 'facebook', url: 'https://www.facebook.com/deyronlabs/' },
  { name: 'Threads', icon: 'threads', url: 'https://www.threads.com/@deyronlabs' },
  { name: 'LinkedIn', icon: 'linkedin', url: 'https://www.linkedin.com/company/deyronlabs/' },
  { name: 'Pinterest', icon: 'pinterest', url: 'https://www.pinterest.com/deyronlabs/' },
  { name: 'Reddit', icon: 'reddit', url: 'https://www.reddit.com/user/DeyronLabs/' },
];

export const absUrl = (path: string): string => new URL(path, SITE.url).toString();

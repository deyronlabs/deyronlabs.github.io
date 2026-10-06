// Funcții pure pentru SEO / schema.org (fără dependențe de Astro, ca să poată fi testate).
import { SITE, absUrl, type Lang } from '../site';

export interface Alternate {
  lang: Lang;
  path: string;
}

export interface ArticleLd {
  title: string;
  summary: string;
  lang: Lang;
  path: string;
  publishedAt: Date;
  updatedAt?: Date;
  sources: { title: string; url: string; publisher?: string; primary?: boolean }[];
  entities: string[];
  topics: string[];
  video?: string;
}

const ORG_ID = `${SITE.url}/#organization`;

export function organizationLd(socials: string[]) {
  return {
    '@type': 'Organization',
    '@id': ORG_ID,
    name: SITE.name,
    url: SITE.url,
    logo: absUrl('/favicon.svg'),
    email: SITE.contactEmail,
    sameAs: socials,
  };
}

export function websiteLd(lang: Lang) {
  return {
    '@type': 'WebSite',
    '@id': `${SITE.url}/#website`,
    url: SITE.url,
    name: SITE.name,
    inLanguage: lang,
    publisher: { '@id': ORG_ID },
  };
}

export function authorLd(lang: Lang) {
  return {
    '@type': 'Organization',
    '@id': `${SITE.url}/#editorial-desk`,
    name: SITE.authorName,
    url: absUrl(`/${lang}/author/deyron-labs/`),
    parentOrganization: { '@id': ORG_ID },
  };
}

export function newsArticleLd(a: ArticleLd) {
  const url = absUrl(a.path);
  return {
    '@type': 'NewsArticle',
    '@id': `${url}#article`,
    headline: a.title,
    description: a.summary,
    inLanguage: a.lang,
    datePublished: a.publishedAt.toISOString(),
    dateModified: (a.updatedAt ?? a.publishedAt).toISOString(),
    mainEntityOfPage: { '@type': 'WebPage', '@id': url },
    url,
    image: [absUrl(SITE.ogImage)],
    isAccessibleForFree: true,
    author: { '@id': `${SITE.url}/#editorial-desk` },
    publisher: { '@id': ORG_ID },
    ...(a.topics.length ? { keywords: a.topics.join(', ') } : {}),
    ...(a.entities.length ? { about: a.entities.map((name) => ({ '@type': 'Thing', name })) } : {}),
    citation: a.sources.map((s) => ({
      '@type': 'CreativeWork',
      name: s.title,
      url: s.url,
      ...(s.publisher ? { publisher: { '@type': 'Organization', name: s.publisher } } : {}),
    })),
    ...(a.video ? { video: { '@type': 'VideoObject', name: a.title, description: a.summary, embedUrl: a.video, uploadDate: a.publishedAt.toISOString(), thumbnailUrl: absUrl(SITE.ogImage) } } : {}),
  };
}

/** Un singur <script type="application/ld+json"> cu @graph. */
export function serializeJsonLd(nodes: object[]): string {
  return JSON.stringify({ '@context': 'https://schema.org', '@graph': nodes }).replace(
    /</g,
    '\\u003c',
  );
}

/** Versiunile pe limbi ale unei pagini statice, ex. staticAlternates(['en'], 'about/'). */
export function staticAlternates(langs: Lang[], sub: string): Alternate[] {
  return langs.map((lang) => ({ lang, path: `/${lang}/${sub}` }));
}

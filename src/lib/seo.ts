// Funcții pure pentru SEO / schema.org (fără dependențe de Astro, ca să poată fi testate).
import { SITE, absUrl, type Lang } from '../site';
import { youtubeId, schemaEmbedUrl } from './video';

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
  videoPublishedAt?: Date;
  image?: string;
}

const ORG_ID = `${SITE.url}/#organization`;

export function organizationLd(socials: string[]) {
  return {
    '@type': 'Organization',
    '@id': ORG_ID,
    name: SITE.name,
    url: SITE.url,
    logo: absUrl('/logo.png'),
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

function videoLd(a: ArticleLd) {
  const id = a.video ? youtubeId(a.video) : null;
  if (!id) return null;
  return {
    '@type': 'VideoObject',
    name: a.title,
    description: a.summary,
    embedUrl: schemaEmbedUrl(id),
    thumbnailUrl: [absUrl(a.image ?? SITE.ogImage)],
    uploadDate: (a.videoPublishedAt ?? a.publishedAt).toISOString(),
    inLanguage: a.lang,
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
    image: [absUrl(a.image ?? SITE.ogImage)],
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
    ...(videoLd(a) ? { video: videoLd(a) } : {}),
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

export interface LabLd {
  title: string;
  summary: string;
  lang: Lang;
  path: string;
  publishedAt: Date;
  updatedAt?: Date;
  video: string;
  durationSeconds: number;
  image: string;
  tools: string[];
  topics: string[];
  chapters: { at: number; title: string }[];
}

/** Episod Lab Sessions: articol-ghid cu VideoObject (și capitole) atașat. */
export function labEpisodeLd(a: LabLd) {
  const url = absUrl(a.path);
  const id = youtubeId(a.video);
  const m = Math.floor(a.durationSeconds / 60);
  const duration = `PT${m}M${a.durationSeconds % 60}S`;
  const video = id
    ? {
        '@type': 'VideoObject',
        '@id': `${url}#video`,
        name: a.title,
        description: a.summary,
        embedUrl: schemaEmbedUrl(id),
        contentUrl: `https://www.youtube.com/watch?v=${id}`,
        thumbnailUrl: [absUrl(a.image)],
        uploadDate: a.publishedAt.toISOString(),
        duration,
        inLanguage: a.lang,
        hasPart: a.chapters.map((c, i) => ({
          '@type': 'Clip',
          name: c.title,
          startOffset: c.at,
          endOffset: a.chapters[i + 1]?.at ?? a.durationSeconds,
          url: `https://www.youtube.com/watch?v=${id}&t=${c.at}s`,
        })),
      }
    : null;
  return [
    {
      '@type': 'TechArticle',
      '@id': `${url}#article`,
      headline: a.title,
      description: a.summary,
      inLanguage: a.lang,
      datePublished: a.publishedAt.toISOString(),
      dateModified: (a.updatedAt ?? a.publishedAt).toISOString(),
      mainEntityOfPage: { '@type': 'WebPage', '@id': url },
      url,
      image: [absUrl(a.image)],
      isAccessibleForFree: true,
      author: { '@id': `${SITE.url}/#editorial-desk` },
      publisher: { '@id': ORG_ID },
      ...(a.topics.length ? { keywords: a.topics.join(', ') } : {}),
      ...(a.tools.length ? { about: a.tools.map((name) => ({ '@type': 'SoftwareApplication', name })) } : {}),
      ...(video ? { video: { '@id': `${url}#video` } } : {}),
    },
    ...(video ? [video] : []),
  ];
}

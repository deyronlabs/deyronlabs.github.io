// Generatoare pure pentru sitemap.xml, RSS, robots.txt și llms.txt.
import { SITE, absUrl, type Lang } from '../site';

export const xmlEscape = (s: string): string =>
  s
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;');

export interface SitemapEntry {
  path: string;
  lang: Lang;
  lastmod?: Date;
  alternates?: { lang: Lang; path: string }[];
}

export function buildSitemap(entries: SitemapEntry[], defaultLang: Lang): string {
  const rows = entries.map((e) => {
    const alts = e.alternates ?? [];
    const links = alts.length > 1 || (alts.length === 1 && alts[0].path !== e.path)
      ? [
          ...alts.map(
            (a) =>
              `    <xhtml:link rel="alternate" hreflang="${a.lang}" href="${xmlEscape(absUrl(a.path))}"/>`,
          ),
          ...alts
            .filter((a) => a.lang === defaultLang)
            .map(
              (a) =>
                `    <xhtml:link rel="alternate" hreflang="x-default" href="${xmlEscape(absUrl(a.path))}"/>`,
            ),
        ].join('\n')
      : '';
    return [
      '  <url>',
      `    <loc>${xmlEscape(absUrl(e.path))}</loc>`,
      e.lastmod ? `    <lastmod>${e.lastmod.toISOString()}</lastmod>` : '',
      links,
      '  </url>',
    ]
      .filter(Boolean)
      .join('\n');
  });
  return `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
${rows.join('\n')}
</urlset>
`;
}

export interface RssItem {
  title: string;
  path: string;
  summary: string;
  publishedAt: Date;
  topics?: string[];
}

export function buildRss(opts: {
  lang: Lang;
  title: string;
  description: string;
  selfPath: string;
  homePath: string;
  items: RssItem[];
}): string {
  const last = opts.items[0]?.publishedAt ?? new Date(0);
  const items = opts.items
    .map((i) =>
      [
        '    <item>',
        `      <title>${xmlEscape(i.title)}</title>`,
        `      <link>${xmlEscape(absUrl(i.path))}</link>`,
        `      <guid isPermaLink="true">${xmlEscape(absUrl(i.path))}</guid>`,
        `      <pubDate>${i.publishedAt.toUTCString()}</pubDate>`,
        `      <description>${xmlEscape(i.summary)}</description>`,
        ...(i.topics ?? []).map((t) => `      <category>${xmlEscape(t)}</category>`),
        '    </item>',
      ].join('\n'),
    )
    .join('\n');
  return `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>${xmlEscape(opts.title)}</title>
    <link>${xmlEscape(absUrl(opts.homePath))}</link>
    <description>${xmlEscape(opts.description)}</description>
    <language>${opts.lang}</language>
    <lastBuildDate>${last.toUTCString()}</lastBuildDate>
    <atom:link href="${xmlEscape(absUrl(opts.selfPath))}" rel="self" type="application/rss+xml"/>
${items}
  </channel>
</rss>
`;
}

// Crawlere AI permise explicit (pe lângă regula generală).
export const AI_CRAWLERS = [
  'GPTBot',
  'OAI-SearchBot',
  'ChatGPT-User',
  'ClaudeBot',
  'Claude-User',
  'Claude-SearchBot',
  'anthropic-ai',
  'PerplexityBot',
  'Perplexity-User',
  'Google-Extended',
  'Googlebot',
  'Bingbot',
  'Applebot',
  'Applebot-Extended',
  'Amazonbot',
  'meta-externalagent',
  'CCBot',
  'xAI-Bot',
  'Grok',
  'DuckAssistBot',
  'cohere-ai',
];

export function buildRobots(): string {
  const blocks = AI_CRAWLERS.map((ua) => `User-agent: ${ua}\nAllow: /\n`).join('\n');
  return `# Deyron Labs: tot conținutul este public și poate fi citat de motoare de căutare și răspuns AI.
User-agent: *
Allow: /

${blocks}
Sitemap: ${absUrl('/sitemap.xml')}
`;
}

export interface LlmsItem {
  title: string;
  path: string;
  summary: string;
}

export function buildLlms(opts: {
  pages: { title: string; path: string; note: string }[];
  articles: LlmsItem[];
}): string {
  const pages = opts.pages
    .map((p) => `- [${p.title}](${absUrl(p.path)}): ${p.note}`)
    .join('\n');
  const articles = opts.articles.length
    ? opts.articles.map((a) => `- [${a.title}](${absUrl(a.path)}): ${a.summary.replace(/\s+/g, ' ')}`).join('\n')
    : '- No stories published yet.';
  return `# ${SITE.name}

> ${SITE.name} is an independent AI news publication. Each story opens with a 2-3 sentence summary, has sections "What happened", "Key details", "Why it matters" and "Sources", shows publication and update dates, and links its primary source. Stories are written with AI assistance and checked by editors before publication.

## Key pages

${pages}

## Latest stories

${articles}

## Feeds

- [RSS feed](${absUrl('/en/rss.xml')}): newest stories
- [Sitemap](${absUrl('/sitemap.xml')}): all pages, with hreflang alternates
`;
}

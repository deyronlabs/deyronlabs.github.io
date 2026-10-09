import type { APIRoute } from 'astro';
import { DEFAULT_LANG, ENABLED_LANGS } from '../site';
import { getAllEnabledEpisodes, episodeUrlPath } from '../lib/lab';
import { getAllEnabledArticles, getTranslations, lastChange, pathOf } from '../lib/articles';
import { getTopicGroups, topicPath } from '../lib/topics';
import { buildSitemap, type SitemapEntry } from '../lib/feeds';

export const GET: APIRoute = async () => {
  const articles = await getAllEnabledArticles();
  const newest = articles.length ? lastChange(articles.reduce((a, b) => (lastChange(a) > lastChange(b) ? a : b))) : undefined;

  const entries: SitemapEntry[] = [];
  for (const sub of ['', 'news/', 'lab-sessions/', 'about/', 'author/deyron-labs/', 'support/', 'sponsors/', 'privacy/']) {
    const alternates = ENABLED_LANGS.map((lang) => ({ lang, path: `/${lang}/${sub}` }));
    for (const lang of ENABLED_LANGS) {
      entries.push({
        lang,
        path: sub === '' && lang === DEFAULT_LANG ? '/' : `/${lang}/${sub}`,
        alternates,
        lastmod: sub === '' || sub === 'news/' ? newest : undefined,
      });
    }
  }
  for (const lang of ENABLED_LANGS) {
    entries.push({ lang, path: `/${lang}/topics/`, alternates: ENABLED_LANGS.map((l) => ({ lang: l, path: `/${l}/topics/` })), lastmod: newest });
    for (const g of await getTopicGroups(lang)) {
      entries.push({ lang, path: topicPath(lang, g.def.slug), alternates: [{ lang, path: topicPath(lang, g.def.slug) }], lastmod: lastChange(g.articles[0]) });
    }
  }
  for (const a of articles) {
    const translations = await getTranslations(a);
    entries.push({
      lang: a.data.lang,
      path: pathOf(a),
      lastmod: lastChange(a),
      alternates: [a, ...translations].map((x) => ({ lang: x.data.lang, path: pathOf(x) })),
    });
  }
  for (const e of await getAllEnabledEpisodes()) {
    entries.push({
      lang: e.data.lang,
      path: episodeUrlPath(e),
      lastmod: e.data.updatedAt ?? e.data.publishedAt,
      alternates: [{ lang: e.data.lang, path: episodeUrlPath(e) }],
    });
  }
  return new Response(buildSitemap(entries, DEFAULT_LANG), {
    headers: { 'Content-Type': 'application/xml; charset=utf-8' },
  });
};

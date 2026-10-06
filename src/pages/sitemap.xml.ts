import type { APIRoute } from 'astro';
import { DEFAULT_LANG, ENABLED_LANGS } from '../site';
import { getAllEnabledArticles, getTranslations, lastChange, pathOf } from '../lib/articles';
import { buildSitemap, type SitemapEntry } from '../lib/feeds';

export const GET: APIRoute = async () => {
  const articles = await getAllEnabledArticles();
  const newest = articles.length ? lastChange(articles.reduce((a, b) => (lastChange(a) > lastChange(b) ? a : b))) : undefined;

  const entries: SitemapEntry[] = [];
  for (const sub of ['', 'news/', 'about/', 'author/deyron-labs/']) {
    const alternates = ENABLED_LANGS.map((lang) => ({ lang, path: `/${lang}/${sub}` }));
    for (const lang of ENABLED_LANGS) {
      entries.push({
        lang,
        path: `/${lang}/${sub}`,
        alternates,
        lastmod: sub === '' || sub === 'news/' ? newest : undefined,
      });
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
  return new Response(buildSitemap(entries, DEFAULT_LANG), {
    headers: { 'Content-Type': 'application/xml; charset=utf-8' },
  });
};

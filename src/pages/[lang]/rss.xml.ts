import type { APIRoute } from 'astro';
import { SITE, type Lang } from '../../site';
import { langPaths, useTranslations } from '../../i18n/utils';
import { getArticles, pathOf } from '../../lib/articles';
import { buildRss } from '../../lib/feeds';

export function getStaticPaths() {
  return langPaths();
}

export const GET: APIRoute = async ({ params }) => {
  const lang = params.lang as Lang;
  const t = useTranslations(lang);
  const articles = (await getArticles(lang)).slice(0, 50);
  const xml = buildRss({
    lang,
    title: SITE.name,
    description: t('meta.home.description'),
    selfPath: `/${lang}/rss.xml`,
    homePath: `/${lang}/`,
    items: articles.map((a) => ({
      title: a.data.title,
      path: pathOf(a),
      summary: a.data.summary,
      publishedAt: a.data.publishedAt,
      topics: a.data.topics,
    })),
  });
  return new Response(xml, { headers: { 'Content-Type': 'application/rss+xml; charset=utf-8' } });
};

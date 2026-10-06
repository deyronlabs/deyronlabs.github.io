// /covers/<lang>/<slug>.png — copertă generată pentru articolele fără `image`.
import type { APIRoute } from 'astro';
import { ENABLED_LANGS, type Lang } from '../../../site';
import { getArticles, slugOf } from '../../../lib/articles';
import { formatDate } from '../../../i18n/utils';
import { renderCover } from '../../../lib/cover';

export async function getStaticPaths() {
  const paths = [];
  for (const lang of ENABLED_LANGS) {
    for (const a of await getArticles(lang)) {
      if (a.data.image) continue;
      paths.push({ params: { lang, slug: slugOf(a) }, props: { article: a } });
    }
  }
  return paths;
}

export const GET: APIRoute = async ({ props }) => {
  const { article } = props as { article: Awaited<ReturnType<typeof getArticles>>[number] };
  const d = article.data;
  const png = await renderCover({
    title: d.title,
    kicker: d.topics[0],
    date: formatDate(d.publishedAt, d.lang as Lang),
  });
  return new Response(new Uint8Array(png), { headers: { 'Content-Type': 'image/png' } });
};

import type { APIRoute } from 'astro';
import type { Lang } from '../../site';
import { langPaths } from '../../i18n/utils';
import { getArticles, pathOf } from '../../lib/articles';
import { getEpisodes, episodeUrlPath } from '../../lib/lab';

export function getStaticPaths() {
  return langPaths();
}

// Index de căutare pentru pagina /<lang>/search/ (căutarea rulează în browser, fără servicii externe).
// k = tip (n = știre, l = Lab Session), t = titlu, s = rezumat, u = adresă, d = dată, x = cuvinte-cheie.
export const GET: APIRoute = async ({ params }) => {
  const lang = params.lang as Lang;
  const [articles, episodes] = await Promise.all([getArticles(lang), getEpisodes(lang)]);
  const items = [
    ...episodes.map((e) => ({
      k: 'l',
      t: e.data.title,
      s: e.data.summary,
      u: episodeUrlPath(e),
      d: e.data.publishedAt.toISOString().slice(0, 10),
      x: [...e.data.tools, ...e.data.topics].join(' '),
    })),
    ...articles.map((a) => ({
      k: 'n',
      t: a.data.title,
      s: a.data.summary,
      u: pathOf(a),
      d: a.data.publishedAt.toISOString().slice(0, 10),
      x: [...a.data.entities, ...a.data.topics].join(' '),
    })),
  ];
  return new Response(JSON.stringify(items), {
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
  });
};

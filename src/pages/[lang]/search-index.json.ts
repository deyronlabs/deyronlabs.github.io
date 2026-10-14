import type { APIRoute } from 'astro';
import type { Lang } from '../../site';
import { langPaths } from '../../i18n/utils';
import { getArticles, pathOf } from '../../lib/articles';
import { getEpisodes, episodeUrlPath } from '../../lib/lab';
import { getInfraEpisodes, infraUrlPath } from '../../lib/infra';

export function getStaticPaths() {
  return langPaths();
}

// Index de căutare pentru pagina /<lang>/search/ (căutarea rulează în browser, fără servicii externe).
// k = tip (n = știre, l = Lab Session, i = AI Infrastructure), t = titlu, s = rezumat, u = adresă, d = dată, x = cuvinte-cheie.
export const GET: APIRoute = async ({ params }) => {
  const lang = params.lang as Lang;
  const [articles, episodes, infra] = await Promise.all([getArticles(lang), getEpisodes(lang), getInfraEpisodes(lang)]);
  const items = [
    ...infra.map((e) => ({
      k: 'i',
      t: e.data.title,
      s: e.data.summary,
      u: infraUrlPath(e),
      d: e.data.publishedAt.toISOString().slice(0, 10),
      x: [...e.data.entities, ...e.data.topics].join(' '),
    })),
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

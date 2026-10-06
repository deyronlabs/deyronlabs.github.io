import type { APIRoute } from 'astro';
import { DEFAULT_LANG } from '../site';
import { ui } from '../i18n/ui';
import { getArticles, pathOf } from '../lib/articles';
import { buildLlms } from '../lib/feeds';

export const GET: APIRoute = async () => {
  const lang = DEFAULT_LANG;
  const t = ui[lang];
  const articles = (await getArticles(lang)).slice(0, 30);
  const body = buildLlms({
    pages: [
      { title: t['nav.news'], path: `/${lang}/news/`, note: 'all stories, newest first' },
      { title: t['about.title'], path: `/${lang}/about/`, note: 'how stories are made, corrections policy, contact' },
      { title: t['author.title'], path: `/${lang}/author/deyron-labs/`, note: 'the editorial desk behind every story' },
    ],
    articles: articles.map((a) => ({ title: a.data.title, path: pathOf(a), summary: a.data.summary })),
  });
  return new Response(body, { headers: { 'Content-Type': 'text/plain; charset=utf-8' } });
};

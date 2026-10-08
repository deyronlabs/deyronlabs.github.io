import type { APIRoute } from 'astro';
import { DEFAULT_LANG } from '../site';
import { ui } from '../i18n/ui';
import { getArticles, pathOf } from '../lib/articles';
import { getEpisodes, episodeUrlPath } from '../lib/lab';
import { buildLlms } from '../lib/feeds';

export const GET: APIRoute = async () => {
  const lang = DEFAULT_LANG;
  const t = ui[lang];
  const articles = (await getArticles(lang)).slice(0, 30);
  const body = buildLlms({
    pages: [
      { title: t['nav.news'], path: `/${lang}/news/`, note: 'all stories, newest first' },
      { title: t['lab.title'], path: `/${lang}/lab-sessions/`, note: 'step-by-step video tutorials for AI tools, each with a written guide' },
      { title: t['about.title'], path: `/${lang}/about/`, note: 'how stories are made, corrections policy, contact' },
      { title: t['author.title'], path: `/${lang}/author/deyron-labs/`, note: 'the editorial desk behind every story' },
      { title: t['sponsors.title'], path: `/${lang}/sponsors/`, note: 'independence rules for sponsors and partners' },
      { title: t['support.title'], path: `/${lang}/support/`, note: 'how reader support works and what it does not buy' },
      { title: t['privacy.title'], path: `/${lang}/privacy/`, note: 'what the site collects and which third-party services are involved' },
    ],
    articles: [
      ...(await getEpisodes(lang)).map((e) => ({ title: `Lab Sessions #${e.data.episode}: ${e.data.title}`, path: episodeUrlPath(e), summary: e.data.summary })),
      ...articles.map((a) => ({ title: a.data.title, path: pathOf(a), summary: a.data.summary })),
    ],
  });
  return new Response(body, { headers: { 'Content-Type': 'text/plain; charset=utf-8' } });
};

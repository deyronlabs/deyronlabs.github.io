import { getCollection, type CollectionEntry } from 'astro:content';
import { ENABLED_LANGS, type Lang } from '../site';

export type Article = CollectionEntry<'news'>;

/** "en/my-story" -> "my-story" */
export const slugOf = (a: Article): string => a.id.split('/').pop()!.replace(/\.md$/, '');

export const articlePath = (lang: Lang, slug: string): string => `/${lang}/news/${slug}/`;

export const pathOf = (a: Article): string => articlePath(a.data.lang, slugOf(a));

const visible = (a: Article) => import.meta.env.DEV || !a.data.draft;

export async function getArticles(lang: Lang): Promise<Article[]> {
  const all = await getCollection('news', (a) => a.data.lang === lang && visible(a));
  return all.sort((a, b) => b.data.publishedAt.valueOf() - a.data.publishedAt.valueOf());
}

export async function getAllEnabledArticles(): Promise<Article[]> {
  const all = await getCollection(
    'news',
    (a) => ENABLED_LANGS.includes(a.data.lang) && visible(a),
  );
  return all.sort((a, b) => b.data.publishedAt.valueOf() - a.data.publishedAt.valueOf());
}

/** Versiunile în alte limbi ale aceluiași articol (după translationKey), doar limbi active. */
export async function getTranslations(article: Article): Promise<Article[]> {
  const key = article.data.translationKey;
  if (!key) return [];
  const all = await getAllEnabledArticles();
  return all.filter((a) => a.data.translationKey === key && a.data.lang !== article.data.lang);
}

export const lastChange = (a: Article): Date => a.data.updatedAt ?? a.data.publishedAt;

/** Actualizat vizibil doar dacă schimbarea e la cel puțin o oră după publicare. */
export const wasUpdated = (a: Article): boolean =>
  !!a.data.updatedAt && a.data.updatedAt.valueOf() - a.data.publishedAt.valueOf() > 3600_000;

/** Imaginea de partajare: cea proprie sau coperta generată automat. */
export const shareImageOf = (a: Article): string =>
  a.data.image ?? `/covers/${a.data.lang}/${slugOf(a)}.png`;

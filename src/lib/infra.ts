import { getCollection, type CollectionEntry } from 'astro:content';
import { ENABLED_LANGS, type Lang } from '../site';

// Ajutoare pentru rubrica AI Infrastructure (aceeași formă ca src/lib/lab.ts).
export type InfraEpisode = CollectionEntry<'infra'>;

export const infraSlug = (e: InfraEpisode): string => e.id.split('/').pop()!.replace(/\.md$/, '');
export const infraPath = (lang: Lang, slug: string): string => `/${lang}/ai-infrastructure/${slug}/`;
export const infraUrlPath = (e: InfraEpisode): string => infraPath(e.data.lang, infraSlug(e));

const visible = (e: InfraEpisode) => import.meta.env.DEV || !e.data.draft;

export async function getInfraEpisodes(lang: Lang): Promise<InfraEpisode[]> {
  const all = await getCollection('infra', (e) => e.data.lang === lang && visible(e));
  return all.sort((a, b) => b.data.episode - a.data.episode);
}

export async function getAllEnabledInfraEpisodes(): Promise<InfraEpisode[]> {
  const all = await getCollection('infra', (e) => ENABLED_LANGS.includes(e.data.lang) && visible(e));
  return all.sort((a, b) => b.data.episode - a.data.episode);
}

/** Ultima modificare a unui episod: cea mai recentă dată din `updatedAt` și din jurnalul de actualizări. */
export function infraLastChange(e: InfraEpisode): Date {
  const dates = [e.data.publishedAt, e.data.updatedAt, ...e.data.updates.map((u) => u.date)].filter(
    (d): d is Date => d instanceof Date,
  );
  return dates.reduce((a, b) => (a > b ? a : b));
}

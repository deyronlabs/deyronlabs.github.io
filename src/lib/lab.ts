import { getCollection, type CollectionEntry } from 'astro:content';
import { ENABLED_LANGS, type Lang } from '../site';
import { youtubeId } from './video';

export type Episode = CollectionEntry<'lab'>;

export const episodeSlug = (e: Episode): string => e.id.split('/').pop()!.replace(/\.md$/, '');
export const episodePath = (lang: Lang, slug: string): string => `/${lang}/lab-sessions/${slug}/`;
export const episodeUrlPath = (e: Episode): string => episodePath(e.data.lang, episodeSlug(e));

const visible = (e: Episode) => import.meta.env.DEV || !e.data.draft;

export async function getEpisodes(lang: Lang): Promise<Episode[]> {
  const all = await getCollection('lab', (e) => e.data.lang === lang && visible(e));
  return all.sort((a, b) => b.data.episode - a.data.episode);
}

export async function getAllEnabledEpisodes(): Promise<Episode[]> {
  const all = await getCollection('lab', (e) => ENABLED_LANGS.includes(e.data.lang) && visible(e));
  return all.sort((a, b) => b.data.episode - a.data.episode);
}

/** "1:29" -> 89 */
export const toSeconds = (t: string): number => {
  const [m, s] = t.split(':').map(Number);
  return m * 60 + s;
};

/** Adresa YouTube pentru un moment din videoclip. */
export function videoAt(video: string, seconds: number): string {
  const id = youtubeId(video);
  return id ? `https://www.youtube.com/watch?v=${id}&t=${seconds}s` : video;
}

export const isoDuration = (secs: number): string => {
  const m = Math.floor(secs / 60);
  const s = secs % 60;
  return `PT${m}M${s}S`;
};

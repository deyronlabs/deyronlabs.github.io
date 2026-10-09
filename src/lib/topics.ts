import type { Lang } from '../site';
import { getArticles, type Article } from './articles';

// Temele din frontmatter sunt libere; aici se grupează în teme canonice (cu pagină proprie).
// O etichetă care nu apare în `aliases` rămâne text simplu. Pagina unei teme se generează doar dacă are cel puțin MIN_TOPIC_ARTICLES articole.
export const MIN_TOPIC_ARTICLES = 2;

export interface TopicDef {
  slug: string;
  label: Record<Lang, string>;
  aliases: string[];
}

export const TOPICS: TopicDef[] = [
  { slug: 'models', label: { en: 'AI models', es: 'Modelos de IA' }, aliases: ['Models', 'Small models', 'Generative AI'] },
  { slug: 'open-weight', label: { en: 'Open-weight models', es: 'Modelos de pesos abiertos' }, aliases: ['Open weights', 'Open-weight', 'Open source'] },
  { slug: 'policy', label: { en: 'Policy and regulation', es: 'Política y regulación' }, aliases: ['Policy', 'Government', 'Standards', 'Europe'] },
  { slug: 'research', label: { en: 'Research', es: 'Investigación' }, aliases: ['Research', 'Science', 'Mathematics', 'Reasoning', 'Publishing'] },
  { slug: 'products', label: { en: 'Products and apps', es: 'Productos y apps' }, aliases: ['Products', 'ChatGPT', 'Free tier', 'Education', 'Games', 'Ads', 'Business'] },
  { slug: 'safety', label: { en: 'Safety and trust', es: 'Seguridad y confianza' }, aliases: ['Safety', 'AI safety', 'Misuse', 'Provenance'] },
  { slug: 'security', label: { en: 'Cybersecurity', es: 'Ciberseguridad' }, aliases: ['Security', 'Cybersecurity'] },
  { slug: 'pricing', label: { en: 'Pricing and funding', es: 'Precios y financiación' }, aliases: ['Pricing', 'Funding', 'API'] },
  { slug: 'agents', label: { en: 'AI agents', es: 'Agentes de IA' }, aliases: ['Agents', 'AI agents'] },
  { slug: 'embeddings', label: { en: 'Embeddings and retrieval', es: 'Embeddings y recuperación' }, aliases: ['Embeddings', 'Retrieval'] },
  { slug: 'coding', label: { en: 'AI for coding', es: 'IA para programar' }, aliases: ['Coding'] },
  { slug: 'hardware', label: { en: 'Hardware and devices', es: 'Hardware y dispositivos' }, aliases: ['Hardware', 'Windows', 'Edge'] },
  { slug: 'image-generation', label: { en: 'Image generation', es: 'Generación de imágenes' }, aliases: ['Image generation'] },
];

const norm = (s: string) => s.trim().toLowerCase();
const byAlias = new Map<string, TopicDef>();
for (const t of TOPICS) for (const a of t.aliases) byAlias.set(norm(a), t);

export const topicPath = (lang: Lang, slug: string): string => `/${lang}/topics/${slug}/`;

/** Temele canonice ale unui articol (fără duplicate). */
export function topicsOf(a: Article): TopicDef[] {
  const out: TopicDef[] = [];
  for (const raw of a.data.topics) {
    const def = byAlias.get(norm(raw));
    if (def && !out.includes(def)) out.push(def);
  }
  return out;
}

export interface TopicGroup {
  def: TopicDef;
  articles: Article[];
}

/** Temele care au destule articole pentru o pagină proprie, cele mai bogate primele. */
export async function getTopicGroups(lang: Lang): Promise<TopicGroup[]> {
  const articles = await getArticles(lang);
  const groups = new Map<string, TopicGroup>();
  for (const a of articles) {
    for (const def of topicsOf(a)) {
      const g = groups.get(def.slug) ?? { def, articles: [] };
      g.articles.push(a);
      groups.set(def.slug, g);
    }
  }
  return [...groups.values()]
    .filter((g) => g.articles.length >= MIN_TOPIC_ARTICLES)
    .sort((x, y) => y.articles.length - x.articles.length || x.def.slug.localeCompare(y.def.slug));
}

/** Articole conexe: cele care au cele mai multe teme canonice în comun; la egalitate, cele mai noi. Completat cu cele mai noi. */
export function relatedArticles(current: Article, all: Article[], limit = 3): Article[] {
  const mine = new Set(topicsOf(current).map((t) => t.slug));
  const scored = all
    .filter((a) => a.id !== current.id)
    .map((a) => ({ a, score: topicsOf(a).filter((t) => mine.has(t.slug)).length }));
  scored.sort((x, y) => y.score - x.score || y.a.data.publishedAt.valueOf() - x.a.data.publishedAt.valueOf());
  return scored.slice(0, limit).map((s) => s.a);
}

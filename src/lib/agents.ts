// Clasamentul agenților AI: calcul comun pentru pagina de clasament și paginile de profil.
import data from '../data/agents.json';

export const PROFILE_COUNT = 20;

type Scores = Record<string, number>;
export const criteria = data.criteria;
export const pts = (s: Scores, key: string, weight: number) => (s[key] / 5) * weight;
export const fmt = (n: number) => (Number.isInteger(n) ? String(n) : n.toFixed(1));
export const total = (s: Scores) => Math.round(criteria.reduce((sum, c) => sum + pts(s, c.key, c.weight), 0));

// Sorted by total score out of 100; ties keep the order of the data file.
export const ranked = data.agents
  .map((a, i) => ({ ...a, total: total(a.scores), i }))
  .sort((a, b) => b.total - a.total || a.i - b.i)
  .map((a, idx) => ({ ...a, rank: idx + 1 }));

export const hasProfile = (rank: number) => rank <= PROFILE_COUNT;
export const isFree = (pricing: string) => /\bfree\b/i.test(pricing) && !/no public prices/i.test(pricing);

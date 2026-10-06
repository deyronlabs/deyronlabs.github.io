import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// Un articol = un fișier Markdown în src/content/news/<limba>/<slug>.md
// Câmpurile de mai jos sunt validate la build: un articol invalid oprește publicarea.
const news = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/news' }),
  schema: z.object({
    // Titlu cu entitatea + evenimentul (cine + ce).
    title: z.string().min(10).max(120),
    // 2-3 propoziții care răspund singure la întrebare; apare sub titlu și în meta description.
    summary: z.string().min(80).max(420),
    lang: z.enum(['en', 'es']),
    publishedAt: z.coerce.date(),
    updatedAt: z.coerce.date().optional(),
    // Cel puțin o sursă marcată primary: true.
    sources: z
      .array(
        z.object({
          title: z.string(),
          url: z.string().url(),
          publisher: z.string().optional(),
          primary: z.boolean().default(false),
        }),
      )
      .min(1)
      .refine((s) => s.some((x) => x.primary), {
        message: 'Cel puțin o sursă trebuie să fie primary: true',
      }),
    // Entități menționate (companii, produse, modele); intră în schema.org "about".
    entities: z.array(z.string()).default([]),
    topics: z.array(z.string()).default([]),
    // Aceeași valoare în en și es pentru același articol; folosită la hreflang.
    translationKey: z.string().optional(),
    // Link YouTube Short (opțional).
    video: z.string().url().optional(),
    // draft: true = vizibil doar în `npm run dev`, nu în build-ul de producție.
    draft: z.boolean().default(false),
  }),
});

export const collections = { news };

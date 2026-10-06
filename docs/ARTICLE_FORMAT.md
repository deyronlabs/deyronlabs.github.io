# Formatul unui articol (pentru fluxul automat)

Un articol = un fișier Markdown în `src/content/news/<limba>/<slug>.md`.
Slug-ul din numele fișierului devine URL-ul: `src/content/news/en/acme-releases-model-x.md` → `/en/news/acme-releases-model-x/`.

## Frontmatter

| Câmp | Obligatoriu | Note |
|---|---|---|
| `title` | da | entitatea + evenimentul (cine + ce), 10-120 caractere |
| `summary` | da | 2-3 propoziții care răspund singure la întrebare, 80-420 caractere; apare sub titlu și în meta description |
| `lang` | da | `en` sau `es`; trebuie să se potrivească cu folderul |
| `publishedAt` | da | ISO 8601 cu fus, ex. `2026-10-06T14:30:00Z` |
| `updatedAt` | nu | se setează la fiecare corectură; apare ca „Updated” dacă e la peste 1 oră după publicare |
| `sources` | da | listă; fiecare are `title`, `url`, opțional `publisher`, `primary: true/false`; cel puțin una `primary: true` |
| `entities` | nu | companii, produse, modele menționate (intră în schema.org `about`) |
| `topics` | nu | etichete scurte |
| `translationKey` | nu | aceeași valoare în `en` și `es` pentru același articol (hreflang) |
| `video` | nu | link YouTube Short |
| `draft` | nu | `true` = nu se publică |

## Corpul

Exact trei secțiuni, în această ordine (în spaniolă: `Qué pasó`, `Detalles clave`, `Por qué importa`):

```md
## What happened
## Key details
## Why it matters
```

Secțiunea **Sources** nu se scrie în corp: se generează din `sources` din frontmatter.

## Reguli editoriale

- Sursa primară linkuită în `sources` (anunț oficial, paper, documentație, document de reglementare).
- Separă clar ce e confirmat de ce e raportat sau zvonit.
- „Why it matters” conține o implicație concretă, nu entuziasm.
- Cifrele vin din sursa primară, cu data la care au fost verificate.

## Verificare înainte de publicare

```
npm run check
```

Verifică folderul/limba, câmpurile principale, lungimea rezumatului, sursa primară și cele trei secțiuni. La build, schema din `src/content.config.ts` validează restul și oprește publicarea dacă ceva e greșit.

## Publicare

Commit pe ramura `main` → GitHub Actions construiește și publică site-ul în 1-2 minute. Sitemap, RSS și `llms.txt` se actualizează singure.

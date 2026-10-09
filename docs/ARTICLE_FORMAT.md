# Formatul unui articol (pentru fluxul automat)

Un articol = un fișier Markdown în `src/content/news/<limba>/<slug>.md`.
Slug-ul din numele fișierului devine URL-ul: `src/content/news/en/acme-releases-model-x.md` → `/en/news/acme-releases-model-x/`.

## Frontmatter

| Câmp | Obligatoriu | Note |
|---|---|---|
| `title` | da | entitatea + evenimentul (cine + ce), 10-120 caractere |
| `summary` | da | 2-3 propoziții care răspund singure la întrebare, 80-420 caractere; apare sub titlu și în meta description |
| `seoTitle` | da | titlul pentru Google (title tag), 15-48 caractere; se adaugă automat „ \| Deyron Labs”, deci totalul rămâne sub ~62. Pune entitatea și cifra/fapta cheie la început. `title` rămâne titlul lung din pagină (H1) |
| `seoDescription` | da | meta description, 70-155 caractere, o propoziție completă cu entitatea, faptul și data/cifra; nu o tăia cu „…” și nu copia `summary` |
| `lang` | da | `en` sau `es`; trebuie să se potrivească cu folderul |
| `publishedAt` | da | ISO 8601 cu fus, ex. `2026-10-06T14:30:00Z` |
| `updatedAt` | nu | se setează la fiecare corectură; apare ca „Updated” dacă e la peste 1 oră după publicare |
| `sources` | da | listă; fiecare are `title`, `url`, opțional `publisher`, `primary: true/false`; cel puțin una `primary: true` |
| `entities` | nu | companii, produse, modele menționate (intră în schema.org `about`) |
| `topics` | da (cel puțin una) | etichete scurte, scrise la fel de la un articol la altul (ex. `Models`, `Pricing`, `Open-weight`, `Safety`, `Policy`); vor deveni pagini de temă și intră în căutare |
| `translationKey` | nu | aceeași valoare în `en` și `es` pentru același articol (hreflang) |
| `video` | nu | link YouTube (video sau Short); apare ca player cu încărcare la click și în schema `VideoObject` |
| `videoPublishedAt` | nu | data publicării videoclipului (implicit data articolului) |
| `image` | nu | cale din `public/`, ex. `/images/news/<slug>.jpg`, 16:9, minim 1200 px lățime; apare în capul articolului și la partajare |
| `imageAlt` | da, dacă există `image` | descriere concretă a imaginii (ce arată, cu cifrele din ea), nu „imagine” sau titlul repetat |
| `draft` | nu | `true` = nu se publică |

## Corpul

Exact trei secțiuni, în această ordine (în spaniolă: `Qué pasó`, `Detalles clave`, `Por qué importa`):

```md
## What happened
## Key details
## Why it matters
```

Secțiunea **Sources** nu se scrie în corp: se generează din `sources` din frontmatter.

## Reguli SEO pentru articole noi (9 oct 2026)

- `seoTitle` ≤ 48 de caractere, `seoDescription` 70-155; ambele diferite de `title`/`summary`, scrise pentru rezultatul din Google.
- Cel puțin o temă în `topics`, din lista deja folosită (vezi celelalte articole), ca să nu apară variante ale aceleiași teme.
- Dacă există `image`, `imageAlt` descriptiv; imaginile din liste (Lab Sessions) primesc automat acest alt.
- Un singur URL de video per articol (cel din `video`); nu amesteca `watch?v=` cu `/shorts/` pentru același videoclip.
- Breadcrumbs, schema `NewsArticle`/`BreadcrumbList`, căutarea și „1 source / 2 sources” se generează singure.

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

## Imagine de partajare automată

Dacă un articol nu are `image`, site-ul generează la build o copertă 1200x630 (logo, primul topic, titlul, data) la `/covers/<limbă>/<slug>.png`; ea este folosită ca imagine Open Graph/Twitter și în datele structurate. Nu trebuie făcut nimic manual. Pagina articolului afișează totuși imaginea doar când `image` sau `video` este setat.

Butoanele de partajare (X, Facebook, LinkedIn, WhatsApp, Telegram, Reddit, e-mail, copiere link) apar automat în panoul din dreapta al fiecărui articol.

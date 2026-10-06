# deyronlabs.com

Site static Astro, multilingv (`/en/` activ, `/es/` pregătit), găzduit pe GitHub Pages.

## Ce conține

- Rute pe limbă în `src/pages/[lang]/`; traducerile interfeței în `src/i18n/ui.ts` (en + es).
- Limbile publicate: `ENABLED_LANGS` în `src/site.ts`. Pentru lansarea în spaniolă: adaugă `'es'` acolo și pune articolele în `src/content/news/es/`.
- Articole: Markdown în `src/content/news/<limba>/` (vezi `docs/ARTICLE_FORMAT.md`).
- Pe fiecare articol: titlu, rezumat, date de publicare/actualizare, secțiunile „What happened / Key details / Why it matters / Sources”, mențiunea AI + verificare editorială, JSON-LD `NewsArticle`, hreflang.
- Tehnic: `/sitemap.xml` (cu hreflang), `/en/rss.xml`, `/robots.txt` (crawlere AI permise), `/llms.txt`, pagina Despre, pagina de autor, 404.
- `public/CNAME` pentru domeniul propriu.

Articolul din `src/content/news/en/sample-story-template.md` este un șablon cu conținut fictiv, marcat `draft: true`: apare doar în `npm run dev`, nu pe site-ul publicat. Șterge-l sau păstrează-l ca model.

## Rulare locală (opțional)

```
npm install
npm run dev      # http://localhost:4321
npm run build
```

## Publicare

Fiecare commit pe `main` rulează `.github/workflows/deploy.yml` și publică site-ul.
În repository: Settings → Pages → Source: **GitHub Actions**.

## DNS la Romarg (după prima publicare reușită)

Înainte de orice modificare, verifică unde arată înregistrările MX (vezi nota de mai jos).

| Tip | Nume | Valoare |
|---|---|---|
| A | deyronlabs.com | 185.199.108.153 |
| A | deyronlabs.com | 185.199.109.153 |
| A | deyronlabs.com | 185.199.110.153 |
| A | deyronlabs.com | 185.199.111.153 |
| CNAME | www | deyronlabs.github.io |

Șterge doar înregistrările A/CNAME vechi pentru `deyronlabs.com` și `www`. **Nu atinge** MX, TXT (SPF, DKIM, DMARC) și `mail`.

**Atenție la email:** în cPanel, MX-ul poate arăta spre `deyronlabs.com` însuși. Dacă e așa, mută întâi MX pe `mail.deyronlabs.com` (care are propriul A către serverul Romarg), altfel emailurile se opresc când schimbi A-ul domeniului.

Apoi, în GitHub: Settings → Pages → Custom domain: `deyronlabs.com` → bifează **Enforce HTTPS** (apare după ce DNS-ul se propagă, de la câteva minute la câteva ore).

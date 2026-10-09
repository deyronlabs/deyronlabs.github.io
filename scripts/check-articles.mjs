// Verificare rapidă (fără dependențe) pentru articolele din src/content/news.
// Rulează: npm run check
// Validarea completă a câmpurilor o face schema Zod din src/content.config.ts la build.
import { existsSync, readdirSync, readFileSync, statSync } from 'node:fs';
import { join, relative, sep } from 'node:path';

const ROOT = new URL('../src/content/news/', import.meta.url).pathname;
const HEADINGS = {
  en: ['What happened', 'Key details', 'Why it matters'],
  es: ['Qué pasó', 'Detalles clave', 'Por qué importa'],
};

function walk(dir) {
  return readdirSync(dir).flatMap((n) => {
    const p = join(dir, n);
    return statSync(p).isDirectory() ? walk(p) : p.endsWith('.md') ? [p] : [];
  });
}

const field = (fm, key) => {
  const m = fm.match(new RegExp(`^${key}:\\s*(.*)$`, 'm'));
  return m ? m[1].trim().replace(/^["']|["']$/g, '') : undefined;
};

let errors = 0;
const fail = (file, msg) => {
  errors++;
  console.error(`✗ ${file}: ${msg}`);
};

const files = walk(ROOT);
for (const file of files) {
  const rel = relative(ROOT, file);
  const text = readFileSync(file, 'utf8');
  const m = text.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n([\s\S]*)$/);
  if (!m) {
    fail(rel, 'lipsește frontmatter-ul');
    continue;
  }
  const [, fm, body] = m;
  const lang = field(fm, 'lang');
  const folder = rel.split(sep)[0];
  if (!lang) fail(rel, 'lipsește lang');
  else if (lang !== folder) fail(rel, `lang: ${lang} nu se potrivește cu folderul ${folder}/`);
  for (const k of ['title', 'summary', 'publishedAt']) if (!field(fm, k)) fail(rel, `lipsește ${k}`);
  const summary = field(fm, 'summary') ?? '';
  if (summary && (summary.length < 80 || summary.length > 420)) fail(rel, `summary are ${summary.length} caractere (80-420)`);
  // SEO (obligatoriu pentru articolele noi): title tag și meta description scrise pentru Google.
  const seoTitle = field(fm, 'seoTitle');
  const seoDesc = field(fm, 'seoDescription');
  if (!seoTitle) fail(rel, 'lipsește seoTitle (15-48 caractere)');
  else if (seoTitle.length < 15 || seoTitle.length > 48) fail(rel, `seoTitle are ${seoTitle.length} caractere (15-48)`);
  if (!seoDesc) fail(rel, 'lipsește seoDescription (70-155 caractere)');
  else if (seoDesc.length < 70 || seoDesc.length > 155) fail(rel, `seoDescription are ${seoDesc.length} caractere (70-155)`);
  if (!/^topics:/m.test(fm)) fail(rel, 'lipsește topics (cel puțin o temă, pentru paginile de temă și căutare)');
  if (!/^sources:/m.test(fm)) fail(rel, 'lipsește sources');
  if (!/primary:\s*true/.test(fm)) fail(rel, 'nicio sursă cu primary: true');
  const img = field(fm, 'image');
  if (img) {
    if (!existsSync(new URL(`../public${img}`, import.meta.url).pathname)) fail(rel, `imaginea ${img} nu există în public/`);
    if (!field(fm, 'imageAlt')) fail(rel, 'imageAlt este obligatoriu când image este setat');
  }
  for (const h of HEADINGS[lang] ?? []) {
    if (!new RegExp(`^##\\s+${h}\\s*$`, 'm').test(body)) fail(rel, `lipsește secțiunea "## ${h}"`);
  }
  if (/^##\s+(Sources|Fuentes|Surse)\b/m.test(body)) fail(rel, 'secțiunea Sources se generează din frontmatter; scoate-o din corp');
}

console.log(`${files.length} articol(e) verificate, ${errors} eroare/erori.`);
process.exit(errors ? 1 : 0);

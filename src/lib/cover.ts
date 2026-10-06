// Copertă de partajare generată automat (1200x630) pentru articolele fără imagine proprie.
import sharp from 'sharp';

export const COVER_W = 1200;
export const COVER_H = 630;

const esc = (s: string) =>
  s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

/** Împarte titlul pe rânduri (estimare conservatoare a lățimii fontului), max `maxLines`. */
export function wrapTitle(title: string, maxChars: number, maxLines: number): string[] {
  const words = title.split(/\s+/).filter(Boolean);
  const lines: string[] = [];
  let cur = '';
  for (const w of words) {
    const next = cur ? `${cur} ${w}` : w;
    if (next.length <= maxChars || !cur) cur = next;
    else {
      lines.push(cur);
      cur = w;
    }
  }
  if (cur) lines.push(cur);
  if (lines.length > maxLines) {
    const kept = lines.slice(0, maxLines);
    kept[maxLines - 1] = kept[maxLines - 1].replace(/[\s.,;:–-]*$/, '') + '…';
    return kept;
  }
  return lines;
}

export interface CoverInput {
  title: string;
  kicker?: string; // ex. primul topic
  date?: string; // text deja formatat
}

export function coverSvg({ title, kicker, date }: CoverInput): string {
  const size = title.length > 95 ? 50 : title.length > 70 ? 56 : 64;
  const maxChars = Math.floor(1040 / (size * 0.6));
  const lines = wrapTitle(title, maxChars, 4);
  const lineH = Math.round(size * 1.18);
  const top = 190;
  const text = lines
    .map((l, i) => `<tspan x="80" y="${top + i * lineH}">${esc(l)}</tspan>`)
    .join('');
  const font = "font-family=\"'Liberation Sans', Arial, 'DejaVu Sans', Helvetica, sans-serif\"";
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${COVER_W}" height="${COVER_H}" viewBox="0 0 ${COVER_W} ${COVER_H}">
  <rect width="1200" height="630" fill="#1a1a1a"/>
  <rect x="0" y="0" width="1200" height="8" fill="#22c55e"/>
  <g transform="translate(80,70) scale(0.19)">
    <g transform="translate(130,176)" stroke="#1a1a1a" stroke-width="9" stroke-linejoin="round">
      <polygon points="-121,-70 0,0 0,140 -121,70" fill="#15803d"/>
      <polygon points="0,0 121,-70 121,70 0,140" fill="#22c55e"/>
      <polygon points="0,-166 121,-96 0,-26 -121,-96" fill="#86efac"/>
    </g>
  </g>
  <text x="140" y="108" ${font} font-size="34" font-weight="800" fill="#f3f6f4" letter-spacing="2">DEYRON <tspan fill="#22c55e" letter-spacing="8">LABS</tspan></text>
  ${kicker ? `<text x="1120" y="108" ${font} font-size="24" font-weight="700" fill="#86efac" text-anchor="end" letter-spacing="3">${esc(kicker.toUpperCase())}</text>` : ''}
  <text ${font} font-size="${size}" font-weight="800" fill="#f3f6f4">${text}</text>
  <rect x="80" y="548" width="64" height="4" fill="#22c55e"/>
  <text x="80" y="590" ${font} font-size="26" fill="#a9b3ad">deyronlabs.com${date ? ` · ${esc(date)}` : ''}</text>
</svg>`;
}

export async function renderCover(input: CoverInput): Promise<Buffer> {
  return sharp(Buffer.from(coverSvg(input))).png({ compressionLevel: 9 }).toBuffer();
}

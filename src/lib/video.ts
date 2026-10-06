// Ajutoare pure pentru videoclipuri YouTube.
export function youtubeId(url: string): string | null {
  try {
    const u = new URL(url);
    let id: string | null = null;
    if (u.hostname === 'youtu.be') id = u.pathname.slice(1);
    else if (u.hostname === 'youtube.com' || u.hostname.endsWith('.youtube.com')) {
      if (u.pathname === '/watch') id = u.searchParams.get('v');
      else {
        const m = u.pathname.match(/^\/(?:shorts|embed|live)\/([\w-]+)/);
        if (m) id = m[1];
      }
    }
    return id && /^[\w-]{11}$/.test(id) ? id : null;
  } catch {
    return null;
  }
}

/** Embed fără cookie-uri, pornit la click. */
export const embedSrc = (id: string): string =>
  `https://www.youtube-nocookie.com/embed/${id}?autoplay=1&rel=0`;

/** Adresa de embed pentru datele structurate (schema.org VideoObject). */
export const schemaEmbedUrl = (id: string): string => `https://www.youtube.com/embed/${id}`;

export const watchUrl = (id: string): string => `https://www.youtube.com/watch?v=${id}`;

export const posterFallback = (id: string): string => `https://i.ytimg.com/vi/${id}/hqdefault.jpg`;

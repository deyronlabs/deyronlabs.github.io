import { defineConfig } from 'astro/config';

// Rutele pe limbă (/en/, /es/) sunt făcute de noi, în src/pages/[lang]/.
// Limbile active se schimbă în src/site.ts (ENABLED_LANGS).
export default defineConfig({
  site: 'https://deyronlabs.com',
  output: 'static',
  trailingSlash: 'ignore',
  build: { format: 'directory' },
  compressHTML: true,
});

// Full-page reference captures with motion off, to compare before/after a refactor. Usage: node snap.js <outdir> [base]
const { chromium } = require('playwright'); const fs = require('fs');
const out = process.argv[2]; const base = process.argv[3] || 'http://127.0.0.1:8765/redesign/a-v3/';
const pages = ['index.html', 'es/index.html', 'invest-in-bogota/index.html', 'radio-a-domicilio/index.html', 'vende-digital/index.html', 'infinited/index.html', 'pro-surge-ja/index.html', 'col40-2018/index.html', '404.html'];
(async () => { fs.mkdirSync(out, { recursive: true }); const b = await chromium.launch();
  for (const w of [1440, 390]) { const ctx = await b.newContext({ viewport: { width: w, height: 900 }, reducedMotion: 'reduce' });
    await ctx.route(/framerusercontent|giphy/, r => r.abort()); await ctx.addInitScript(() => { Date = class extends Date { constructor(...a) { super(...(a.length ? a : [1790000000000])); } static now() { return 1790000000000; } }; });
    const p = await ctx.newPage();
    for (const pg of pages) { await p.goto(base + pg); await p.evaluate(() => { document.querySelectorAll('img[loading=lazy]').forEach(i => i.loading = 'eager'); document.querySelectorAll('iframe,video').forEach(e => e.style.visibility = 'hidden'); return document.fonts.ready; });
      await p.evaluate(async () => { for (let y = 0; y <= document.body.scrollHeight; y += 600) { scrollTo(0, y); await new Promise(r => setTimeout(r, 60)); } scrollTo(0, 0); }); await p.waitForTimeout(700);
      await p.screenshot({ path: `${out}/${pg.replace(/[\/.]/g, '_')}-${w}.png`, fullPage: true }); }
    await ctx.close(); }
  await b.close(); })();

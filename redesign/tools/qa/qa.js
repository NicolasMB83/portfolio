const { chromium } = require('playwright');
const fs = require('fs');
const base = process.env.QA_BASE || 'http://127.0.0.1:8765/redesign/a-v3/';
const axe = fs.readFileSync(require.resolve('axe-core/axe.min.js'), 'utf8');
const route = (ctx) => ctx.route(/framerusercontent\.com|giphy\.com/, r => r.abort());
const pages = process.argv[2] ? process.argv[2].split(',') : ['', 'es/', 'invest-in-bogota/', 'es/invest-in-bogota/', 'radio-a-domicilio/', 'es/radio-a-domicilio/', 'vende-digital/', 'es/vende-digital/', 'infinited/', 'es/infinited/', 'pro-surge-ja/', 'es/pro-surge-ja/', '404.html'];
const fmt = (v) => v.map(v => `${v.impact} ${v.id} (${v.nodes.length}): ${v.nodes.slice(0, 2).map(n => n.target.join(' ')).join(' | ')}`);
(async () => {
  const b = await chromium.launch();
  for (const pg of pages) {
    const url = base + pg;
    for (const w of [1440, 390]) {
      const ctx = await b.newContext({ viewport: { width: w, height: 900 }, reducedMotion: 'reduce' }); await route(ctx);
      const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('requestfailed', r => { if (!/framerusercontent|giphy|fonts.g/.test(r.url())) errs.push('404? ' + r.url()); });
      p.on('response', r => { if (r.status() >= 400) errs.push(r.status() + ' ' + r.url()); });
      await p.goto(url, { waitUntil: 'load' }); await p.evaluate(() => document.querySelectorAll('img[loading=lazy],iframe[loading=lazy]').forEach(i => i.loading = 'eager')); await p.waitForTimeout(2000);
      await p.addScriptTag({ content: axe });
      const res = await p.evaluate(async () => (await axe.run(document, { runOnly: ['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa', 'best-practice'] })).violations);
      let sheetRes = [];
      if (w === 1440) { await p.evaluate(() => document.getElementById('contact-sheet').showModal()); await p.waitForTimeout(500);
        sheetRes = await p.evaluate(async () => (await axe.run(document.getElementById('contact-sheet'), { runOnly: ['wcag2a', 'wcag2aa'] })).violations); }
      console.log(`[${pg || 'home'}] axe ${w}:`, res.length ? '\n   ' + fmt(res).join('\n   ') : 'ok', sheetRes.length ? '\n   SHEET ' + fmt(sheetRes).join('\n   ') : '', errs.length ? '\n   ERR ' + [...new Set(errs)].join('\n   ERR ') : '');
      await ctx.close();
    }
    const over = [];
    for (const w of [320, 375, 414, 600, 768, 1024, 1280, 1920, 2560]) {
      const ctx = await b.newContext({ viewport: { width: w, height: 900 } }); await route(ctx);
      const p = await ctx.newPage(); await p.goto(url, { waitUntil: 'load' }); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(900);
      const r = await p.evaluate(() => { const vw = document.documentElement.clientWidth; const bad = [];
        document.querySelectorAll('h1,h2,h3,h4,p,a,li,dd,figure,iframe,span:not(.horizon):not(.sun)').forEach(el => { if (el.closest('.chapter-nav ol')) return; const rc = el.getBoundingClientRect(); if (rc.width && (rc.right > vw + 0.5 || rc.left < -0.5)) bad.push(el.tagName + '.' + el.className + ' ' + Math.round(rc.left) + '→' + Math.round(rc.right)); });
        return { sw: document.documentElement.scrollWidth, vw, bad: bad.slice(0, 3) }; });
      over.push(`${w}:${r.sw > r.vw ? 'OVERFLOW' : 'ok'}${r.bad.length ? JSON.stringify(r.bad) : ''}`);
      await ctx.close();
    }
    console.log(`[${pg || 'home'}] widths:`, over.join(' '));
    const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, javaScriptEnabled: false }); await route(ctx);
    const p = await ctx.newPage(); await p.goto(url, { waitUntil: 'load' }); await p.waitForTimeout(1500);
    console.log(`[${pg || 'home'}] no-JS hidden text:`, await p.evaluate(() => [...document.querySelectorAll('h1,h2,h3,h4,p,li')].filter(e => { if (e.closest('[hidden],dialog,[popover]')) return false; const cs = getComputedStyle(e); return cs.visibility === 'hidden' || +cs.opacity < 0.99; }).length));
    await ctx.close();
    const ctx2 = await b.newContext({ viewport: { width: 1440, height: 900 }, reducedMotion: 'reduce' }); await route(ctx2);
    const p2 = await ctx2.newPage(); await p2.goto(url, { waitUntil: 'load' }); await p2.waitForTimeout(300);
    console.log(`[${pg || 'home'}] reduced-motion animations:`, await p2.evaluate(() => document.getAnimations().filter(a => a.constructor.name !== 'CSSTransition').map(a => a.animationName).join(',') || 0));
    await ctx2.close();
  }
  await b.close();
})();

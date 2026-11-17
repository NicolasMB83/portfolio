// Technical measurements per page: weight, requests, LCP, CLS, unused CSS. Usage: node measure.js [base] [pages,comma]
const { chromium } = require('playwright');
const base = process.argv[2] || 'http://127.0.0.1:8765/redesign/a-v3/';
const pages = (process.argv[3] || 'index.html,es/index.html,invest-in-bogota/index.html,radio-a-domicilio/index.html,pro-surge-ja/index.html').split(',');
(async () => {
  const b = await chromium.launch();
  for (const pg of pages) {
    const ctx = await b.newContext({ viewport: { width: 412, height: 823 }, deviceScaleFactor: 2, isMobile: true });
    const p = await ctx.newPage(); const cdp = await ctx.newCDPSession(p);
    await cdp.send('Network.enable'); await cdp.send('DOM.enable'); await cdp.send('CSS.enable'); await cdp.send('CSS.startRuleUsageTracking');
    let bytes = 0, reqs = 0, failed = []; const byType = {};
    cdp.on('Network.loadingFinished', e => { bytes += e.encodedDataLength; reqs++; });
    cdp.on('Network.responseReceived', e => { byType[e.requestId] = e.type; if (e.response.status >= 400) failed.push(e.response.status + ' ' + e.response.url.slice(-60)); });
    cdp.on('Network.loadingFailed', e => failed.push('failed ' + (e.errorText || '')));
    await p.addInitScript(() => { window.__m = { lcp: 0, cls: 0 };
      new PerformanceObserver(l => { for (const e of l.getEntries()) window.__m.lcp = e.startTime, window.__m.lcpEl = (e.element && (e.element.tagName + '.' + e.element.className)) || ''; }).observe({ type: 'largest-contentful-paint', buffered: true });
      new PerformanceObserver(l => { for (const e of l.getEntries()) if (!e.hadRecentInput) window.__m.cls += e.value; }).observe({ type: 'layout-shift', buffered: true }); });
    await p.goto(base + pg, { waitUntil: 'load' }); await p.waitForTimeout(2500);
    const m = await p.evaluate(() => window.__m);
    const { ruleUsage } = await cdp.send('CSS.stopRuleUsageTracking');
    const used = ruleUsage.filter(r => r.used).reduce((a, r) => a + (r.endOffset - r.startOffset), 0), all = ruleUsage.reduce((a, r) => a + (r.endOffset - r.startOffset), 0);
    console.log(`${pg.padEnd(34)} ${String(Math.round(bytes / 1024)).padStart(5)} KB ${String(reqs).padStart(3)} req  LCP ${String(Math.round(m.lcp)).padStart(5)} ms (${(m.lcpEl || '').slice(0, 28)})  CLS ${m.cls.toFixed(3)}  CSS used ${Math.round(100 * used / all)}%${failed.length ? '  !! ' + [...new Set(failed)].join('; ') : ''}`);
    await ctx.close();
  }
  await b.close();
})();

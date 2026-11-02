/* Nicolas MB — portfolio, Option A v2. Progressive enhancement only:
   every page is complete and usable without this file. */
(() => {
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const html = document.documentElement;
  const here = document.currentScript ? document.currentScript.src : location.href; // assets/ folder, for self-hosted files
  const pageLang = (html.lang || "en").slice(0, 2);
  const store = {
    get(k) { try { return localStorage.getItem(k); } catch (_) { return null; } },
    set(k, v) { try { localStorage.setItem(k, v); } catch (_) {} },
  };

  /* Header hairline once the page has scrolled */
  const header = document.querySelector("[data-header]");
  if (header && "IntersectionObserver" in window) {
    const sentinel = document.createElement("div");
    sentinel.setAttribute("aria-hidden", "true");
    sentinel.style.cssText = "position:absolute;top:0;left:0;width:1px;height:1px;";
    document.body.prepend(sentinel);
    new IntersectionObserver(([entry]) => header.toggleAttribute("data-scrolled", !entry.isIntersecting)).observe(sentinel);
  }

  /* Mobile menu: native popover; sync aria-expanded and close on navigation */
  const menu = document.getElementById("menu");

  /* The header pill gets out of the way while you read down and returns as soon as you scroll up a little.
     It never hides near the top, while the menu is open, or while something inside it has keyboard focus. */
  if (header) {
    let lastY = window.scrollY, hidden = false, ticking = false;
    const setHidden = (h) => {
      if (h === hidden) return;
      hidden = h;
      header.toggleAttribute("data-hidden", h);
      html.toggleAttribute("data-header-hidden", h);
    };
    const update = () => {
      ticking = false;
      const y = window.scrollY, dy = y - lastY;
      if (Math.abs(dy) < 6) return; // ignore tiny movements
      const menuOpen = menu && menu.matches && menu.matches(":popover-open");
      setHidden(dy > 0 && y > 160 && !menuOpen && !header.contains(document.activeElement));
      lastY = y;
    };
    window.addEventListener("scroll", () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
    header.addEventListener("focusin", () => setHidden(false));
  }
  const menuToggle = document.querySelector('[popovertarget="menu"]');
  if (menu && menuToggle) {
    menu.addEventListener("toggle", (e) => menuToggle.setAttribute("aria-expanded", String(e.newState === "open")));
    menu.querySelectorAll("a").forEach((a) => a.addEventListener("click", () => menu.hidePopover && menu.hidePopover()));
  }

  /* Click feedback: the dot of the logotype spreads from the exact point of the click */
  if (!reduceMotion.matches) {
    document.addEventListener("pointerdown", (e) => {
      const el = e.target.closest(".btn, .socials a, .sheet-close");
      if (!el || e.button !== 0) return;
      const r = el.getBoundingClientRect();
      const x = e.clientX - r.left, y = e.clientY - r.top;
      const size = 2 * Math.hypot(Math.max(x, r.width - x), Math.max(y, r.height - y));
      const dot = document.createElement("span");
      dot.className = "press-dot";
      dot.style.cssText = `left:${x}px;top:${y}px;width:${size}px;height:${size}px`;
      el.append(dot);
      dot.addEventListener("animationend", () => dot.remove(), { once: true });
    });
  }

  /* Contact sheet. Links marked [data-contact] open a native dialog (focus moves in, Esc closes,
     focus returns to the button). Without JS they stay plain links to #contact. */
  const sheet = document.getElementById("contact-sheet");
  if (sheet && typeof sheet.showModal === "function") {
    document.querySelectorAll("[data-contact]").forEach((link) => {
      link.addEventListener("click", (e) => {
        if (e.metaKey || e.ctrlKey || e.shiftKey || e.button === 1) return;
        e.preventDefault();
        if (menu && menu.matches && menu.matches(":popover-open")) { try { menu.hidePopover(); } catch (_) {} }
        sheet.showModal();
      });
    });
    sheet.querySelectorAll("[data-close]").forEach((b) => b.addEventListener("click", () => sheet.close()));
    sheet.addEventListener("click", (e) => { if (e.target === sheet) sheet.close(); }); // backdrop
  }

  /* Copy email: the address is always visible; this only saves a step */
  document.querySelectorAll("[data-copy]").forEach((btn) => {
    const status = btn.parentElement.querySelector("[data-copy-status]");
    let timer;
    btn.addEventListener("click", async () => {
      let ok = false;
      try { await navigator.clipboard.writeText(btn.getAttribute("data-copy")); ok = true; } catch (_) {
        const target = btn.parentElement.querySelector(".email-address");
        if (target) { const r = document.createRange(); r.selectNodeContents(target); const s = getSelection(); s.removeAllRanges(); s.addRange(r); }
      }
      if (!ok) return;
      btn.setAttribute("data-copied", "");
      if (status) status.textContent = btn.querySelector(".when-done").textContent.trim();
      clearTimeout(timer);
      timer = setTimeout(() => { btn.removeAttribute("data-copied"); if (status) status.textContent = ""; }, 2200);
    });
  });

  /* Language. Never redirect (Google Search Central). Suggest once, remember the visitor's choice. */
  document.querySelectorAll("[data-lang-switch]").forEach((a) => a.addEventListener("click", () => store.set("nmb-lang", a.getAttribute("hreflang"))));
  const hint = document.querySelector("[data-lang-hint]");
  if (hint) {
    const other = hint.getAttribute("data-lang-hint");
    const chosen = store.get("nmb-lang");
    const prefs = (navigator.languages && navigator.languages.length ? navigator.languages : [navigator.language || ""]).map((l) => String(l).slice(0, 2).toLowerCase());
    const prefersOther = prefs.indexOf(other) !== -1 && (prefs.indexOf(pageLang) === -1 || prefs.indexOf(other) < prefs.indexOf(pageLang));
    if (!chosen && prefersOther) {
      setTimeout(() => { hint.hidden = false; }, 1200);
      hint.querySelector("[data-dismiss]").addEventListener("click", () => { hint.hidden = true; store.set("nmb-lang", pageLang); });
    }
  }

  /* Current section in the nav (and the current chapter in a case study's chapter bar) */
  const navLinks = Array.from(document.querySelectorAll('.nav-links a[href*="#"], .chapter-nav a'));
  if (navLinks.length && "IntersectionObserver" in window) {
    const map = new Map();
    navLinks.forEach((a) => { const id = a.hash.slice(1); const el = id && document.getElementById(id); if (el) map.set(el, a); });
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        const a = map.get(e.target);
        if (!a) return;
        if (e.isIntersecting) {
          a.setAttribute("aria-current", "true");
          const bar = a.closest(".chapter-nav ol"); // on narrow screens the chapter bar scrolls sideways: keep the current one in view
          if (bar && bar.scrollWidth > bar.clientWidth) bar.scrollTo({ left: a.offsetLeft - 16, behavior: reduceMotion.matches ? "auto" : "smooth" });
        } else a.removeAttribute("aria-current");
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    map.forEach((_, el) => io.observe(el));
  }

  /* 404: a new random GIF for the search word in data-giphy-tag ("cat") rises inside the sun on every visit.
     If the API fails or the hourly limit is reached, the sun simply stays as it is.
     GIPHY's terms require the "Powered by GIPHY" credit. */
  const gifSky = document.querySelector("[data-giphy-key]");
  if (gifSky && gifSky.getAttribute("data-giphy-key")) {
    const key = gifSky.getAttribute("data-giphy-key");
    const tag = gifSky.getAttribute("data-giphy-tag") || "";
    /* Search ranks by relevance (random-by-tag only returns something "related"), so: one random pick
       among the 200 most relevant results for the tag. One API call per visit. */
    const offset = Math.floor(Math.random() * 200);
    fetch(`https://api.giphy.com/v1/gifs/search?api_key=${encodeURIComponent(key)}&q=${encodeURIComponent(tag)}&limit=1&offset=${offset}&rating=g&lang=en`, { cache: "no-store" })
      .then((r) => (r.ok ? r.json() : Promise.reject(r.status)))
      .then(({ data }) => {
        const gif = Array.isArray(data) ? data[0] : data;
        const img = gif && gif.images;
        if (!img) return;
        const sun = gifSky.querySelector(".sun");
        let media;
        if (reduceMotion.matches || !img.downsized_small || !img.downsized_small.mp4) {
          media = new Image();
          media.src = (img.fixed_height_still || img.original_still || {}).url;
          media.alt = "";
        } else {
          media = document.createElement("video");
          Object.assign(media, { src: img.downsized_small.mp4, muted: true, loop: true, autoplay: true, playsInline: true });
          media.setAttribute("aria-hidden", "true");
        }
        media.className = "sun-media";
        const ready = () => { gifSky.classList.add("has-gif"); const credit = document.querySelector("[data-giphy-credit]"); if (credit) credit.hidden = false; };
        media.addEventListener(media.tagName === "VIDEO" ? "loadeddata" : "load", ready, { once: true });
        sun.append(media);
      })
      .catch(() => {});
  }

  /* Placeholders: the tessellation only holds an image's place while it loads (or if it fails).
     Once an image has loaded, its frame drops the texture and the tint. */
  document.querySelectorAll(".gallery > figure > img, .project-media > img, .chapter-figure > img, .cover-shot > img").forEach((img) => {
    const mark = () => img.parentElement.setAttribute("data-loaded", "");
    if (img.complete && img.naturalWidth) mark(); else img.addEventListener("load", mark, { once: true });
  });

  /* Footer logotype: its letters rise from the bottom edge, one after another, when it comes into view */
  const endMark = document.querySelector(".end-mark[data-reveal]");
  if (endMark) {
    if (reduceMotion.matches || !("IntersectionObserver" in window)) endMark.classList.add("is-in");
    else {
      endMark.classList.add("is-armed");
      new IntersectionObserver(([e], obs) => { if (e.isIntersecting) { endMark.classList.add("is-in"); obs.disconnect(); } }, { threshold: 0.6 }).observe(endMark);
    }
  }

  /* Parallax openings: CSS scroll-driven animations do it where supported; elsewhere, the same drift here */
  const drifting = Array.from(document.querySelectorAll(".cover-shot.parallax > img, .cover-shot.parallax > video"));
  if (drifting.length && !reduceMotion.matches && !(window.CSS && CSS.supports("animation-timeline: view()"))) {
    let queued = false;
    const drift = () => {
      queued = false;
      const vh = window.innerHeight;
      drifting.forEach((el) => {
        const r = el.parentElement.getBoundingClientRect();
        if (r.bottom < 0 || r.top > vh) return;
        const progress = Math.min(1, Math.max(0, (vh - r.top) / (vh + r.height)));
        const amp = el.tagName === "VIDEO" ? 12 : 15;
        el.style.translate = `0 ${(-amp + 2 * amp * progress).toFixed(2)}%`;
      });
    };
    window.addEventListener("scroll", () => { if (!queued) { queued = true; requestAnimationFrame(drift); } }, { passive: true });
    drift();
  }

  /* Lottie covers: load the player only when a cover is about to be seen, pause off-screen */
  const covers = Array.from(document.querySelectorAll("[data-lottie]"));
  if (!covers.length || !("IntersectionObserver" in window)) return;
  const LOTTIE_SRC = new URL("vendor/lottie_light-5.12.2.min.js", here).href; // self-hosted (MIT), no CDN
  let player;
  const loadPlayer = () => player || (player = new Promise((resolve, reject) => {
    const s = document.createElement("script");
    s.src = LOTTIE_SRC; s.async = true;
    s.onload = () => (window.lottie ? resolve(window.lottie) : reject());
    s.onerror = reject;
    document.head.append(s);
  }));
  const start = (el) => {
    if (el._anim || el._loading) return;
    el._loading = true;
    loadPlayer().then((lottie) => {
      const stage = document.createElement("div");
      stage.className = "lottie-stage";
      stage.setAttribute("aria-hidden", "true");
      el.prepend(stage);
      const anim = lottie.loadAnimation({
        container: stage, renderer: "svg", loop: true, autoplay: false, path: el.dataset.lottie,
        rendererSettings: { preserveAspectRatio: "xMidYMid slice", progressiveLoad: true }
      });
      el._anim = anim;
      anim.addEventListener("DOMLoaded", () => {
        el.setAttribute("data-ready", "");
        if (reduceMotion.matches) anim.goToAndStop(Math.floor(anim.totalFrames / 2), true);
        else if (el._inView) anim.play();
      });
      anim.addEventListener("data_failed", () => { stage.remove(); el._anim = null; });
    }).catch(() => {});
  };
  const io = new IntersectionObserver((entries) => {
    entries.forEach(({ target: el, isIntersecting }) => {
      el._inView = isIntersecting;
      if (isIntersecting) {
        start(el);
        if (el._anim && el.hasAttribute("data-ready") && !reduceMotion.matches) el._anim.play();
      } else if (el._anim) {
        el._anim.pause();
      }
    });
  }, { rootMargin: "240px 0px" });
  covers.forEach((el) => io.observe(el));
})();

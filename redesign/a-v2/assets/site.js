/* Nicolas MB — portfolio, Option A v2. Progressive enhancement only:
   every page is complete without this file. */
(() => {
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

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
  const menuToggle = document.querySelector('[popovertarget="menu"]');
  if (menu && menuToggle) {
    menu.addEventListener("toggle", (e) => menuToggle.setAttribute("aria-expanded", String(e.newState === "open")));
    menu.querySelectorAll("a").forEach((a) => a.addEventListener("click", () => menu.hidePopover && menu.hidePopover()));
  }

  /* Contact sheet: links marked [data-contact] open a native dialog instead of jumping to the footer.
     Without JS (or without <dialog>) they keep working as plain anchors to #contact. */
  const sheet = document.getElementById("contact-sheet");
  if (sheet && typeof sheet.showModal === "function") {
    document.querySelectorAll("[data-contact]").forEach((link) => {
      link.addEventListener("click", (e) => {
        if (e.metaKey || e.ctrlKey || e.shiftKey || e.button === 1) return;
        e.preventDefault();
        if (menu && menu.hidePopover) { try { menu.hidePopover(); } catch (_) {} }
        sheet.showModal();
      });
    });
    sheet.querySelectorAll("[data-close]").forEach((b) => b.addEventListener("click", () => sheet.close()));
    // Click on the backdrop closes the sheet
    sheet.addEventListener("click", (e) => { if (e.target === sheet) sheet.close(); });
  }

  /* Copy email: the address is always visible; this only saves a step */
  document.querySelectorAll("[data-copy]").forEach((btn) => {
    const status = btn.parentElement.querySelector("[data-copy-status]");
    let timer;
    btn.addEventListener("click", async () => {
      const value = btn.getAttribute("data-copy");
      let ok = false;
      try { await navigator.clipboard.writeText(value); ok = true; } catch (_) {
        // Fallback: select the address so the visitor can copy it by hand
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

  /* Current section in the nav */
  const navLinks = Array.from(document.querySelectorAll('.nav-links a[href*="#"]'));
  if (navLinks.length && "IntersectionObserver" in window) {
    const map = new Map();
    navLinks.forEach((a) => { const id = a.hash.slice(1); const el = id && document.getElementById(id); if (el) map.set(el, a); });
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        const a = map.get(e.target);
        if (!a) return;
        if (e.isIntersecting) a.setAttribute("aria-current", "true"); else a.removeAttribute("aria-current");
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    map.forEach((_, el) => io.observe(el));
  }

  /* Lottie covers: load the player only when a cover is about to be seen, pause off-screen */
  const covers = Array.from(document.querySelectorAll("[data-lottie]"));
  if (!covers.length || !("IntersectionObserver" in window)) return;
  const LOTTIE_SRC = "https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.12.2/lottie_light.min.js";
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

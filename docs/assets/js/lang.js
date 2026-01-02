(function () {
  const DEFAULT_LANG = "es";

  function getPreferredLang() {
    const stored = window.localStorage.getItem("site-lang");
    if (stored === "es" || stored === "en") return stored;

    const browser = (navigator.language || navigator.userLanguage || "").toLowerCase();
    if (browser.startsWith("es")) return "es";
    if (browser.startsWith("en")) return "en";
    return DEFAULT_LANG;
  }

  function setPreferredLang(lang) {
    window.localStorage.setItem("site-lang", lang);
  }

  function tagTocByLanguage() {
    const tocLinks = document.querySelectorAll("#TOC a.nav-link");
    tocLinks.forEach(link => {
      let selector = link.getAttribute("data-scroll-target");

      if (!selector) {
        const hrefAttr = link.getAttribute("href") || "";
        const hashIndex = hrefAttr.indexOf("#");
        if (hashIndex === -1) return;
        selector = hrefAttr.slice(hashIndex);
      }

      if (!selector || !selector.startsWith("#")) return;

      const target = document.querySelector(selector);
      if (!target) return;
      const li = link.closest("li");
      if (!li) return;

      if (target.closest(".lang-es")) {
        li.classList.add("lang-es");
      } else if (target.closest(".lang-en")) {
        li.classList.add("lang-en");
      }
    });
  }

  function prepareNavbarLabels() {
    const navTexts = document.querySelectorAll("#quarto-header .navbar-nav .menu-text");
    navTexts.forEach(span => {
      if (span.dataset.bilingualPrepared === "true") return;
      const raw = span.textContent || "";
      const parts = raw.split("/");
      if (parts.length !== 2) return;

      const es = parts[0].trim();
      const en = parts[1].trim();
      span.textContent = "";

      const esSpan = document.createElement("span");
      esSpan.className = "lang-es";
      esSpan.textContent = es;

      const enSpan = document.createElement("span");
      enSpan.className = "lang-en";
      enSpan.textContent = en;

      span.appendChild(esSpan);
      span.appendChild(enSpan);
      span.dataset.bilingualPrepared = "true";
    });
  }

  function moveLangSwitchToNavbar() {
    const switchEl = document.querySelector(".lang-switch");
    const tools = document.querySelector(".quarto-navbar-tools");
    if (switchEl && tools && !tools.contains(switchEl)) {
      tools.appendChild(switchEl);
    }
  }

  function updateTocTitle(lang) {
    const titleEl = document.querySelector("#TOC #toc-title");
    if (!titleEl) return;
    titleEl.textContent = lang === "es" ? "En esta página" : "On this page";
  }

  function updateFooterYear() {
    const yearEl = document.getElementById("footer-year");
    if (yearEl && !yearEl.textContent) {
      yearEl.textContent = new Date().getFullYear();
    }
  }

  function setupScrollReveal() {
    const prefersReduced = window.matchMedia &&
      window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (prefersReduced) return;

    const targets = document.querySelectorAll(
      ".content .level1.lang, .card, .hero-subtitle"
    );
    if (!("IntersectionObserver" in window)) {
      targets.forEach(el => el.classList.add("is-visible"));
      return;
    }

    targets.forEach(el => el.classList.add("reveal-on-scroll"));

    const observer = new IntersectionObserver(
      entries => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      {
        threshold: 0.15,
        rootMargin: "0px 0px -10% 0px"
      }
    );

    targets.forEach(el => observer.observe(el));
  }

  function setupHeroParallax() {
    const prefersReduced = window.matchMedia &&
      window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (prefersReduced) return;

    const photos = Array.from(document.querySelectorAll(".hero-photo"));
    if (!photos.length) return;

    let ticking = false;

    const update = () => {
      const scrollY = window.scrollY || window.pageYOffset || 0;
      const offset = Math.max(Math.min(scrollY * 0.12, 80), 0); // se mueve más lento que el scroll

      photos.forEach(photo => {
        const rect = photo.getBoundingClientRect();

        // Si está oculta (idioma no activo), no aplicar efecto
        if (rect.height === 0 || rect.width === 0) {
          photo.style.transform = "translateY(0)";
          return;
        }

        photo.style.transform = `translateY(${offset * -1}px)`;
      });
      ticking = false;
    };

    update();

    window.addEventListener("scroll", () => {
      if (!ticking) {
        window.requestAnimationFrame(update);
        ticking = true;
      }
    });
  }

  function applyLang(lang) {
    document.querySelectorAll(".lang-es").forEach(el =>
      el.classList.toggle("lang-hidden", lang !== "es")
    );
    document.querySelectorAll(".lang-en").forEach(el =>
      el.classList.toggle("lang-hidden", lang !== "en")
    );
    document.querySelectorAll("[data-lang-btn]").forEach(btn =>
      btn.classList.toggle("active", btn.getAttribute("data-lang-btn") === lang)
    );
    updateTocTitle(lang);
  }

  document.addEventListener("DOMContentLoaded", () => {
    prepareNavbarLabels();
    tagTocByLanguage();
    moveLangSwitchToNavbar();
    updateFooterYear();
    setupScrollReveal();
    setupHeroParallax();

    const lang = getPreferredLang();
    applyLang(lang);

    document.querySelectorAll("[data-lang-btn]").forEach(btn =>
      btn.addEventListener("click", e => {
        e.preventDefault();
        const lang = btn.getAttribute("data-lang-btn");
        setPreferredLang(lang);
        applyLang(lang);
      })
    );
  });
})();

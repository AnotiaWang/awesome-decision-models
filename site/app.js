(function () {
  var root = document.documentElement;
  var search = document.getElementById("search");
  var status = document.getElementById("search-status");
  var empty = document.getElementById("empty");
  var sections = Array.prototype.slice.call(document.querySelectorAll("[data-section]"));

  // --- Language ---

  function setLang(lang, save) {
    root.dataset.lang = lang;
    root.lang = lang === "zh" ? "zh-CN" : "en";
    search.placeholder = search.dataset["placeholder" + (lang === "zh" ? "Zh" : "En")];
    document.querySelectorAll("[data-set-lang]").forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.dataset.setLang === lang));
    });
    if (save) {
      try { localStorage.setItem("lang", lang); } catch (e) {}
      var url = new URL(location.href);
      url.searchParams.set("lang", lang);
      history.replaceState(null, "", url);
    }
    filter();
  }

  document.querySelectorAll("[data-set-lang]").forEach(function (b) {
    b.addEventListener("click", function () { setLang(b.dataset.setLang, true); });
  });

  // --- Search ---

  function filter() {
    var terms = search.value.toLowerCase().split(/\s+/).filter(Boolean);
    var shown = 0;
    sections.forEach(function (sec) {
      var n = 0;
      sec.querySelectorAll(".entry").forEach(function (li) {
        var text = li.dataset.search;
        var hit = terms.every(function (t) { return text.indexOf(t) !== -1; });
        li.hidden = !hit;
        if (hit) n++;
      });
      // Subsection headings and notes follow their entries.
      sec.querySelectorAll("h3, .note").forEach(function (el) { el.hidden = terms.length > 0; });
      sec.hidden = n === 0;
      sec.querySelector("[data-count]").textContent = n;
      var tc = document.querySelector('[data-toc-count="' + sec.id + '"]');
      tc.textContent = n;
      tc.parentElement.classList.toggle("dim", n === 0);
      shown += n;
    });
    empty.hidden = shown > 0;
    status.textContent = terms.length
      ? (root.dataset.lang === "zh" ? shown + " 个结果" : shown + (shown === 1 ? " result" : " results"))
      : "";
  }

  search.addEventListener("input", filter);
  document.addEventListener("keydown", function (e) {
    if (e.key === "/" && document.activeElement !== search) {
      e.preventDefault();
      search.focus();
    } else if (e.key === "Escape" && document.activeElement === search) {
      search.value = "";
      filter();
    }
  });

  // --- Highlight the current section in the sidebar ---

  if ("IntersectionObserver" in window) {
    var links = {};
    document.querySelectorAll("[data-toc]").forEach(function (a) { links[a.dataset.toc] = a; });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          Object.keys(links).forEach(function (id) { links[id].classList.toggle("active", id === e.target.id); });
        }
      });
    }, { rootMargin: "-20% 0px -70% 0px" });
    sections.forEach(function (s) { io.observe(s); });
  }

  setLang(root.dataset.lang, false);
})();

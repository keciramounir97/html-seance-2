(function () {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];

  const state = {
    lang: localStorage.getItem("aboni-lang") || "fr",
    theme: localStorage.getItem("aboni-theme") || "light",
    view: "home",
    chapter: "revision",
    exoTab: "theory",
    progress: JSON.parse(localStorage.getItem("aboni-progress") || "{}")
  };

  const t = (obj) => {
    if (!obj) return "";
    if (typeof obj === "string") return obj;
    return obj[state.lang] || obj.fr || "";
  };

  function save() {
    localStorage.setItem("aboni-lang", state.lang);
    localStorage.setItem("aboni-theme", state.theme);
    localStorage.setItem("aboni-progress", JSON.stringify(state.progress));
  }

  function applyChrome() {
    document.documentElement.lang = state.lang === "ar" ? "ar" : state.lang;
    document.documentElement.dir = state.lang === "ar" ? "rtl" : "ltr";
    document.documentElement.setAttribute("data-theme", state.theme);
    $("#lang").value = state.lang;
    $("#search").placeholder = t(UI.search);
    $("#btn-menu").textContent = t(UI.menu);
    $("#link-home").textContent = t(UI.home);
    $("#link-exos").textContent = t(UI.exercises);
    const lists = chapters().find((c) => c.id === "chapitre-6");
    const boxes = chapters().find((c) => c.id === "chapitre-8");
    const vid = chapters().find((c) => c.id === "chapitre-9");
    const sym = chapters().find((c) => c.id === "chapitre-13");
    if (lists) $("#link-lists").textContent = t(lists.titles);
    if (boxes) $("#link-containers").textContent = t(boxes.titles);
    if (vid) $("#link-video").textContent = t(vid.titles);
    if (sym) $("#link-symbols").textContent = t(sym.titles);
    $("#brand-text").textContent = t(UI.brand);
    $("#btn-theme").textContent = state.theme === "dark" ? "☀ " + t(UI.light) : "🌙 " + t(UI.dark);
    $("#footer-txt").textContent = t(UI.footer);
  }

  function chapters() {
    return window.CHAPTERS;
  }

  function chById(id) {
    return chapters().find((c) => c.id === id);
  }

  function parseHash() {
    const h = (location.hash || "#/").replace(/^#/, "");
    const parts = h.split("/").filter(Boolean);
    if (!parts.length) return { view: "home" };
    if (parts[0] === "exos") return { view: "exos", chapter: parts[1] || "revision" };
    if (parts[0] === "chapitre") return { view: "doc", chapter: parts[1] || "revision" };
    return { view: "home" };
  }

  function navTo(hash) {
    location.hash = hash;
  }

  function renderSidebar() {
    const q = ($("#search").value || "").trim().toLowerCase();
    const box = $("#sidebar-list");
    const items = chapters().filter((c) => {
      const blob = (t(c.titles) + " " + c.id).toLowerCase();
      return !q || blob.includes(q);
    });
    if (!items.length) {
      box.innerHTML = `<p class="group-title">${t(UI.emptySearch)}</p>`;
      return;
    }
    let html = `<div class="group-title">${t(UI.docs)}</div>`;
    html += items
      .map((c) => {
        const active = state.view === "doc" && state.chapter === c.id ? "active" : "";
        return `<a class="${active}" href="#/chapitre/${c.id}">${c.num ? c.num + ". " : ""}${t(c.titles)}</a>`;
      })
      .join("");
    html += `<div class="group-title">${t(UI.exercises)}</div>`;
    html += items
      .map((c) => {
        const active = state.view === "exos" && state.chapter === c.id ? "active" : "";
        return `<a class="${active}" href="#/exos/${c.id}">${t(c.titles)}</a>`;
      })
      .join("");
    box.innerHTML = html;
    const pct = progressPct();
    $("#progress-fill").style.width = pct + "%";
    $("#progress-label").textContent = `${t(UI.progress)} : ${pct}%`;
  }

  function progressPct() {
    const keys = Object.keys(state.progress);
    const total = chapters().length * 40;
    return total ? Math.min(100, Math.round((keys.length / total) * 100)) : 0;
  }

  function pager(id) {
    const list = chapters();
    const i = list.findIndex((c) => c.id === id);
    const prev = list[i - 1];
    const next = list[i + 1];
    const prefix = state.view === "exos" ? "exos" : "chapitre";
    return `<div class="pager">
      ${prev ? `<a class="btn ghost" href="#/${prefix}/${prev.id}">${t(UI.prev)}</a>` : "<span></span>"}
      ${next ? `<a class="btn" href="#/${prefix}/${next.id}">${t(UI.next)}</a>` : "<span></span>"}
    </div>`;
  }

  function esc(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
  }

  function renderTable(table) {
    const heads = table.headers[state.lang] || table.headers.fr;
    const th = heads.map((h) => `<th>${h}</th>`).join("");
    const tr = table.rows
      .map((row) => `<tr>${row.map((cell) => `<td>${t(cell)}</td>`).join("")}</tr>`)
      .join("");
    return `<table class="w3"><tr>${th}</tr>${tr}</table>`;
  }

  function tryBtn(code) {
    const b64 = encodeURIComponent(code);
    return `<button class="btn small tryit" data-code="${b64}">${t(UI.tryit)}</button>`;
  }

  function interactiveBlock(kind) {
    if (kind === "entities") {
      const items = [
        ["©", "&copy;"], ["€", "&euro;"], ["<", "&lt;"], [">", "&gt;"],
        ["&", "&amp;"], ["®", "&reg;"], ["°", "&deg;"], ["×", "&times;"],
        ["≠", "&ne;"], ["½", "&frac12;"], ["←", "&larr;"], ["♥", "&hearts;"]
      ];
      return `<div class="note">${t(UI.clickEntity)}</div>
        <div class="entity-grid">${items.map(([sym, ent]) =>
          `<button type="button" class="ent" data-ent="${ent}">${sym}<small>${ent}</small></button>`
        ).join("")}</div>
        <p id="ent-out"></p>`;
    }
    if (kind === "icons") {
      return `<div class="note">${t(UI.interactive)}</div>
        <p>
          <label>font-size <input id="icon-size" type="range" min="16" max="80" value="46"></label>
          <label>color <input id="icon-color" type="color" value="#1877f2"></label>
        </p>
        <p><i id="demo-icon" class="ai-facebook-fill" style="color:#1877f2;font-size:46px;"></i></p>`;
    }
    if (kind === "semantic") {
      return `<div class="note">${t(UI.interactive)} — header / nav / main / article / aside / footer</div>
        <div class="compare">
          <div class="example"><h3>&lt;div&gt; ${t(window.T("non sémantique", "non-semantic", "غير دلالي"))}</h3>
            <pre>&lt;div&gt;menu&lt;/div&gt;\n&lt;div&gt;annonce&lt;/div&gt;\n&lt;div&gt;copyright&lt;/div&gt;</pre></div>
          <div class="example"><h3>${t(window.T("sémantique", "semantic", "دلالي"))}</h3>
            <pre>&lt;nav&gt;menu&lt;/nav&gt;\n&lt;article&gt;annonce&lt;/article&gt;\n&lt;footer&gt;copyright&lt;/footer&gt;</pre></div>
        </div>`;
    }
    return "";
  }

  function liveHref(id) {
    if (!id || id === "revision") return "revision_notes.md";
    return id + "/index.html";
  }

  function renderHome() {
    const cards = chapters()
      .map(
        (c) => `<div class="card">
          <a href="#/chapitre/${c.id}" style="text-decoration:none;color:inherit">
            <h3>${c.num ? "Ch. " + c.num + " — " : ""}${t(c.titles)}</h3>
            <p>${t(c.lead)}</p>
          </a>
          <p><a class="btn small" href="${liveHref(c.id)}" target="_blank" rel="noopener">${t(UI.openLive)}</a></p>
        </div>`
      )
      .join("");
    const files = chapters()
      .filter((c) => c.num)
      .map((c) => `<li><a href="${c.id}/index.html" target="_blank" rel="noopener">${c.id}/index.html</a> — ${t(c.titles)}</li>`)
      .join("");
    $("#content").innerHTML = `
      <section class="home-hero">
        <h1>${t(UI.heroTitle)}</h1>
        <p>${t(UI.heroLead)}</p>
        <p>
          <a class="btn" href="#/chapitre/revision">${t(UI.openCourse)}</a>
          <a class="btn ghost" href="#/exos/revision">${t(UI.openExos)}</a>
        </p>
      </section>
      <h2>${t(UI.chapters)}</h2>
      <div class="cards">${cards}</div>
      <h2>${t(UI.files)}</h2>
      <ul>${files}<li><a href="exos/README.md" target="_blank" rel="noopener">exos/</a></li></ul>`;
  }

  function renderDoc(id) {
    const ch = chById(id);
    if (!ch) return renderHome();
    let html = pager(id);
    html += `<h1>${t(ch.titles)}</h1><p class="lead">${t(ch.lead)}</p>`;
    ch.sections.forEach((sec) => {
      html += `<h2>${t(sec.title)}</h2>`;
      (sec.p || []).forEach((para) => (html += `<p>${t(para)}</p>`));
      if (sec.table) html += renderTable(sec.table);
      if (sec.code) {
        html += `<div class="example"><h3>${t(UI.example)}</h3>`;
        if (sec.preview) html += `<div class="preview">${sec.code}</div>`;
        html += `<pre>${esc(sec.code)}<button type="button" class="btn small copy-code" style="margin-top:8px">${t(UI.copy)}</button></pre>${tryBtn(sec.code)}</div>`;
      }
      if (sec.interactive) html += interactiveBlock(sec.interactive);
    });
    if (ch.remember && ch.remember.length) {
      html += `<h2>${t(UI.remember)}</h2><ul>${ch.remember.map((x) => `<li>${t(x)}</li>`).join("")}</ul>`;
    }
    html += `<p>
      <a class="btn" href="#/exos/${ch.id}">${t(UI.exercises)} — ${t(ch.titles)}</a>
      <a class="btn ghost" href="${liveHref(ch.id)}" target="_blank" rel="noopener">${t(UI.openLive)}</a>
    </p>`;
    html += pager(id);
    $("#content").innerHTML = html;
  }

  function markProgress(id, kind, i) {
    state.progress[`${id}:${kind}:${i}`] = 1;
    save();
    renderSidebar();
  }

  function renderExos(id) {
    const ch = chById(id);
    const pack = (window.EXERCISES || {})[id];
    if (!ch || !pack) {
      $("#content").innerHTML = `<h1>${t(UI.exercises)}</h1><p>…</p>`;
      return;
    }
    const theory = pack.theoretical || [];
    const prac = pack.practical || [];
    let html = pager(id);
    html += `<h1>${t(UI.exercises)} — ${t(ch.titles)}</h1>
      <div class="tabs">
        <button data-tab="theory" class="${state.exoTab === "theory" ? "on" : ""}">${t(UI.quiz)} (${theory.length})</button>
        <button data-tab="practice" class="${state.exoTab === "practice" ? "on" : ""}">${t(UI.lab)} (${prac.length})</button>
      </div>
      <p class="score" id="live-score"></p>`;

    if (state.exoTab === "theory") {
      theory.forEach((q, i) => {
        html += `<article class="quiz-item" data-i="${i}">
          <h3>${i + 1}. ${t(q.q)}</h3>
          <div class="options">${q.options
            .map(
              (opt, j) =>
                `<button type="button" class="opt" data-j="${j}">${String.fromCharCode(97 + j)}) ${t(opt)}</button>`
            )
            .join("")}</div>
          <button class="btn small check-q">${t(UI.check)}</button>
          <div class="explain">${t(q.why)}</div>
        </article>`;
      });
    } else {
      prac.forEach((p, i) => {
        html += `<article class="prac-item" data-i="${i}">
          <h3>${i + 1}. ${t(p.task)}</h3>
          <p><b>${t(UI.hint)} :</b> ${t(p.hint)}</p>
          <div class="editor-wrap">
            <textarea class="editor">${esc(p.starter || "")}</textarea>
            <iframe class="live" sandbox="allow-scripts allow-same-origin"></iframe>
          </div>
          <p>
            <button class="btn small run-p">${t(UI.run)}</button>
            <button class="btn small ghost sol-p">${t(UI.solution)}</button>
            ${tryBtn(p.solution)}
          </p>
          <pre class="sol hidden">${esc(p.solution)}</pre>
        </article>`;
      });
    }
    html += pager(id);
    $("#content").innerHTML = html;
    updateScore(id);
  }

  function updateScore(id) {
    const pack = window.EXERCISES[id] || { theoretical: [], practical: [] };
    const total = (pack.theoretical || []).length + (pack.practical || []).length;
    const done = Object.keys(state.progress).filter((k) => k.startsWith(id + ":")).length;
    const el = $("#live-score");
    if (el) el.textContent = `${t(UI.score)} : ${done} / ${total}`;
  }

  function openTryit(code) {
    $("#try-code").value = code;
    runTry();
    $("#overlay").classList.add("show");
  }

  function runTry() {
    const html = $("#try-code").value;
    const doc = $("#try-frame").contentDocument;
    doc.open();
    doc.write(html);
    doc.close();
  }

  function route() {
    const r = parseHash();
    state.view = r.view;
    if (r.chapter) state.chapter = r.chapter;
    applyChrome();
    renderSidebar();
    if (state.view === "home") renderHome();
    else if (state.view === "exos") renderExos(state.chapter);
    else renderDoc(state.chapter);
    $("#sidebar").classList.remove("open");
    window.scrollTo(0, 0);
  }

  document.addEventListener("click", (e) => {
    const tab = e.target.closest("[data-tab]");
    if (tab) {
      state.exoTab = tab.getAttribute("data-tab");
      renderExos(state.chapter);
      return;
    }
    const tryb = e.target.closest("[data-code]");
    if (tryb) {
      openTryit(decodeURIComponent(tryb.getAttribute("data-code")));
      return;
    }
    const opt = e.target.closest(".opt");
    if (opt) {
      const item = opt.closest(".quiz-item");
      $$(".opt", item).forEach((b) => b.classList.remove("picked"));
      opt.classList.add("picked");
      return;
    }
    const check = e.target.closest(".check-q");
    if (check) {
      const item = check.closest(".quiz-item");
      const i = Number(item.dataset.i);
      const q = window.EXERCISES[state.chapter].theoretical[i];
      const picked = item.querySelector(".opt.picked");
      $$(".opt", item).forEach((b) => {
        b.classList.remove("correct", "wrong");
        if (Number(b.dataset.j) === q.a) b.classList.add("correct");
      });
      if (picked && Number(picked.dataset.j) !== q.a) picked.classList.add("wrong");
      item.querySelector(".explain").classList.add("show");
      markProgress(state.chapter, "t", i);
      updateScore(state.chapter);
      return;
    }
    const run = e.target.closest(".run-p");
    if (run) {
      const item = run.closest(".prac-item");
      const i = Number(item.dataset.i);
      const html = item.querySelector("textarea").value;
      const frame = item.querySelector("iframe");
      frame.srcdoc = html;
      markProgress(state.chapter, "p", i);
      updateScore(state.chapter);
      return;
    }
    const sol = e.target.closest(".sol-p");
    if (sol) {
      const item = sol.closest(".prac-item");
      item.querySelector(".sol").classList.toggle("hidden");
      return;
    }
    const ent = e.target.closest(".ent");
    if (ent) {
      navigator.clipboard.writeText(ent.dataset.ent);
      $("#ent-out").textContent = t(UI.copied) + " : " + ent.dataset.ent;
      return;
    }
    const copy = e.target.closest(".copy-code");
    if (copy) {
      const pre = copy.closest("pre");
      const text = pre.innerText.replace(copy.innerText, "").trim();
      navigator.clipboard.writeText(text);
      copy.textContent = t(UI.copied);
      setTimeout(() => (copy.textContent = t(UI.copy)), 1200);
      return;
    }
  });

  document.addEventListener("input", (e) => {
    if (e.target.id === "icon-size" || e.target.id === "icon-color") {
      const ic = $("#demo-icon");
      if (!ic) return;
      ic.style.fontSize = ($("#icon-size").value || 46) + "px";
      ic.style.color = $("#icon-color").value;
    }
  });

  $("#lang").addEventListener("change", () => {
    state.lang = $("#lang").value;
    save();
    route();
  });
  $("#btn-theme").addEventListener("click", () => {
    state.theme = state.theme === "dark" ? "light" : "dark";
    save();
    applyChrome();
  });
  $("#search").addEventListener("input", renderSidebar);
  $("#btn-menu").addEventListener("click", () => $("#sidebar").classList.toggle("open"));
  $("#btn-close-try").addEventListener("click", () => $("#overlay").classList.remove("show"));
  $("#btn-run-try").addEventListener("click", runTry);
  window.addEventListener("hashchange", route);
  applyChrome();
  route();
})();

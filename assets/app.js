/* Cote Boostée — une interface de lecture : aucun calcul de « value » n'est inventé ici. */
(() => {
  'use strict';

  const REPO_DATA = 'https://raw.githubusercontent.com/Matttgic/cotes-boostees/donnees/';
  const PARIS = 'Europe/Paris';
  const REFRESH_MS = 5 * 60 * 1000;
  const RECENT_AT_SCAN_MS = 150 * 60 * 1000;
  const STALE_MS = 3 * 60 * 60 * 1000;
  const PAGE_SIZE = 12;
  // Registre lisible : clés identiques à celles produites par le moteur Python.
  const STRATEGY_META = Object.freeze({
    A: ['A', 'TOUT PRENDRE', 'MISE MAX BOOKMAKER'],
    B_exacte: ['B1', 'EV EXACTE', '≥ 5 % · MISE MAX'],
    B_approx: ['B2', 'EV APPROCHÉE', '≥ 5 % · MISE MAX'],
    C_plafond: ['C', 'MISE PLAFONNÉE', 'TOUT · 10 € MAX'],
    D_moderee: ['D', 'COTES MODÉRÉES', '1,60–3,50 · 10 € MAX'],
    E_48h: ['E', 'HORIZON COURT', 'MATCH ≤ 48 H · 10 € MAX'],
    F_ev8: ['F', 'EV STRICTE', 'EXACTE ≥ 8 % · 10 € MAX'],
    G_kelly: ['G', 'QUART KELLY', 'EXACTE ≥ 5 % · RISQUE LIMITÉ'],
    H_1_match: ['H', 'UN PAR MATCH', '1ER BOOST VU · 10 € MAX'],
  });
  const state = {
    boosts: [], bilan: {}, etat: {}, view: 'actifs', strategy: 'A',
    search: '', sport: 'tous', bookmaker: 'tous', sort: 'recent',
    favoritesOnly: false, favorites: readFavorites(), expanded: new Set(),
    limit: PAGE_SIZE, loading: false, ready: false,
  };
  const $ = (id) => document.getElementById(id);
  const number = (v) => v === null || v === undefined || v === '' ? null : Number.isFinite(Number(v)) ? Number(v) : null;
  const fmt = (v, max = 1) => Number.isFinite(v) ? new Intl.NumberFormat('fr-FR', {maximumFractionDigits: max}).format(v) : '—';
  const euros = (v, decimals = 2) => Number.isFinite(v) ? `${v > 0 ? '+' : v < 0 ? '−' : ''}${new Intl.NumberFormat('fr-FR', {minimumFractionDigits: decimals, maximumFractionDigits: decimals}).format(Math.abs(v))} €` : '—';
  const pct = (v) => Number.isFinite(v) ? `${v > 0 ? '+' : ''}${fmt(v, 1)} %` : '—';
  const datetime = (s) => { const d = s ? new Date(s) : null; return d && Number.isFinite(d.getTime()) ? d : null; };
  const dateText = (s, options = {}) => {
    const d = datetime(s);
    return d ? new Intl.DateTimeFormat('fr-FR', {timeZone: PARIS, day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit', ...options}).format(d).replace(',', ' · ').toUpperCase() : 'DATE INCONNUE';
  };
  const esc = (v) => String(v ?? '').replace(/[&<>"']/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));
  const plain = (v) => String(v ?? '').trim();
  const valid = (v) => Number.isFinite(number(v));

  function readFavorites() {
    try { const s = JSON.parse(localStorage.getItem('cote-boostee:favorites') || '[]'); return new Set(Array.isArray(s) ? s.filter(x => typeof x === 'string') : []); }
    catch { return new Set(); }
  }
  function persistFavorites() { try { localStorage.setItem('cote-boostee:favorites', JSON.stringify([...state.favorites])); } catch {} }
  function notice(text) { const el = $('notice'); el.textContent = text; el.hidden = false; clearTimeout(notice._timer); notice._timer = setTimeout(() => { el.hidden = true; }, 5500); }
  function lastScan() { return state.etat?.dernier_passage?.date || null; }
  function scanAge() { const d = datetime(lastScan()); return d ? Date.now() - d.getTime() : Infinity; }
  function observedRecently(b) {
    const debut = datetime(b.debut), seen = datetime(b.derniere_vue), scan = datetime(lastScan());
    return Boolean(b.disponible && debut && debut.getTime() > Date.now() && seen && scan &&
      scan.getTime() - seen.getTime() <= RECENT_AT_SCAN_MS && seen.getTime() <= scan.getTime() + 60 * 1000);
  }
  function evData(b) {
    const cur = b.valeur_derniere, initial = b.valeur_initiale;
    if (cur && ['exacte', 'approx'].includes(cur.statut) && valid(cur.ev_pct)) return cur;
    if (initial && ['exacte', 'approx'].includes(initial.statut) && valid(initial.ev_pct)) return initial;
    return null;
  }
  function confirmedValue(b) { const v = b.valeur_derniere; return observedRecently(b) && v && v.statut === 'exacte' && number(v.ev_pct) >= 5; }
  function boostLift(b) {
    const uplift = number(b.hausse_pct);
    if (uplift !== null) return uplift;
    const before = number(b.cote_origine), after = number(b.cote_boostee);
    return before && after ? (after / before - 1) * 100 : null;
  }
  function allBoosts() { return state.boosts; }
  function visibleBoosts() {
    let all = allBoosts();
    if (state.view === 'actifs') all = all.filter(observedRecently);
    if (state.view === 'value') all = all.filter(confirmedValue);
    if (state.favoritesOnly) all = all.filter(b => state.favorites.has(b.id));
    if (state.sport !== 'tous') all = all.filter(b => plain(b.sport) === state.sport);
    if (state.bookmaker !== 'tous') all = all.filter(b => plain(b.bookmaker) === state.bookmaker);
    if (state.search) {
      const q = state.search.toLocaleLowerCase('fr-FR');
      all = all.filter(b => [b.match, b.pari, b.sport, b.bookmaker, b.ligue].some(s => plain(s).toLocaleLowerCase('fr-FR').includes(q)));
    }
    const timestamp = b => datetime(b.premiere_vue)?.getTime() || 0;
    const kickoff = b => datetime(b.debut)?.getTime() || Infinity;
    const odds = b => number(b.cote_boostee) || 0;
    const sorters = {
      recent: (a, b) => timestamp(b) - timestamp(a),
      soon: (a, b) => kickoff(a) - kickoff(b),
      uplift: (a, b) => (boostLift(b) ?? -Infinity) - (boostLift(a) ?? -Infinity),
      odd: (a, b) => odds(b) - odds(a),
    };
    return [...all].sort(sorters[state.sort] || sorters.recent);
  }

  function refreshHeader() {
    const scan = lastScan();
    const d = datetime(scan);
    $('scan-date').textContent = d ? dateText(scan, {day: '2-digit', month: 'short', hour: undefined, minute: undefined}) : '—';
    $('scan-time').textContent = d ? `À ${new Intl.DateTimeFormat('fr-FR', {timeZone: PARIS, hour: '2-digit', minute: '2-digit'}).format(d)} · Paris` : 'Aucune collecte connue';
    const age = scanAge();
    const failures = Object.entries(state.etat?.dernier_passage?.bookmakers || {}).filter(([, v]) => v?.erreur).map(([name]) => name);
    const stale = age > STALE_MS;
    $('data-status').textContent = stale ? '⚠ DONNÉES À REVÉRIFIER' : failures.length ? 'COLLECTE PARTIELLE' : 'DERNIÈRE COLLECTE ENREGISTRÉE';
    $('freshness-note').textContent = stale ? 'Dernière collecte ancienne : disponibilité non garantie.' : failures.length ? `${failures.join(', ')} : collecte en erreur.` : 'Présence au dernier scan, pas en temps réel.';
  }

  function refreshMetrics() {
    const a = state.bilan?.A?.global || {};
    const active = allBoosts().filter(observedRecently).length;
    const values = allBoosts().filter(confirmedValue).length;
    $('metric-all').textContent = fmt(allBoosts().length, 0);
    $('metric-active').textContent = fmt(active, 0);
    $('metric-settled').textContent = fmt(number(a.regles), 0);
    $('metric-roi').textContent = pct(number(a.roi_pct));
    $('tab-active-count').textContent = fmt(active, 0);
    $('tab-value-count').textContent = fmt(values, 0);
    $('tab-all-count').textContent = fmt(allBoosts().length, 0);
    $('count-value').textContent = fmt(values, 0);
    $('value-summary').textContent = values
      ? 'Ces offres dépassent +5 % d’EV selon une référence calculée « exacte ». Cela ne garantit pas de gain.'
      : 'Aucune offre encore disponible ne remplit actuellement le filtre strict. Une absence d’EV n’est pas une EV négative.';
  }

  function rebuildFilters() {
    for (const [id, field, fallback] of [['sport','sport','TOUS LES SPORTS'],['bookmaker','bookmaker','TOUS LES BOOKS']]) {
      const select = $(id), before = select.value;
      const options = [...new Set(state.boosts.map(b => plain(b[field])).filter(Boolean))].sort((a,b) => a.localeCompare(b, 'fr'));
      select.replaceChildren();
      const all = document.createElement('option'); all.value = 'tous'; all.textContent = fallback; select.append(all);
      for (const value of options) { const option = document.createElement('option'); option.value = value; option.textContent = value.toUpperCase(); select.append(option); }
      select.value = options.includes(before) ? before : 'tous'; state[id] = select.value;
    }
  }

  function resultMarkup(b) {
    const settle = b.reglement?.statut;
    if (settle === 'gagné') return '<span class="tiny-tag value">GAGNÉ · RÉGLÉ</span>';
    if (settle === 'perdu') return '<span class="tiny-tag expired">PERDU · RÉGLÉ</span>';
    if (settle === 'remboursé') return '<span class="tiny-tag">REMBOURSÉ</span>';
    return '';
  }
  function boostCard(b, idx) {
    const original = number(b.cote_origine), boosted = number(b.cote_boostee);
    const rise = boostLift(b), v = evData(b), here = observedRecently(b);
    const fav = state.favorites.has(b.id), expanded = state.expanded.has(b.id);
    const evMarkup = v ? `<span class="tiny-tag ${v.statut === 'exacte' ? 'value' : 'uncertain'}">${v === b.valeur_initiale && v !== b.valeur_derniere ? 'EV INIT.' : v.statut === 'exacte' ? 'EV' : 'EV ≈'} ${esc(pct(number(v.ev_pct)))}</span>` : '<span class="tiny-tag">EV NON ÉVALUÉE</span>';
    const date = b.long_terme ? 'SAISON / LONG TERME' : dateText(b.debut);
    const quality = v?.statut === 'exacte' ? 'Exacte selon la méthode du moteur.' : v?.statut === 'approx' ? 'Approchée : les conditions liées peuvent fausser la probabilité.' : 'Pas de référence suffisamment fiable.';
    const reason = b.valeur_derniere?.raison || b.valeur_initiale?.raison || '';
    const source = (v?.sources || []).join(', ') || 'Aucune source vérifiée';
    const ref = number(v?.cote_juste);
    const details = expanded ? `<div class="boost-detail" id="detail-${idx}">
      <div class="detail-item"><span>COTE JUSTE / RÉFÉRENCE</span><strong>${esc(ref === null ? 'Non disponible' : fmt(ref, 3))}</strong></div>
      <div class="detail-item"><span>MISE MAX REPÉRÉE</span><strong>${esc(valid(b.mise_max) ? fmt(number(b.mise_max), 2) + ' €' + (b.mise_max_supposee ? ' (estimée)' : '') : 'Inconnue')}</strong></div>
      <div class="detail-item"><span>VÉRIFIÉE POUR LA PREMIÈRE FOIS</span><strong>${esc(dateText(b.premiere_vue))}</strong></div>
      <div class="detail-item"><span>DERNIÈRE OBSERVATION</span><strong>${esc(dateText(b.derniere_vue))}</strong></div>
      <div class="detail-item"><span>SOURCE DE LA COTE JUSTE</span><strong>${esc(source)}</strong></div>
      <div class="detail-item"><span>STATUT DE L'ÉVALUATION</span><strong>${esc(quality)}</strong></div>
      <div class="detail-wide"><p class="detail-note">${esc(reason || 'Une cote boostée ne constitue pas une recommandation. L’EV affichée peut changer avec les prix du marché.')} ${here ? 'Présente au dernier scan ; sa disponibilité a pu changer.' : 'Cette offre n’est pas confirmée présente au dernier scan.'}</p></div>
    </div>` : '';
    return `<article class="boost-card" data-id="${esc(b.id)}">
      <div class="card-index">${String(idx + 1).padStart(2, '0')}</div>
      <div class="card-core"><div class="card-meta"><span class="bookmarker">${esc(plain(b.bookmaker) || 'BOOK INCONNU')}</span><span class="bullet">/</span><span>${esc(plain(b.sport) || 'SPORT INCONNU')}</span><span class="bullet">/</span><span>${esc(date)}</span></div>
        <h3 class="card-match">${esc(plain(b.match) || 'RENCONTRE NON RENSEIGNÉE')}</h3><p class="card-bet">${esc(plain(b.pari) || 'Intitulé indisponible')}</p>
        <div class="card-foot">${evMarkup}${here ? '<span class="tiny-tag">VU AU DERNIER SCAN</span>' : resultMarkup(b) || '<span class="tiny-tag expired">ARCHIVE</span>'}</div>
      </div>
      <div class="card-odds"><span class="odds-caption">COTE BOOSTÉE</span><strong class="odds-new">${esc(fmt(boosted, 2))}</strong>${original !== null ? `<span class="odds-old">${esc(fmt(original, 2))}</span>` : ''}${rise !== null ? `<span class="odd-lift">${esc(pct(rise))} DE HAUSSE</span>` : ''}<div class="card-actions"><button class="fav-btn" type="button" data-action="favorite" data-id="${esc(b.id)}" aria-pressed="${fav}" aria-label="${fav ? 'Retirer des favoris' : 'Ajouter aux favoris'}">${fav ? '★' : '☆'}</button><button class="more-btn" type="button" data-action="detail" data-id="${esc(b.id)}" aria-expanded="${expanded}" aria-controls="detail-${idx}">${expanded ? 'FERMER −' : 'DÉTAIL +'} </button></div></div>
      ${details}
    </article>`;
  }

  function renderList() {
    if (!state.ready) return;
    const rows = visibleBoosts();
    $('result-count').textContent = `${fmt(rows.length, 0)} OFFRE${rows.length > 1 ? 'S' : ''} / ${state.view === 'tous' ? 'HISTORIQUE COMPLET' : state.view === 'value' ? 'FILTRE EXACT EV ≥ 5 %' : 'DERNIÈRE COLLECTE'}`;
    if (!rows.length) {
      const description = state.view === 'value' && !state.search && !state.favoritesOnly
        ? 'Aucune offre récente avec une EV exacte d’au moins +5 %. Les modèles ne peuvent pas évaluer tous les boosts.'
        : state.favoritesOnly ? 'Aucun repère enregistré pour ces filtres. Étoile une offre dans la liste pour la retrouver.'
        : 'Aucun résultat avec ces filtres. Essaie le registre complet ou élargis la recherche.';
      $('boost-list').innerHTML = `<div class="empty-state"><span class="empty-state-symbol">∅</span><strong>RIEN À SIGNALER</strong><p>${esc(description)}</p><button type="button" id="reset-filters">EFFACER LES FILTRES ↗</button></div>`;
      $('reset-filters').addEventListener('click', () => { state.view = 'tous'; state.search = ''; state.sport = 'tous'; state.bookmaker = 'tous'; state.favoritesOnly = false; state.limit = PAGE_SIZE; $('search').value = ''; $('sport').value = 'tous'; $('bookmaker').value = 'tous'; syncControls(); renderList(); });
    } else { $('boost-list').innerHTML = rows.slice(0, state.limit).map(boostCard).join(''); }
    $('load-more').hidden = rows.length <= state.limit;
  }

  function syncControls() {
    document.querySelectorAll('[data-view]').forEach(btn => { const yes = state.view === btn.dataset.view; btn.classList.toggle('is-active', yes); btn.setAttribute('aria-pressed', String(yes)); });
    $('favorites-only').setAttribute('aria-pressed', String(state.favoritesOnly));
    $('favorites-only').firstChild.textContent = state.favoritesOnly ? '★ ' : '☆ ';
  }

  function drawChart(points) {
    const wrapper = $('chart');
    const data = (Array.isArray(points) ? points : []).map(p => number(p.cumul)).filter(v => v !== null);
    if (!data.length) { wrapper.setAttribute('aria-label', 'Aucun pari réglé, aucune courbe disponible'); wrapper.innerHTML = '<div class="chart-empty">PAS DE COURBE : AUCUN PARI RÉGLÉ POUR CETTE STRATÉGIE.</div>'; return; }
    const plot = [0, ...data];
    const lo = Math.min(0, ...plot), hi = Math.max(0, ...plot), pad = Math.max(10, (hi - lo) * .13);
    const low = lo - pad, high = hi + pad;
    const width = 800, height = 240, pX = 14, pY = 25;
    const x = i => pX + i / Math.max(1, plot.length - 1) * (width - pX * 2);
    const y = v => height - pY - (v - low) / (high - low) * (height - pY * 2);
    const pointsStr = plot.map((v, i) => `${x(i).toFixed(1)},${y(v).toFixed(1)}`).join(' ');
    const lastX = x(plot.length - 1).toFixed(1), lastY = y(plot[plot.length - 1]).toFixed(1);
    const color = data[data.length - 1] >= 0 ? '#20644a' : '#a5351b';
    const zero = y(0).toFixed(1);
    const intervals = [0.25, 0.5, 0.75].map(f => (pY + (height - pY * 2) * f).toFixed(1));
    const shape = `${pX},${zero} ${pointsStr} ${lastX},${zero}`;
    wrapper.setAttribute('aria-label', `Gain cumulé fictif après ${data.length} paris réglés : ${euros(data[data.length - 1])}`);
    wrapper.innerHTML = `<svg viewBox="0 0 ${width} ${height}" role="presentation" preserveAspectRatio="none" aria-hidden="true">
      ${intervals.map(yy => `<line x1="0" x2="800" y1="${yy}" y2="${yy}" stroke="#b7bcae" stroke-width="1" stroke-dasharray="3 6"/>`).join('')}
      <line x1="0" x2="800" y1="${zero}" y2="${zero}" stroke="#7a8175" stroke-width="1.5"/>
      <polygon points="${shape}" fill="${color}" fill-opacity=".09"/><polyline points="${pointsStr}" fill="none" stroke="${color}" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" vector-effect="non-scaling-stroke"/>
      <circle cx="${lastX}" cy="${lastY}" r="6" fill="${color}" stroke="#dfe0d2" stroke-width="3" vector-effect="non-scaling-stroke"/>
    </svg>`;
  }

  function renderStrategyChoices() {
    const keys = Object.keys(state.bilan || {}).filter(key => STRATEGY_META[key]);
    if (!keys.includes(state.strategy)) state.strategy = 'A';
    $('strategy-switch').innerHTML = keys.map(key => {
      const [tag, title, subtitle] = STRATEGY_META[key];
      return `<button type="button" data-strategy="${esc(key)}" class="strategy-button" aria-pressed="false">
        <span>STRATÉGIE ${esc(tag)}</span><strong>${esc(title)}</strong><small>${esc(subtitle)}</small>
      </button>`;
    }).join('');
  }

  function renderLab() {
    const b = state.bilan?.[state.strategy] || {}, g = b.global || {};
    const gain = number(g.gain_net), roi = number(g.roi_pct), settled = number(g.regles) || 0;
    const el = $('lab-gain'); el.textContent = gain === null ? '—' : euros(gain, 2); el.classList.toggle('positive', gain > 0); el.classList.toggle('negative', gain < 0);
    $('lab-roi').textContent = pct(roi);
    $('lab-settled').textContent = fmt(settled, 0);
    $('lab-detail').textContent = `${fmt(number(g.paris) || 0, 0)} paris fictifs · ${fmt(number(g.en_attente) || 0, 0)} en attente · mises réglées ${fmt(number(g.mise_totale) || 0, 0)} € · pire baisse ${euros(number(g.pire_baisse))}`;
    $('chart-caption').textContent = `${settled} PARI${settled > 1 ? 'S' : ''} RÉGLÉ${settled > 1 ? 'S' : ''}`;
    drawChart(b.courbe);
    document.querySelectorAll('[data-strategy]').forEach(btn => { const yes = btn.dataset.strategy === state.strategy; btn.classList.toggle('is-active', yes); btn.setAttribute('aria-pressed', String(yes)); });
  }

  function renderSettlements() {
    const settled = (state.bilan?.A?.paris || []).filter(p => ['gagné','perdu','remboursé'].includes(p.statut)).sort((a,b) => (datetime(b.debut)?.getTime() || 0) - (datetime(a.debut)?.getTime() || 0)).slice(0, 10);
    if (!settled.length) { $('settled-table').innerHTML = '<tr><td colspan="5">Aucun résultat réglé disponible.</td></tr>'; return; }
    $('settled-table').innerHTML = settled.map(p => {
      const won = p.statut === 'gagné', lost = p.statut === 'perdu', gain = number(p.gain);
      return `<tr><td>${esc(plain(p.match) || 'Rencontre inconnue')}<small>${esc(plain(p.pari))}</small></td><td>${esc(plain(p.bookmaker))}</td><td>${esc(fmt(number(p.cote),2))}</td><td><span class="result-chip ${won ? 'won' : lost ? 'lost' : ''}">${esc(plain(p.statut).toUpperCase())}</span></td><td class="${gain > 0 ? 'money-positive' : gain < 0 ? 'money-negative' : ''}">${esc(euros(gain))}</td></tr>`;
    }).join('');
  }

  async function getJSON(file, cacheKey) {
    const res = await fetch(`${REPO_DATA}${file}?edition=${cacheKey}`, {cache:'no-store'});
    if (!res.ok) throw new Error(`${file} : HTTP ${res.status}`);
    return await res.json();
  }
  async function refresh() {
    if (state.loading) return;
    state.loading = true;
    $('refresh').disabled = true; $('refresh').classList.add('is-loading');
    try {
      const key = Math.floor(Date.now() / 60000);
      const [boosts, bilan, etat] = await Promise.all(['boosts.json','bilan.json','etat.json'].map(file => getJSON(file, key)));
      if (!boosts || typeof boosts !== 'object' || Array.isArray(boosts) || !bilan?.A?.global || !etat?.dernier_passage) throw new Error('Format des données inattendu');
      state.boosts = Object.values(boosts).filter(b => b && typeof b === 'object' && typeof b.id === 'string');
      state.bilan = bilan; state.etat = etat; state.ready = true;
      rebuildFilters(); refreshHeader(); refreshMetrics(); syncControls(); renderList(); renderStrategyChoices(); renderLab(); renderSettlements();
    } catch (error) {
      if (!state.ready) {
        $('boost-list').innerHTML = '<div class="empty-state"><span class="empty-state-symbol">!</span><strong>REGISTRE INACCESSIBLE</strong><p>Les fichiers publics GitHub ne répondent pas. Aucun chiffre de remplacement n’est affiché.</p><button id="retry" type="button">RÉESSAYER ↗</button></div>';
        $('retry').addEventListener('click', refresh);
        $('data-status').textContent = 'CONNEXION IMPOSSIBLE';
      }
      notice('Impossible d’actualiser les données. Dernières données conservées si disponibles.');
      console.warn('[Cote Boostée] Chargement échoué :', error);
    } finally { state.loading = false; $('refresh').disabled = false; $('refresh').classList.remove('is-loading'); }
  }

  function initialize() {
    $('refresh').addEventListener('click', refresh);
    $('search').addEventListener('input', (e) => { state.search = e.target.value.trim(); state.limit = PAGE_SIZE; renderList(); });
    for (const id of ['sport','bookmaker','sort']) $(id).addEventListener('change', e => { state[id] = e.target.value; state.limit = PAGE_SIZE; renderList(); });
    document.querySelectorAll('[data-view]').forEach(button => button.addEventListener('click', () => { state.view = button.dataset.view; state.limit = PAGE_SIZE; syncControls(); renderList(); }));
    $('strategy-switch').addEventListener('click', event => { const button = event.target.closest('button[data-strategy]'); if (button && STRATEGY_META[button.dataset.strategy]) { state.strategy = button.dataset.strategy; renderLab(); } });
    $('favorites-only').addEventListener('click', () => { state.favoritesOnly = !state.favoritesOnly; state.limit = PAGE_SIZE; syncControls(); renderList(); });
    $('load-more').addEventListener('click', () => { state.limit += PAGE_SIZE; renderList(); });
    $('boost-list').addEventListener('click', (e) => {
      const button = e.target.closest('button[data-action]'); if (!button) return;
      const id = button.dataset.id;
      if (button.dataset.action === 'favorite') { state.favorites.has(id) ? state.favorites.delete(id) : state.favorites.add(id); persistFavorites(); }
      if (button.dataset.action === 'detail') { state.expanded.has(id) ? state.expanded.delete(id) : state.expanded.add(id); }
      renderList();
    });
    refresh();
    setInterval(() => { if (!document.hidden) refresh(); }, REFRESH_MS);
    document.addEventListener('visibilitychange', () => { if (!document.hidden && state.ready && scanAge() > STALE_MS) refreshHeader(); });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initialize); else initialize();
})();

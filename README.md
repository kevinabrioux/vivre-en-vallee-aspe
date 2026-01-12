<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Bien immobilier à vendre – Bedous (Vallée d’Aspe) | 300 m² + chambres d’hôtes</title>
  <meta name="description" content="Ensemble immobilier ~300 m² au centre de Bedous (Vallée d’Aspe). Chambres d’hôtes en activité avec revenus immédiats, potentiel commercial et partie privative." />
  <meta name="theme-color" content="#0b1f17" />

  <!-- Open Graph -->
  <meta property="og:title" content="Bien immobilier de caractère à vendre – Bedous (Vallée d’Aspe)" />
  <meta property="og:description" content="~300 m², chambres d’hôtes en activité, revenus immédiats, fort potentiel de reconversion commerciale, centre village." />
  <meta property="og:type" content="website" />
  <meta property="og:image" content="assets/hero.jpg" />
  <meta property="og:locale" content="fr_FR" />

  <!-- Minimal schema.org (à ajuster si besoin) -->
  <script type="application/ld+json">
  {
    "@context":"https://schema.org",
    "@type":"RealEstateListing",
    "name":"Bien immobilier de caractère à vendre – Bedous (Vallée d’Aspe)",
    "description":"Ensemble immobilier d’environ 300 m² au centre de Bedous. Chambres d’hôtes en activité et potentiel commercial, avec possibilité d’habitation privative.",
    "address":{
      "@type":"PostalAddress",
      "addressLocality":"Bedous",
      "addressRegion":"Pyrénées-Atlantiques",
      "addressCountry":"FR"
    },
    "url":""
  }
  </script>

  <style>
    :root{
      --bg:#07140f;
      --card:#0b1f17;
      --text:#e7f3ee;
      --muted:#b8c9c2;
      --brand:#3ddc97;
      --brand2:#56a3ff;
      --line:rgba(255,255,255,.10);
      --shadow: 0 18px 60px rgba(0,0,0,.35);
      --radius: 18px;
      --max: 1120px;
      --pad: clamp(16px, 3vw, 28px);
    }
    *{box-sizing:border-box}
    html,body{height:100%}
    body{
      margin:0;
      font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial, "Apple Color Emoji", "Segoe UI Emoji";
      color:var(--text);
      background:
        radial-gradient(900px 500px at 20% 10%, rgba(61,220,151,.18), transparent 55%),
        radial-gradient(900px 500px at 80% 20%, rgba(86,163,255,.16), transparent 55%),
        linear-gradient(180deg, #06120d, #04100b);
      line-height:1.55;
    }
    a{color:inherit}
    .wrap{max-width:var(--max); margin:0 auto; padding:0 var(--pad)}
    .nav{
      position:sticky; top:0; z-index:20;
      backdrop-filter:saturate(140%) blur(10px);
      background:rgba(4,16,11,.6);
      border-bottom:1px solid var(--line);
    }
    .navinner{
      display:flex; align-items:center; justify-content:space-between;
      gap:16px; padding:14px 0;
    }
    .logo{
      display:flex; align-items:center; gap:10px; text-decoration:none;
      font-weight:700; letter-spacing:.2px;
    }
    .dot{width:12px;height:12px;border-radius:999px;background:linear-gradient(135deg,var(--brand),var(--brand2))}
    .navlinks{
      display:flex; gap:14px; align-items:center; flex-wrap:wrap;
      font-size:14px; color:var(--muted);
    }
    .navlinks a{ text-decoration:none; padding:8px 10px; border-radius:12px; }
    .navlinks a:hover{ background:rgba(255,255,255,.06); color:var(--text); }
    .btn{
      display:inline-flex; align-items:center; justify-content:center;
      gap:10px;
      padding:12px 14px;
      border-radius:14px;
      border:1px solid rgba(255,255,255,.14);
      background:rgba(255,255,255,.06);
      color:var(--text);
      text-decoration:none;
      box-shadow: 0 12px 40px rgba(0,0,0,.15);
      font-weight:600;
      cursor:pointer;
    }
    .btn.primary{
      border:none;
      background:linear-gradient(135deg,var(--brand),var(--brand2));
      color:#04100b;
    }
    .btn:hover{ transform:translateY(-1px); transition:transform .15s ease }
    .hero{
      padding: clamp(30px, 6vw, 68px) 0 26px;
    }
    .grid{
      display:grid;
      grid-template-columns: 1.1fr .9fr;
      gap: clamp(16px, 3.5vw, 34px);
      align-items:stretch;
    }
    @media (max-width: 900px){
      .grid{grid-template-columns: 1fr}
      .navlinks{display:none}
    }
    .badge{
      display:inline-flex; align-items:center; gap:8px;
      padding:8px 12px; border-radius:999px;
      border:1px solid rgba(255,255,255,.14);
      background:rgba(255,255,255,.06);
      color:var(--muted);
      font-size:14px;
    }
    .h1{
      font-size: clamp(32px, 5vw, 54px);
      line-height:1.05;
      margin: 14px 0 12px;
      letter-spacing:-.8px;
    }
    .sub{
      color:var(--muted);
      font-size: clamp(16px, 2vw, 18px);
      margin:0 0 18px;
      max-width: 60ch;
    }
    .heroCard{
      background:rgba(255,255,255,.04);
      border:1px solid rgba(255,255,255,.12);
      border-radius: var(--radius);
      overflow:hidden;
      box-shadow: var(--shadow);
      display:flex;
      flex-direction:column;
      min-height: 420px;
    }
    .heroImg{
      background:
        linear-gradient(180deg, rgba(0,0,0,.0), rgba(0,0,0,.55)),
        url("assets/hero.jpg");
      background-size:cover;
      background-position:center;
      flex:1;
      min-height:260px;
    }
    .heroMeta{
      padding:16px 18px;
      border-top:1px solid rgba(255,255,255,.10);
      display:grid;
      grid-template-columns: repeat(3, 1fr);
      gap:10px;
      background: rgba(11,31,23,.75);
    }
    .kpi{
      padding:12px 12px;
      border-radius:14px;
      background: rgba(255,255,255,.05);
      border:1px solid rgba(255,255,255,.10);
    }
    .kpi b{display:block; font-size:14px}
    .kpi span{display:block; color:var(--muted); font-size:13px}
    .section{padding: 26px 0}
    .titleRow{
      display:flex; align-items:flex-end; justify-content:space-between; gap:14px; flex-wrap:wrap;
      margin-bottom:14px;
    }
    h2{margin:0; font-size: clamp(22px, 3vw, 30px); letter-spacing:-.3px}
    .lead{margin:0; color:var(--muted); max-width:75ch}
    .cards{
      display:grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 14px;
    }
    @media (max-width: 900px){
      .cards{grid-template-columns: 1fr}
      .heroMeta{grid-template-columns:1fr}
    }
    .card{
      background: rgba(255,255,255,.04);
      border:1px solid rgba(255,255,255,.12);
      border-radius: var(--radius);
      padding: 16px 16px;
      box-shadow: 0 10px 28px rgba(0,0,0,.18);
    }
    .card h3{margin:0 0 8px; font-size:18px}
    .card p{margin:0; color:var(--muted)}
    .list{
      display:grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px 16px;
      margin-top: 12px;
    }
    @media (max-width: 900px){ .list{grid-template-columns:1fr} }
    .li{
      display:flex; gap:10px; align-items:flex-start;
      padding:12px 12px;
      border-radius:16px;
      background: rgba(255,255,255,.04);
      border:1px solid rgba(255,255,255,.10);
    }
    .ico{width:28px;height:28px;border-radius:10px;display:grid;place-items:center;background:rgba(61,220,151,.14);border:1px solid rgba(61,220,151,.28)}
    .li b{display:block}
    .li span{display:block; color:var(--muted); font-size:14px}
    .gallery{
      display:grid;
      grid-template-columns: 1.2fr .8fr .8fr;
      gap: 12px;
    }
    .g{
      border-radius: var(--radius);
      border:1px solid rgba(255,255,255,.12);
      background: rgba(255,255,255,.04);
      overflow:hidden;
      min-height: 210px;
      position:relative;
    }
    .g.big{grid-row: span 2; min-height: 432px;}
    .g img{
      width:100%; height:100%; object-fit:cover; display:block;
      filter:saturate(1.02) contrast(1.02);
    }
    .g .cap{
      position:absolute; left:12px; bottom:12px;
      padding:8px 10px; border-radius:14px;
      background: rgba(4,16,11,.62);
      border:1px solid rgba(255,255,255,.12);
      color: var(--text);
      font-size:13px;
    }
    @media (max-width: 900px){
      .gallery{grid-template-columns:1fr}
      .g.big{grid-row:auto; min-height:260px}
    }
    .cta{
      padding: 26px 0 48px;
    }
    .ctaBox{
      border-radius: calc(var(--radius) + 6px);
      border:1px solid rgba(255,255,255,.14);
      background:
        radial-gradient(600px 300px at 20% 0%, rgba(61,220,151,.18), transparent 60%),
        radial-gradient(600px 300px at 90% 30%, rgba(86,163,255,.18), transparent 60%),
        rgba(255,255,255,.04);
      box-shadow: var(--shadow);
      padding: clamp(16px, 3vw, 22px);
      display:grid;
      grid-template-columns: 1fr 1fr;
      gap: 18px;
      align-items:start;
    }
    @media (max-width: 900px){ .ctaBox{grid-template-columns:1fr} }
    form{
      display:grid;
      gap: 10px;
    }
    label{font-size:13px; color:var(--muted)}
    input, textarea{
      width:100%;
      padding: 12px 12px;
      border-radius: 14px;
      border: 1px solid rgba(255,255,255,.14);
      background: rgba(4,16,11,.35);
      color: var(--text);
      outline:none;
    }
    textarea{min-height:120px; resize:vertical}
    .hint{color:var(--muted); font-size:13px; margin:8px 0 0}
    footer{
      padding: 18px 0 28px;
      color: rgba(231,243,238,.72);
      border-top: 1px solid var(--line);
      background: rgba(4,16,11,.35);
    }
    .small{font-size:13px; color:rgba(231,243,238,.72)}
    .pillRow{display:flex; gap:10px; flex-wrap:wrap; margin-top: 14px}
    .pill{
      font-size:13px;
      padding:8px 10px;
      border-radius:999px;
      border:1px solid rgba(255,255,255,.14);
      background: rgba(255,255,255,.05);
      color: var(--muted);
    }
  </style>
</head>

<body>
  <!-- NAV -->
  <header class="nav" role="banner">
    <div class="wrap navinner">
      <a class="logo" href="#top" aria-label="Retour en haut de page">
        <span class="dot" aria-hidden="true"></span>
        <span>Bedous • Vallée d’Aspe</span>
      </a>

      <nav class="navlinks" aria-label="Navigation principale">
        <a href="#points-forts">Points forts</a>
        <a href="#chambres">Chambres d’hôtes</a>
        <a href="#rdc">Rez-de-chaussée</a>
        <a href="#galerie">Galerie</a>
        <a href="#contact">Contact</a>
      </nav>

      <a class="btn primary" href="#contact">📞 Demander infos / visite</a>
    </div>
  </header>

  <!-- HERO -->
  <main id="top" class="hero">
    <div class="wrap grid">
      <section>
        <div class="badge">🏡 Bien immobilier de caractère à vendre – <b>Bedous</b> (Vallée d’Aspe)</div>
        <h1 class="h1">Un lieu de vie + une activité au cœur des Pyrénées-Atlantiques</h1>
        <p class="sub">
          Situé au <b>centre du village</b> (commodités à pied), cet ensemble immobilier d’environ <b>300 m²</b> offre une opportunité rare :
          <b>habiter sur place</b> tout en générant <b>immédiatement des revenus</b> grâce à une activité de <b>chambres d’hôtes</b> déjà en place.
        </p>

        <div class="pillRow" aria-label="Résumé">
          <span class="pill">📍 Centre village</span>
          <span class="pill">🏠 ~300 m²</span>
          <span class="pill">💼 Activité en cours</span>
          <span class="pill">🔄 Potentiel commerce</span>
          <span class="pill">🔑 Projet clé en main</span>
        </div>

        <div style="display:flex; gap:12px; flex-wrap:wrap; margin-top:18px">
          <a class="btn primary" href="#contact">Recevoir photos & bilans</a>
          <a class="btn" href="#galerie">Voir la galerie</a>
        </div>

        <p class="hint">Astuce : remplacez <code>assets/hero.jpg</code> et les images de la galerie par vos photos.</p>
      </section>

      <aside class="heroCard" aria-label="Aperçu">
        <div class="heroImg" role="img" aria-label="Photo principale du bien (à remplacer)"></div>
        <div class="heroMeta">
          <div class="kpi">
            <b>Surface</b>
            <span>~300 m²</span>
          </div>
          <div class="kpi">
            <b>Usage</b>
            <span>Habitation + activité</span>
          </div>
          <div class="kpi">
            <b>Localisation</b>
            <span>Bedous, Vallée d’Aspe</span>
          </div>
        </div>
      </aside>
    </div>
  </main>

  <!-- POINTS FORTS -->
  <section id="points-forts" class="section">
    <div class="wrap">
      <div class="titleRow">
        <h2>✨ Les points forts</h2>
        <p class="lead">Un bien rare pour un projet de vie, touristique ou commercial, avec un démarrage immédiat.</p>
      </div>

      <div class="cards">
        <article class="card">
          <h3>📍 Emplacement central</h3>
          <p>Au centre de Bedous, avec les commodités accessibles à pied.</p>
        </article>
        <article class="card">
          <h3>🏔️ Cadre naturel exceptionnel</h3>
          <p>Vallée d’Aspe, Pyrénées : un environnement très recherché par la clientèle.</p>
        </article>
        <article class="card">
          <h3>💼 Revenus immédiats</h3>
          <p>Chambres d’hôtes <b>toujours en activité</b>, activité touristique existante.</p>
        </article>
        <article class="card">
          <h3>🔄 Fort potentiel</h3>
          <p>Reconversion possible : restaurant, café, concept-store, bien-être, etc.</p>
        </article>
        <article class="card">
          <h3>🔑 Clé en main</h3>
          <p>Structure déjà fonctionnelle, idéale pour démarrer sans attendre.</p>
        </article>
        <article class="card">
          <h3>🏠 Vie privée préservée</h3>
          <p>Possibilité de conserver une partie privative pour l’habitation.</p>
        </article>
      </div>
    </div>
  </section>

  <!-- CHAMBRES D'HOTES -->
  <section id="chambres" class="section">
    <div class="wrap">
      <div class="titleRow">
        <h2>🛏️ Espace chambres d’hôtes (1er étage)</h2>
        <p class="lead">Un espace chaleureux, apprécié par la clientèle, pensé pour le confort et l’exploitation.</p>
      </div>

      <div class="list">
        <div class="li"><div class="ico">🛌</div><div><b>4 chambres confortables</b><span>Disposition idéale pour accueillir des voyageurs.</span></div></div>
        <div class="li"><div class="ico">🚿</div><div><b>Salles d’eau privatives</b><span>Confort et autonomie pour chaque chambre.</span></div></div>
        <div class="li"><div class="ico">🚻</div><div><b>WC privatifs</b><span>Atout important pour la clientèle.</span></div></div>
        <div class="li"><div class="ico">❄️</div><div><b>Climatisation</b><span>Confort été/hiver (selon équipements en place).</span></div></div>
        <div class="li"><div class="ico">🧖‍♂️</div><div><b>Sauna</b><span>Différenciant, idéal après randonnée.</span></div></div>
        <div class="li"><div class="ico">🧺</div><div><b>Lingerie</b><span>Organisation facilitée pour l’exploitation.</span></div></div>
        <div class="li"><div class="ico">🛋️</div><div><b>Salon commun</b><span>Espace convivial pour les hôtes.</span></div></div>
        <div class="li"><div class="ico">🌿</div><div><b>Petite terrasse</b><span>Un extérieur appréciable pour les pauses.</span></div></div>
      </div>
    </div>
  </section>

  <!-- RDC -->
  <section id="rdc" class="section">
    <div class="wrap">
      <div class="titleRow">
        <h2>🍽️ Espaces communs (rez-de-chaussée)</h2>
        <p class="lead">Des espaces adaptés à l’accueil et à une activité de restauration légère / commerciale.</p>
      </div>

      <div class="cards">
        <article class="card">
          <h3>☕ Salle petits-déjeuners</h3>
          <p>Espace dédié pour servir les clients et structurer l’activité.</p>
        </article>
        <article class="card">
          <h3>👩‍🍳 Cuisine pro avec extraction</h3>
          <p>Base solide pour une offre de restauration légère ou un concept alimentaire.</p>
        </article>
        <article class="card">
          <h3>🧩 Polyvalence</h3>
          <p>Possibilités : café, restaurant, concept-store, bien-être, atelier, etc.</p>
        </article>
      </div>
    </div>
  </section>

  <!-- GALERIE -->
  <section id="galerie" class="section">
    <div class="wrap">
      <div class="titleRow">
        <h2>📷 Galerie (photos à ajouter)</h2>
        <p class="lead">Ajoutez vos photos dans le dossier <code>assets/</code> puis mettez à jour les chemins ci-dessous.</p>
      </div>

      <div class="gallery" aria-label="Galerie photos">
        <figure class="g big">
          <img src="assets/galerie-1.jpg" alt="Vue principale du bien (à remplacer)" onerror="this.style.display='none'; this.parentElement.style.background='rgba(255,255,255,.04)';" />
          <figcaption class="cap">Photo 1 — Façade / vue principale</figcaption>
        </figure>
        <figure class="g">
          <img src="assets/galerie-2.jpg" alt="Chambre (à remplacer)" onerror="this.style.display='none'; this.parentElement.style.background='rgba(255,255,255,.04)';" />
          <figcaption class="cap">Photo 2 — Chambre</figcaption>
        </figure>
        <figure class="g">
          <img src="assets/galerie-3.jpg" alt="Salle petit-déjeuner (à remplacer)" onerror="this.style.display='none'; this.parentElement.style.background='rgba(255,255,255,.04)';" />
          <figcaption class="cap">Photo 3 — Salle petit-déjeuner</figcaption>
        </figure>
        <figure class="g">
          <img src="assets/galerie-4.jpg" alt="Cuisine (à remplacer)" onerror="this.style.display='none'; this.parentElement.style.background='rgba(255,255,255,.04)';" />
          <figcaption class="cap">Photo 4 — Cuisine</figcaption>
        </figure>
        <figure class="g">
          <img src="assets/galerie-5.jpg" alt="Terrasse / extérieur (à remplacer)" onerror="this.style.display='none'; this.parentElement.style.background='rgba(255,255,255,.04)';" />
          <figcaption class="cap">Photo 5 — Terrasse</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <!-- CONTACT -->
  <section id="contact" class="cta">
    <div class="wrap">
      <div class="titleRow">
        <h2>📞 Intéressé(e) ? Recevez infos, photos, bilans & planifiez une visite</h2>
        <p class="lead">Remplissez le formulaire ci-dessous (envoi par email) ou appelez directement.</p>
      </div>

      <div class="ctaBox">
        <div>
          <h3 style="margin:0 0 8px">✅ Ce que vous pouvez demander</h3>
          <div class="list">
            <div class="li"><div class="ico">📸</div><div><b>Dossier photos</b><span>Intérieur / extérieur / plans si disponibles</span></div></div>
            <div class="li"><div class="ico">📊</div><div><b>Bilans d’activité</b><span>Chiffres & informations utiles</span></div></div>
            <div class="li"><div class="ico">🗓️</div><div><b>Visite</b><span>Proposition de créneaux</span></div></div>
            <div class="li"><div class="ico">💬</div><div><b>Questions</b><span>Potentiel commercial, travaux, organisation, etc.</span></div></div>
          </div>

          <div style="margin-top:14px; display:flex; gap:12px; flex-wrap:wrap">
            <a class="btn" href="tel:+33000000000">📱 Appeler (à modifier)</a>
            <a class="btn" href="mailto:contact@exemple.fr?subject=Demande%20d%27informations%20-%20Bien%20%C3%A0%20Bedous">✉️ Email direct (à modifier)</a>
          </div>

          <p class="hint">Pensez à remplacer le numéro et l’email ci-dessus.</p>
        </div>

        <form id="leadForm">
          <div>
            <label for="name">Nom</label>
            <input id="name" name="name" placeholder="Votre nom" autocomplete="name" required />
          </div>

          <div>
            <label for="email">Email</label>
            <input id="email" name="email" type="email" placeholder="votre@email.com" autocomplete="email" required />
          </div>

          <div>
            <label for="phone">Téléphone (optionnel)</label>
            <input id="phone" name="phone" placeholder="06 00 00 00 00" autocomplete="tel" />
          </div>

          <div>
            <label for="msg">Message</label>
            <textarea id="msg" name="msg" required
              placeholder="Bonjour, je souhaite recevoir les photos / bilans et organiser une visite. Mes disponibilités sont…"></textarea>
          </div>

          <button class="btn primary" type="submit">Envoyer la demande</button>
          <p class="small" style="margin:0">
            En cliquant sur “Envoyer”, votre logiciel email s’ouvrira (envoi via <code>mailto:</code>).
            Pour un vrai envoi sans client mail, il faudra brancher un service (Formspree, Netlify Forms, etc.).
          </p>
        </form>
      </div>
    </div>
  </section>

  <footer>
    <div class="wrap" style="display:flex; justify-content:space-between; gap:12px; flex-wrap:wrap; align-items:center">
      <div class="small">© <span id="year"></span> • Bien immobilier – Bedous (Vallée d’Aspe)</div>
      <div class="small">Site statique prêt pour GitHub Pages</div>
    </div>
  </footer>

  <script>
    // Année automatique
    document.getElementById("year").textContent = new Date().getFullYear();

    // Envoi via mailto (simple et compatible GitHub Pages)
    const form = document.getElementById("leadForm");
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const name = document.getElementById("name").value.trim();
      const email = document.getElementById("email").value.trim();
      const phone = document.getElementById("phone").value.trim();
      const msg = document.getElementById("msg").value.trim();

      const to = "contact@exemple.fr"; // <-- à modifier
      const subject = "Demande d'informations – Bien à Bedous (Vallée d’Aspe)";
      const body =
`Bonjour,

Nom: ${name}
Email: ${email}
Téléphone: ${phone || "—"}

Message:
${msg}

Cordialement,
${name}`;

      const mailto = `mailto:${encodeURIComponent(to)}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
      window.location.href = mailto;
    });
  </script>
</body>
</html>

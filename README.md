<html lang="fr">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Bien immobilier à vendre – Bedous (Vallée d’Aspe) | 311 m² + chambres d’hôtes</title>
  <meta name="description" content="Ensemble immobilier de 311 m² au centre de Bedous (Vallée d’Aspe). Chambres d’hôtes en activité avec revenus immédiats, potentiel commercial et partie privative." />
  <meta name="theme-color" content="#ffffff" />

  <!-- Police serif (retours Natalie : Garamond) -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400..800;1,400..800&display=swap" rel="stylesheet" />

  <!-- Open Graph -->
  <meta property="og:title" content="Bien immobilier de caractère à vendre – Bedous (Vallée d’Aspe)" />
  <meta property="og:description" content="311 m², chambres d’hôtes en activité, revenus immédiats, fort potentiel de reconversion commerciale, centre village." />
  <meta property="og:type" content="website" />
  <meta property="og:image" content="assets/hero.jpg" />
  <meta property="og:locale" content="fr_FR" />

  <!-- Minimal schema.org (à ajuster si besoin) -->
  <script type="application/ld+json">
  {
    "@context":"https://schema.org",
    "@type":"RealEstateListing",
    "name":"Bien immobilier de caractère à vendre – Bedous (Vallée d’Aspe)",
    "description":"Ensemble immobilier de 311 m² au centre de Bedous. DPE classe C, GES classe B. Chambres d’hôtes en activité et potentiel commercial, avec possibilité d’habitation privative.",
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
      /* Palette Natalie : ocre brûlé / ocre doré / crème / bleu marine / bleu nuit */
      --bg:#ffffff;
      --card:#ffffff;
      --cream:#F1EBE0;
      --text:#172B69;
      --navy:#0A1237;
      --muted:#4a5678;
      --brand:#99460E;
      --brand2:#E8A93F;
      --accent:#E8A93F;
      --line:rgba(23,43,105,.14);
      --shadow: 0 12px 40px rgba(10,18,55,.08);
      --radius: 18px;
      --max: 1120px;
      --pad: clamp(16px, 3vw, 28px);
    }
    *{box-sizing:border-box}
    html,body{height:100%}
    body{
      margin:0;
      font-family: "EB Garamond", Garamond, "Book Antiqua", "Palatino Linotype", Palatino, Georgia, serif;
      color:var(--text);
      background:var(--bg);
      line-height:1.55;
      font-size:17px;
    }
    a{color:inherit}
    .wrap{max-width:var(--max); margin:0 auto; padding:0 var(--pad)}
    .nav{
      position:sticky; top:0; z-index:20;
      backdrop-filter:saturate(140%) blur(10px);
      background:rgba(255,255,255,.92);
      border-bottom:1px solid var(--line);
    }
    .navinner{
      display:flex; align-items:center; justify-content:space-between;
      gap:16px; padding:14px 0;
    }
    .logo{
      display:flex; align-items:center; gap:10px; text-decoration:none;
      font-weight:700; letter-spacing:.2px; white-space:nowrap;
    }
    .dot{width:12px;height:12px;border-radius:999px;background:linear-gradient(135deg,var(--brand),var(--brand2))}
    .navlinks{
      display:flex; gap:6px; align-items:center; flex-wrap:nowrap;
      font-size:16px; color:var(--text); font-weight:600;
    }
    .navlinks a{ text-decoration:none; padding:8px 9px; border-radius:12px; white-space:nowrap; }
    .navlinks a:hover{ background:var(--cream); color:var(--navy); }
    .btn{
      display:inline-flex; align-items:center; justify-content:center;
      gap:10px;
      padding:12px 14px;
      border-radius:14px;
      border:1px solid var(--line);
      background:#ffffff;
      color:var(--text);
      text-decoration:none;
      box-shadow: 0 6px 20px rgba(10,18,55,.08);
      font-weight:600;
      cursor:pointer;
    }
    .btn.primary{
      border:2px solid var(--brand);
      background:#ffffff;
      color:var(--text);
      font-weight:700;
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
    @media (max-width: 1080px){
      .navlinks{display:none}
    }
    @media (max-width: 900px){
      .grid{grid-template-columns: 1fr}
    }
    .badge{
      display:inline-flex; align-items:center; gap:8px;
      padding:8px 12px; border-radius:999px;
      border:1px solid rgba(153,70,14,.35);
      background:var(--cream);
      color:var(--text);
      font-size:15px;
    }
    .h1{
      font-size: clamp(28px, 4vw, 44px);
      line-height:1.12;
      margin: 14px 0 12px;
      letter-spacing:0;
      color:var(--navy);
    }
    .sub{
      color:var(--muted);
      font-size: clamp(17px, 2vw, 19px);
      margin:0 0 18px;
      max-width: 60ch;
    }
    .heroCard{
      background:var(--card);
      border:1px solid rgba(153,70,14,.30);
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
        url("photos/M.Abrioux-005.jpg");
      background-size:cover;
      background-position:center;
      flex:1;
      min-height:260px;
    }
    .heroMeta{
      padding:16px 18px;
      border-top:1px solid var(--line);
      display:grid;
      grid-template-columns: repeat(3, 1fr);
      gap:10px;
      background: #ffffff;
    }
    .kpi{
      padding:12px 12px;
      border-radius:14px;
      background: var(--cream);
      border:1px solid rgba(153,70,14,.20);
    }
    .kpi b{display:block; font-size:15px}
    .kpi span{display:block; color:var(--muted); font-size:14px}
    /* Retours Natalie (2/5) : sections démarquées par de grands espaces blancs + fine ligne */
    .section{padding: clamp(48px, 7vw, 84px) 0; border-top:1px solid var(--line)}
    .titleRow{
      margin-bottom:28px;
    }
    .titleRow .lead{margin-top:10px}
    h2{margin:0; font-size: clamp(24px, 3vw, 32px); letter-spacing:0; color:var(--navy)}
    .lead{margin:0; color:var(--muted); max-width:75ch; font-size:17px}
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
      background: var(--card);
      border:1px solid var(--line);
      border-radius: var(--radius);
      padding: 16px 16px;
      box-shadow: 0 8px 24px rgba(10,18,55,.07);
      border-top:3px solid var(--brand2);
    }
    .card h3{margin:0 0 8px; font-size:20px; color:var(--navy)}
    .card p{margin:0; color:var(--muted); font-size:16px}
    a.card{display:block; text-decoration:none}
    a.card:hover{transform:translateY(-2px); transition:transform .15s ease}
    .subhead{margin:48px 0 6px; font-size:22px; color:var(--navy)}
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
      background: rgba(241,235,224,.45);
      border:1px solid rgba(153,70,14,.18);
    }
    .ico{width:28px;height:28px;border-radius:10px;display:grid;place-items:center;background:rgba(232,169,63,.22);border:1px solid rgba(153,70,14,.35)}
    .li b{display:block; font-size:16px}
    .li span{display:block; color:var(--muted); font-size:15px}
    .carousel-wrap{
      position: relative;
      max-width: var(--max);
      margin: 28px auto 0;
    }
    .gallery{
      display: flex;
      gap: 12px;
      overflow-x: auto;
      scroll-snap-type: x mandatory;
      scroll-behavior: smooth;
      -webkit-overflow-scrolling: touch;
      padding-bottom: 4px;
    }
    .gallery::-webkit-scrollbar{ height: 5px; }
    .gallery::-webkit-scrollbar-track{ background: rgba(0,0,0,.06); border-radius: 3px; }
    .gallery::-webkit-scrollbar-thumb{ background: var(--accent); border-radius: 3px; }
    .g{
      flex: 0 0 min(600px, 90vw);
      scroll-snap-align: start;
      border-radius: var(--radius);
      overflow: hidden;
      cursor: pointer;
    }
    .g img{
      width: 100%; height: 380px; object-fit: cover; display: block;
      filter: saturate(1.02) contrast(1.02);
    }
    @media (max-width: 600px){ .g img{ height: 220px; } }
    .car-btn{
      position: absolute;
      top: 50%; transform: translateY(-50%);
      z-index: 5;
      background: rgba(10,18,55,.50);
      color: #fff;
      border: none;
      border-radius: 50%;
      width: 52px; height: 52px;
      font-size: 2rem;
      cursor: pointer;
      display: flex; align-items: center; justify-content: center;
      backdrop-filter: blur(4px);
      transition: background .2s;
    }
    .car-btn:hover{ background: rgba(0,0,0,.7); }
    .car-btn.prev{ left: 16px; }
    .car-btn.next{ right: 16px; }
    .car-counter{
      text-align: center;
      margin-top: 10px;
      font-size: 13px;
      color: var(--muted);
    }
    /* Lightbox */
    #lb{
      display:none; position:fixed; inset:0; z-index:100;
      background:rgba(0,0,0,.92); place-items:center;
    }
    #lb.open{ display:grid; }
    #lb img{ max-width:92vw; max-height:92vh; border-radius:12px; }
    #lb-close{
      position:fixed; top:18px; right:22px;
      font-size:32px; color:#fff; cursor:pointer;
      background:none; border:none; line-height:1;
    }
    #lb-prev, #lb-next{
      position:fixed; top:50%; transform:translateY(-50%);
      font-size:28px; color:#fff; cursor:pointer;
      background:rgba(255,255,255,.12); border:none;
      border-radius:50%; width:48px; height:48px;
      display:grid; place-items:center;
    }
    #lb-prev{ left:14px; }
    #lb-next{ right:14px; }
    .cta{
      padding: clamp(48px, 7vw, 84px) 0 64px;
      border-top:1px solid var(--line);
    }
    .ctaBox{
      border-radius: calc(var(--radius) + 6px);
      border:1px solid rgba(153,70,14,.30);
      background: #ffffff;
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
    label{font-size:14px; color:var(--muted)}
    input, textarea{
      width:100%;
      padding: 12px 12px;
      border-radius: 14px;
      border: 1px solid var(--line);
      background: #ffffff;
      color: var(--text);
      outline:none;
      font-family: inherit;
      font-size: 16px;
    }
    input:focus, textarea:focus{ border-color: var(--brand); }
    textarea{min-height:120px; resize:vertical}
    .hint{color:var(--muted); font-size:13px; margin:8px 0 0}
    footer{
      padding: 18px 0 28px;
      color: var(--muted);
      border-top: 1px solid var(--line);
      background: #ffffff;
    }
    .small{font-size:14px; color:var(--muted)}
    .pillRow{display:flex; gap:10px; flex-wrap:wrap; margin-top: 14px}
    .pill{
      font-size:14px;
      padding:8px 10px;
      border-radius:999px;
      border:1px solid rgba(153,70,14,.30);
      background: var(--cream);
      color: var(--text);
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
        <a href="#presentation">Présentation</a>
        <a href="#rdc">RDC</a>
        <a href="#chambres">Chambres d’hôtes</a>
        <a href="#appartement">Appartement</a>
        <a href="#visite">Visite 360°</a>
        <a href="#galerie">Galerie</a>
        <a href="#carte">Carte</a>
      </nav>

      <a class="btn primary" style="white-space:nowrap" href="#contact">📞 Demander infos / visite</a>
    </div>
  </header>

  <!-- HERO -->
  <main id="top" class="hero">
    <div class="wrap grid">
      <section>
        <div class="badge">🏡 Bien immobilier de caractère à vendre – <b>Bedous</b> (<span style="white-space:nowrap">Vallée d’Aspe</span>)</div>
        <h1 class="h1">Un lieu de vie + une activité au cœur des Pyrénées-Atlantiques</h1>
        <p class="sub">
          Situé au <b>centre du village</b> (commodités à pied), cet ensemble immobilier de <b>311 m²</b> offre une opportunité rare :
          <b>habiter sur place</b> tout en générant <b>immédiatement des revenus</b> grâce à une activité de <b>chambres d’hôtes</b> déjà en place.
        </p>

        <div class="pillRow" aria-label="Résumé">
          <span class="pill">📍 Bedous, centre village</span>
          <span class="pill">🏠 311 m²</span>
          <span class="pill">⚡ DPE C · GES B</span>
          <span class="pill">🏡 Habitation + chambres d’hôtes en activité</span>
          <span class="pill">🔄 Potentiel commerce</span>
          <span class="pill">🔑 Projet clé en main</span>
        </div>

        <div style="display:flex; gap:12px; flex-wrap:wrap; margin-top:18px">
          <a class="btn primary" href="#contact">Recevoir photos & bilans</a>
        </div>

      </section>

      <aside class="heroCard" aria-label="Aperçu">
        <div class="heroImg" role="img" aria-label="Photo principale du bien"></div>
      </aside>
    </div>
  </main>

  <!-- PRESENTATION (retours Natalie 2/5 : fil rouge — résumé des trois niveaux + vallée d'Aspe) -->
  <section id="presentation" class="section">
    <div class="wrap">
      <div class="titleRow">
        <h2>🏔️ Présentation</h2>
        <p class="lead">Au cœur de la vallée d’Aspe, dans les Pyrénées, cet ensemble immobilier situé au centre de Bedous se déploie sur trois niveaux — détaillés plus bas dans l’ordre de la visite.</p>
      </div>

      <div class="cards">
        <a class="card" href="#rdc">
          <h3>🍽️ Rez-de-chaussée</h3>
          <p>Salle de petits-déjeuners, cuisine professionnelle avec extraction et espaces polyvalents à fort potentiel commercial.</p>
        </a>
        <a class="card" href="#chambres">
          <h3>🛏️ 1er étage — chambres d’hôtes</h3>
          <p>4 chambres en activité, salles d’eau et WC privatifs, sauna et salon commun.</p>
        </a>
        <a class="card" href="#appartement">
          <h3>🏔️ 2e étage — appartement privatif</h3>
          <p>Un appartement rénové sous les toits, lumineux, avec vues sur les montagnes.</p>
        </a>
      </div>

      <h3 class="subhead" id="points-forts">✨ Les points forts</h3>
      <p class="lead" style="margin:0 0 20px">Un bien rare pour un projet de vie, touristique ou commercial, avec un démarrage immédiat.</p>

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

  <!-- RDC -->
  <section id="rdc" class="section">
    <div class="wrap">
      <div class="titleRow">
        <h2>🍽️ RDC</h2>
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
    <div class="carousel-wrap">
      <button class="car-btn prev" id="rdc-prev" aria-label="Précédente">‹</button>
      <div class="gallery" id="gallery-rdc" aria-label="Photos espaces communs"></div>
      <button class="car-btn next" id="rdc-next" aria-label="Suivante">›</button>
    </div>
    <p class="car-counter" id="rdc-counter">1 / 21</p>
  </section>

  <!-- CHAMBRES D’HOTES -->
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
      </div>
    </div>
    <div class="carousel-wrap">
      <button class="car-btn prev" id="ch-prev" aria-label="Précédente">‹</button>
      <div class="gallery" id="gallery-ch" aria-label="Photos chambres d'hôtes"></div>
      <button class="car-btn next" id="ch-next" aria-label="Suivante">›</button>
    </div>
    <p class="car-counter" id="ch-counter">1 / 27</p>
  </section>

  <!-- APPARTEMENT 2E ETAGE -->
  <section id="appartement" class="section">
    <div class="wrap">
      <div class="titleRow">
        <h2>🏔️ Appartement privatif (2e étage)</h2>
        <p class="lead">Un appartement rénové sous les toits, lumineux, avec vues sur les toits du village et les montagnes — l’espace d’habitation idéal pour exploiter les chambres d’hôtes en habitant sur place.</p>
      </div>

      <div class="list">
        <div class="li"><div class="ico">🛋️</div><div><b>Séjour lumineux</b><span>Grand espace de vie sous rampants avec cuisine ouverte équipée.</span></div></div>
        <div class="li"><div class="ico">🛏️</div><div><b>3 chambres mansardées</b><span>Rénovées, avec puits de lumière.</span></div></div>
        <div class="li"><div class="ico">🚿</div><div><b>Salle d’eau moderne</b><span>Douche, meuble vasque, rénovée récemment.</span></div></div>
        <div class="li"><div class="ico">🧺</div><div><b>Buanderie</b><span>Espace lave-linge indépendant.</span></div></div>
        <div class="li"><div class="ico">🏔️</div><div><b>Vues montagne</b><span>Fenêtres panoramiques sur les toits et les sommets de la vallée.</span></div></div>
        <div class="li"><div class="ico">🔑</div><div><b>Indépendant</b><span>Partie privative séparée de l’activité chambres d’hôtes.</span></div></div>
      </div>
    </div>
    <div class="carousel-wrap">
      <button class="car-btn prev" id="ap-prev" aria-label="Précédente">‹</button>
      <div class="gallery" id="gallery-ap" aria-label="Photos appartement"></div>
      <button class="car-btn next" id="ap-next" aria-label="Suivante">›</button>
    </div>
    <p class="car-counter" id="ap-counter">1 / 29</p>
  </section>

  <!-- VISITE VIRTUELLE -->
  <section id="visite" class="section">
    <div class="wrap">
      <div class="titleRow">
        <h2>🎥 Visite virtuelle 360°</h2>
        <p class="lead">Parcourez le bien comme si vous y étiez — naviguez de pièce en pièce directement ci-dessous.</p>
      </div>
      <div style="position:relative; width:100%; aspect-ratio:16/9; border-radius:var(--radius); overflow:hidden; box-shadow:var(--shadow); border:1px solid var(--line)">
        <iframe src="https://www.meilleurevisite.com/visit/21c939a1-1814-11ea-9031-00155d174307" title="Visite virtuelle du bien" style="position:absolute; inset:0; width:100%; height:100%; border:0" allowfullscreen allow="fullscreen; gyroscope; accelerometer"></iframe>
      </div>
      <p class="small" style="margin-top:10px"><a href="https://www.meilleurevisite.com/visit/21c939a1-1814-11ea-9031-00155d174307" target="_blank" rel="noopener">Ouvrir la visite en plein écran ↗</a></p>
    </div>
  </section>

  <!-- GALERIE -->
  <section id="galerie" class="section">
    <div class="wrap">
      <div class="titleRow">
        <h2>📷 Galerie</h2>
        <p class="lead">133 photos du bien — cliquez pour agrandir.</p>
      </div>
    </div>
    <div class="carousel-wrap">
      <button class="car-btn prev" id="car-prev" aria-label="Précédente">‹</button>
      <div class="gallery" id="gallery" aria-label="Galerie photos"></div>
      <button class="car-btn next" id="car-next" aria-label="Suivante">›</button>
    </div>
    <p class="car-counter" id="car-counter">1 / 133</p>
  </section>

  <!-- LIGHTBOX -->
  <div id="lb" role="dialog" aria-modal="true" aria-label="Photo agrandie">
    <button id="lb-close" aria-label="Fermer">✕</button>
    <button id="lb-prev" aria-label="Précédente">‹</button>
    <img id="lb-img" src="" alt="" />
    <button id="lb-next" aria-label="Suivante">›</button>
  </div>

  <!-- CARTE (retours Natalie 2/5 : fil rouge … → Carte → Contact) -->
  <section id="carte" class="section">
    <div class="wrap">
      <div class="titleRow">
        <h2>🗺️ Où se situe le bien ?</h2>
        <p class="lead">Au centre de Bedous, village principal de la vallée d’Aspe (Pyrénées-Atlantiques), sur l’axe Oloron-Sainte-Marie ↔ Espagne et sur le chemin de Saint-Jacques-de-Compostelle (voie d’Arles).</p>
      </div>
      <div style="position:relative; width:100%; aspect-ratio:16/8; border-radius:var(--radius); overflow:hidden; box-shadow:var(--shadow); border:1px solid var(--line)">
        <iframe src="https://www.openstreetmap.org/export/embed.html?bbox=-0.6555%2C42.9750%2C-0.5500%2C43.0250&layer=mapnik&marker=43.0002%2C-0.6028" title="Carte — Bedous, vallée d’Aspe" style="position:absolute; inset:0; width:100%; height:100%; border:0" loading="lazy"></iframe>
      </div>
      <p class="small" style="margin-top:10px"><a href="https://www.openstreetmap.org/?mlat=43.0002&mlon=-0.6028#map=14/43.0002/-0.6028" target="_blank" rel="noopener">Ouvrir la carte en grand ↗</a></p>
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
            <a class="btn" href="tel:+33681945189">📱 06 81 94 51 89</a>
            <a class="btn" href="mailto:michel.abrioux@gmail.com?subject=Demande%20d%27informations%20-%20Bien%20%C3%A0%20Bedous">✉️ michel.abrioux@gmail.com</a>
          </div>
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
            En cliquant sur “Envoyer”, votre logiciel de messagerie s’ouvre avec votre demande pré-remplie.
          </p>
        </form>
      </div>
    </div>
  </section>

  <footer>
    <div class="wrap" style="display:flex; justify-content:space-between; gap:12px; flex-wrap:wrap; align-items:center">
      <div class="small">© <span id="year"></span> • Bien immobilier – Bedous (Vallée d’Aspe)</div>
      <div class="small">Bedous · Vallée d’Aspe · Pyrénées-Atlantiques</div>
    </div>
  </footer>

  <script>
    // Année automatique
    document.getElementById("year").textContent = new Date().getFullYear();



    // Fonction générique de carrousel
    function buildCarousel(galleryEl, files, folder, counterEl, onClickPhoto) {
      files.forEach((name, idx) => {
        const fig = document.createElement("figure");
        fig.className = "g";
        const img = document.createElement("img");
        img.src = `${folder}/${name}`;
        img.alt = `Photo ${idx+1}`;
        img.loading = "lazy";
        fig.appendChild(img);
        if(onClickPhoto) fig.addEventListener("click", () => onClickPhoto(idx));
        galleryEl.appendChild(fig);
      });
      const slideWidth = () => galleryEl.firstChild ? galleryEl.firstChild.offsetWidth + 12 : 612;
      galleryEl.parentElement.querySelector(".prev").addEventListener("click", () => galleryEl.scrollBy({left: -slideWidth(), behavior:"smooth"}));
      galleryEl.parentElement.querySelector(".next").addEventListener("click", () => galleryEl.scrollBy({left: slideWidth(), behavior:"smooth"}));
      galleryEl.addEventListener("scroll", () => {
        const idx = Math.round(galleryEl.scrollLeft / slideWidth());
        counterEl.textContent = `${idx + 1} / ${files.length}`;
      }, {passive:true});
    }

    // Galerie principale : concaténation dédupliquée de tous les dossiers
    const photos = ["photos/M.Abrioux-001.jpg","photos/M.Abrioux-002.jpg","photos/M.Abrioux-003.jpg","photos/M.Abrioux-004.jpg","photos/M.Abrioux-005.jpg","photos/M.Abrioux-006.jpg","photos/M.Abrioux-007.jpg","photos/M.Abrioux-008.jpg","photos/M.Abrioux-009.jpg","photos/M.Abrioux-012.jpg","photos/M.Abrioux-013.jpg","photos/M.Abrioux-014.jpg","photos/M.Abrioux-015.jpg","photos/M.Abrioux-016.jpg","photos/M.Abrioux-017.jpg","photos/M.Abrioux-018.jpg","photos/M.Abrioux-019.jpg","photos/M.Abrioux-020.jpg","photos/M.Abrioux-021.jpg","photos/M.Abrioux-022.jpg","photos/M.Abrioux-023.jpg","photos/M.Abrioux-024.jpg","photos/M.Abrioux-025.jpg","photos/M.Abrioux-026.jpg","photos/M.Abrioux-027.jpg","photos/M.Abrioux-028.jpg","photos/M.Abrioux-029.jpg","photos/M.Abrioux-030.jpg","photos/M.Abrioux-031.jpg","photos/M.Abrioux-032.jpg","photos/M.Abrioux-033.jpg","photos/M.Abrioux-034.jpg","photos/M.Abrioux-035.jpg","photos/M.Abrioux-036.jpg","photos/M.Abrioux-037.jpg","photos/M.Abrioux-038.jpg","photos/M.Abrioux-039.jpg","photos/M.Abrioux-040.jpg","photos/M.Abrioux-041.jpg","photos/M.Abrioux-042.jpg","photos/M.Abrioux-043.jpg","photos/M.Abrioux-044.jpg","photos/M.Abrioux-047.jpg","photos/M.Abrioux-051.jpg","photos/M.Abrioux-052.jpg","photos/M.Abrioux-053.jpg","photos/M.Abrioux-055.jpg","photos/M.Abrioux-056.jpg","photos/M.Abrioux-057.jpg","photos/M.Abrioux-058.jpg","photos/M.Abrioux-062.jpg","photos/M.Abrioux-063.jpg","photos/M.Abrioux-064.jpg","photos/M.Abrioux-065.jpg","photos/M.Abrioux-068.jpg","photos/M.Abrioux-069.jpg","photos/M.Abrioux-070.jpg","photos/M.Abrioux-073.jpg","photos/M.Abrioux-074.jpg","photos/M.Abrioux-075.jpg","photos/M.Abrioux-076.jpg","photos/DSCN3402(1).JPG","photos/DSCN3402.JPG","photos/DSCN3403.JPG","photos/IMG_0071.JPG","photos/IMG_0420.JPG","photos/IMG_1997.JPG","photos/IMG_1999.JPG","photos/IMG_20150714_192039.jpg","photos/IMG_3078.JPG","photos/IMG_3080.JPG","photos/IMG_3081.JPG","photos/IMG_3084.JPG","photos/IMG_3085.JPG","photos/IMG_3086.JPG","photos/IMG_3277.JPG","photos/IMG_3278.JPG","photos/IMG_3741.JPG","photos/IMG_3743.JPG","photos/salle d eau (1)(1).JPG","photos/salle d eau (1)(2).JPG","photos/salle d eau (1).JPG","photos/salle d eau.JPG","photos-chambres/chambre-2026-01.jpg","photos-chambres/chambre-2026-02.jpg","photos-chambres/chambre-2026-03.jpg","photos-chambres/chambre-2026-04.jpg","photos-chambres/chambre-2026-05.jpg","photos-chambres/chambre-2026-06.jpg","photos-chambres/chambre-2026-07.jpg","photos-chambres/CIMG1380.JPG","photos-chambres/CIMG1392.JPG","photos-chambres/CIMG1395.JPG","photos-chambres/CIMG1396.JPG","photos-chambres/CIMG1397.JPG","photos-chambres/CIMG1401.JPG","photos-chambres/CIMG1402.JPG","photos-chambres/CIMG1403.JPG","photos-chambres/CIMG1404.JPG","photos-chambres/DSCN3400(1).JPG","photos-chambres/DSCN3400.JPG","photos-chambres/IMG_0385.JPG","photos-chambres/IMG_0386.JPG","photos-chambres/IMG_0387.JPG","photos-appartement/M.Abrioux-079.jpg","photos-appartement/M.Abrioux-080.jpg","photos-appartement/M.Abrioux-081.jpg","photos-appartement/M.Abrioux-082.jpg","photos-appartement/M.Abrioux-083.jpg","photos-appartement/M.Abrioux-084.jpg","photos-appartement/M.Abrioux-085.jpg","photos-appartement/M.Abrioux-086.jpg","photos-appartement/M.Abrioux-087.jpg","photos-appartement/M.Abrioux-088.jpg","photos-appartement/M.Abrioux-089.jpg","photos-appartement/M.Abrioux-090.jpg","photos-appartement/M.Abrioux-091.jpg","photos-appartement/M.Abrioux-092.jpg","photos-appartement/M.Abrioux-093.jpg","photos-appartement/M.Abrioux-094.jpg","photos-appartement/M.Abrioux-095.jpg","photos-appartement/M.Abrioux-096.jpg","photos-appartement/M.Abrioux-097.jpg","photos-appartement/M.Abrioux-098.jpg","photos-appartement/M.Abrioux-099.jpg","photos-appartement/M.Abrioux-100.jpg","photos-appartement/M.Abrioux-101.jpg","photos-appartement/M.Abrioux-102.jpg","photos-appartement/M.Abrioux-103.jpg","photos-appartement/M.Abrioux-104.jpg","photos-appartement/M.Abrioux-105.jpg","photos-appartement/M.Abrioux-106.jpg","photos-appartement/appartement-2026-01.jpg"];
    const gallery = document.getElementById("gallery");
    buildCarousel(gallery, photos, ".", document.getElementById("car-counter"), idx => openLb(idx, photos, "."));

    // Carrousel RDC — dossier dédié (couloirs, salle petits-déjeuners, cuisines, lingerie, sauna)
    const photosRdc = ["M.Abrioux-001.jpg","M.Abrioux-006.jpg","M.Abrioux-019.jpg","M.Abrioux-021.jpg","M.Abrioux-022.jpg","M.Abrioux-023.jpg","M.Abrioux-024.jpg","M.Abrioux-025.jpg","M.Abrioux-026.jpg","M.Abrioux-027.jpg","M.Abrioux-028.jpg","M.Abrioux-029.jpg","M.Abrioux-030.jpg","M.Abrioux-031.jpg","M.Abrioux-032.jpg","M.Abrioux-051.jpg","M.Abrioux-052.jpg","M.Abrioux-053.jpg","M.Abrioux-055.jpg","M.Abrioux-073.jpg","M.Abrioux-074.jpg"];
    buildCarousel(
      document.getElementById("gallery-rdc"), photosRdc, "photos-rdc",
      document.getElementById("rdc-counter"),
      idx => openLb(idx, photosRdc, "photos-rdc")
    );

    // Carrousel Chambres d'hôtes — photos actualisées 2026
    const photosChambres = ["M.Abrioux-051.jpg","M.Abrioux-052.jpg","M.Abrioux-053.jpg","M.Abrioux-055.jpg","M.Abrioux-073.jpg","M.Abrioux-074.jpg","chambre-2026-01.jpg","chambre-2026-02.jpg","chambre-2026-03.jpg","chambre-2026-04.jpg","chambre-2026-05.jpg","chambre-2026-06.jpg","chambre-2026-07.jpg","CIMG1380.JPG","CIMG1392.JPG","CIMG1395.JPG","CIMG1396.JPG","CIMG1397.JPG","CIMG1401.JPG","CIMG1402.JPG","CIMG1403.JPG","CIMG1404.JPG","DSCN3400(1).JPG","DSCN3400.JPG","IMG_0385.JPG","IMG_0386.JPG","IMG_0387.JPG"];
    buildCarousel(
      document.getElementById("gallery-ch"), photosChambres, "photos-chambres",
      document.getElementById("ch-counter"),
      idx => openLb(idx, photosChambres, "photos-chambres")
    );

    // Carrousel Appartement (2e étage) — photos pro existantes + nouvelles
    const photosAppartement = ["M.Abrioux-079.jpg","M.Abrioux-080.jpg","M.Abrioux-081.jpg","M.Abrioux-082.jpg","M.Abrioux-083.jpg","M.Abrioux-084.jpg","M.Abrioux-085.jpg","M.Abrioux-086.jpg","M.Abrioux-087.jpg","M.Abrioux-088.jpg","M.Abrioux-089.jpg","M.Abrioux-090.jpg","M.Abrioux-091.jpg","M.Abrioux-092.jpg","M.Abrioux-093.jpg","M.Abrioux-094.jpg","M.Abrioux-095.jpg","M.Abrioux-096.jpg","M.Abrioux-097.jpg","M.Abrioux-098.jpg","M.Abrioux-099.jpg","M.Abrioux-100.jpg","M.Abrioux-101.jpg","M.Abrioux-102.jpg","M.Abrioux-103.jpg","M.Abrioux-104.jpg","M.Abrioux-105.jpg","M.Abrioux-106.jpg","appartement-2026-01.jpg"];
    buildCarousel(
      document.getElementById("gallery-ap"), photosAppartement, "photos-appartement",
      document.getElementById("ap-counter"),
      idx => openLb(idx, photosAppartement, "photos-appartement")
    );

    // Lightbox
    const lb = document.getElementById("lb");
    const lbImg = document.getElementById("lb-img");
    let current = 0, lbFiles = photos, lbFolder = "photos";
    function openLb(idx, files, folder) {
      if(files) { lbFiles = files; lbFolder = folder; }
      current = idx;
      lbImg.src = `${lbFolder}/${lbFiles[idx]}`;
      lbImg.alt = `Photo ${idx+1}`;
      lb.classList.add("open");
      document.body.style.overflow = "hidden";
    }
    function closeLb() {
      lb.classList.remove("open");
      document.body.style.overflow = "";
    }
    document.getElementById("lb-close").addEventListener("click", closeLb);
    document.getElementById("lb-prev").addEventListener("click", () => openLb((current - 1 + lbFiles.length) % lbFiles.length));
    document.getElementById("lb-next").addEventListener("click", () => openLb((current + 1) % lbFiles.length));
    lb.addEventListener("click", e => { if(e.target === lb) closeLb(); });
    document.addEventListener("keydown", e => {
      if(!lb.classList.contains("open")) return;
      if(e.key === "Escape") closeLb();
      if(e.key === "ArrowLeft") openLb((current - 1 + lbFiles.length) % lbFiles.length);
      if(e.key === "ArrowRight") openLb((current + 1) % lbFiles.length);
    });

    // Envoi via mailto (simple et compatible GitHub Pages)
    const form = document.getElementById("leadForm");
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const name = document.getElementById("name").value.trim();
      const email = document.getElementById("email").value.trim();
      const phone = document.getElementById("phone").value.trim();
      const msg = document.getElementById("msg").value.trim();

      const to = "michel.abrioux@gmail.com";
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

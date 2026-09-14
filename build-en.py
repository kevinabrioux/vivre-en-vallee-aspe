#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère en/index.html (version anglaise) à partir de README.md (version FR).

Traduction : Natalie Worden, 27/07/2026 (anglais britannique).
Chaque remplacement est vérifié : si une chaîne source est absente ou n'apparaît
pas le nombre de fois attendu, le script s'arrête plutôt que de produire une page
à moitié traduite.
"""
import io, os, sys

SITE = "/Users/kevinabrioux/Library/CloudStorage/GoogleDrive-kevin.abrioux@gmail.com/My Drive/Vente Gambetta/vivre-en-vallee-aspe"
BASE = "https://kevinabrioux.github.io/vivre-en-vallee-aspe"

src = io.open(os.path.join(SITE, "README.md"), encoding="utf-8").read()
html = src
errors = []

def rep(old, new, n=1):
    """Remplace `old` par `new`, en exigeant exactement n occurrences."""
    global html
    c = html.count(old)
    if c != n:
        errors.append("attendu %d occurrence(s), trouve %d : %r" % (n, c, old[:90]))
        return
    html = html.replace(old, new)

# ---------------------------------------------------------------- <head>
rep('<html lang="fr">', '<html lang="en">')

rep('<title>Chambres d’hôtes à vendre – Bedous, vallée d’Aspe (Pyrénées) | 266 m², activité clé en main</title>',
    '<title>Bed &amp; Breakfast for Sale – Bedous, Vallée d’Aspe, French Pyrenees | 266 m² turnkey business</title>')

rep('<meta name="description" content="À vendre à Bedous, village étape du chemin de Saint-Jacques-de-Compostelle : ensemble immobilier de 266 m² avec chambres d’hôtes en activité, appartement privatif et potentiel commercial. Nature, randonnée et tranquillité au cœur de la vallée d’Aspe (Pyrénées)." />',
    '<meta name="description" content="For sale in Bedous, a village on the Camino de Santiago in the French Pyrenees: a 266 m² property with an established Bed &amp; Breakfast, a private apartment and strong commercial potential. Nature, hiking and tranquillity in the heart of the Vallée d’Aspe." />')

rep('<meta property="og:title" content="Chambres d’hôtes à vendre – Bedous, vallée d’Aspe (Pyrénées)" />',
    '<meta property="og:title" content="Bed &amp; Breakfast for Sale – Bedous, Vallée d’Aspe, French Pyrenees" />')

rep('<meta property="og:description" content="266 m², chambres d’hôtes en activité sur le chemin de Saint-Jacques-de-Compostelle, appartement privatif, fort potentiel commercial — au cœur de la vallée d’Aspe." />',
    '<meta property="og:description" content="266 m², an established Bed &amp; Breakfast on the Camino de Santiago, a private apartment and strong commercial potential — in the heart of the Vallée d’Aspe, France." />')

rep('<meta property="og:locale" content="fr_FR" />', '<meta property="og:locale" content="en_GB" />')
rep('<meta property="og:url" content="%s/" />' % BASE, '<meta property="og:url" content="%s/en/" />' % BASE)
rep('<link rel="canonical" href="%s/" />' % BASE, '<link rel="canonical" href="%s/en/" />' % BASE)
# les trois <link rel="alternate" hreflang=...> sont identiques dans les deux versions : inchanges

# JSON-LD
rep('"name":"Chambres d’hôtes à vendre – Bedous, vallée d’Aspe (Pyrénées)"',
    '"name":"Bed & Breakfast for Sale – Bedous, Vallée d’Aspe, French Pyrenees"')
rep('"description":"Ensemble immobilier de 266 m² au centre de Bedous, village étape du chemin de Saint-Jacques-de-Compostelle. DPE classe C, GES classe B. Chambres d’hôtes en activité, appartement privatif et potentiel commercial, au cœur de la vallée d’Aspe : nature, randonnée, tranquillité."',
    '"description":"A 266 m² property in the centre of Bedous, a village on the Camino de Santiago in the French Pyrenees. EPC rating C, GHG rating B. An established Bed & Breakfast, a private apartment and commercial potential, in the heart of the Vallée d’Aspe: nature, hiking and tranquillity."')
rep('"url":"%s/"' % BASE, '"url":"%s/en/"' % BASE)
rep('"inLanguage"', '"inLanguage"', 0) if False else None

# ---------------------------------------------------------------- CSS
# Les libelles de nav anglais sont plus longs : on masque la nav plus tot
rep('    @media (max-width: 1080px){\n      .navlinks{display:none}',
    '    @media (max-width: 1150px){\n      .navlinks{display:none}')
rep('url("photos/panorama-vallee-aspe.jpg");', 'url("../photos/panorama-vallee-aspe.jpg");')

# ---------------------------------------------------------------- NAV
rep('<a class="logo" href="#top" aria-label="Retour en haut de page">',
    '<a class="logo" href="#top" aria-label="Back to top">')
# logo : on garde le nom court (le « France » est porte par le title, le hero et la section Location)
rep('<span>Bedous • Vallée d’Aspe</span>', '<span>Bedous • Vallée d’Aspe</span>')
rep('<nav class="navlinks" aria-label="Navigation principale">',
    '<nav class="navlinks" aria-label="Main navigation">')
rep('<a href="#presentation">Présentation</a>', '<a href="#presentation">Overview</a>')
rep('<a href="#rdc">RDC</a>', '<a href="#rdc">Ground Floor</a>')
rep('<a href="#chambres">Chambres</a>', '<a href="#chambres">B&amp;B</a>')
rep('<a href="#appartement">Appartement</a>', '<a href="#appartement">Apartment</a>')
rep('<a href="#visite">Visite 360°</a>', '<a href="#visite">360° Tour</a>')
rep('<a href="#galerie">Galerie</a>', '<a href="#galerie">Gallery</a>')
rep('<a href="#avis">Avis</a>', '<a href="#avis">Reviews</a>')
rep('<a href="#carte">Carte</a>', '<a href="#carte">Location</a>')
rep('<a class="langSwitch" href="en/" hreflang="en" lang="en" title="See the English version">EN</a>',
    '<a class="langSwitch" href="../" hreflang="fr" lang="fr" title="Voir la version française">FR</a>')
rep('<a class="btn primary" style="white-space:nowrap" href="#contact">📞 Demander infos / visite</a>',
    '<a class="btn primary" style="white-space:nowrap" href="#contact">📞 Request Information</a>')

# ---------------------------------------------------------------- HERO
rep('<div class="badge">🏡 Bien immobilier de caractère à vendre – Bedous (<span style="white-space:nowrap">Vallée d’Aspe</span>)</div>',
    '<div class="badge">🏡 Charming Property for Sale – Bedous (<span style="white-space:nowrap">Vallée d’Aspe, France</span>)</div>')
rep('<h1 class="h1">Un lieu où vivre et entreprendre au cœur des Pyrénées-Atlantiques</h1>',
    '<h1 class="h1">A place to live, welcome guests and embrace a unique opportunity in the heart of the Pyrénées-Atlantiques</h1>')
rep("""          Au cœur de Bedous, village étape sur le chemin de Saint-Jacques-de-Compostelle, cette propriété de 266 m²
          offre une opportunité rare de conjuguer art de vivre et activité touristique. Une propriété où habiter,
          accueillir et entreprendre grâce à une activité de chambres d’hôtes déjà établie, dans la magnifique
          vallée d’Aspe recherchée par les voyageurs en quête d’authenticité, de randonnée et de nature.""",
    """          Nestled in the heart of Bedous, a quaint village along the Camino de Santiago (Saint James’ Way), this
          266 m² property offers a rare opportunity to combine an exceptional quality of life with an established
          hospitality business. A place to call home while welcoming guests from around the world, set in the stunning
          Vallée d’Aspe — a valley that attracts visitors seeking authenticity, outdoor adventures, peaceful
          surroundings and the beauty of the Pyrenean landscape.""")

rep('<div class="pillRow" aria-label="Résumé">', '<div class="pillRow" aria-label="Summary">')
rep('<span class="pill">📍 Bedous, centre village</span>', '<span class="pill">📍 Bedous village centre</span>')
rep('<span class="pill">🏠 266 m² Carrez</span>', '<span class="pill">🏠 266 m² (Carrez)</span>')
rep('<span class="pill">⚡ DPE C · GES B</span>', '<span class="pill">⚡ EPC Rating C · GHG Rating B</span>')
rep('<span class="pill">🏡 Habitation + chambres d’hôtes en activité</span>',
    '<span class="pill">🏡 Private residence + established B&amp;B</span>')
rep('<span class="pill">🔄 Potentiel commerce</span>', '<span class="pill">🔄 Commercial potential</span>')
rep('<span class="pill">🔑 Projet clé en main</span>', '<span class="pill">🔑 Turnkey opportunity</span>')
rep('<a class="btn primary" href="#contact">Recevoir photos & bilans</a>',
    '<a class="btn primary" href="#contact">Receive photos &amp; business information</a>')
rep('<aside class="heroCard" aria-label="Aperçu">', '<aside class="heroCard" aria-label="Preview">')
rep('aria-label="Vue panoramique sur la vallée d’Aspe et le village de Bedous, au cœur des Pyrénées"',
    'aria-label="Panoramic view over the Vallée d’Aspe and the village of Bedous, in the heart of the Pyrenees"')

# ---------------------------------------------------------------- SE PROJETER (visuels IA)
rep('<h2>💡 Et demain ? Imaginez…</h2>', '<h2>💡 And tomorrow? Imagine…</h2>')
rep("<p class=\"lead\">L'immeuble est déclaré à usage d'habitation et de commerce : le rez-de-chaussée, ancien bar-restaurant avec magasin, peut redevenir un lieu ouvert sur le village. Trois exemples parmi bien d'autres, imaginés à partir des volumes existants.</p>",
    '<p class="lead">The building is registered for both residential and commercial use: the ground floor, a former bar-restaurant with a shop, could once again open onto village life. Here are three ideas among many, imagined from the existing spaces.</p>')
rep('alt="Projection par intelligence artificielle : la salle du rez-de-chaussée aménagée en restaurant chaleureux"',
    'alt="AI-generated visualisation: the ground-floor room laid out as a welcoming restaurant"')
rep("<b>🍽️ Un restaurant ou une table d'hôtes</b>", '<b>🍽️ A restaurant or table d\'hôtes</b>')
rep("<span>La salle du rez-de-chaussée et sa cuisine professionnelle se prêtent à une table ouverte aux hôtes comme aux gens de passage — sur le chemin de Saint-Jacques, la clientèle est là.</span>",
    '<span>The ground-floor dining room and its professional kitchen lend themselves to a table welcoming both guests and passers-by — on the Camino de Santiago, the customers are already there.</span>')
rep('alt="Projection par intelligence artificielle : l\'espace magasin aménagé en boutique d\'équipement de montagne et de randonnée"',
    'alt="AI-generated visualisation: the former shop laid out as a mountain and hiking equipment store"')
rep('<b>🥾 Une boutique d\'équipement montagne & randonnée</b>', '<b>🥾 A mountain &amp; hiking equipment store</b>')
rep("<span>Entre le Parc national des Pyrénées, le GR 10 et le chemin de Saint-Jacques, Bedous voit passer randonneurs et pèlerins toute la saison — le magasin d'origine retrouverait sa vocation.</span>",
    '<span>Between the Pyrenees National Park, the GR 10 trail and the Camino de Santiago, Bedous sees hikers and pilgrims pass through all season long — the original shop could return to its calling.</span>')
rep('alt="Projection par intelligence artificielle : l\'espace magasin aménagé en atelier-boutique de vélos"',
    'alt="AI-generated visualisation: the former shop laid out as a bicycle workshop and store"')
rep('<b>🚲 Un atelier-boutique de cycles</b>', '<b>🚲 A bicycle workshop &amp; store</b>')
rep("<span>Réparation, location, vente : entre le col du Somport et les grands cols du Tour, la vallée d'Aspe voit défiler cyclotouristes et vététistes — un service qui manque aujourd'hui dans le bourg.</span>",
    '<span>Repairs, hire and sales: between the Col du Somport and the great climbs of the Tour, the Vallée d\'Aspe sees a steady stream of cycle tourists and mountain bikers — a service the village currently lacks.</span>')
rep("<p class=\"projNote\">Visuels générés par intelligence artificielle à partir des espaces existants — simples suggestions d'aménagement, non contractuelles. L'état réel des lieux est visible dans les photos et la visite virtuelle 360°.</p>",
    '<p class="projNote">These visuals were generated by artificial intelligence from the existing spaces — they are suggestions only and are not contractually binding. The actual condition of the property can be seen in the photographs and the 360° virtual tour.</p>')
rep('src="photos/projection-restaurant.jpg"', 'src="../photos/projection-restaurant.jpg"')
rep('src="photos/projection-montagne.jpg"', 'src="../photos/projection-montagne.jpg"')
rep('src="photos/projection-cycles.jpg"', 'src="../photos/projection-cycles.jpg"')

# ---------------------------------------------------------------- PRESENTATION
rep('<p class="lead" style="font-size:15px; margin-top:10px">266 m² au sens de la loi Carrez ; la surface de référence du diagnostic de performance énergétique, qui inclut les combles aménagés sous rampants, est de 311 m².</p>',
    '<p class="lead" style="font-size:15px; margin-top:10px">266 m² under the French Carrez law, which excludes floor area under 1.80 m in height; the reference area used for the energy performance certificate, which includes the converted attic rooms, is 311 m².</p>')
rep('<h2>🏔️ Présentation</h2>', '<h2>🏔️ Overview</h2>')
rep('<p class="lead">Au cœur de la vallée d’Aspe, dans les Pyrénées, cet ensemble immobilier situé au centre de Bedous se déploie sur trois niveaux — détaillés plus bas dans l’ordre de la visite.</p>',
    '<p class="lead">Set in the heart of the Vallée d’Aspe, in the beautiful French Pyrenees, this charming property enjoys a prime location in the centre of Bedous and unfolds over three floors, each offering its own unique spaces and character, presented below in the order of the visit.</p>')
rep('<h3>🍽️ Rez-de-chaussée</h3>', '<h3>🍽️ Ground Floor</h3>')
rep('<p>Salle de petits-déjeuners, cuisine professionnelle avec extraction et espaces polyvalents à fort potentiel commercial.</p>',
    '<p>A welcoming breakfast room, a fully equipped professional kitchen with extraction system, and versatile spaces offering excellent potential for a variety of commercial ventures.</p>')
rep('<h3>🛏️ 1er étage — chambres d’hôtes</h3>', '<h3>🛏️ First Floor — Bed &amp; Breakfast</h3>')
rep('<p>4 chambres en activité, salles d’eau et WC privatifs, sauna et salon commun.</p>',
    '<p>Four established guest bedrooms, each with private shower rooms and WCs, together with a sauna and a cosy shared lounge.</p>')
rep('<h3>🏔️ 2e étage — appartement privatif</h3>', '<h3>🏔️ Second Floor — Private Apartment</h3>')
rep('<p>Un appartement rénové sous les toits, lumineux, avec vues sur les montagnes.</p>',
    '<p>A beautifully renovated top-floor apartment filled with natural light and offering wonderful views over the surrounding mountains.</p>')

rep('<h3 class="subhead" id="points-forts">✨ Les points forts</h3>', '<h3 class="subhead" id="points-forts">✨ Highlights</h3>')
rep('<p class="lead" style="margin:0 0 20px">Un bien rare pour un projet de vie, touristique ou commercial, avec un démarrage immédiat.</p>',
    '<p class="lead" style="margin:0 0 20px">A rare and versatile property offering a harmonious blend of hospitality, living and future possibilities — inviting its next owners to imagine and create their own vision in the heart of the Vallée d’Aspe.</p>')

rep('<h3>📍 Un emplacement privilégié</h3>', '<h3>📍 An ideal location</h3>')
rep('<p>Au cœur de Bedous, profitez de tous les commerces et services accessibles à pied.</p>',
    '<p>Located in the centre of Bedous, with shops, cafés and everyday services all within easy walking distance.</p>')
rep('<h3>🏔️ Une destination prisée</h3>', '<h3>🏔️ A sought-after destination</h3>')
rep('<p>Au cœur de la vallée d’Aspe, dans les Pyrénées, un emplacement bénéficiant d’une forte attractivité touristique en toute saison.</p>',
    '<p>Nestled in the Vallée d’Aspe, this exceptional setting enjoys year-round appeal, attracting visitors drawn to nature, hiking and authentic mountain experiences.</p>')
rep('<h3>💼 Une activité clé en main</h3>', '<h3>💼 An established Bed &amp; Breakfast business</h3>')
rep('<p>Chambres d’hôtes en activité, avec une exploitation opérationnelle dès la reprise.</p>',
    '<p>A fully operational hospitality business offering a smooth transition for new owners.</p>')
rep('<h3>🔄 Un fort potentiel d’évolution</h3>', '<h3>🔄 Strong potential for future development</h3>')
rep('<p>La propriété se prête à de nombreux projets : restaurant, café, concept store, espace bien-être, atelier, etc.</p>',
    '<p>The property offers many possibilities, including a restaurant, café, concept store, wellness space, creative studio or other inspiring ventures.</p>')
rep('<h3>🔑 Un projet prêt à vivre</h3>', '<h3>🔑 A seamless transition</h3>')
rep('<p>Une activité déjà installée, avec ses équipements professionnels, offrant une transition simple et sereine pour les futurs propriétaires.</p>',
    '<p>With an established business and professional equipment already in place, future owners can step into a fully operational opportunity with confidence.</p>')
rep('<h3>🏠 Une vie privée préservée</h3>', '<h3>🏠 A private space to call your own</h3>')
rep('<p>Un espace dédié à l’habitation permet de concilier confort personnel et activité professionnelle.</p>',
    '<p>A dedicated living area allows you to enjoy personal comfort while creating the perfect balance between private life and welcoming guests.</p>')

# ---------------------------------------------------------------- RDC
rep('<h2>🍽️ RDC</h2>', '<h2>🍽️ Ground Floor</h2>')
rep('<p class="lead">Un lieu prêt à accueillir votre projet.</p>',
    '<p class="lead">A space ready to bring your vision to life.</p>')
rep('<h3>☕ Salle de petits-déjeuners</h3>', '<h3>☕ Breakfast Room</h3>')
rep('<p>Un espace aménagé pour accueillir les clients dans les meilleures conditions.</p>',
    '<p>A thoughtfully designed space created to welcome guests in a warm and comfortable setting.</p>')
rep('<h3>👩‍🍳 Cuisine professionnelle équipée</h3>', '<h3>👩‍🍳 Fully Equipped Professional Kitchen</h3>')
rep('<p>Dotée d’un système d’extraction et vendue avec ses équipements professionnels, elle offre une base idéale pour développer une activité de restauration.</p>',
    '<p>Featuring a commercial extraction system and sold with its professional equipment, the kitchen provides an excellent foundation for developing a restaurant or food-based venture.</p>')
rep('<h3>🧩 Un lieu aux multiples possibilités</h3>', '<h3>🧩 A space full of possibilities</h3>')
rep('<p>Idéal pour un café, un restaurant, un concept store, un espace bien-être, un atelier créatif…</p>',
    '<p>A versatile area offering exciting potential, ideal for creating a café, restaurant, concept store, wellness space, creative workshop or another inspiring project.</p>')
rep('aria-label="Rez-de-chaussée : salle de petits-déjeuners et cuisine professionnelle à Bedous"',
    'aria-label="Ground floor: breakfast room and professional kitchen in Bedous"')

# ---------------------------------------------------------------- CHAMBRES
rep('<h2>🛏️ Un espace chambres d’hôtes au 1er étage</h2>',
    '<h2>🛏️ Bed &amp; Breakfast Accommodation on the First Floor</h2>')
rep('<p class="lead">Un espace chaleureux, pensé pour le confort des hôtes et le bon fonctionnement de l’activité.</p>',
    '<p class="lead">A warm and inviting area designed with guests’ comfort in mind while supporting the smooth running of the business.</p>')
rep('<b>4 chambres pleines de charme</b><span>Un cadre chaleureux pour accueillir les voyageurs venus découvrir la vallée d’Aspe et ses paysages préservés.</span>',
    '<b>Four Charming Guest Bedrooms</b><span>Characterful and peaceful rooms offering a relaxing retreat for travellers discovering the beauty, authenticity and unspoilt landscapes of the Vallée d’Aspe.</span>')
rep('<b>Salles d’eau privatives</b><span>Un confort apprécié des voyageurs, offrant intimité et autonomie à chaque chambre.</span>',
    '<b>Private Shower Rooms</b><span>A highly valued feature for guests, providing each bedroom with privacy, comfort and independence.</span>')
rep('<b>Des sanitaires privatifs</b><span>Un confort apprécié des voyageurs et un véritable atout pour l’activité d’accueil.</span>',
    '<b>Private WCs</b><span>A valued comfort for guests and an important asset for a successful hospitality business.</span>')
rep('<b>Un confort en toute saison</b><span>Des équipements adaptés pour accueillir les voyageurs été comme hiver.</span>',
    '<b>Comfort in Every Season</b><span>Thoughtfully equipped to welcome guests throughout the year, from sunny summer stays to peaceful winter escapes.</span>')
rep('<b>Un espace bien-être avec sauna</b><span>Un véritable atout pour offrir aux voyageurs un moment de détente après une journée de randonnée ou de découverte de la vallée.</span>',
    '<b>A Wellness Area with Sauna</b><span>A wonderful feature allowing guests to relax and unwind after a day exploring the mountains, hiking the trails or discovering the beauty of the valley.</span>')
rep('<b>Un espace lingerie dédié</b><span>Un espace fonctionnel facilitant la gestion quotidienne de l’activité de chambres d’hôtes.</span>',
    '<b>A Dedicated Laundry Room</b><span>A practical and functional space designed to make the day-to-day management of the Bed &amp; Breakfast simple and efficient.</span>')
rep('<b>Un salon commun chaleureux</b><span>Un espace convivial où les voyageurs peuvent se retrouver et se détendre, avec machine à café, réfrigérateur et télévision.</span>',
    '<b>A Cosy Shared Lounge</b><span>A welcoming communal area where guests can relax, connect and enjoy their stay, complete with a coffee machine, refrigerator and television.</span>')
rep('aria-label="Chambres d\'hôtes en vallée d\'Aspe : chambres, terrasse, sauna et salles d\'eau"',
    'aria-label="Bed &amp; Breakfast in the Vallée d’Aspe: bedrooms, terrace, sauna and shower rooms"')

# ---------------------------------------------------------------- APPARTEMENT
rep('<h2>🏔️ Un appartement avec vue sur la vallée (2e étage)</h2>',
    '<h2>🏔️ A Private Apartment with Valley Views (Second Floor)</h2>')
rep('<p class="lead">Sous les toits du village, cet appartement rénové offre lumière, charme et vues dégagées sur les montagnes, pour vivre pleinement son projet d’accueil.</p>',
    '<p class="lead">Tucked beneath the village rooftops, this beautifully renovated apartment combines natural light, charm and breathtaking mountain views, offering a peaceful private retreat alongside the Bed &amp; Breakfast.</p>')
rep('<b>Un espace de vie lumineux et chaleureux</b><span>Un grand séjour sous rampants avec cuisine ouverte équipée, pensé pour un quotidien confortable.</span>',
    '<b>A Bright and Welcoming Living Space</b><span>A spacious open-plan living area featuring a fully equipped kitchen and designed for comfortable everyday living.</span>')
rep('<b>3 chambres pleines de charme</b><span>Des chambres mansardées rénovées, baignées de lumière naturelle grâce aux puits de lumière.</span>',
    '<b>Three Charming Bedrooms</b><span>Beautifully renovated bedrooms filled with natural light thanks to the roof windows, creating cosy and inviting spaces to relax and unwind.</span>')
rep('<b>Une salle d’eau moderne</b><span>Un espace récemment rénové avec douche et meuble vasque, alliant confort et fonctionnalité au quotidien.</span>',
    '<b>A Modern Shower Room</b><span>A recently renovated space featuring a walk-in shower and vanity unit, combining everyday comfort with practicality.</span>')
rep('<b>Un espace buanderie pratique</b><span>Un espace indépendant avec lave-linge, pensé pour faciliter l’organisation quotidienne.</span>',
    '<b>A Practical Utility Area</b><span>A functional space with a washing machine, designed to make daily organisation simple and effortless.</span>')
rep('<b>Des vues exceptionnelles sur la vallée</b><span>De grandes ouvertures offrent un panorama sur les toits du village et les sommets environnants.</span>',
    '<b>Exceptional Views Over the Valley</b><span>Large windows frame beautiful panoramic views across the village rooftops and the surrounding mountain peaks.</span>')
rep('<b>Un équilibre entre vie privée et activité</b><span>Une partie habitation indépendante permettant de vivre sur place tout en accueillant les voyageurs en toute sérénité.</span>',
    '<b>The Perfect Balance Between Private Life and Hospitality</b><span>A separate living area allows you to enjoy the comfort of your own home while welcoming guests in complete peace and tranquillity.</span>')
rep('aria-label="Appartement sous les toits avec vue montagne à Bedous"',
    'aria-label="Top-floor apartment with mountain views in Bedous"')

# ---------------------------------------------------------------- VISITE 360
rep('<h2>🎥 Visite virtuelle 360°</h2>', '<h2>🎥 360° Virtual Tour</h2>')
rep('<p class="lead">Entrez, explorez, découvrez : visitez la propriété comme si vous étiez sur place grâce à la visite virtuelle ci-dessous.</p>',
    '<p class="lead">Step inside, explore and discover the property from wherever you are. Experience the home as though you were already here through the virtual tour below.</p>')
rep('title="Visite virtuelle du bien"', 'title="Virtual tour of the property"')
rep('>Ouvrir la visite en plein écran ↗</a>', '>Open the tour in full screen ↗</a>')

# ---------------------------------------------------------------- GALERIE
rep('<h2>📷 Galerie</h2>', '<h2>📷 Gallery</h2>')
rep('<p class="lead">135 photos pour découvrir chaque détail du bien — explorez la galerie complète.</p>',
    '<p class="lead">Discover every detail of this charming property through 135 photographs. Explore the full gallery and picture yourself in each space.</p>')
rep('aria-label="Galerie du bien à vendre à Bedous, vallée d\'Aspe"',
    'aria-label="Gallery of the property for sale in Bedous, Vallée d’Aspe"')

# ---------------------------------------------------------------- LIGHTBOX / boutons
rep('aria-label="Photo agrandie"', 'aria-label="Enlarged photo"')
rep('<button id="lb-close" aria-label="Fermer">✕</button>', '<button id="lb-close" aria-label="Close">✕</button>')
rep('aria-label="Précédente"', 'aria-label="Previous"', n=5)
rep('aria-label="Suivante"', 'aria-label="Next"', n=5)

# ---------------------------------------------------------------- AVIS
rep('<h2>💬 Ils ont séjourné ici</h2>', '<h2>💬 Guests Who Have Stayed Here</h2>')
rep('<p class="lead">La réputation des chambres d’hôtes est déjà faite : une clientèle fidèle et d’excellentes notes sur les plateformes de réservation — la garantie de reprendre une activité clé en main. L’activité génère un chiffre d’affaires d’environ 30 000 € par an, avec une clientèle présente d’avril à octobre.</p>',
    '<p class="lead">The Bed &amp; Breakfast already enjoys an excellent reputation, with loyal returning guests and outstanding reviews across booking platforms — a reassuring foundation for future owners taking over a fully operational business. The business generates a turnover of around €30,000 a year, with guests staying from April to October.</p>')
rep('aria-label="Notes des plateformes"', 'aria-label="Platform ratings"')
rep('<span class="pill">⭐ <b>4,8 / 5</b>&nbsp;« Excellent » sur Google (119 avis)</span>',
    '<span class="pill">⭐ <b>4.8 / 5</b>&nbsp;“Excellent” on Google (119 reviews)</span>')
rep('<span class="pill">⭐ <b>4,8 / 5</b>&nbsp;sur TripAdvisor</span>',
    '<span class="pill">⭐ <b>4.8 / 5</b>&nbsp;on TripAdvisor</span>')
rep('<span class="pill">⭐ <b>9,1 / 10</b>&nbsp;« Superbe » sur Booking.com (165 avis)</span>',
    '<span class="pill">⭐ <b>9.1 / 10</b>&nbsp;“Superb” on Booking.com (165 reviews)</span>')
rep('<p style="font-style:italic">« Si vous avez l’occasion, foncez, vous y serez reçus comme des princes ! »</p>',
    '<p style="font-style:italic">“If you get the chance, go for it — you will be welcomed like royalty!”</p>')
rep('Raphaelle, de passage sur sa traversée des Pyrénées à vélo — Google, août 2026',
    'Raphaelle, passing through on her cycle crossing of the Pyrenees — Google, August 2026')
rep('<p style="font-style:italic">« Annie et Michel sont aux petits soins et la chambre est impeccable. »</p>',
    '<p style="font-style:italic">“Annie and Michel look after your every need and the room is immaculate.”</p>')
rep('Kim — Google, août 2026', 'Kim — Google, August 2026')
rep('<p style="font-style:italic">« Une excellente adresse où l’on a plaisir à revenir. »</p>',
    '<p style="font-style:italic">“A wonderful place that you will always be happy to return to.”</p>')

# ---------------------------------------------------------------- CARTE
rep('<h2>🗺️ Où se situe le bien ?</h2>', '<h2>🗺️ Where is the property located?</h2>')
rep('<p class="lead">Au centre de Bedous, village principal de la vallée d’Aspe (Pyrénées-Atlantiques), sur l’axe Oloron-Sainte-Marie ↔ Espagne et sur le chemin de Saint-Jacques-de-Compostelle (voie d’Arles) — une étape appréciée des pèlerins, des randonneurs et des amoureux de la nature.</p>',
    '<p class="lead">Located in the heart of Bedous, the main village of the Vallée d’Aspe (Pyrénées-Atlantiques), the property enjoys a privileged position between Oloron-Sainte-Marie and Spain, and along the Camino de Santiago (Arles Route). A popular stopping point for pilgrims, hikers and nature lovers, Bedous offers an authentic mountain setting surrounded by breathtaking landscapes, outdoor adventures and the peaceful beauty of the Pyrenees.</p>')
rep('title="Carte — Bedous, vallée d’Aspe"', 'title="Map — Bedous, Vallée d’Aspe"')
rep('>Ouvrir la carte en grand ↗</a>', '>Open full-size map ↗</a>')

# ---------------------------------------------------------------- CONTACT
rep('<h2>📞 Envie d’en savoir plus ?</h2>', '<h2>📞 Would you like to find out more?</h2>')
rep('<p class="lead">Recevez le dossier complet du bien (photos, informations, éléments d’activité) et échangez avec nous pour organiser une visite — via le formulaire ci-dessous ou directement par téléphone.</p>',
    '<p class="lead">Receive the complete property information pack — photographs, business details and key information — and get in touch with us to arrange a viewing, either through the form below or directly by telephone.</p>')
rep('<h3 style="margin:0 0 8px">✅ Un dossier complet à votre disposition</h3>',
    '<h3 style="margin:0 0 8px">✅ A complete information pack is available</h3>')
rep('<b>Un dossier photos complet</b><span>Découvrez les espaces intérieurs, extérieurs et les plans de la propriété.</span>',
    '<b>A full photo portfolio</b><span>Explore the interior and exterior spaces, as well as the property plans, and discover every detail of this home and business opportunity.</span>')
rep('<b>Les éléments clés de l’activité</b><span>Chiffres, bilans et informations essentielles pour vous accompagner dans votre projet.</span>',
    '<b>Key business information</b><span>Essential figures, business details and information to help you confidently plan your next steps.</span>')
rep('<b>Venez découvrir la propriété</b><span>Nous vous proposons un rendez-vous selon vos disponibilités.</span>',
    '<b>Come and discover the property</b><span>We would be delighted to arrange a viewing at a time that suits your schedule.</span>')
rep('<b>Parlons de votre projet</b><span>Nous répondons à vos questions pour vous aider à vous projeter dans cette propriété.</span>',
    '<b>Let’s talk about your project</b><span>We are here to answer your questions and help you imagine the possibilities this unique property has to offer.</span>')
rep('<a class="btn" href="tel:+33681945189">📱 06 81 94 51 89</a>',
    '<a class="btn" href="tel:+33681945189">📱 +33 6 81 94 51 89</a>')
rep('href="mailto:michel.abrioux@gmail.com?subject=Demande%20d%27informations%20-%20Bien%20%C3%A0%20Bedous"',
    'href="mailto:michel.abrioux@gmail.com?subject=Property%20enquiry%20-%20Bedous%2C%20Vall%C3%A9e%20d%27Aspe"')

# Formulaire
rep('<label for="name">Nom</label>', '<label for="name">Name</label>')
rep('placeholder="Votre nom"', 'placeholder="Your name"')
rep('<label for="email">Email</label>', '<label for="email">Email</label>')
rep('placeholder="votre@email.com"', 'placeholder="your@email.com"')
rep('<label for="phone">Téléphone (optionnel)</label>', '<label for="phone">Telephone (optional)</label>')
rep('placeholder="06 00 00 00 00"', 'placeholder="+44…"')
rep('<label for="msg">Message</label>', '<label for="msg">Message</label>')
rep('placeholder="Bonjour, je souhaite recevoir les photos / bilans et organiser une visite. Mes disponibilités sont…"',
    'placeholder="Hello, I would like to receive the photographs and business information, and arrange a viewing. My availability is…"')
rep('<button class="btn primary" type="submit">Envoyer ma demande</button>',
    '<button class="btn primary" type="submit">Send My Enquiry</button>')
rep('En cliquant sur “Envoyer”, votre logiciel de messagerie s’ouvre avec votre demande pré-remplie.',
    'By clicking “Send”, your email application will open with your enquiry already prepared.')

# ---------------------------------------------------------------- FOOTER
rep('<div class="small">© <span id="year"></span> • Bien immobilier – Bedous (Vallée d’Aspe)</div>',
    '<div class="small">© <span id="year"></span> • Property for sale – Bedous (Vallée d’Aspe, France)</div>')
rep('<div class="small">Chambres d’hôtes & habitation · Bedous · Vallée d’Aspe · Pyrénées-Atlantiques</div>',
    '<div class="small">Bed &amp; Breakfast &amp; private residence · Bedous · Vallée d’Aspe · Pyrénées-Atlantiques, France</div>')

# ---------------------------------------------------------------- JS : chemins + textes
rep('buildCarousel(gallery, photos, ".", document.getElementById("car-counter"), idx => openLb(idx, photos, "."));',
    'buildCarousel(gallery, photos, "..", document.getElementById("car-counter"), idx => openLb(idx, photos, ".."));')
rep('document.getElementById("gallery-rdc"), photosRdc, "photos-rdc",',
    'document.getElementById("gallery-rdc"), photosRdc, "../photos-rdc",')
rep('idx => openLb(idx, photosRdc, "photos-rdc")', 'idx => openLb(idx, photosRdc, "../photos-rdc")')
rep('document.getElementById("gallery-ch"), photosChambres, "photos-chambres",',
    'document.getElementById("gallery-ch"), photosChambres, "../photos-chambres",')
rep('idx => openLb(idx, photosChambres, "photos-chambres")', 'idx => openLb(idx, photosChambres, "../photos-chambres")')
rep('document.getElementById("gallery-ap"), photosAppartement, "photos-appartement",',
    'document.getElementById("gallery-ap"), photosAppartement, "../photos-appartement",')
rep('idx => openLb(idx, photosAppartement, "photos-appartement")', 'idx => openLb(idx, photosAppartement, "../photos-appartement")')
rep('let current = 0, lbFiles = photos, lbFolder = "photos";', 'let current = 0, lbFiles = photos, lbFolder = "..";')

rep('const subject = "Demande d\'informations – Bien à Bedous (Vallée d’Aspe)";',
    'const subject = "Property enquiry – Bedous (Vallée d’Aspe, France)";')
rep("""`Bonjour,

Nom: ${name}
Email: ${email}
Téléphone: ${phone || "—"}

Message:
${msg}

Cordialement,
${name}`;""",
    """`Hello,

Name: ${name}
Email: ${email}
Telephone: ${phone || "—"}

Message:
${msg}

Kind regards,
${name}`;""")

# ---------------------------------------------------------------- FAQ
rep('''  <!-- ===================== FAQ ===================== -->
  <section id="faq" class="section">
    <div class="wrap">
      <div class="titleRow">
        <h2>❓ Questions fréquentes</h2>
        <p class="lead">Les réponses aux questions que les acheteurs nous posent le plus souvent. Une autre question ? Écrivez-nous via le formulaire en bas de page.</p>
      </div>
      <div class="faq">
        <details class="faqItem"><summary>Pourquoi vendez-vous ?</summary><p>Après de belles années consacrées à l’accueil des voyageurs, Michel et Annie souhaitent passer la main. La maison familiale et son activité cherchent de nouveaux propriétaires pour écrire la suite de leur histoire.</p></details>
        <details class="faqItem"><summary>Le prix est-il négociable ?</summary><p>Le prix de 350 000 € a été fixé avec soin, mobilier et équipement compris. Toute offre sérieuse, en particulier après une visite, sera étudiée avec attention.</p></details>
        <details class="faqItem"><summary>Pourquoi voit-on deux prix en ligne ?</summary><p>Ici, le bien est proposé en vente directe par la famille : 350 000 €, sans commission d’agence. Une agence locale le présente aussi, avec ses honoraires en plus. C’est le même bien — en nous contactant directement, l’acheteur économise les frais d’agence.</p></details>
        <details class="faqItem"><summary>Faut-il reprendre l’activité de chambres d’hôtes ?</summary><p>Non, rien n’oblige à poursuivre l’activité. Le bien peut devenir une grande maison familiale ou accueillir un autre commerce : l’immeuble est déclaré à usage d’habitation et de commerce. Et pour qui veut se lancer, la reprise est possible sans interruption d’exploitation, mobilier et équipement compris.</p></details>
        <details class="faqItem"><summary>Quels sont les chiffres de l’activité ?</summary><p>L’activité génère un chiffre d’affaires d’environ 30 000 € par an, avec une clientèle présente d’avril à octobre. Un dossier détaillé est disponible sur demande.</p></details>
        <details class="faqItem"><summary>Pourquoi deux surfaces, 266 et 311 m² ?</summary><p>266 m² est la surface loi Carrez, qui exclut notamment les parties sous 1,80 m — c’est le chiffre qui figurera dans l’acte de vente. 311 m² est la surface de référence du DPE, qui inclut les combles aménagés sous rampants. Les deux chiffres sont exacts : ils ne mesurent pas la même chose.</p></details>
        <details class="faqItem"><summary>Comment organiser une visite ?</summary><p>Les visites se font sur rendez-vous, en contactant Michel par téléphone ou via le formulaire en bas de page. La visite virtuelle 360° permet déjà un premier tour complet de la maison à distance.</p></details>
      </div>
    </div>
  </section>

''',
    '''  <!-- ===================== FAQ ===================== -->
  <section id="faq" class="section">
    <div class="wrap">
      <div class="titleRow">
        <h2>❓ Frequently asked questions</h2>
        <p class="lead">Answers to the questions buyers ask us most often. Have another question? Write to us using the form at the bottom of the page.</p>
      </div>
      <div class="faq">
        <details class="faqItem"><summary>Why are you selling?</summary><p>After many happy years welcoming travellers, Michel and Annie feel it is time to hand over the keys. The family home and its business are looking for new owners to write the next chapter of their story.</p></details>
        <details class="faqItem"><summary>Is the price negotiable?</summary><p>The price of €350,000 has been set with care, furniture and equipment included. Any serious offer, particularly following a visit, will be given careful consideration.</p></details>
        <details class="faqItem"><summary>Why are there two prices online?</summary><p>Here, the property is offered for sale directly by the family: €350,000, with no agency commission. A local estate agency also markets the property, with its fees added on top. It is the same property — by contacting us directly, the buyer saves the agency fees.</p></details>
        <details class="faqItem"><summary>Do we have to take over the bed &amp; breakfast business?</summary><p>No — there is no obligation to continue the business. The property could become a large family home or house another type of business: the building is officially registered for both residential and commercial use. And for those who wish to take the plunge, the business can be taken over without any interruption to trading, furniture and equipment included.</p></details>
        <details class="faqItem"><summary>What are the business figures?</summary><p>The business generates a turnover of around €30,000 a year, with guests staying from April to October. Detailed figures are available on request.</p></details>
        <details class="faqItem"><summary>Why two floor areas, 266 and 311 m²?</summary><p>266 m² is the “loi Carrez” floor area, which excludes areas with less than 1.80 m of head height — this is the figure that will appear in the deed of sale. 311 m² is the reference area used for the energy survey, which includes the converted attic space under the eaves. Both figures are correct: they simply measure different things.</p></details>
        <details class="faqItem"><summary>How can I arrange a visit?</summary><p>Visits are by appointment — contact Michel by telephone or using the form at the bottom of the page. The 360° virtual tour already lets you explore the whole house from a distance.</p></details>
      </div>
    </div>
  </section>

''')

# ---------------------------------------------------------------- garde-fou
if errors:
    sys.stderr.write("\n".join("ECHEC : " + e for e in errors) + "\n")
    sys.exit(1)

# Aucun texte francais residuel evident ?
suspects = ["Chambres d’hôtes", "Précédente", "Suivante", "petits-déjeuners", "Envoyer"]
found = [s for s in suspects if s in html]

os.makedirs(os.path.join(SITE, "en"), exist_ok=True)
io.open(os.path.join(SITE, "en", "index.html"), "w", encoding="utf-8").write(html)
print("OK : en/index.html ecrit (%d caracteres)" % len(html))
if found:
    print("A verifier, chaines FR encore presentes : %s" % ", ".join(found))

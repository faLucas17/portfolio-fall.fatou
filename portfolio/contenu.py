"""
Textes du portfolio partagés entre la commande charger_contenu (base vide)
et les migrations de données (base déjà remplie sur Render).
"""

ACCROCHE = (
    "Je transforme une idée en application qui tourne vraiment, "
    "du premier écran jusqu'à la mise en ligne."
)

A_PROPOS = (
    "Je suis développeuse Full Stack, et j'adore ça. Mais ce qui rend mon profil un peu différent, "
    "c'est que je termine en parallèle un deuxième Master en Sciences des Données. Résultat : je sais coder "
    "une application de A à Z, et je sais aussi analyser les données qu'elle produit.\n\n"
    "Ce qui me motive au quotidien, c'est de transformer une idée en une vraie application que les gens "
    "utilisent. Pendant 6 mois chez Bakeli, je l'ai fait sur des produits bien réels : un chatbot de support, "
    "une appli mobile, et un système d'authentification unique.\n\n"
    "Et le fameux « ça marche sur ma machine » ? Très peu pour moi. Mon truc, c'est d'aller jusqu'au bout : "
    "je déploie, je configure la base de données, les e-mails, et je vérifie que l'utilisateur final n'a aucun "
    "souci. J'aime aussi rendre mes applications concrètes et utiles au quotidien, en intégrant des solutions "
    "de paiement mobile (Wave, Orange Money) par exemple.\n\n"
    "Et la Data dans tout ça ? C'est mon atout en plus. Quand une application génère des chiffres, je suis "
    "capable de les transformer en tableaux de bord clairs et en réponses concrètes. En gros, je code votre "
    "produit, et je vous aide aussi à comprendre ce qu'il raconte.\n\n"
    "Ma devise ? Faire simple, faire utile, et faire en sorte que ça tourne en prod."
)

GLOWLUXE = dict(
    sous_titre="Boutique de mode en ligne, projet client réalisé à deux",
    description=(
        "Boutique de mode (prêt-à-porter, crochet fait main, accessoires) réalisée pour une cliente "
        "avec une amie développeuse. Une seule base de code pour iPhone, Android et le web, "
        "du catalogue jusqu'à la livraison suivie en direct sur une carte."
    ),
    points_cles=(
        "Panier sans compte, fusionné automatiquement à la connexion\n"
        "Paiement Wave, Orange Money et carte, avec acompte selon le montant\n"
        "Attribution automatique des livreurs (disponibilité, charge, distance) et suivi en direct\n"
        "Espace livreur dans l'appli : disponibilité, GPS, encaissement\n"
        "E-mails Brevo : confirmation, paiement reçu, livreur désigné, promotions\n"
        "Version web en production sur Cloudflare Pages"
    ),
    technologies="Expo, React Native, Django, PostgreSQL, Cloudflare, Brevo",
    categorie="client",
    statut="en_ligne",
    lien_demo="https://glowluxe-99q.pages.dev/",
)

BAYT_AL_ILM = dict(
    titre="Bayt Al-Ilm CATK",
    sous_titre="Bibliothèque numérique, projet client (anciennement Maktaba CATK)",
    description=(
        "Bibliothèque numérique avec une API Django et une interface React, réalisée pour un client. "
        "Déploiements automatiques à chaque mise à jour du code."
    ),
    categorie="client",
)

AL_BARAKAH = dict(
    titre="Al-Barakah",
    sous_titre="Plateforme de Zakat et de dons",
    description=(
        "Plateforme pour calculer sa Zakat, faire des dons et suivre des campagnes de collecte. "
        "Le projet est parti d'un cahier des charges et d'un document technique que j'ai rédigés en LaTeX."
    ),
    points_cles=(
        "Calcul de la Zakat\n"
        "Dons et campagnes de collecte\n"
        "Environnement conteneurisé avec Docker, déploiement prévu sur Render"
    ),
    technologies="Laravel, Docker, Render",
    categorie="perso",
    statut="en_cours",
    icone="shield-check",
    ordre=6,
)

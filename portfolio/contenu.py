"""
Textes du portfolio partagés entre la commande charger_contenu (base vide)
et les migrations de données (base déjà remplie sur Render).
"""

ACCROCHE = (
    "Je transforme une idée en application qui tourne vraiment, "
    "du premier écran jusqu'à la mise en ligne."
)

A_PROPOS = (
    "En fin de double cursus : Génie Logiciel d'un côté, Sciences des Données de l'autre. "
    "On m'a souvent demandé de choisir entre les deux. Je n'ai jamais vraiment compris pourquoi : "
    "j'aime autant penser l'architecture d'une application que comprendre ce que racontent les chiffres.\n\n"
    "Chez Bakeli, j'ai passé six mois sur des produits utilisés par de vrais clients. J'y ai appris "
    "une chose simple : « ça marche sur ma machine » ne prouve rien. Le vrai test, c'est la production, "
    "avec des utilisateurs qui cliquent exactement là où on ne les attendait pas.\n\n"
    "Depuis, j'ai une petite obsession : livrer. Je configure les e-mails, le stockage, la base de "
    "données, et je ne lâche pas tant que le lien ne s'ouvre pas sur le téléphone du client. "
    "J'ai aussi un faible pour les applications pensées pour chez nous : paiement Wave et Orange Money, "
    "factures en FCFA, dossiers au format OHADA.\n\n"
    "Travailler avec moi, c'est avoir quelqu'un qui pose des questions avant d'écrire la première ligne, "
    "qui explique simplement ce qu'elle fait, et pour qui un bug est d'abord une énigme à résoudre."
)

GLOWLUXE = dict(
    sous_titre="Application mobile e-commerce de mode",
    description=(
        "Boutique de mode (prêt-à-porter, crochet fait main, accessoires) sur iPhone, Android et web. "
        "Du catalogue jusqu'à la livraison suivie en direct sur une carte."
    ),
    points_cles=(
        "Panier sans compte, fusionné automatiquement à la connexion\n"
        "Paiement Wave, Orange Money et carte, avec acompte selon le montant\n"
        "Attribution automatique des livreurs (disponibilité, charge, distance) et suivi en direct\n"
        "Espace livreur dans l'appli : disponibilité, GPS, encaissement\n"
        "E-mails Brevo : confirmation, paiement reçu, livreur désigné, promotions"
    ),
    technologies="Expo, React Native, Django, PostgreSQL, Brevo",
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

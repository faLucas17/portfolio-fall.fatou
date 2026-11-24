"""
Textes du portfolio partagés entre la commande charger_contenu (base vide)
et les migrations de données (base déjà remplie sur Render).
"""

ACCROCHE = (
    "Je transforme une idée en application qui tourne vraiment, "
    "du premier écran jusqu'à la mise en ligne."
)

A_PROPOS = (
    "J'ai commencé par le développement, puis je me suis passionnée pour les données. "
    "Aujourd'hui, je termine deux Masters : un en Génie Logiciel, un en Sciences des Données. "
    "Concrètement, je sais créer une application de A à Z, et je sais aussi analyser les données qu'elle contient.\n\n"
    "Ce que je préfère, c'est voir une idée devenir une vraie application que des gens utilisent. "
    "Pendant mon stage chez Bakeli, j'ai travaillé six mois sur des produits en ligne : un chatbot de support, "
    "une application mobile, et une connexion unique pour plusieurs applications.\n\n"
    "Je ne m'arrête pas quand le code marche sur mon ordinateur. Je mets l'application en ligne, je configure "
    "les e-mails et la base de données, et je vérifie que tout fonctionne pour l'utilisateur. J'aime aussi créer "
    "des applications adaptées à chez nous, avec Wave, Orange Money et le FCFA.\n\n"
    "Côté données, j'aime prendre un tableau de chiffres et en tirer quelque chose de clair : "
    "un graphique, un tableau de bord, une réponse à une vraie question."
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

"""
Charge le contenu initial du portfolio (profil, projets, services, parcours, compétences).
Ne fait rien si des projets existent déjà : vos modifications faites dans l'admin sont conservées.
Pour tout réinitialiser : python manage.py charger_contenu --reset
"""
from django.core.management.base import BaseCommand

from portfolio.models import GroupeCompetences, Parcours, Profil, Projet, Service

A_PROPOS = (
    "Je suis développeuse full stack, en fin de double cursus de Master 2 à l'Université "
    "Iba Der Thiam de Thiès : Génie Logiciel d'un côté, Sciences des Données (statistique, "
    "économétrie, modélisation) de l'autre.\n\n"
    "Pendant six mois chez Bakeli, j'ai travaillé sur des produits utilisés en production : "
    "une plateforme de support client avec chatbot, son intégration sur le web et le mobile, "
    "et l'authentification unique entre plusieurs applications.\n\n"
    "Ce qui me distingue : je ne m'arrête pas au code. Je déploie, je configure les e-mails, "
    "le stockage et la base de données, et je livre une application qui tourne vraiment. "
    "Et grâce à ma formation en données, je sais aussi transformer vos chiffres en tableaux "
    "de bord utiles."
)

PROJETS = [
    dict(
        titre="Easy Desk et chatbot WAGAN AI",
        sous_titre="Plateforme de support client multi-projets, Bakeli",
        description=(
            "Plateforme de support client multi-tenant avec un chatbot qui répond aux questions "
            "fréquentes et transfère vers un agent humain quand il le faut. Intégrée dans plusieurs "
            "produits de l'écosystème Easy Suite."
        ),
        points_cles=(
            "Chatbot FAQ par mots-clés avec escalade vers un agent par Discord et e-mail\n"
            "Intégration dans Easy Event web (React) et mobile (Expo)\n"
            "Identification des utilisateurs via Laravel Sanctum, escalades gérées dans Filament\n"
            "SSO Easy Suite intégré dans EasyCoop\n"
            "API, base PostgreSQL et interface React déployées sur Render"
        ),
        technologies="Django, DRF, PostgreSQL, React, Expo, Laravel, Filament, Render",
        categorie="pro", statut="en_ligne", icone="bot", en_vedette=True, ordre=1,
    ),
    dict(
        titre="KSJI, Kébé Services Juridiques Islamiques",
        sous_titre="Site professionnel pour un cabinet, projet client",
        description=(
            "Site web d'un cabinet de services juridiques islamiques, livré au client et en ligne. "
            "Présentation du cabinet, des services et prise de contact."
        ),
        points_cles=(
            "Base de données PostgreSQL hébergée sur Neon\n"
            "Fichiers et médias stockés sur Cloudflare R2\n"
            "E-mails transactionnels avec Brevo\n"
            "Déployé sur Render"
        ),
        technologies="Django, PostgreSQL, Neon, Cloudflare R2, Brevo, Render",
        categorie="client", statut="en_ligne", icone="scale",
        lien_demo="https://ksji-cabinet.onrender.com",
        lien_code="https://github.com/faLucas17/KSJI",
        en_vedette=True, ordre=2,
    ),
    dict(
        titre="Maktaba CATK",
        sous_titre="Bibliothèque numérique",
        description=(
            "Bibliothèque numérique avec une API Django et une interface React. "
            "Déploiements automatiques à chaque mise à jour du code."
        ),
        points_cles=(
            "Backend Django déployé sur Render\n"
            "Frontend React déployé sur Netlify\n"
            "Médias sur Cloudflare R2, e-mails avec Brevo\n"
            "Publication sur le Play Store et l'App Store prévue"
        ),
        technologies="Django, React, Render, Netlify, Cloudflare R2, Brevo",
        categorie="perso", statut="en_ligne", icone="book-open", en_vedette=True, ordre=3,
    ),
    dict(
        titre="Teranga Voyages",
        sous_titre="Application pour agence de voyage",
        description=(
            "Application complète pour une agence de voyage : offres, réservations et gestion. "
            "Conteneurisée avec Docker pour être déployée et revendue facilement."
        ),
        points_cles=(
            "API Laravel et interface React\n"
            "Environnement entièrement conteneurisé avec Docker\n"
            "Pensée comme un produit prêt à vendre à des agences"
        ),
        technologies="Laravel, React, Docker, Render, Brevo",
        categorie="perso", statut="en_cours", icone="plane",
        lien_code="https://github.com/faLucas17/teranga-voyages",
        en_vedette=True, ordre=4,
    ),
    dict(
        titre="GlowLuxe By Sofa",
        sous_titre="Application mobile e-commerce de mode",
        description=(
            "Boutique de mode (vêtements, crochet, accessoires) sous forme d'application mobile, "
            "avec comptes clients, panier, commandes et paiements adaptés au Sénégal."
        ),
        points_cles=(
            "Application mobile React Native (Expo)\n"
            "Backend Django\n"
            "Paiement par Wave, Orange Money et carte\n"
            "Suivi des livraisons et e-mails avec Brevo"
        ),
        technologies="Expo, React Native, Django, PostgreSQL, Brevo",
        categorie="perso", statut="en_cours", icone="shopping-bag",
        lien_code="https://github.com/faLucas17/glowluxe",
        ordre=5,
    ),
    dict(
        titre="LocaGest API",
        sous_titre="API de location de véhicules",
        description=(
            "API REST de location de véhicules avec authentification JWT et deux rôles : "
            "administrateur et client."
        ),
        points_cles="Gestion des véhicules, contrats et paiements\nRapports\nSécurité par JWT et rôles",
        technologies="Spring Boot, MySQL, JWT",
        categorie="perso", statut="termine", icone="car", ordre=6,
    ),
    dict(
        titre="Gestion de stock",
        sous_titre="API REST",
        description="API de gestion de stock : produits, niveaux de stock, entrées et sorties.",
        points_cles="Opérations CRUD complètes\nSuivi des mouvements de stock",
        technologies="Spring Boot, H2",
        categorie="academique", statut="termine", icone="package", ordre=7,
    ),
    dict(
        titre="Gestion des emplois du temps",
        sous_titre="Projet de fin d'études, Licence",
        description=(
            "Application de gestion et de suivi des emplois du temps d'un établissement : "
            "édition, publication, statistiques, avancement des cours et émargement des professeurs."
        ),
        points_cles="Publication des emplois du temps\nSuivi statistique de l'avancement\nÉmargement des professeurs",
        technologies="Web, SQL",
        categorie="academique", statut="termine", icone="calendar-days", ordre=8,
    ),
]

SERVICES = [
    ("globe", "Sites vitrines professionnels",
     "Un site rapide et soigné pour présenter votre entreprise, votre cabinet ou votre activité, livré en ligne avec votre nom de domaine."),
    ("layout-dashboard", "Applications web sur mesure",
     "Gestion, réservation, e-commerce, espace client : une application pensée pour votre métier, avec Django, Laravel ou React."),
    ("smartphone", "Applications mobiles",
     "Applications Android et iOS avec React Native (Expo) ou Flutter, connectées à votre API, avec paiement Wave et Orange Money."),
    ("plug", "API et intégrations",
     "API REST sécurisées (JWT, Sanctum, SSO), chatbots, e-mails automatiques, connexion à vos outils existants."),
    ("chart-column", "Tableaux de bord et analyse de données",
     "Vos données transformées en indicateurs clairs : Power BI, R, SQL. Ma double formation en données fait la différence."),
    ("rocket", "Déploiement et mise en ligne",
     "Votre projet existant mis en production proprement : Docker, Render, Netlify, base de données, stockage et e-mails."),
]

PARCOURS = [
    ("experience", "Développeuse Full Stack (stage)", "Bakeli School of Technology, Dakar", "Mars à septembre 2026",
     "Plateforme de support client avec chatbot, intégration web et mobile, SSO Easy Suite, création et déploiement d'Easy Desk.", 1),
    ("formation", "Master 2 Informatique, Génie Logiciel", "Université Iba Der Thiam de Thiès", "2025 à 2026", "", 1),
    ("formation", "Master 2 Sciences des Données et Applications", "Université Iba Der Thiam de Thiès", "2024 à 2025",
     "Option Statistique, Économétrie et Modélisation.", 2),
    ("formation", "Licence Informatique, Génie Logiciel", "Université Iba Der Thiam de Thiès", "2020 à 2023", "", 3),
    ("formation", "Initiation au développement web avec Django", "She Codes", "Septembre à octobre 2024", "", 4),
]

COMPETENCES = [
    ("Back-end", "Django, Django REST Framework, Laravel, Spring Boot, API REST"),
    ("Front-end et mobile", "React, Vue.js, React Native (Expo), Flutter, Bootstrap"),
    ("Bases de données", "PostgreSQL, MySQL, MongoDB, SQL Server, Firebase"),
    ("Sécurité", "JWT, Laravel Sanctum, SSO, CORS"),
    ("Déploiement et outils", "Docker, Git, GitHub, Render, Netlify, Neon, Cloudflare R2, Brevo"),
    ("Données", "Python, R (ggplot2), SQL, Power BI, Stata"),
    ("Langages", "Python, JavaScript, PHP, Java, R, SQL"),
    ("Langues", "Français courant, Anglais usuel"),
]


class Command(BaseCommand):
    help = "Charge le contenu initial du portfolio si la base est vide."

    def add_arguments(self, parser):
        parser.add_argument("--reset", action="store_true", help="Efface et recharge tout le contenu.")

    def handle(self, *args, **options):
        if options["reset"]:
            for m in (Projet, Service, Parcours, GroupeCompetences, Profil):
                m.objects.all().delete()
        elif Projet.objects.exists():
            self.stdout.write("Contenu déjà présent, rien à faire.")
            return

        profil = Profil.get()
        if not profil.a_propos:
            profil.a_propos = A_PROPOS
            profil.save()

        for p in PROJETS:
            Projet.objects.create(**p)
        for i, (icone, titre, desc) in enumerate(SERVICES, 1):
            Service.objects.create(icone=icone, titre=titre, description=desc, ordre=i)
        for type_, titre, org, periode, desc, ordre in PARCOURS:
            Parcours.objects.create(type=type_, titre=titre, organisation=org, periode=periode, description=desc, ordre=ordre)
        for i, (nom, comp) in enumerate(COMPETENCES, 1):
            GroupeCompetences.objects.create(nom=nom, competences=comp, ordre=i)

        self.stdout.write(self.style.SUCCESS("Contenu du portfolio chargé."))

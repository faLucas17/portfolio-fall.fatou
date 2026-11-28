"""
Charge le contenu initial du portfolio (profil, projets, services, parcours, compétences).
Ne fait rien si des projets existent déjà : vos modifications faites dans l'admin sont conservées.
Pour tout réinitialiser : python manage.py charger_contenu --reset
"""
from django.core.management.base import BaseCommand

from portfolio.contenu import A_PROPOS, ACCROCHE, AL_BARAKAH, BAYT_AL_ILM, GLOWLUXE
from portfolio.models import GroupeCompetences, Parcours, Profil, Projet, Service

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
        categorie="pro", statut="en_ligne", icone="bot",
        lien_demo="https://support-platform-admin.onrender.com/",
        en_vedette=True, ordre=1,
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
        categorie="client", statut="en_ligne", icone="globe",
        lien_demo="https://ksji-cabinet.onrender.com",
        en_vedette=True, ordre=2,
    ),
    dict(
        titre="Lexora",
        sous_titre="Logiciel SaaS de gestion de cabinets d'avocats",
        description=(
            "Plateforme SaaS pensée pour les cabinets d'avocats d'Afrique de l'Ouest : dossiers, "
            "audiences, agenda, facturation en FCFA et portail client. Chaque cabinet s'inscrit "
            "librement et ses données restent strictement isolées des autres."
        ),
        points_cles=(
            "Multi-cabinets avec isolation des données couverte par des tests automatisés\n"
            "Dossiers, audiences avec renvois automatiques, agenda unifié et tâches en Kanban\n"
            "Factures générées à partir du temps passé, TVA 18 %, paiement Wave, Orange Money, virement\n"
            "Portail client, e-mails Brevo et rappel automatique la veille de chaque audience\n"
            "Sécurité : Cloudflare Turnstile, protection anti force brute, documents privés sur R2\n"
            "CI GitHub Actions, Docker multi-services (Nginx, PHP-FPM, Redis), déployé sur Render"
        ),
        technologies="Laravel, React, TypeScript, Tailwind CSS, PostgreSQL, Redis, Docker, Cloudflare R2, Brevo, Render",
        categorie="perso", statut="en_ligne", icone="scale",
        lien_demo="https://lexora-80dr.onrender.com/",
        en_vedette=True, ordre=0,
    ),
    dict(
        **BAYT_AL_ILM,
        points_cles=(
            "Backend Django déployé sur Render\n"
            "Frontend React déployé sur Netlify\n"
            "Médias sur Cloudflare R2, e-mails avec Brevo\n"
            "Publication sur le Play Store et l'App Store prévue"
        ),
        technologies="Django, React, Render, Netlify, Cloudflare R2, Brevo",
        statut="en_ligne", icone="book-open",
        lien_demo="https://maktaba-catk.netlify.app/",
        en_vedette=True, ordre=3,
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
        en_vedette=True, ordre=4,
    ),
    dict(
        titre="GlowLuxe By Sofa", **GLOWLUXE,
        icone="shopping-bag", ordre=5,
    ),
    AL_BARAKAH,
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
            profil.accroche = ACCROCHE
            profil.save()

        for p in PROJETS:
            Projet.objects.create(**dict(p))
        for i, (icone, titre, desc) in enumerate(SERVICES, 1):
            Service.objects.create(icone=icone, titre=titre, description=desc, ordre=i)
        for type_, titre, org, periode, desc, ordre in PARCOURS:
            Parcours.objects.create(type=type_, titre=titre, organisation=org, periode=periode, description=desc, ordre=ordre)
        for i, (nom, comp) in enumerate(COMPETENCES, 1):
            GroupeCompetences.objects.create(nom=nom, competences=comp, ordre=i)

        self.stdout.write(self.style.SUCCESS("Contenu du portfolio chargé."))

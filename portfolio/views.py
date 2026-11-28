import logging

from django.contrib import messages
from django.shortcuts import redirect, render

from .emails import envoyer_accuse_reception, envoyer_notification
from .forms import ContactForm
from .models import GroupeCompetences, Parcours, Projet, Service

logger = logging.getLogger(__name__)

# Logos de la boîte à outils (accueil) : chacun mène à ses projets
HERO_STACK = ["Django", "React", "Laravel", "Docker", "PostgreSQL", "Expo", "Python", "Spring Boot", "TypeScript"]

# Technos proposées en filtre sur la page Projets
FILTRES_TECHNOS = [
    "Django", "Laravel", "React", "TypeScript", "Expo", "Spring Boot",
    "PostgreSQL", "MySQL", "Docker", "Cloudflare R2", "Brevo", "Render",
]


def erreur_csrf(request, reason=""):
    logger.warning(
        "CSRF refusé : %s | chemin=%s | origin=%s | referer=%s | cookie_csrf=%s",
        reason, request.path, request.META.get("HTTP_ORIGIN"),
        request.META.get("HTTP_REFERER"), "csrftoken" in request.COOKIES,
    )
    return render(request, "erreur_csrf.html", {"retour": request.path}, status=403)


def accueil(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = form.save()
            site_url = request.build_absolute_uri("/").rstrip("/")
            for envoi in (lambda: envoyer_notification(msg), lambda: envoyer_accuse_reception(msg, site_url)):
                try:
                    envoi()
                except Exception:  # le message reste enregistré dans l'admin
                    logger.exception("Envoi d'un e-mail de contact impossible")
            messages.success(request, "Merci ! Votre message a bien été envoyé. Je vous réponds rapidement.")
            return redirect("/#contact")
        messages.error(request, "Merci de vérifier les champs du formulaire.")
    else:
        form = ContactForm()

    projets = Projet.objects.filter(visible=True)
    contexte = {
        "form": form,
        "projets": projets,
        "categories": Projet.CATEGORIES,
        "services": Service.objects.all(),
        "experiences": Parcours.objects.filter(type="experience"),
        "formations": Parcours.objects.filter(type="formation"),
        "competences": GroupeCompetences.objects.all(),
        "nb_projets": projets.count(),
        "nb_en_ligne": projets.filter(statut="en_ligne").count(),
        "hero_stack": HERO_STACK,
    }
    return render(request, "portfolio/accueil.html", contexte)


def projets(request):
    techno = request.GET.get("techno", "").strip()
    categorie = request.GET.get("categorie", "").strip()
    statut = request.GET.get("statut", "").strip()

    qs = Projet.objects.filter(visible=True)
    if categorie:
        qs = qs.filter(categorie=categorie)
    if statut:
        qs = qs.filter(statut=statut)
    liste = [p for p in qs if not techno or p.utilise(techno)]

    titre = "Tous mes projets"
    if techno:
        titre = f"Mes projets {techno}"
    elif statut == "en_ligne":
        titre = "Mes projets en ligne"
    elif categorie:
        titre = dict(Projet.CATEGORIES).get(categorie, titre)

    return render(request, "portfolio/projets.html", {
        "projets": liste,
        "titre": titre,
        "techno": techno,
        "categorie": categorie,
        "statut": statut,
        "categories": Projet.CATEGORIES,
        "filtres_technos": FILTRES_TECHNOS,
        "total": Projet.objects.filter(visible=True).count(),
    })


def bakeli(request):
    easy_desk = Projet.objects.filter(categorie="pro").first()
    return render(request, "portfolio/bakeli.html", {"easy_desk": easy_desk})


def formations(request):
    return render(request, "portfolio/formations.html", {
        "formations": Parcours.objects.filter(type="formation"),
    })

import logging

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import ContactForm
from .models import GroupeCompetences, Parcours, Projet, Service

logger = logging.getLogger(__name__)


def accueil(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = form.save()
            try:
                send_mail(
                    subject=f"[Portfolio] {msg.sujet or 'Nouveau message'} de {msg.nom}",
                    message=f"De : {msg.nom} <{msg.email}>\n\n{msg.contenu}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_RECEIVER_EMAIL],
                    fail_silently=False,
                )
            except Exception:  # le message reste enregistré dans l'admin
                logger.exception("Envoi de l'e-mail de contact impossible")
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
        "hero_stack": ["Django", "React", "Laravel", "Docker", "PostgreSQL", "Expo", "Python", "Spring Boot", "Flutter"],
    }
    return render(request, "portfolio/accueil.html", contexte)

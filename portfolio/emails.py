"""
E-mails du formulaire de contact :
- une notification à Fatou (avec « Répondre » vers le visiteur)
- un accusé de réception automatique au visiteur

Render (offre gratuite) bloque les ports SMTP 25, 465 et 587 : on passe donc par
l'API HTTP de Brevo (port 443). Sans clé API (en local), on retombe sur l'envoi
Django classique (console ou SMTP).
"""
import json
import logging
import urllib.error
import urllib.request

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

logger = logging.getLogger(__name__)


def _envoyer(*, a_email, a_nom, sujet, texte, html=None, repondre_a=None):
    """Envoie un e-mail via l'API Brevo, ou via Django en local. Renvoie True si parti."""
    if not settings.BREVO_API_KEY:
        mail = EmailMultiAlternatives(
            sujet, texte, settings.DEFAULT_FROM_EMAIL, [a_email],
            reply_to=[repondre_a["email"]] if repondre_a else None,
        )
        if html:
            mail.attach_alternative(html, "text/html")
        mail.send()
        return True

    donnees = {
        "sender": {"name": "Fatou FALL", "email": settings.DEFAULT_FROM_EMAIL},
        "to": [{"email": a_email, "name": a_nom}],
        "subject": sujet,
        "textContent": texte,
    }
    if html:
        donnees["htmlContent"] = html
    if repondre_a:
        donnees["replyTo"] = repondre_a

    requete = urllib.request.Request(
        settings.BREVO_API_URL,
        data=json.dumps(donnees).encode("utf-8"),
        headers={
            "api-key": settings.BREVO_API_KEY,
            "accept": "application/json",
            "content-type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(requete, timeout=10) as rep:
            return 200 <= rep.status < 300
    except urllib.error.HTTPError as e:
        logger.error("Brevo a refusé l'e-mail (%s) : %s", e.code, e.read().decode("utf-8", "ignore")[:500])
    except Exception:
        logger.exception("Envoi Brevo impossible")
    return False


def envoyer_notification(msg):
    """Prévient Fatou d'un nouveau message ; « Répondre » écrit directement au visiteur."""
    return _envoyer(
        a_email=settings.CONTACT_RECEIVER_EMAIL,
        a_nom="Fatou FALL",
        sujet=f"[Portfolio] {msg.sujet or 'Nouveau message'} de {msg.nom}",
        texte=f"De : {msg.nom} <{msg.email}>\nSujet : {msg.sujet or '-'}\n\n{msg.contenu}",
        repondre_a={"email": msg.email, "name": msg.nom},
    )


def envoyer_accuse_reception(msg, site_url):
    """Confirme au visiteur que son message est bien arrivé."""
    contexte = {"msg": msg, "site_url": site_url}
    return _envoyer(
        a_email=msg.email,
        a_nom=msg.nom,
        sujet="J'ai bien reçu votre message",
        texte=render_to_string("emails/accuse_reception.txt", contexte),
        html=render_to_string("emails/accuse_reception.html", contexte),
        repondre_a={"email": settings.CONTACT_RECEIVER_EMAIL, "name": "Fatou FALL"},
    )

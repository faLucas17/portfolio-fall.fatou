"""
Envoi de la notification du formulaire de contact.

Render (offre gratuite) bloque les ports SMTP 25, 465 et 587 : on passe donc par
l'API HTTP de Brevo (port 443). Sans clé API (en local), on retombe sur l'envoi
Django classique (console ou SMTP).
"""
import json
import logging
import urllib.error
import urllib.request

from django.conf import settings
from django.core.mail import send_mail

logger = logging.getLogger(__name__)

BREVO_URL = "https://api.brevo.com/v3/smtp/email"


def envoyer_notification(msg):
    """Prévient Fatou d'un nouveau message. Renvoie True si l'e-mail est parti."""
    sujet = f"[Portfolio] {msg.sujet or 'Nouveau message'} de {msg.nom}"
    texte = f"De : {msg.nom} <{msg.email}>\nSujet : {msg.sujet or '-'}\n\n{msg.contenu}"

    if not settings.BREVO_API_KEY:
        send_mail(sujet, texte, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_RECEIVER_EMAIL])
        return True

    donnees = {
        "sender": {"name": "Portfolio Fatou FALL", "email": settings.DEFAULT_FROM_EMAIL},
        "to": [{"email": settings.CONTACT_RECEIVER_EMAIL, "name": "Fatou FALL"}],
        "replyTo": {"email": msg.email, "name": msg.nom},  # « Répondre » écrit directement au visiteur
        "subject": sujet,
        "textContent": texte,
    }
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

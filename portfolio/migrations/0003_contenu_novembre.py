"""
Mise à jour du contenu d'une base déjà remplie (Render) :
- nouveau texte « À propos » et nouvelle accroche
- fiche GlowLuxe enrichie
- ajout du projet Al-Barakah
Sur une base vide, ne fait rien : la commande charger_contenu s'en charge.
"""
from django.db import migrations

from portfolio.contenu import A_PROPOS, ACCROCHE, AL_BARAKAH, GLOWLUXE


def appliquer(apps, schema_editor):
    Profil = apps.get_model("portfolio", "Profil")
    Projet = apps.get_model("portfolio", "Projet")

    if not Projet.objects.exists():
        return  # base vide : charger_contenu chargera tout

    Profil.objects.filter(pk=1).update(a_propos=A_PROPOS, accroche=ACCROCHE)
    Projet.objects.filter(titre="GlowLuxe By Sofa").update(**GLOWLUXE)
    if not Projet.objects.filter(titre=AL_BARAKAH["titre"]).exists():
        Projet.objects.create(**AL_BARAKAH)


class Migration(migrations.Migration):
    dependencies = [("portfolio", "0002_profil_anecdote")]
    operations = [migrations.RunPython(appliquer, migrations.RunPython.noop)]

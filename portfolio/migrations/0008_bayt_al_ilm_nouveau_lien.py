"""Bayt Al-Ilm CATK : nouvelle adresse en ligne, fin de la mention « anciennement Maktaba CATK »."""
from django.db import migrations

from portfolio.contenu import BAYT_AL_ILM


def appliquer(apps, schema_editor):
    Projet = apps.get_model("portfolio", "Projet")
    Projet.objects.filter(titre__in=["Bayt Al-Ilm CATK", "Maktaba CATK"]).update(
        titre=BAYT_AL_ILM["titre"],
        sous_titre=BAYT_AL_ILM["sous_titre"],
        lien_demo=BAYT_AL_ILM["lien_demo"],
    )


class Migration(migrations.Migration):
    dependencies = [("portfolio", "0007_glowluxe_developpe_seule")]
    operations = [migrations.RunPython(appliquer, migrations.RunPython.noop)]

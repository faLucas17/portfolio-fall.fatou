"""GlowLuxe passe en ligne (projet client) ; Maktaba CATK devient Bayt Al-Ilm CATK (projet client)."""
from django.db import migrations

from portfolio.contenu import BAYT_AL_ILM, GLOWLUXE


def appliquer(apps, schema_editor):
    Projet = apps.get_model("portfolio", "Projet")
    Projet.objects.filter(titre="GlowLuxe By Sofa").update(**GLOWLUXE)
    Projet.objects.filter(titre="Maktaba CATK").update(**BAYT_AL_ILM)


class Migration(migrations.Migration):
    dependencies = [("portfolio", "0005_a_propos_fatou")]
    operations = [migrations.RunPython(appliquer, migrations.RunPython.noop)]

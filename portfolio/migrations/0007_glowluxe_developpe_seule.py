"""GlowLuxe : co-fondé avec une amie, développé seule par Fatou."""
from django.db import migrations

from portfolio.contenu import GLOWLUXE


def appliquer(apps, schema_editor):
    Projet = apps.get_model("portfolio", "Projet")
    Projet.objects.filter(titre="GlowLuxe By Sofa").update(**GLOWLUXE)


class Migration(migrations.Migration):
    dependencies = [("portfolio", "0006_glowluxe_bayt_al_ilm")]
    operations = [migrations.RunPython(appliquer, migrations.RunPython.noop)]

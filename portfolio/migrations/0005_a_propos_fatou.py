"""Texte « À propos » écrit par Fatou."""
from django.db import migrations

from portfolio.contenu import A_PROPOS


def appliquer(apps, schema_editor):
    apps.get_model("portfolio", "Profil").objects.filter(pk=1).update(a_propos=A_PROPOS)


class Migration(migrations.Migration):
    dependencies = [("portfolio", "0004_a_propos_simplifie")]
    operations = [migrations.RunPython(appliquer, migrations.RunPython.noop)]

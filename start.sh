#!/bin/sh
set -e

echo "==> Migrations"
python manage.py migrate --noinput

echo "==> Contenu initial (ignoré si déjà présent)"
python manage.py charger_contenu

# Crée le compte admin au premier démarrage si les variables sont définies
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
  python manage.py createsuperuser --noinput 2>/dev/null || echo "Compte admin déjà existant."
fi

echo "==> Démarrage sur le port ${PORT:-8000}"
exec gunicorn config.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 2 --timeout 60

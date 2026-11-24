# Portfolio de Fatou FALL

Site portfolio en **Django + Docker**, prêt à déployer sur **Render**, avec base **Neon** et e-mails **Brevo**.

Tout le contenu (profil, projets, liens, services, parcours, compétences) se modifie depuis l'administration, sans toucher au code.

## Sections du site

Accueil, À propos, Services (pour les clients freelance), Projets avec filtres, Expérience et formation, Compétences, Contact (formulaire, e-mail, WhatsApp, GitHub) et bouton de téléchargement du CV.

## 1. Lancer en local

```bash
cp .env.example .env            # puis mettez un mot de passe dans DJANGO_SUPERUSER_PASSWORD
python -m venv venv
venv\Scripts\activate           # Windows  (Mac/Linux : source venv/bin/activate)
pip install -r requirements.txt
python manage.py migrate
python manage.py charger_contenu
python manage.py createsuperuser
python manage.py runserver
```

Ou avec Docker :

```bash
cp .env.example .env
docker compose up --build
```

Site : http://localhost:8000 · Administration : http://localhost:8000/gestion/

## 2. Mettre sur GitHub

```bash
git init
git add .
git commit -m "Portfolio Fatou FALL"
git branch -M main
git remote add origin https://github.com/faLucas17/portfolio.git
git push -u origin main
```

## 3. Créer la base sur Neon

1. Sur neon.tech, créez un projet `portfolio`.
2. Copiez la **connection string** (elle commence par `postgresql://`).

Sans base Neon, le site marche quand même, mais sur l'offre gratuite de Render les modifications faites dans l'admin seraient perdues à chaque redémarrage.

## 4. Déployer sur Render

1. Render, **New > Blueprint**, choisissez le dépôt `faLucas17/portfolio`. Render lit le fichier `render.yaml`.
2. Remplissez les variables demandées :
   - `DATABASE_URL` : l'URL Neon
   - `DJANGO_SUPERUSER_USERNAME`, `DJANGO_SUPERUSER_EMAIL`, `DJANGO_SUPERUSER_PASSWORD` : votre compte admin
   - `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL` : identifiants SMTP Brevo (facultatif)
3. Cliquez sur **Apply**. Au premier démarrage, le site crée les tables, charge vos projets et votre compte admin.

Chaque `git push` redéploie automatiquement le site.

## 5. Ajouter les liens de vos projets

1. Allez sur `https://votre-site.onrender.com/gestion/` et connectez-vous.
2. **Projets** : collez le lien Render ou Netlify dans la colonne « Lien du site déployé », puis Enregistrer.
3. Vous pouvez aussi changer le statut (En ligne, En cours), l'ordre, mettre un projet en avant ou le masquer.
4. **Profil** : ajoutez votre LinkedIn, votre profil Malt ou Upwork, et le lien d'une photo si vous le souhaitez.
5. **Messages reçus** : tous les messages du formulaire de contact y sont gardés, même si Brevo n'est pas configuré.

### Ajouter une capture d'écran à un projet

Envoyez l'image dans votre bucket Cloudflare R2 (accès public activé), copiez son lien et collez-le dans « Lien d'une capture d'écran ».

## 6. Mettre à jour le CV

Remplacez le fichier `static/cv/CV_Fatou_Fall.pdf` par la nouvelle version (même nom), puis `git push`.

## 7. Nom de domaine (plus tard)

Achetez par exemple `fatoufall.dev`, ajoutez-le dans Render (Settings > Custom Domains) et dans Cloudflare (DNS), puis ajoutez-le à `ALLOWED_HOSTS` et `CSRF_TRUSTED_ORIGINS` (avec `https://`).

## Recharger le contenu d'origine

```bash
python manage.py charger_contenu --reset
```

Attention : cette commande efface tout ce que vous avez modifié dans l'admin.

## Structure

```
config/          réglages Django (settings, urls)
portfolio/       modèles, admin, vues, formulaire, commande charger_contenu
templates/       pages HTML
static/          CSS, JavaScript, CV
Dockerfile       image de production (gunicorn + whitenoise)
render.yaml      configuration Render
start.sh         migrations, contenu initial, compte admin, démarrage
```

## Icônes

- Pictogrammes : [Lucide](https://lucide.dev) (licence ISC), dans `static/img/icons`. Pour changer l'icône d'un projet ou d'un service, mettez dans l'admin le nom d'un fichier de ce dossier, par exemple `globe` ou `rocket`. Pour en ajouter, copiez un SVG depuis lucide.dev dans ce dossier.
- Logos des technologies : [Devicon](https://devicon.dev) (licence MIT), dans `static/img/tech`. Ils s'affichent automatiquement à partir des technologies que vous écrivez.
- Police : Inter, la même que dans Maktaba CATK.

## Pages

- `/` accueil · `/projets/` tous les projets (filtres `?techno=Django`, `?categorie=pro`, `?statut=en_ligne`)
- `/experience/bakeli/` le détail du stage · `/formations/` les deux Masters
- Les chiffres de l'accueil, les logos et les technologies des projets mènent à ces pages.

## CV

Le PDF est dans `static/cv/CV_Fatou_Fall.pdf`. Sa source LaTeX est dans `docs/cv/CV_Fatou_Fall.tex` :
importez-la dans Overleaf (compilateur pdfLaTeX) pour la modifier, puis remplacez le PDF.

## Mettre à jour le contenu en ligne

Le contenu de la base Render se met à jour par des migrations de données
(exemple : `portfolio/migrations/0003_contenu_novembre.py`), qui ne touchent pas aux liens modifiés dans l'admin.
Le champ « Petite anecdote » du Profil (admin) ajoute une phrase à la fin de « À propos ».

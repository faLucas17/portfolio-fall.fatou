from django.db import models


class Profil(models.Model):
    """Informations générales affichées sur le site (une seule fiche)."""

    nom = models.CharField(max_length=100, default="Fatou FALL")
    titre = models.CharField(max_length=150, default="Développeuse Full Stack")
    accroche = models.CharField(
        max_length=255,
        default="Je conçois et je mets en ligne des applications web et mobiles fiables.",
    )
    a_propos = models.TextField(blank=True)
    disponible = models.BooleanField("Disponible pour missions", default=True)
    texte_disponibilite = models.CharField(
        max_length=120, default="Disponible : CDI, CDD et missions freelance à distance"
    )
    localisation = models.CharField(max_length=100, default="Dakar, Sénégal")
    email = models.EmailField(default="fatou.fall4@univ-thies.sn")
    telephone = models.CharField(max_length=30, default="+221 77 822 84 60")
    whatsapp = models.CharField(
        "Numéro WhatsApp (chiffres uniquement, avec indicatif)", max_length=20, default="221778228460"
    )
    github = models.URLField(default="https://github.com/faLucas17")
    linkedin = models.URLField(blank=True)
    malt = models.URLField("Profil freelance (Malt, Upwork…)", blank=True)
    photo_url = models.URLField(
        "Lien d'une photo (optionnel)",
        blank=True,
        help_text="Lien direct vers votre photo (ex. Cloudflare R2). Laissez vide pour afficher vos initiales.",
    )

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profil"

    def __str__(self):
        return self.nom

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class Projet(models.Model):
    CATEGORIES = [
        ("pro", "Expérience pro"),
        ("client", "Projet client"),
        ("perso", "Projet personnel"),
        ("academique", "Académique"),
    ]
    STATUTS = [
        ("en_ligne", "En ligne"),
        ("en_cours", "En cours"),
        ("termine", "Terminé"),
    ]

    titre = models.CharField(max_length=120)
    sous_titre = models.CharField(max_length=160, blank=True)
    description = models.TextField()
    points_cles = models.TextField(
        "Points clés", blank=True, help_text="Un point par ligne."
    )
    technologies = models.CharField(
        max_length=255, help_text="Séparées par des virgules : Django, React, Docker"
    )
    categorie = models.CharField(max_length=20, choices=CATEGORIES, default="perso")
    statut = models.CharField(max_length=20, choices=STATUTS, default="termine")
    lien_demo = models.URLField("Lien du site déployé (Render, Netlify…)", blank=True)
    lien_code = models.URLField("Lien GitHub", blank=True)
    image_url = models.URLField(
        "Lien d'une capture d'écran (optionnel)", blank=True
    )
    icone = models.CharField(
        max_length=40, default="code-xml",
        help_text="Nom d'icône affichée si aucune capture n'est fournie (voir static/img/icons).",
    )
    en_vedette = models.BooleanField("Mettre en avant", default=False)
    visible = models.BooleanField(default=True)
    ordre = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["ordre", "-id"]
        verbose_name = "Projet"

    def __str__(self):
        return self.titre

    def liste_technos(self):
        return [t.strip() for t in self.technologies.split(",") if t.strip()]

    def liste_points(self):
        return [p.strip() for p in self.points_cles.splitlines() if p.strip()]


class Service(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    icone = models.CharField(
        max_length=40, default="code-xml", help_text="Nom d'icône (voir static/img/icons)."
    )
    ordre = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["ordre"]

    def __str__(self):
        return self.titre


class Parcours(models.Model):
    TYPES = [("experience", "Expérience"), ("formation", "Formation")]

    type = models.CharField(max_length=20, choices=TYPES)
    titre = models.CharField(max_length=150)
    organisation = models.CharField(max_length=150)
    periode = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    ordre = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["type", "ordre"]
        verbose_name = "Étape du parcours"
        verbose_name_plural = "Parcours"

    def __str__(self):
        return f"{self.titre} ({self.periode})"


class GroupeCompetences(models.Model):
    nom = models.CharField(max_length=80)
    competences = models.CharField(max_length=400, help_text="Séparées par des virgules")
    ordre = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["ordre"]
        verbose_name = "Groupe de compétences"
        verbose_name_plural = "Compétences"

    def __str__(self):
        return self.nom

    def liste(self):
        return [c.strip() for c in self.competences.split(",") if c.strip()]


class Message(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=150, blank=True)
    contenu = models.TextField("Message")
    recu_le = models.DateTimeField(auto_now_add=True)
    lu = models.BooleanField(default=False)

    class Meta:
        ordering = ["-recu_le"]
        verbose_name = "Message reçu"
        verbose_name_plural = "Messages reçus"

    def __str__(self):
        return f"{self.nom} : {self.sujet or 'sans sujet'}"

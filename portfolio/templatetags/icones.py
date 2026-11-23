"""
Icônes du site :
- {% icone "globe" %}      pictogramme Lucide (SVG intégré, prend la couleur du texte)
- {% logo_tech "Django" %} logo officiel de la technologie (Devicon), vide si inconnu
Les fichiers sont dans static/img/icons et static/img/tech.
"""
from functools import lru_cache

from django import template
from django.conf import settings
from django.templatetags.static import static
from django.utils.safestring import mark_safe

register = template.Library()

ICONS_DIR = settings.BASE_DIR / "static" / "img" / "icons"
TECH_DIR = settings.BASE_DIR / "static" / "img" / "tech"

# Nom affiché -> fichier de logo
TECH = {
    "django": "django",
    "react": "react", "react native (expo)": "react", "react native": "react",
    "expo": "expo", "laravel": "laravel", "laravel sanctum": "laravel", "filament": "laravel",
    "docker": "docker", "spring boot": "spring", "spring": "spring",
    "netlify": "netlify", "cloudflare r2": "cloudflare", "cloudflare": "cloudflare",
    "firebase": "firebase", "r": "r", "r (ggplot2)": "r", "flutter": "flutter",
    "sql server": "microsoftsqlserver", "postgresql": "postgresql", "neon": "postgresql",
    "mysql": "mysql", "mongodb": "mongodb", "python": "python", "javascript": "javascript",
    "php": "php", "java": "java", "vue.js": "vuejs", "bootstrap": "bootstrap",
    "git": "git", "github": "github", "html": "html5",
    "typescript": "typescript", "tailwind css": "tailwindcss", "redis": "redis",
}


@lru_cache(maxsize=None)
def _svg(nom):
    chemin = ICONS_DIR / f"{nom}.svg"
    if not chemin.exists():
        chemin = ICONS_DIR / "code-xml.svg"
    return chemin.read_text(encoding="utf-8")


@register.simple_tag
def icone(nom, classe=""):
    svg = _svg(nom or "code-xml")
    svg = svg.replace('class="lucide', f'aria-hidden="true" class="icon {classe} lucide', 1)
    return mark_safe(svg)


@register.simple_tag
def logos_uniques(technos, maximum=6):
    """Liste (nom, url) des logos d'un projet, sans doublons."""
    vus, res = set(), []
    for t in technos:
        url = logo_tech(t)
        if url and url not in vus:
            vus.add(url)
            res.append((t, url))
    return res[:maximum]


@register.simple_tag
def logo_tech(nom):
    fichier = TECH.get((nom or "").strip().lower())
    if fichier and (TECH_DIR / f"{fichier}.svg").exists():
        return static(f"img/tech/{fichier}.svg")
    return ""

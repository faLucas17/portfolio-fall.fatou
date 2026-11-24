from django.urls import path

from . import views

urlpatterns = [
    path("", views.accueil, name="accueil"),
    path("projets/", views.projets, name="projets"),
    path("experience/bakeli/", views.bakeli, name="bakeli"),
    path("formations/", views.formations, name="formations"),
]

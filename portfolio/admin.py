from django.contrib import admin

from .models import GroupeCompetences, Message, Parcours, Profil, Projet, Service


@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not Profil.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ("titre", "categorie", "statut", "lien_demo", "en_vedette", "visible", "ordre")
    list_editable = ("statut", "lien_demo", "en_vedette", "visible", "ordre")
    list_filter = ("categorie", "statut", "visible")
    search_fields = ("titre", "technologies")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("titre", "ordre")
    list_editable = ("ordre",)


@admin.register(Parcours)
class ParcoursAdmin(admin.ModelAdmin):
    list_display = ("titre", "organisation", "type", "periode", "ordre")
    list_editable = ("ordre",)
    list_filter = ("type",)


@admin.register(GroupeCompetences)
class GroupeCompetencesAdmin(admin.ModelAdmin):
    list_display = ("nom", "competences", "ordre")
    list_editable = ("ordre",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("nom", "email", "sujet", "recu_le", "lu")
    list_editable = ("lu",)
    list_filter = ("lu",)
    readonly_fields = ("nom", "email", "sujet", "contenu", "recu_le")

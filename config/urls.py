from django.conf import settings
from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "Portfolio de Fatou FALL"
admin.site.site_title = "Portfolio Fatou FALL"
admin.site.index_title = "Gérer mon portfolio"

urlpatterns = [
    path(settings.ADMIN_PATH, admin.site.urls),
    path("", include("portfolio.urls")),
]

from django.db.utils import DatabaseError

from .models import Profil


def profil(request):
    try:
        return {"profil": Profil.get()}
    except DatabaseError:
        return {"profil": None}

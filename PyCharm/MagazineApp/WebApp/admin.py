from django.contrib import admin
from .models import Magazyn


# Register your models here.
@admin.register(Magazyn)
class AllEntiryAdmin(admin.ModelAdmin):
    list_display = ("idMagazynu", "idMagazynu")

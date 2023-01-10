from django.contrib import admin
from .models import Magazyn, Produkt, Opakowanie, Dokument

# https://docs.djangoproject.com/en/4.1/topics/db/queries/
# https://books.agiliq.com/projects/django-admin-cookbook/en/latest/database_view.html
# Register your models here.
@admin.register(Magazyn)
class AdmMag (admin.ModelAdmin):
    display = ("idMagazynu")

@admin.register(Produkt)
class AdmPro (admin.ModelAdmin):
    list_display = ("nazwaProduktu", "cenaBrutto")

@admin.register(Opakowanie)
class AdmOpa (admin.ModelAdmin):
    list_display = ("idPudelka", "towar", "magazyn")

@admin.register(Dokument)
class AdmWyd (admin.ModelAdmin):
    list_display = ("NrDokumentu", "sumaBrutto", "sumaNetto", "typ")

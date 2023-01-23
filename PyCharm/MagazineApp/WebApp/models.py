from django.db import models
from datetime import date

# Create your models here.

# https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_one/
# https://docs.djangoproject.com/en/4.1/topics/db/models/

VAT_CHOICES = [
    ('A', '23%'),
    ('B', '5%'),
    ('C', '0%'),
    ('D', 'Nie dotyczy'),
]
TYPE_OF_ILOSC = [
    ('KG', 'kg'),
    ('SZT', 'szt.'),
]


class Produkt(models.Model):
    nazwaProduktu = models.CharField(max_length=20, default=' ', primary_key=True)
    cenaBrutto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cenaNetto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stawkaVat = models.CharField(max_length=5, choices=VAT_CHOICES, default=' ')
    typIlosci = models.CharField(max_length=5, choices=TYPE_OF_ILOSC, default=' ')

    def __str__(self):
        return self.nazwaProduktu

    class Meta:
        # https://docs.djangoproject.com/en/4.1/ref/models/options/#verbose-name
        verbose_name_plural = "Produkty"


class Magazyn(models.Model):
    idMagazynu = models.CharField(max_length=20, default=' ', primary_key=True)

    def __str__(self):
        return self.idMagazynu

    class Meta:
        verbose_name_plural = "Magazyny"


class Opakowanie(models.Model):
    idPudelka = models.CharField(max_length=20, default=' ', primary_key=True)
    iloscProduktu = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    towar = models.ForeignKey(Produkt, on_delete=models.RESTRICT, default=0)
    magazyn = models.ForeignKey(Magazyn, on_delete=models.RESTRICT, default=0)

    def __str__(self):
        return self.idPudelka

    class Meta:
        verbose_name_plural = "Opakowania"


TYPE_OF_DOCUMENT = [
    ('Dostawa', 'Dostawa'),
    ('Wydanie', 'Wydanie'),
]
class Dokument(models.Model):
    NrDokumentu = models.IntegerField(primary_key=True)
    sumaBrutto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sumaNetto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    typ = models.CharField(max_length=10, choices=TYPE_OF_DOCUMENT, default=' ')
    data = models.DateField(default=date.today)

    #dodac zagubioną listę towarów i przeliczanie cen

    def __str__(self):
        return str(self.NrDokumentu)

    class Meta:
        # https://docs.djangoproject.com/en/4.1/ref/models/options/#verbose-name
        verbose_name_plural = "Dokumenty"
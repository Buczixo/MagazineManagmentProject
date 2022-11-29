from django.db import models

# Create your models here.


VAT_CHOICES = [
    ('A', '23%'),
    ('B', '5%'),
    ('C', '0%'),
    ('d', 'Nie dotyczy'),
]


class Produkt(models.Model):
    nazwaProduktu = models.CharField(max_length=20, default=' ')
    cenaBrutto = models.DecimalField(max_digits=10, decimal_places=2)
    cenaNetto = models.DecimalField(max_digits=10, decimal_places=2)
    stawkaVat = models.CharField(max_length=3, choices=VAT_CHOICES, default=' ')
    typIlosci = models.CharField(max_length=20, default=' ')

    def __str__(self):
        return self.nazwaProduktu


class Opakowanie(Produkt):
    idPudelka = models.IntegerField(default=0)
    iloscProduktu = models.DecimalField(max_digits=10, decimal_places=2)


class Magazyn(Opakowanie):
    idMagazynu = models.IntegerField(default=0)

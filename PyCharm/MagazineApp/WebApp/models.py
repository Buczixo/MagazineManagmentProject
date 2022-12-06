from django.db import models

# Create your models here.

# https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_one/

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
    cenaBrutto = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    cenaNetto = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    stawkaVat = models.CharField(max_length=5, choices=VAT_CHOICES, default=' ')
    typIlosci = models.CharField(max_length=5, choices=TYPE_OF_ILOSC, default=' ')

    def __str__(self):
        return self.nazwaProduktu


class Opakowanie(models.Model):
    idPudelka = models.IntegerField(default=0, primary_key=True)
    iloscProduktu = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    towar = models.ForeignKey(Produkt, on_delete=models.RESTRICT)

    def __str__(self):
        return self.idPudelka


class Magazyn(models.Model):
    idMagazynu = models.IntegerField(default=0, primary_key=True)
    nrOpakowania = models.ForeignKey(Opakowanie, on_delete=models.RESTRICT)

    def __str__(self):
        return self.idMagazynu

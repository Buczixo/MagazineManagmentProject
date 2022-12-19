# Generated by Django 4.1.2 on 2022-12-06 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produkt',
            fields=[
                ('nazwaProduktu', models.CharField(default=' ', max_length=20, primary_key=True, serialize=False)),
                ('cenaBrutto', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('cenaNetto', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('stawkaVat', models.CharField(choices=[('A', '23%'), ('B', '5%'), ('C', '0%'), ('D', 'Nie dotyczy')], default=' ', max_length=5)),
                ('typIlosci', models.CharField(choices=[('KG', 'kg'), ('SZT', 'szt.')], default=' ', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Opakowanie',
            fields=[
                ('idPudelka', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('iloscProduktu', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('towar', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='WebApp.produkt')),
            ],
        ),
        migrations.CreateModel(
            name='Magazyn',
            fields=[
                ('idMagazynu', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('nrOpakowania', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='WebApp.opakowanie')),
            ],
        ),
    ]
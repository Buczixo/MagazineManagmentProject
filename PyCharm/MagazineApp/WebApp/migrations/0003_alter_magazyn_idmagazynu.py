# Generated by Django 4.1.4 on 2022-12-13 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0002_remove_magazyn_nropakowania_opakowanie_magazyn_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazyn',
            name='idMagazynu',
            field=models.CharField(default=' ', max_length=20, primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-13 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0003_alter_magazyn_idmagazynu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opakowanie',
            name='idPudelka',
            field=models.CharField(default=' ', max_length=20, primary_key=True, serialize=False),
        ),
    ]

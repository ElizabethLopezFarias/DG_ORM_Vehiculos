# Generated by Django 4.2 on 2024-05-31 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desafio_vehiculos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]

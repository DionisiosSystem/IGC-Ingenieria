# Generated by Django 3.1 on 2020-11-22 02:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0006_auto_20201102_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='Fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 21, 23, 37, 31, 861974)),
        ),
        migrations.AlterField(
            model_name='listaprecio',
            name='Actualizacion',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 21, 23, 37, 31, 862971)),
        ),
    ]

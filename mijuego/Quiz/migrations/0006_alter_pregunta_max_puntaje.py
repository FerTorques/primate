# Generated by Django 3.2.4 on 2021-09-01 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0005_alter_preguntasrespondidas_respuesta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='max_puntaje',
            field=models.DecimalField(decimal_places=0, default=130, max_digits=6, verbose_name='Maximo Puntaje'),
        ),
    ]

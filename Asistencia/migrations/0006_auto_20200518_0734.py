# Generated by Django 3.0.5 on 2020-05-18 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencia', '0005_auto_20200517_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materias',
            name='nom_mat',
            field=models.CharField(max_length=80, verbose_name='Nombre de la Materia'),
        ),
    ]

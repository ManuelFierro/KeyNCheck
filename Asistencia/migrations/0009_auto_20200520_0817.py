# Generated by Django 3.0.5 on 2020-05-20 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencia', '0008_auto_20200519_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnos',
            name='semestre',
            field=models.IntegerField(default=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='materias',
            name='semestre',
            field=models.IntegerField(default=7, verbose_name='Clave de la Materia'),
            preserve_default=False,
        ),
    ]

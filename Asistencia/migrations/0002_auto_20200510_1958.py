# Generated by Django 3.0.5 on 2020-05-11 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistencia',
            name='num_control',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asistencia.Alumnos'),
        ),
    ]
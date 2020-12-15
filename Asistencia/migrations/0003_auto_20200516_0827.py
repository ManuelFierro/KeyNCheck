# Generated by Django 3.0.5 on 2020-05-16 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencia', '0002_auto_20200510_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='nom_alu',
            field=models.CharField(max_length=30, verbose_name='Nombre del Alumno'),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='num_control',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='Número de Control'),
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='clave_matA',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asistencia.Materias', verbose_name='Datos de la materia'),
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='fecha',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='num_control',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asistencia.Alumnos', verbose_name='Número de Control/Nombre'),
        ),
        migrations.AlterField(
            model_name='docentes',
            name='clave_mae',
            field=models.CharField(max_length=3, primary_key=True, serialize=False, verbose_name='Clave del Maestro'),
        ),
        migrations.AlterField(
            model_name='docentes',
            name='nomb_mae',
            field=models.CharField(max_length=30, verbose_name='Nombre del Maestro'),
        ),
        migrations.AlterField(
            model_name='materias',
            name='clave_mae',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asistencia.Docentes', verbose_name='Datos del Maestro'),
        ),
        migrations.AlterField(
            model_name='materias',
            name='clave_mat',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='Clave de la Materia'),
        ),
        migrations.AlterField(
            model_name='materias',
            name='nom_mat',
            field=models.CharField(max_length=40, verbose_name='Nombre de la Materia'),
        ),
    ]

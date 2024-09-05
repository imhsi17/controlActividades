# Generated by Django 5.1 on 2024-09-02 05:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_empresa', models.CharField(max_length=150, verbose_name='Nombre')),
                ('ruc', models.CharField(max_length=11, verbose_name='RUC')),
                ('direccion', models.CharField(max_length=250, verbose_name='Dirección')),
                ('correo_empresa', models.CharField(max_length=150, verbose_name='Correo')),
                ('rubro', models.CharField(blank=True, max_length=150, verbose_name='Rubro')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=75, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
            },
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_trabajador', models.CharField(max_length=250, verbose_name='Nombre Completo')),
                ('celular', models.CharField(blank=True, max_length=9, verbose_name='Número Celular')),
                ('correo_trabajador', models.CharField(blank=True, max_length=150, verbose_name='Coreo')),
                ('especialidad', models.CharField(max_length=150, verbose_name='Especialidad')),
            ],
            options={
                'verbose_name': 'Trabajador',
                'verbose_name_plural': 'Trabajadores',
            },
        ),
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_actividad', models.CharField(max_length=150, verbose_name='Actividad')),
                ('tiempo_establecido_actividad', models.IntegerField(verbose_name='Tiempo Establecido')),
                ('estado_actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlWeb.estado')),
            ],
            options={
                'verbose_name': 'Actividad',
                'verbose_name_plural': 'Actividades',
            },
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tarea', models.CharField(max_length=150, verbose_name='Nombre')),
                ('descripcion_tarea', models.TextField(verbose_name='Descripción')),
                ('tiempo_establecido_tarea', models.IntegerField(verbose_name='Tiempo Establecido')),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlWeb.actividad')),
                ('estado_tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlWeb.estado')),
            ],
            options={
                'verbose_name': 'Tarea',
                'verbose_name_plural': 'Tareas',
            },
        ),
        migrations.CreateModel(
            name='Jornada',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_realizada', models.DateField(verbose_name='Fecha Realizada')),
                ('hora_inicio', models.TimeField(verbose_name='Hora Inicio')),
                ('hora_final', models.TimeField(verbose_name='Hora Fin')),
                ('comentario', models.TextField(verbose_name='Comentario')),
                ('progreso', models.IntegerField(verbose_name='Progreso')),
                ('tiempo_empleado', models.TimeField(verbose_name='Tiempo Empleado')),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlWeb.tarea')),
                ('trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlWeb.trabajador')),
            ],
            options={
                'verbose_name': 'Jornada',
                'verbose_name_plural': 'Jornadas',
            },
        ),
    ]

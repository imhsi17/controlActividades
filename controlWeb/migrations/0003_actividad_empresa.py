# Generated by Django 5.1 on 2024-09-04 04:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlWeb', '0002_alter_jornada_trabajador_delete_trabajador'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='controlWeb.empresa'),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.1 on 2024-08-17 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_publicacion_archivos_publicacion_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='models.usuario'),
        ),
    ]
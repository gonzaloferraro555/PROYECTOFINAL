# Generated by Django 4.1 on 2022-10-26 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0008_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='NombreYApellido',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='email',
        ),
        migrations.AddField(
            model_name='comentario',
            name='us',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='receta',
            name='ingrediente',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]

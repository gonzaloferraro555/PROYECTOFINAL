# Generated by Django 4.1 on 2022-10-27 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0013_comentario_nivel'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta_amateur',
            name='us',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-03 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prestadores', '0003_detallesede_es_usada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sedesprestador',
            name='dv',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
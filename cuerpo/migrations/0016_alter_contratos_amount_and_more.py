# Generated by Django 4.2.4 on 2023-09-20 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuerpo', '0015_contratos_lanzamiento_licitacion_planificacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contratos',
            name='amount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='contratos',
            name='contractPeriod_endDate',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='contratos',
            name='contractPeriod_starDate',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='contratos',
            name='dateSigned',
            field=models.CharField(max_length=60, null=True),
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-21 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuerpo', '0024_alter_premios_contractperiod_endtdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premios',
            name='contractPeriod_endtDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='premios',
            name='contractPeriod_startDate',
            field=models.DateTimeField(null=True),
        ),
    ]
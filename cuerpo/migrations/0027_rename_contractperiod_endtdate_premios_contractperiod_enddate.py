# Generated by Django 4.2.4 on 2023-09-21 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuerpo', '0026_rename_contractperiod_stardate_contratos_contractperiod_startdate_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='premios',
            old_name='contractPeriod_endtDate',
            new_name='contractPeriod_endDate',
        ),
    ]

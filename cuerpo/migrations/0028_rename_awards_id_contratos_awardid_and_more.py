# Generated by Django 4.2.4 on 2023-09-21 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuerpo', '0027_rename_contractperiod_endtdate_premios_contractperiod_enddate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contratos',
            old_name='awards_ID',
            new_name='awardID',
        ),
        migrations.AlterField(
            model_name='premios',
            name='contractPeriod_endDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='premios',
            name='contractPeriod_startDate',
            field=models.DateTimeField(null=True),
        ),
    ]

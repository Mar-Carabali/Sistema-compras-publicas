# Generated by Django 4.2.4 on 2023-09-24 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuerpo', '0032_rename_awardperiod_enddate_licitacion_awardperiod_enddate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licitacion',
            name='tenderPeriod_endDate',
            field=models.DateTimeField(null=True),
        ),
    ]
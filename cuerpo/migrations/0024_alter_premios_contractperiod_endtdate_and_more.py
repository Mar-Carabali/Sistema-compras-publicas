# Generated by Django 4.2.4 on 2023-09-20 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuerpo', '0023_alter_licitacion_enquiryperiod_enddate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premios',
            name='contractPeriod_endtDate',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='premios',
            name='contractPeriod_startDate',
            field=models.CharField(max_length=600, null=True),
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-20 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuerpo', '0019_alter_premios_contractperiod_endtdate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lanzamiento',
            name='budget_name',
        ),
        migrations.AddField(
            model_name='lanzamiento',
            name='buyer_name',
            field=models.CharField(max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='lanzamiento',
            name='date',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='planificacion',
            name='budget_id',
            field=models.CharField(max_length=800, null=True),
        ),
    ]

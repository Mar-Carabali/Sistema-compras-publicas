# Generated by Django 4.2.4 on 2023-09-20 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuerpo', '0021_rename_awards_id_provedores_award_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provedores',
            name='name',
            field=models.CharField(max_length=600, null=True),
        ),
    ]

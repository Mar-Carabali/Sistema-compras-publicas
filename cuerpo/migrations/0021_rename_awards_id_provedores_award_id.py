# Generated by Django 4.2.4 on 2023-09-20 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuerpo', '0020_remove_lanzamiento_budget_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='provedores',
            old_name='awards_id',
            new_name='award_id',
        ),
    ]

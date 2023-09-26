# Generated by Django 4.2.4 on 2023-09-13 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuerpo', '0002_awards_csv_delete_filedata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awards',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='awards',
            name='description',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='awards',
            name='id',
            field=models.CharField(max_length=600, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='awards',
            name='ocid',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='awards',
            name='release_id',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='awards',
            name='status',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='awards',
            name='title',
            field=models.CharField(max_length=600),
        ),
    ]

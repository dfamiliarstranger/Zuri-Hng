# Generated by Django 4.2.5 on 2023-09-17 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
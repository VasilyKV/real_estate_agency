# Generated by Django 3.2.13 on 2022-07-22 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20190829_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(blank=True, null=True, verbose_name='Новостройка'),
        ),
    ]
# Generated by Django 3.2.13 on 2022-09-04 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0026_auto_20220904_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='name',
            field=models.CharField(blank=True, db_index=True, max_length=200, verbose_name='ФИО владельца'),
        ),
    ]

# Generated by Django 3.2.13 on 2022-07-25 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0019_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='owners_flats',
            field=models.ManyToManyField(related_name='flat_owners', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
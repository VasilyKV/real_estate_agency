# Generated by Django 3.2.13 on 2022-07-25 10:51

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.AlterField(
            model_name='flat',
            name='owners_phonenumber',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Нормализованный номер владельца'),
        ),
    ]
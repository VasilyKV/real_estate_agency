# Generated by Django 3.2.13 on 2022-08-28 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0020_alter_owner_owners_flats'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owners_flats',
            new_name='flats',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owner',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owners_phonenumber',
            new_name='phonenumber',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owner_pure_phone',
            new_name='pure_phone',
        ),
    ]

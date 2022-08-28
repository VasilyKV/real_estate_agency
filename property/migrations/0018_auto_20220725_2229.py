# Generated by Django 3.2.13 on 2022-07-25 18:29

from django.db import migrations
import phonenumbers

def get_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        parsed_phone = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(parsed_phone):
            flat.owner_pure_phone = f'+{parsed_phone.country_code}{parsed_phone.national_number}'
            flat.save()

def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.all()
    for flat in Flat.objects.all():
        flat.owner_pure_phone = None
        flat.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_alter_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(get_pure_phone),
    ]
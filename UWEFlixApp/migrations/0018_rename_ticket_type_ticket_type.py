# Generated by Django 4.1.6 on 2023-04-24 16:52
# Edited by hand with love by Josh a short time after <3

import django
from django.db import migrations, models
from django.utils.text import slugify


def populate_tickets(apps, schema_editor):
    Ticket = apps.get_model('UWEFlixApp', 'Ticket')
    Ticket.objects.bulk_create([
        Ticket(type='adult', price='4.99'),
        Ticket(type='child', price='2.99'),
        Ticket(type='student', price='3.99'),
    ])

class Migration(migrations.Migration):

    dependencies = [
        ('UWEFlixApp', '0017_remove_screening_seats_remaining_and_more'),
    ]

    operations = [
        migrations.DeleteModel('Ticket'),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.SlugField(unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(limit_value=0)])),
            ],
        ),
        migrations.RunPython(populate_tickets, lambda a, s: None), # no action required for backwards migrate
    ]
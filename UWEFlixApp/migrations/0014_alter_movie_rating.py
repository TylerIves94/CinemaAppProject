# Generated by Django 4.1.6 on 2023-04-22 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UWEFlixApp', '0013_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.CharField(choices=[('E', 'E'), ('U', 'U'), ('PG', 'PG'), ('12A', '12A'), ('15', '15'), ('18', '18')], default='E', max_length=3),
        ),
    ]

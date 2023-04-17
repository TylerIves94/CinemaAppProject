# Generated by Django 4.1.6 on 2023-04-17 15:18

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UWEFlixApp', '0010_rename_minutes_long_movie_running_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='running_time',
            field=models.DurationField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.timedelta(seconds=60))]),
        ),
    ]

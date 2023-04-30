# Generated by Django 4.1.6 on 2023-04-30 20:04

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('card_number', models.CharField(max_length=128)),
                ('card_expiry', models.DateField()),
                ('discount_rate', models.DecimalField(decimal_places=2, max_digits=4, validators=[django.core.validators.MinValueValidator(limit_value=0)])),
                ('address', models.CharField(max_length=500)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('running_time', models.DurationField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.timedelta(seconds=60))])),
                ('description', models.TextField()),
                ('rating', models.CharField(choices=[('E', 'E'), ('U', 'U'), ('PG', 'PG'), ('12A', '12A'), ('15', '15'), ('18', '18')], default='E', max_length=3)),
                ('image', models.ImageField(blank=True, default='images/no_image_available.png', null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('description', models.TextField(blank=True)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.SlugField(unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(limit_value=0)])),
            ],
        ),
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('showing_at', models.DateTimeField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UWEFlixApp.movie')),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UWEFlixApp.screen')),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyStatement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UWEFlixApp.club')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_adult_tickets', models.IntegerField()),
                ('number_of_child_tickets', models.IntegerField()),
                ('number_of_student_tickets', models.IntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(limit_value=0)])),
                ('date', models.DateTimeField(auto_now=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Cancellation Requested', 'Cancellation Requested'), ('Cancelled', 'Cancelled')], default='Active', max_length=25)),
                ('club', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UWEFlixApp.club')),
                ('screening', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UWEFlixApp.screening')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

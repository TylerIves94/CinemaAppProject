# Generated by Django 4.1.6 on 2023-03-03 11:47

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


# tuple of "special" Group names to be used for Roles
ROLE_GROUPS = (
    'Cinema Manager',
    'Account Manager',
    'Club Representative',
    'Customer',
)

def create_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')  # django.contrib.auth.models.Group
    Group.objects.bulk_create(Group(name=n) for n in ROLE_GROUPS)

def delete_groups(apps, schema_editor):
    """
    Reverse migration in case anyone ever needs to undo this one for some reason
    """
    Group = apps.get_model('auth', 'Group')  # django.contrib.auth.models.Group
    Group.objects.filter(name__in=ROLE_GROUPS).delete()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('card_number', models.CharField(max_length=16)),
                ('card_expiry', models.DateField()),
                ('discount_rate', models.DecimalField(decimal_places=2, max_digits=4)),
                ('address', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('minutes_long', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(limit_value=1)])),
                ('description', models.TextField()),
                ('rating', models.CharField(max_length=3)),
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
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('M', 'Cinema Manager'), ('A', 'Account Manager'), ('R', 'Club Representative'), ('C', 'Customer')], default='C', max_length=1)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('showing_at', models.DateTimeField()),
                ('seats_remaining', models.IntegerField()),
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
                ('number_of_tickets', models.IntegerField()),
                ('num_total', models.IntegerField()),
                ('screening', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UWEFlixApp.screening')),
            ],
        ),
        migrations.RunPython(create_groups, delete_groups),
    ]

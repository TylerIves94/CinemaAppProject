# Generated by Django 4.1.7 on 2023-04-17 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("UWEFlixApp", "0009_alter_user_options_user_club_alter_user_role_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
    ]

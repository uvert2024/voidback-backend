# Generated by Django 5.1.1 on 2024-11-25 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("voidbackApi", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="ban_exp",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="account",
            name="is_banned",
            field=models.BooleanField(blank=True, default=False),
        ),
    ]

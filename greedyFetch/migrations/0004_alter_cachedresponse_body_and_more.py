# Generated by Django 5.1.1 on 2024-11-18 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("greedyFetch", "0003_alter_cachedresponse_body_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cachedresponse",
            name="body",
            field=models.JSONField(blank=True, default={}),
        ),
        migrations.AlterField(
            model_name="cachedresponse",
            name="headers",
            field=models.JSONField(blank=True, default={}),
        ),
    ]

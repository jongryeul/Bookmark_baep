# Generated by Django 5.0.2 on 2024-02-17 02:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("bookmark", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="bookmark",
            old_name="urllib",
            new_name="url",
        ),
    ]
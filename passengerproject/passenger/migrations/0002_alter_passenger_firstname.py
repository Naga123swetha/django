# Generated by Django 5.0.6 on 2025-03-06 12:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("passenger", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="passenger",
            name="firstname",
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]

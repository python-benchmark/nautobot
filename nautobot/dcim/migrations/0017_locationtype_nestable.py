# Generated by Django 3.2.15 on 2022-10-13 16:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dcim", "0016_device_components__timestamp_data_migration"),
    ]

    operations = [
        migrations.AddField(
            model_name="locationtype",
            name="nestable",
            field=models.BooleanField(default=False),
        ),
    ]
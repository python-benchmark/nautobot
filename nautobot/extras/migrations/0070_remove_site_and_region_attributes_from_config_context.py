# Generated by Django 3.2.16 on 2023-02-01 17:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("dcim", "0034_migrate_region_and_site_data_to_locations"),
        ("extras", "0069_created_datetime"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="configcontext",
            name="regions",
        ),
        migrations.RemoveField(
            model_name="configcontext",
            name="sites",
        ),
    ]

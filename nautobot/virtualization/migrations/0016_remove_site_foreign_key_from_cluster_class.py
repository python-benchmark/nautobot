# Generated by Django 3.2.16 on 2023-01-31 16:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("dcim", "0034_migrate_region_and_site_data_to_locations"),
        ("virtualization", "0015_rename_foreignkey_fields"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cluster",
            name="site",
        ),
    ]

# Generated by Django 3.2.18 on 2023-06-06 21:12

from django.db import migrations, models

from nautobot.core.utils.migrations import check_for_duplicates_with_natural_key_fields_in_migration


def ensure_virtual_chassis_names_are_all_unique(apps, schema_editor):
    VirtualChassis = apps.get_model("dcim", "VirtualChassis")
    check_for_duplicates_with_natural_key_fields_in_migration(VirtualChassis, ["name"])


class Migration(migrations.Migration):
    dependencies = [
        ("dcim", "0047_status_nonnullable"),
    ]

    operations = [
        migrations.RunPython(ensure_virtual_chassis_names_are_all_unique, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="virtualchassis",
            name="name",
            field=models.CharField(max_length=64, unique=True),
        ),
    ]

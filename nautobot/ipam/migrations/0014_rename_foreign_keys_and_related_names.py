# Generated by Django 3.2.16 on 2023-01-11 15:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("ipam", "0013_delete_role"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="vlan",
            options={"ordering": ("site", "vlan_group", "vid"), "verbose_name": "VLAN", "verbose_name_plural": "VLANs"},
        ),
        migrations.RenameField(
            model_name="service",
            old_name="ipaddresses",
            new_name="ip_addresses",
        ),
        migrations.RenameField(
            model_name="vlan",
            old_name="group",
            new_name="vlan_group",
        ),
        migrations.AlterUniqueTogether(
            name="vlan",
            unique_together={("vlan_group", "vid"), ("vlan_group", "name")},
        ),
    ]

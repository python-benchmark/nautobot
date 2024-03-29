# Generated by Django 3.2.18 on 2023-03-14 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("ipam", "0026_ipaddress_remove_assigned_object"),
        ("dcim", "0044_tagsfield"),
    ]

    operations = [
        migrations.AddField(
            model_name="interface",
            name="vrf",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="interfaces",
                to="ipam.vrf",
            ),
        ),
    ]

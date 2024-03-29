# Generated by Django 3.2.18 on 2023-06-12 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("dcim", "0048_ensure_virtual_chassis_names_are_unique_and_add_uniqueness_constraint"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="location",
            name="slug",
        ),
        migrations.RemoveField(
            model_name="locationtype",
            name="slug",
        ),
        migrations.AlterUniqueTogether(
            name="devicetype",
            unique_together={("manufacturer", "model")},
        ),
        migrations.AlterUniqueTogether(
            name="rackgroup",
            unique_together={("location", "name")},
        ),
        migrations.RemoveField(
            model_name="devicetype",
            name="slug",
        ),
        migrations.RemoveField(
            model_name="rackgroup",
            name="slug",
        ),
        migrations.AlterField(
            model_name="device",
            name="primary_ip4",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="primary_ip4_for",
                to="ipam.ipaddress",
            ),
        ),
        migrations.AlterField(
            model_name="device",
            name="primary_ip6",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="primary_ip6_for",
                to="ipam.ipaddress",
            ),
        ),
    ]

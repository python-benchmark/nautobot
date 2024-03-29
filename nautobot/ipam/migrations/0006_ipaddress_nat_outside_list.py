# Generated by Django 3.1.14 on 2022-02-28 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("ipam", "0005_auto_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ipaddress",
            name="nat_inside",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="nat_outside_list",
                to="ipam.ipaddress",
            ),
        ),
    ]

# Generated by Django 3.2.13 on 2022-06-15 14:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dcim", "0013_location_location_type"),
        ("extras", "0037_configcontextschema__remove_name_unique__create_constraint_unique_name_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="configcontext",
            name="locations",
            field=models.ManyToManyField(
                blank=True, related_name="_extras_configcontext_locations_+", to="dcim.Location"
            ),
        ),
    ]

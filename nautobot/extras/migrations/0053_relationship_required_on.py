# Generated by Django 3.2.16 on 2022-11-04 20:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("extras", "0052_configcontext_device_redundancy_groups"),
    ]

    operations = [
        migrations.AddField(
            model_name="relationship",
            name="required_on",
            field=models.CharField(blank=True, default="", max_length=12),
        ),
    ]

# Generated by Django 3.2.13 on 2022-06-01 14:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("extras", "0036_job_add_has_sensitive_variables"),
    ]

    operations = [
        migrations.AlterField(
            model_name="configcontextschema",
            name="name",
            field=models.CharField(max_length=200),
        ),
        migrations.AddConstraint(
            model_name="configcontextschema",
            constraint=models.UniqueConstraint(
                fields=("name", "owner_content_type", "owner_object_id"), name="unique_name_owner"
            ),
        ),
    ]

# Generated by Django 3.1.14 on 2022-03-19 23:21

from django.db import migrations, models

import nautobot.extras.utils


class Migration(migrations.Migration):
    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("extras", "0030_webhook_alter_unique_together"),
    ]

    operations = [
        migrations.AddField(
            model_name="tag",
            name="content_types",
            field=models.ManyToManyField(
                limit_choices_to=nautobot.extras.utils.TaggableClassesQuery(),
                related_name="tags",
                to="contenttypes.ContentType",
            ),
        ),
    ]
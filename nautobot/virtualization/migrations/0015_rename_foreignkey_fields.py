# Generated by Django 3.2.16 on 2023-01-12 15:41

from django.db import migrations, models
import django.db.models.deletion

import nautobot.extras.utils


class Migration(migrations.Migration):
    dependencies = [
        ("extras", "0066_rename_configcontext_role"),
        ("contenttypes", "0002_remove_content_type_name"),
        ("virtualization", "0014_rename_virtualmachine_roles"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cluster",
            old_name="group",
            new_name="cluster_group",
        ),
        migrations.RenameField(
            model_name="cluster",
            old_name="type",
            new_name="cluster_type",
        ),
        migrations.RenameField(
            model_name="virtualmachine",
            old_name="local_context_data",
            new_name="local_config_context_data",
        ),
        migrations.RenameField(
            model_name="virtualmachine",
            old_name="local_context_data_owner_object_id",
            new_name="local_config_context_data_owner_object_id",
        ),
        migrations.RenameField(
            model_name="virtualmachine",
            old_name="local_context_data_owner_content_type",
            new_name="local_config_context_data_owner_content_type",
        ),
        migrations.RenameField(
            model_name="virtualmachine",
            old_name="local_context_schema",
            new_name="local_config_context_schema",
        ),
        migrations.AlterField(
            model_name="virtualmachine",
            name="local_config_context_data_owner_content_type",
            field=models.ForeignKey(
                blank=True,
                default=None,
                limit_choices_to=nautobot.extras.utils.FeatureQuery("config_context_owners"),
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="virtualization_virtualmachine_related",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AlterField(
            model_name="virtualmachine",
            name="local_config_context_schema",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="virtualization_virtualmachine_related",
                to="extras.configcontextschema",
            ),
        ),
    ]

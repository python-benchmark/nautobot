# Generated by Django 3.2.18 on 2023-05-17 19:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("extras", "0088_job__commit_default_data_migration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="joblogentry",
            name="log_level",
            field=models.CharField(db_index=True, default="info", max_length=32),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-21 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("templates", "0005_alter_templatetag_template"),
    ]

    operations = [
        migrations.AlterField(
            model_name="templatetag",
            name="Template",
            field=models.ForeignKey(
                db_column="template_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="templates.template",
            ),
        ),
    ]

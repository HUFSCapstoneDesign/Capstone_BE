# Generated by Django 4.2.1 on 2023-05-21 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("templates", "0002_rename_template_category_template_category_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="templatetag", name="introduce",),
        migrations.AddField(
            model_name="templatetag",
            name="Template",
            field=models.ForeignKey(
                db_column="template_id",
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="templates.template",
            ),
            preserve_default=False,
        ),
    ]

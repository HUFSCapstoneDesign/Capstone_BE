# Generated by Django 4.2.1 on 2023-05-29 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("templates", "0015_rename_back_color_text_backcolor_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="text", name="align", field=models.CharField(max_length=10),
        ),
    ]

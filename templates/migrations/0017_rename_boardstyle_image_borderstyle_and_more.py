# Generated by Django 4.2.1 on 2023-05-31 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("templates", "0016_alter_text_align"),
    ]

    operations = [
        migrations.RenameField(
            model_name="image", old_name="boardstyle", new_name="borderstyle",
        ),
        migrations.RenameField(
            model_name="image", old_name="radis", new_name="radius",
        ),
    ]

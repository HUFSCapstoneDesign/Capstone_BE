# Generated by Django 4.2.1 on 2023-05-27 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("templates", "0013_rename_radius_image_invert_rename_pont_text_font_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="image", old_name="border_color", new_name="boardstyle",
        ),
        migrations.RenameField(
            model_name="image", old_name="border_style", new_name="bordercolor",
        ),
        migrations.RenameField(
            model_name="image", old_name="border_size", new_name="bordersize",
        ),
        migrations.RenameField(
            model_name="image", old_name="gray_scale", new_name="grayscale",
        ),
        migrations.RenameField(
            model_name="member", old_name="nick_name", new_name="nickname",
        ),
        migrations.RenameField(
            model_name="template", old_name="template_category", new_name="category",
        ),
        migrations.RemoveField(model_name="text", name="cursive",),
    ]
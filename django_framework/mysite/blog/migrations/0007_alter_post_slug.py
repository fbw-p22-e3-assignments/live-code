# Generated by Django 4.2 on 2023-05-02 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_alter_comment_created_alter_post_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(
                max_length=200, unique_for_date="publish", verbose_name="Slug"
            ),
        ),
    ]

# Generated by Django 4.0.1 on 2022-02-17 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_category_alter_newsstory_options_newsstory_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]

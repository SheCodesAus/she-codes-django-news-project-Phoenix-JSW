# Generated by Django 4.0.1 on 2022-02-24 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_customuser_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Profile_img',
            new_name='profile_img',
        ),
    ]
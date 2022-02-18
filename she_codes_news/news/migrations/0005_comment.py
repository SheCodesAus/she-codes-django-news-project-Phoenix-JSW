# Generated by Django 4.0.1 on 2022-02-18 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0004_alter_newsstory_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='news.newsstory')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]
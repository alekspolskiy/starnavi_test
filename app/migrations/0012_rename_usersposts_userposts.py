# Generated by Django 3.2 on 2021-04-16 08:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0011_usersposts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UsersPosts',
            new_name='UserPosts',
        ),
    ]

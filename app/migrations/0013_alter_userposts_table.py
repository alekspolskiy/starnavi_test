# Generated by Django 3.2 on 2021-04-16 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_rename_usersposts_userposts'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='userposts',
            table='user_posts',
        ),
    ]
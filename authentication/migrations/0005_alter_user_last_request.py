# Generated by Django 3.2 on 2021-04-13 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_user_last_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_request',
            field=models.DateTimeField(null=True),
        ),
    ]

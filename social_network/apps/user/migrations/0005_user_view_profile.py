# Generated by Django 3.1.6 on 2021-02-27 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210227_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='View_profile',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 3.1.6 on 2021-03-01 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20210301_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='following',
            name='followed',
            field=models.ManyToManyField(related_name='follower', to='user.User'),
        ),
        migrations.AlterField(
            model_name='following',
            name='follower',
            field=models.ManyToManyField(related_name='followed', to='user.User'),
        ),
    ]

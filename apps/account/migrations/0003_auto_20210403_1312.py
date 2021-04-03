# Generated by Django 3.1.6 on 2021-04-03 08:42

import common.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210403_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, validators=[common.validators.mobile_length_validator, common.validators.mobile_validator]),
        ),
    ]
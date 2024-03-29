# Generated by Django 3.1.6 on 2021-04-03 08:39

import common.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, unique=True, validators=[common.validators.mobile_length_validator, common.validators.mobile_validator]),
        ),
    ]

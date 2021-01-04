# Generated by Django 3.1.3 on 2020-12-25 13:06

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('SH', '0011_auto_20201122_1818'),
    ]

    operations = [
        migrations.RenameField(
            model_name='espsensor',
            old_name='value',
            new_name='valueTemp',
        ),
        migrations.AddField(
            model_name='espsensor',
            name='valueAvgDay',
            field=models.CharField(blank=True, default='', max_length=24, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]),
        ),
        migrations.AddField(
            model_name='espsensor',
            name='valueAvgWeek',
            field=models.CharField(blank=True, default='', max_length=7, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]),
        ),
    ]

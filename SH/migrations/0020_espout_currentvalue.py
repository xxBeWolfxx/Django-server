# Generated by Django 3.1.3 on 2021-01-18 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SH', '0019_auto_20210116_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='espout',
            name='currentValue',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]

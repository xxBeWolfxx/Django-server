# Generated by Django 3.1.3 on 2021-01-16 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SH', '0017_espsensor_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='espsensor',
            name='valueTemp',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
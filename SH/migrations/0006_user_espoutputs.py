# Generated by Django 3.1.3 on 2020-11-22 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SH', '0005_auto_20201122_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ESPoutputs',
            field=models.ManyToManyField(blank=True, null=True, to='SH.ESPOut'),
        ),
    ]

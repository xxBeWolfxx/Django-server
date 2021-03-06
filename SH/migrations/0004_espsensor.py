# Generated by Django 3.1.3 on 2020-11-21 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SH', '0003_auto_20201121_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='ESPSensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='PIN', max_length=20)),
                ('pin', models.IntegerField(default=-1)),
                ('value', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]

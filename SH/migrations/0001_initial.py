# Generated by Django 3.1.3 on 2020-11-09 20:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ESPOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pins', models.CharField(max_length=30, validators=[django.core.validators.int_list_validator])),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('ESPmodulesIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SH.espout')),
            ],
        ),
    ]

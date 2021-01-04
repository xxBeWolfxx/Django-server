# Generated by Django 3.1.3 on 2020-11-21 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SH', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='espout',
            name='pins',
        ),
        migrations.AddField(
            model_name='espout',
            name='name',
            field=models.CharField(default='PIN', max_length=20),
        ),
        migrations.AddField(
            model_name='espout',
            name='pin',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='espout',
            name='statusOfPin',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
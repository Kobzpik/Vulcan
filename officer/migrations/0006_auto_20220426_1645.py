# Generated by Django 3.1.13 on 2022-04-26 11:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0005_auto_20220426_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accident',
            name='time',
            field=models.TimeField(default=datetime.datetime(2022, 4, 26, 16, 45, 24, 111511)),
        ),
        migrations.AlterField(
            model_name='fine',
            name='time',
            field=models.TimeField(default=datetime.datetime(2022, 4, 26, 16, 45, 24, 110619)),
        ),
    ]

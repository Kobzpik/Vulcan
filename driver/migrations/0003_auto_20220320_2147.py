# Generated by Django 3.1.13 on 2022-03-20 16:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0002_auto_20220320_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='time',
            field=models.TimeField(default=datetime.datetime(2022, 3, 20, 21, 47, 39, 782388)),
        ),
    ]

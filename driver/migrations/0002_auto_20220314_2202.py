# Generated by Django 3.1.13 on 2022-03-14 16:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='time',
            field=models.TimeField(default=datetime.datetime(2022, 3, 14, 22, 2, 48, 632831)),
        ),
    ]

# Generated by Django 3.1.13 on 2022-02-13 13:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0003_auto_20220213_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fine',
            name='time',
            field=models.TimeField(default=datetime.datetime(2022, 2, 13, 19, 10, 43, 169521)),
        ),
    ]

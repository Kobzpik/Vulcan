# Generated by Django 3.1.13 on 2022-01-20 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0002_auto_20220115_1700'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='Driver',
        ),
        migrations.RenameModel(
            old_name='Employee',
            new_name='Officer',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_customer',
            new_name='is_driver',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_employee',
            new_name='is_officer',
        ),
    ]
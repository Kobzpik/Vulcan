# Generated by Django 2.2.14 on 2021-12-31 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='list',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'beta',
            },
        ),
    ]
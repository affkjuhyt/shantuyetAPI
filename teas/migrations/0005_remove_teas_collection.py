# Generated by Django 3.0.8 on 2020-12-17 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teas', '0004_auto_20201217_0724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teas',
            name='collection',
        ),
    ]

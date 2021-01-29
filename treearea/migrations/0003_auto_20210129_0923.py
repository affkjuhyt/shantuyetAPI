# Generated by Django 3.0.8 on 2021-01-29 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('treearea', '0002_auto_20210129_0917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treearea',
            name='coordinate',
        ),
        migrations.AddField(
            model_name='coordinate',
            name='tree_area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='treearea.TreeArea'),
        ),
    ]
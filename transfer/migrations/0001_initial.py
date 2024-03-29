# Generated by Django 3.0.8 on 2021-01-25 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofile', '0001_initial'),
        ('teas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=1000, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('wait_owner_agree', 'Wait owner to agree'), ('government_agree', 'Wait government to agree'), ('approved', 'Approved'), ('reject', 'Reject')], default='wait_owner_agree', max_length=20)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='userprofile.Owner')),
                ('secondary_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secondary_owner', to='userprofile.SecondaryOwner')),
                ('tea', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teas.Teas')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

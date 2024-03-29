# Generated by Django 3.0.8 on 2021-01-25 06:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('fullname', models.CharField(max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=20)),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('processing', 'Processing'), ('approved', 'Approved'), ('reject', 'Reject')], default='processing', max_length=20)),
                ('user_type', models.CharField(choices=[('owner', 'Owner'), ('secondary_owner', 'SecondaryOwner'), ('government', 'Government')], default='secondary_owner', max_length=20)),
                ('id_card', models.CharField(blank=True, max_length=12, null=True)),
                ('permanent_residence', models.CharField(blank=True, max_length=2000, null=True)),
                ('issued_by', models.CharField(blank=True, max_length=1000, null=True)),
                ('issued_date', models.DateField(blank=True, null=True)),
                ('province', models.CharField(blank=True, max_length=500, null=True)),
                ('district', models.CharField(blank=True, max_length=500, null=True)),
                ('sub_district', models.CharField(blank=True, max_length=500, null=True)),
                ('street', models.CharField(blank=True, max_length=500, null=True)),
                ('front_view_photo', models.ImageField(blank=True, null=True, upload_to='userprofile/%Y/%m/%d')),
                ('back_view_photo', models.ImageField(blank=True, null=True, upload_to='userprofile/%Y/%m/%d')),
                ('image', models.ImageField(blank=True, null=True, upload_to='userprofile/%Y/%m/%d')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Government',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='userprofile.UserProfile')),
                ('is_enable', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('userprofile.userprofile',),
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='userprofile.UserProfile')),
                ('is_enable', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('userprofile.userprofile',),
        ),
        migrations.CreateModel(
            name='SecondaryOwner',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='userprofile.UserProfile')),
                ('is_enable', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('userprofile.userprofile',),
        ),
    ]

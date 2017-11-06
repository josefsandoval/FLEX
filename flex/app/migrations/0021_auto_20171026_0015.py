# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 07:15
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0020_auto_20171026_0003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=100)),
                ('last_name', models.CharField(default='', max_length=100)),
                ('date_of_birth', models.DateField(default=datetime.datetime(2017, 10, 26, 7, 15, 39, 780515, tzinfo=utc))),
                ('gender', models.CharField(default='', max_length=1)),
                ('address_street', models.CharField(default='', max_length=100)),
                ('address_city', models.CharField(default='', max_length=100)),
                ('address_zip', models.CharField(default='', max_length=100)),
                ('address_country', models.CharField(default='', max_length=100)),
                ('height', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('weight', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('bio', models.CharField(default='', max_length=4096)),
                ('image_url', models.CharField(default='https://www.1plusx.com/app/mu-plugins/all-in-one-seo-pack-pro/images/default-user-image.png', max_length=1000)),
                ('activities', models.ManyToManyField(to='app.Activity')),
                ('goals', models.ManyToManyField(to='app.Goal')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='activities',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='goals',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]

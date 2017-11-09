# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-08 07:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20171026_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address_state',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2017, 11, 8, 7, 32, 51, 415492, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='height',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='weight',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=6),
        ),
    ]

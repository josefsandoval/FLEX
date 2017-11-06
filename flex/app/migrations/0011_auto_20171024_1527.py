# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 22:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0010_auto_20171024_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password_hash', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=1)),
                ('address_street', models.CharField(max_length=100)),
                ('address_city', models.CharField(max_length=100)),
                ('address_zip', models.CharField(max_length=100)),
                ('address_country', models.CharField(max_length=100)),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=6)),
                ('bio', models.CharField(max_length=4096)),
                ('image_url', models.CharField(default='https://www.1plusx.com/app/mu-plugins/all-in-one-seo-pack-pro/images/default-user-image.png', max_length=1000)),
                ('activities', models.ManyToManyField(to='app.Activity')),
                ('goals', models.ManyToManyField(to='app.Goal')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='activities',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='goals',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AlterField(
            model_name='usermatch',
            name='user_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_match_from', to='app.User'),
        ),
        migrations.AlterField(
            model_name='usermatch',
            name='user_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_match_to', to='app.User'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]

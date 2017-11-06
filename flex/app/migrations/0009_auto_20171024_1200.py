# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 19:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0008_remove_user_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
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
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='activities',
        ),
        migrations.RemoveField(
            model_name='user',
            name='goals',
        ),
        migrations.AlterField(
            model_name='usermatch',
            name='user_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_match_from', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usermatch',
            name='user_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_match_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

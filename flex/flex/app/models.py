# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    email           = models.EmailField()
    pasword_hash    = models.CharField(max_length=100)
    first_name      = models.CharField(max_length=100)
    last_name       = models.CharField(max_length=100)
    date_of_birth   = models.DateField()
    gender          = models.CharField(max_length=1)
    address_street  = models.CharField(max_length=100)
    address_city    = models.CharField(max_length=100)
    address_zip     = models.CharField(max_length=100)
    address_country = models.CharField(max_length=100)
    height          = models.DecimalField(max_digits=5, decimal_places=2)
    weight          = models.DecimalField(max_digits=6, decimal_places=2)
    bio             = models.CharField(max_length=4096)
    def __str__(self):
        return self.first_name

class MatchSetting(models.Model):
    distance = models.IntegerField()
    gender   = models.CharField(max_length=1)
    age_min  = models.IntegerField()
    age_max  = models.IntegerField()

class UserMatch(models.Model):
    user_from = models.ForeignKey('User', related_name='user_match_from', on_delete=models.CASCADE)
    user_to   = models.ForeignKey('User', related_name='user_match_to', on_delete=models.CASCADE)

# TODO: Activity, Goal, UserActivity, UserGoal

# TODO: Post, PostComment

# TODO: Message

# TODO: Event, Invitee

# Create your models here.

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    email = models.EmailField()
    password_hash = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1)
    address_street = models.CharField(max_length=100)
    address_city = models.CharField(max_length=100)
    address_zip = models.CharField(max_length=100)
    address_country = models.CharField(max_length=100)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    bio = models.CharField(max_length=4096)

    def __str__(self):
        return self.first_name + self.last_name


class MatchSetting(models.Model):
    distance = models.IntegerField()
    gender = models.CharField(max_length=1)
    age_min = models.IntegerField()
    age_max = models.IntegerField()


class UserMatch(models.Model):
    user_from = models.ForeignKey(User, related_name='user_match_from', on_delete=models.CASCADE)
    user_to = models.ForeignKey(User, related_name='user_match_to', on_delete=models.CASCADE)


# TODO: Activity, Goal, UserActivity, UserGoal
class UserActivity(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    LOW_PRIORITY = 1
    MEDIUM_PRIORITY = 2
    HIGH_PRIORITY = 3
    ACTIVITY_PRIORITY = (
        (LOW_PRIORITY, 'Not Interested'),
        (MEDIUM_PRIORITY, 'Interested'),
        (HIGH_PRIORITY, 'Very Interested')
    )
    priority = models.IntegerField(choices=ACTIVITY_PRIORITY, default=LOW_PRIORITY)


class Activity(models.Model):
    activity_id = models.ForeignKey(UserActivity, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=4096)


class UserGoal(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    LOW_PRIORITY = 1
    MEDIUM_PRIORITY = 2
    HIGH_PRIORITY = 3
    GOAL_PRIORITY = (
        (LOW_PRIORITY, 'Not Important'),
        (MEDIUM_PRIORITY, 'Important'),
        (HIGH_PRIORITY, 'Very Important')
    )
    priority = models.IntegerField(choices=GOAL_PRIORITY, default=LOW_PRIORITY)


class Goal(models.Model):
    goal_id = models.ForeignKey(UserGoal, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=4096)

class Post(models.Model):
    text=models.CharField(max_length=1000)
    timestamp=models.DateField()

class PostComment(models.Model):
    text=models.CharField(max_length=1000)
    timestamp=models.DateField()

class Message(models.Model):
    text=models.CharField(max_length=1000)
    timestamp=models.DateField()

# TODO: Event, Invitee

# Create your models here.

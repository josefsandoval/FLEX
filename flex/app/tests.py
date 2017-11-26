# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.contrib.auth.models import User
from django.template.defaultfilters import length
from django.test import TestCase
from .models import UserProfile
from django.test import Client


class UserProfileTests(TestCase):

    # Test method that returns Users age
    def test_user_correct_age(self):
        birthday = datetime.datetime(1990,11,9)
        user = UserProfile(date_of_birth=birthday)
        self.assertIs(user.user_age(), 27, 'User age was not calculated correctly')


class UserTests(TestCase):

    def test_user_creation(self):
        new_user = User.objects.create_user('newuser',None,None)
        other_user = User.objects.create_user('otheruser',None,None)

        queryset = User.objects.all()
        self.assertQuerysetEqual(queryset, ["<User: newuser>", "<User: otheruser>"], ordered=False)

    # Test if creating a user creates a UserProfile Object
    def test_user_profile_creation(self):
        user = User.objects.create_user('user', None, None)
        self.assertIsNotNone(user.userprofile, 'User profile was not created along with user')


class AuthenticationTest(TestCase):
    # Test Django's Authentication System for logging in users
    def test_client_login(self):
        user = User.objects.create_user(username='jon', password='secret')
        c = Client()
        logged_in = c.login(username='jon', password='secret')
        self.assertTrue(logged_in)


class queryTest(TestCase):
    def intersectit(self,a, b):
        return list(set(a) & set(b))

    def test_it(self):
        b1 = [1, 2, 3, 4, 5, 9, 11, 15]
        b2 = [4, 5, 6, 7, 8]
        b3 = self.intersectit(b1,b2)

        self.assertQuerysetEqual(b3, ['4','5'])
        print ("Length: " + len(b3).__str__())

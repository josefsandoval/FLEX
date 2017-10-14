# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import User
from .models import MatchSetting
from .models import UserMatch

class IndexView(generic.ListView):
    template_name = 'app/index.html'

    def get_queryset(self):
        """TODO!"""
        return User.objects.order_by('first_name')

class UserView(generic.DetailView):
    model = User

class MatchSettingView(generic.DetailView):
    model = MatchSetting

class UserMatchView(generic.DetailView):
    model = UserMatch

# Create your views here.

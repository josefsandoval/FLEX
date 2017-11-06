# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import UserProfile, Activity, Goal
from .models import MatchSetting
from .models import UserMatch

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(MatchSetting)
admin.site.register(UserMatch)
admin.site.register(Activity)
admin.site.register(Goal)

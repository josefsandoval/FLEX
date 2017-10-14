# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from  .models import User
from  .models import MatchSetting
from  .models import UserMatch

# Register your models here.
admin.site.register(User)
admin.site.register(MatchSetting)
admin.site.register(UserMatch)

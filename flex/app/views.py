# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
# login required decorator(give added functionality to a function)
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import UserProfile
from .models import MatchSetting
from .models import UserMatch
from .forms import UserRegisterForm, UserProfileForm


class IndexView(generic.ListView):
    template_name = 'app/index1.html'

    def get_queryset(self):
        return UserProfile.objects.order_by('first_name')


# multiple models:
# https://stackoverflow.com/questions/18419328/refer-to-multiple-models-in-view-template-in-django
# add function get_context_data()
class ProfileView(generic.DetailView):
    template_name = 'app/otherprofile.html'
    model = User


class MatchView(generic.ListView):
    template_name = 'app/matches.html'

    def get_queryset(self):
        return User.objects.all().filter().exclude(userprofile=self.request.user.userprofile).order_by('username')


class MatchSettingView(generic.DetailView):
    model = MatchSetting


class UserMatchView(generic.DetailView):
    model = UserMatch


def register(request):
    # handle when there is POST data( when user fills out the form)
    if request.method == 'POST':
        # take the post data from the form
        form = UserRegisterForm(request.POST)
        if form.is_valid():  # if data has passed validation checks
            form.save()  # save the form contents
            return redirect('/app')

    else:
        # blank user registration form for user to fill in
        form = UserRegisterForm()


    context = {'form': form}
    if request.user.is_authenticated:
        return redirect('/app')
    return render(request, 'app/registration_form.html', context)


# request holds several data including data from Django's User obj.
# pass in the User object to the profile.html template
@login_required
def profile(request):
    args = {'user': request.user}
    return render(request, 'app/profile.html', args)


# Form for user to update profile information
def edit_profile(request):
    instance = request.user.userprofile
    form = UserProfileForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/app/profile')
    return render(request, 'app/edit_profile_form.html', {'form': form})

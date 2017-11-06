from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'app'

urlpatterns = [
    # front page
    url(r'^$', views.IndexView.as_view(), name='index'),

    # user registration
    url(r'^register/$', views.register, name='register'),

    # user login page
    url(r'^login/$', auth_views.login, {'template_name': 'app/login.html'}),
    # user logout page
    url(r'^logout/$', auth_views.logout, {'template_name': 'app/logout.html'}),
    # individual models
    url(r'^profile/(?P<pk>[0-9]+)/$', views.ProfileView.as_view(), name='profile'),
    # view list of other user profiles
    url(r'^matches/$', views.MatchView.as_view(), name='matches'),
    # view users own profile
    url(r'^profile/$', views.profile, name='profile'),

    url(r'^matchSetting/(?P<pk>[0-9]+)/$', views.MatchSettingView.as_view(), name='matchSetting'),

    url(r'^userMatch/(?P<pk>[0-9]+)/$', views.UserMatchView.as_view(), name='userMatch'),

    # edit User Profile url
    # url(r'^profile/edit/$', views.edit_profile, name = 'edit_profile'),
]

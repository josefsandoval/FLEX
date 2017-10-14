from django.conf.urls import url

from . import views

app_name = 'app'

urlpatterns = [
    # frontpage
    url(r'^$', views.IndexView.as_view(), name='index'),
    # individual models
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserView.as_view(), name='user'),
    url(r'^matchSetting/(?P<pk>[0-9]+)/$', views.MatchSettingView.as_view(), name='matchSetting'),
    url(r'^userMatch/(?P<pk>[0-9]+)/$', views.UserMatchView.as_view(), name='userMatch'),
]

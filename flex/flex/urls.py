from django.conf.urls import include, url
from django.contrib import admin
from flex.views import redirect_to_login


urlpatterns = [
    # root, redirect the user to login page
    url(r'^$', redirect_to_login, name='redirect_to_login'),
    url(r'^app/', include('app.urls')),
    url(r'^admin/', admin.site.urls),
]

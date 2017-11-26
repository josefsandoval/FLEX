from django.conf.urls import include, url
from django.contrib import admin
from flex.views import redirect_to_login
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # root, redirect the user to login page
    url(r'^$', redirect_to_login, name='redirect_to_login'),
    url(r'^app/', include('app.urls')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

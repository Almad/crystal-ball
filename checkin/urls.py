"""urlconf for the checkin application"""

from django.conf.urls import url, patterns


urlpatterns = patterns('checkin.views',
    url(r'^$', 'home', name='checkin_home'),
)

""" Default urlconf for crystal_ball """

from django.conf.urls import include, patterns, url
from django.contrib import admin

import ball.urls

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'', include('base.urls')),
)


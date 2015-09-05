"""Ball URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
"""

from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard_view, name='ball_dashboard_view'),
]

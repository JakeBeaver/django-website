from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
     url(r'^$', 'page.views.home', name='home'),
     url(r'^posts/$', 'page.views.create', name='new post'),
     url(r'^(?P<name>[a-zA-Z0-9.+-_@]{0,30})//?$', 'page.views.profile', name='profile'),
     
]

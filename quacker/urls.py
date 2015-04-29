from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'quacker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^', include('page.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
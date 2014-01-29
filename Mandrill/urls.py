from django.conf.urls import patterns, include, url
from djrill import DjrillAdminSite
from django.contrib import admin

admin.site = DjrillAdminSite()
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Mandrill.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^' , include('apps.home.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

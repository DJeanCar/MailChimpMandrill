from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	url(r'^$' , 'apps.home.views.home'),
	url(r'^send_email/$' , 'apps.home.views.send_email'),
)

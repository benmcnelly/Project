from django.conf.urls import patterns, include, url
from prettyreport.views import HomeView


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^tests/', 'prettyreport.views.tests', name='tests'),
	url(r'^reports/', 'prettyreport.views.reports', name='reports'),
	url(r'^dreports/', 'prettyreport.views.dreports', name='dreports'),
	url(r'^cwreports/', 'cwreport.views.cwreports', name='cwreports'),
	url(r'^$', HomeView.as_view()),
)

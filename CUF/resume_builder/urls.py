from django.conf.urls import patterns, url

from resume_builder import views

urlpatterns = patterns('',
		url(r'^upload$', views.upload_file, name='upload_file'),
		url(r'^contact$', views.contact, name='contact'),
)

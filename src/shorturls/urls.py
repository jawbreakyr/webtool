from django.conf.urls import patterns, url
from shorturls import views


urlpatterns = patterns('',
	url(r'^$', views.get_key_gen, name='home'),
    )
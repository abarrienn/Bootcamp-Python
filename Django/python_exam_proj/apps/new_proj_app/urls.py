from django.conf.urls import url
from . import views
from django.contrib.auth.views import logout
from django.conf import settings
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^process_quote$', views.process_quote),
    url(r'^destroy/(?P<id>\d+)$', views.destroy),
    url(r'^my_quotes/(?P<id>\d+)$', views.my_quotes),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^update/(?P<id>\d+)$', views.update),


]
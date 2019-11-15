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
    url(r'^add_book$', views.add_book),

]
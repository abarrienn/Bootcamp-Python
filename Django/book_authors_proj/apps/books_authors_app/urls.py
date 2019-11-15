from django.conf.urls import url
from . import views
from django.conf import settings
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_book$', views.add_book),
    url(r'^view_book/(?P<id>\d+)$', views.view_book),
    url(r'^add_auth_to_list/(?P<id>\d+)$', views.add_auth_to_list),
    url(r'^author_template/$', views.author_template),
    url(r'^view_author/(?P<id>\d+)$', views.view_author),
]

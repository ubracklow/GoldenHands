from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.start, name='start'),
    url(r'^guests/(?P<pk>[0-9]+)/$', views.guests, name = 'guests'),
    url(r'^assignments/(?P<pk>[0-9]+)/$', views.assignments, name = 'assignments'),
    #url(r'^result/(?P<pk>[0-9]+)/$', views.result, name = 'result'),
]
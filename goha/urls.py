from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.event, name='event'),
    url(r'^host/(?P<pk>[0-9]+)/$', views.host, name = 'host'),
    url(r'^guests/(?P<pk>[0-9]+)/$', views.guests, name = 'guests'),
    url(r'^assignment_email/(?P<pk>[0-9]+)/$', views.assignment_email, name = 'assignment_email'),
]
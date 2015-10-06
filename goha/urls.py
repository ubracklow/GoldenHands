from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.start, name='start'),
    url(r'^guests/$', views.guests, name = 'guests'),
]
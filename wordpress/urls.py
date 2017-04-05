#encoding: utf-8

from django.conf.urls import include, url
from . import views
urlpatterns = [
    #url(r'^$', views.transformer, name='transformer'),
    url(r'send', views.take_message),
    url(r'test', views.test),

]

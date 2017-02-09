from django.conf.urls import include, url
from django.contrib import admin

from . import views

app_name = 'soters'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dog_tmpl/$', views.DogView.as_view(), name = 'dog_tmpl'),
    url(r'^name/$', views.get_name, name = 'name'),
    url(r'^myview/$',views.myview, name = 'myview'),
    url(r'^myview2/$',views.myview2, name = 'myview2'),
]

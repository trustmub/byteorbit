from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.weather_view, name='weather'),
    url(r'^reload/$', views.weatherupdate, name='load')
]
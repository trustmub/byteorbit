from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.weather_view, name='weather'),
    url(r'^reload/$', views.weatherupdate, name='load'),
    url(r'^api/v1/', views.ListWeather.as_view(), name='api'),
    # the api url in this case will be http://127.0.0.1:8000/weather/api/v1/

]
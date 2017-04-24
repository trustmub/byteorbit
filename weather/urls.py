from django.conf.urls import url

from . import views

urlpatterns = [
    # Class based Vews url
    url(r'^$', views.WeatherListView.as_view(), name='weather'),
    # function based view url
    url(r'^reload/$', views.weatherupdate, name='load'),
    # Class based Vews url for API
    url(r'^api/v1/', views.ListWeather.as_view(), name='api'),
    # the api url in this case will be http://127.0.0.1:8000/weather/api/v1/
    url(r'(?P<pk>\d+)/$', views.RetrieveUpdateDestroyView.as_view(), name='api_update'),

]
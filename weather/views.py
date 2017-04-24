import time
import urllib.request
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import ListView

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Weather
from . import models
from . import serializers


# Create your views here.

def load_weather_data_to_db():
    try:
        # this is the API for the Cape Town Weather details in Json format
        with urllib.request.urlopen(
                "https://api.forecast.io/forecast/3872aff4b3988622b10adb56abbbbeeb/-33.92584,18.42322") as url:
            json_data = json.loads(url.read().decode())
            record_len = len(json_data['daily']['data'])
            i = 0
            custome_record = []
            # Extract Relevant Data from the web API
            while i < record_len:
                daily_min_temp = json_data['daily']['data'][i]['temperatureMin']
                daily_max_temp = json_data['daily']['data'][i]['temperatureMax']
                daily_wind_speed = json_data['daily']['data'][i]['windSpeed']
                daily_rain = json_data['daily']['data'][i]['humidity']
                daily_date = json_data['daily']['data'][i]['time']
                daily_date = time.strftime('%Y%m%d', time.localtime(int(daily_date)))  # make date readable
                daily_date = int(daily_date)
                daily_summary = json_data['daily']['data'][i]['summary']

                i += 1

                all_data = Weather.objects.all()
                # this list all the record in the database by dates to mitigate duplicates
                datelist = []
                for x in all_data:
                    datelist = datelist + [x.my_date]
                # if record is already in the database, then the record is not created
                if daily_date in datelist:
                    print("this record is already available will not add to database")
                else:
                    # if record is not in the database, it is created
                    Weather.objects.create(min_temp=daily_min_temp,
                                           max_temp=daily_max_temp,
                                           wind_speed=daily_wind_speed,
                                           my_date=daily_date,
                                           rain=daily_rain,
                                           summary=daily_summary)
                    print("Record Inserted")
    except Exception as e:
        return HttpResponseNotFound('<h1>No internet connection</h1><br><p>Data cannot be loaded at this point,'
                                    'please click <a href="{% url "weather" %}">here</a></p>')
        # return "Please Check Your Internet Connection: {}".format(e)  # json_data['daily':['summary']]


# def weather_view(request):
#     weather = Weather.objects.all()
#     # load_weather_data_to_db()
#     return render(request, 'weather/weather_list.html', {'weather': weather})

# this is a Class Based View for the list of database entries
# with a respective weather_list.html template
# and same context object in the template
class WeatherListView(ListView):
    context_object_name = "weather"
    model = models.Weather


def weatherupdate(request):
    load_weather_data_to_db()
    return render(request, 'weather/weather_list.html')
    # return load_weather_data_to_db()


# used a generic class based view to manage pagination gracefully
class ListWeather(generics.ListCreateAPIView):
    queryset = models.Weather.objects.all()
    serializer_class = serializers.WeatherSerializer


class RetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Weather.objects.all()
    serializer_class = serializers.WeatherSerializer

import time
import urllib.request
import json

from django.shortcuts import render
from .models import Weather


# Create your views here.

def load_weather_data_to_db():
    try:
        with urllib.request.urlopen(
                "https://api.forecast.io/forecast/3872aff4b3988622b10adb56abbbbeeb/-33.92584,18.42322") as url:
            json_data = json.loads(url.read().decode())
            record_len = len(json_data['daily']['data'])
            # print(record_len)
            i = 0
            custome_record = []
            # extracting
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
                print("before print")
                all_data = Weather.objects.all()
                datelist = []
                for x in all_data:
                    datelist = datelist + [x.my_date]

                if daily_date in datelist:
                    print("this record is already available will not add to database")
                else:
                    print("adding record in the database")
                    Weather.objects.create(min_temp=daily_min_temp,
                                           max_temp=daily_max_temp,
                                           wind_speed=daily_wind_speed,
                                           my_date=daily_date,
                                           rain=daily_rain,
                                           summary=daily_summary)
                    print("Record Inserted")
    except Exception as e:
        return "Please Check Your Internet Connection: {}".format(e)  # json_data['daily':['summary']]


def weather_view(request):
    weather = Weather.objects.all()
    # load_weather_data_to_db()
    return render(request, 'weather/weather_view.html', {'weather': weather})


def weatherupdate(request):
    load_weather_data_to_db()
    return render(request, 'weather/weather_view.html')

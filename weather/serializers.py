from rest_framework import serializers
from . import models


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'min_temp',
            'max_temp',
            'wind_speed',
            'my_date',
            'rain',
            'summary'
        )
        model = models.Weather

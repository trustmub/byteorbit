from django.db import models


# Create your models here.

class Weather(models.Model):
    min_temp = models.CharField(max_length=255)
    max_temp = models.CharField(max_length=255)
    wind_speed = models.CharField(max_length=255)
    my_date = models.IntegerField()  # time
    rain = models.FloatField()  # humidity
    summary = models.CharField(max_length=256)  # summary

    def __str__(self):
        return self.summary

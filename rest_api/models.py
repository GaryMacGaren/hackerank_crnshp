from django.db import models
from jsonfield import JSONField


class Weather(models.Model):
    date = models.DateField()
    lat = models.FloatField()
    lon = models.FloatField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    temperatures = JSONField()

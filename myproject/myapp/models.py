from django.db import models

# Create your models here.
class Location(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return f"Longitude: {self.longitude}, Latitude: {self.latitude}"
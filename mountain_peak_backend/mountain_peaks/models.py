from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

# https://python.plainenglish.io/build-geodjango-webapp-to-store-and-query-locations-91637d485a37


class Location(models.Model):
    coordinates = models.PointField(geography=True)

    def __str__(self):
        return f"Location: (lat={self.coordinates.y}, long={self.coordinates.x}) ({self.pk})"


# Create your models here.
class MountainPeak(models.Model):
    name = models.CharField(verbose_name="Mountain's peak name", max_length=255)
    location = models.OneToOneField(
        Location,
        on_delete=models.CASCADE,
    )
    altitude = models.IntegerField()

    def __str__(self):
        return f"MountainPeak: {self.name} ({self.pk})"

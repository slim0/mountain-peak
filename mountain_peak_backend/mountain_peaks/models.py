from django.contrib.gis.db import models
from django.contrib.gis.geos import Polygon
from pydantic import validate_arguments


class LocationManager(models.Manager):
    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    def in_bbox(self, bbox: Polygon):
        return self.filter(coordinates__intersects=bbox)


class Location(models.Model):
    coordinates = models.PointField(geography=True)

    objects = LocationManager()

    def __str__(self):
        return f"Location: (lat={self.latitude}, long={self.longitude}) ({self.pk})"

    @property
    def longitude(self):
        return self.coordinates.x

    @property
    def latitude(self):
        return self.coordinates.y


class MountainPeak(Location):
    name = models.CharField(verbose_name="Mountain's peak name", max_length=255)
    altitude = models.IntegerField()

    def __str__(self):
        return f"MountainPeak: {self.name} ({self.pk})"

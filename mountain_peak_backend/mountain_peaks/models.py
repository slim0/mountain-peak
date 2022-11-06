from django.contrib.gis.db import models

# https://python.plainenglish.io/build-geodjango-webapp-to-store-and-query-locations-91637d485a37


class Location(models.Model):
    coordinates = models.PointField(geography=True)

    def __str__(self):
        return f"Location: (lat={self.latitude}, long={self.longitude}) ({self.pk})"

    @property
    def longitude(self):
        return self.coordinates.x

    @property
    def latitude(self):
        return self.coordinates.y


class MountainPeakManager(models.Manager):
    def in_bbox(self, bbox):
        return self.filter(location__coordinates__intersects=bbox)


# Create your models here.
class MountainPeak(models.Model):
    name = models.CharField(verbose_name="Mountain's peak name", max_length=255)
    location = models.OneToOneField(
        Location,
        on_delete=models.CASCADE,
    )
    altitude = models.IntegerField()

    objects = MountainPeakManager()

    def __str__(self):
        return f"MountainPeak: {self.name} ({self.pk})"

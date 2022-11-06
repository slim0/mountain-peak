from django.contrib.gis.geos import Polygon
from drf_extra_fields.geo_fields import PointField
from rest_framework import serializers

from .models import MountainPeak


class MountainPeakSerializer(serializers.ModelSerializer):
    coordinates = PointField(required=True)

    class Meta:
        model = MountainPeak
        fields = ["id", "name", "altitude", "coordinates"]


class BboxPolygonSerializer(serializers.Serializer):
    top_left = PointField(required=True)
    bottom_right = PointField(required=True)

    def to_internal_value(self, data):
        values = super().to_internal_value(data)
        top_left = values["top_left"]
        bottom_right = values["bottom_right"]
        return Polygon.from_bbox((top_left.x, top_left.y, bottom_right.x, bottom_right.y))

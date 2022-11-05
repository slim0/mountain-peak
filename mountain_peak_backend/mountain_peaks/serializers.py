from django.contrib.gis.geos import Polygon
from drf_extra_fields.geo_fields import PointField
from rest_framework import serializers

from .models import Location, MountainPeak


class LocationSerializer(serializers.ModelSerializer):
    coordinates = PointField(required=True)

    class Meta:
        model = Location
        fields = ["coordinates"]


class MountainPeakSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = MountainPeak
        fields = ["id", "name", "altitude", "location"]

    def get_location(self, obj):
        return str(obj.location.coordinates)  # Or however you want to format it

    def create(self, validated_data):
        location_data = validated_data.pop("location")
        peak_location = Location.objects.create(coordinates=location_data["coordinates"])
        mountain_peak = MountainPeak.objects.create(**validated_data, location=peak_location)
        # for track_data in tracks_data:
        #     Track.objects.create(album=album, **trxack_data)
        return mountain_peak


class BboxPolygonSerializer(serializers.Serializer):
    top_left = PointField(required=True)
    bottom_right = PointField(required=True)

    def to_internal_value(self, data):
        values = super().to_internal_value(data)
        top_left = values["top_left"]
        bottom_right = values["bottom_right"]
        return Polygon.from_bbox((top_left.x, top_left.y, bottom_right.x, bottom_right.y))

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

from rest_framework import serializers

from .models import MountainPeak


class MountainPeakSerializer(serializers.ModelSerializer):
    class Meta:
        model = MountainPeak
        fields = ["id", "name", "altitude", "coordinates"]

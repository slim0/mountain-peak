from django.contrib.gis.geos import Polygon
from rest_framework import generics, viewsets

from .models import MountainPeak
from .serializers import MountainPeakSerializer


# Create your views here.
class MountainPeakViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """

    queryset = MountainPeak.objects.all()
    serializer_class = MountainPeakSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]

    def perform_destroy(self, instance):
        instance.location.delete()


class MountainPeaksInBbox(generics.ListAPIView):
    serializer_class = MountainPeakSerializer

    def get_queryset(self):
        request = self.request
        bbox = Polygon.from_bbox(
            (request.query_params["long1"], request.query_params["lat1"], request.query_params["long2"], request.query_params["lat2"])
        )
        return MountainPeak.objects.filter(location__coordinates__intersects=bbox)

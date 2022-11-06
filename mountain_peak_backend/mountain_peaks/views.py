from rest_framework import generics, viewsets

from .models import MountainPeak
from .serializers import BboxPolygonSerializer, MountainPeakSerializer


# Create your views here.
class MountainPeakViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """

    queryset = MountainPeak.objects.all()
    serializer_class = MountainPeakSerializer

    def perform_destroy(self, instance):
        instance.location.delete()


class MountainPeaksInBbox(generics.ListAPIView):
    serializer_class = MountainPeakSerializer

    def get_queryset(self):
        query_params = self.request.GET
        bbox_polygon_serializer = BboxPolygonSerializer(
            data={
                "top_left": {"longitude": query_params.get("xmin", None), "latitude": query_params.get("ymin", None)},
                "bottom_right": {"longitude": query_params.get("xmax", None), "latitude": query_params.get("ymax", None)},
            }  # type: ignore
        )
        bbox_polygon_serializer.is_valid(raise_exception=True)
        bbox_polygon = bbox_polygon_serializer.validated_data
        return MountainPeak.objects.in_bbox(bbox=bbox_polygon)

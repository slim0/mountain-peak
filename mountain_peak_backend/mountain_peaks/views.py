from rest_framework import generics, viewsets

from .models import MountainPeak
from .serializers import BboxPolygonSerializer, MountainPeakSerializer


# Create your views here.
class MountainPeakViewSet(viewsets.ModelViewSet):
    """
    DRF ModelViewSet : https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
    list(), .retrieve(), .create(), .update(), .partial_update(), and .destroy() methods provided.
    """

    queryset = MountainPeak.objects.all()
    serializer_class = MountainPeakSerializer


class MountainPeaksInBbox(generics.ListAPIView):
    """
    list() view (GET method) that retrieves all MountainPeak instance in a given bouding box.
    Bouding box must be define with the 4 following query parameters:
    - xmin: top-left longitude of the bounding box
    - ymin: top-left latitude of the bounding box
    - xmax: bottom-right longitude of the bounding box
    - ymax: bottom-right latitude of the bounding box

    URL looks like : http://localhost:8000/mountains_peaks/in-bbox?xmin=1.4&ymin=46&xmax=1.5&ymax=44
    """

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
        return MountainPeak.objects.in_bbox(bbox=bbox_polygon)  # type: ignore

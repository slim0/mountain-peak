from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework_gis.filters import InBBoxFilter

from .models import MountainPeak
from .serializers import MountainPeakSerializer


class MountainPeakViewSet(viewsets.ModelViewSet):
    """
    DRF ModelViewSet : https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset\n
    list(), .retrieve(), .create(), .update(), .partial_update(), and .destroy() methods provided.\n
    On POST, PUT and PATCH methods, 'coordinates' field must be a string like : "POINT(0 0)"
    """

    queryset = MountainPeak.objects.all()
    serializer_class = MountainPeakSerializer
    bbox_filter_field = "coordinates"
    filter_backends = (InBBoxFilter,)  # Polygon.from_bbox((p1x, p1y, p2x, p2y))
    bbox_filter_include_overlapping = True  # Optional

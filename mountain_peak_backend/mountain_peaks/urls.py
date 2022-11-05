from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"", views.MountainPeakViewSet, basename="mountain")
urlpatterns = router.urls

urlpatterns += [
    path("in-bbox", views.MountainPeaksInBbox.as_view()),
]

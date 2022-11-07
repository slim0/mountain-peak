from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"", views.MountainPeakViewSet, basename="mountain")
urlpatterns = router.urls

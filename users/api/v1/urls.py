from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import GhjhljkyhlkhViewSet, HjulikuiukjhjViewSet

router = DefaultRouter()
router.register("hjulikuiukjhj", HjulikuiukjhjViewSet)
router.register("ghjhljkyhlkh", GhjhljkyhlkhViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

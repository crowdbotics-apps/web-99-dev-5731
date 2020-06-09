from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import HjulikuiukjhjViewSet

router = DefaultRouter()
router.register("hjulikuiukjhj", HjulikuiukjhjViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

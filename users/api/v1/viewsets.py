from rest_framework import authentication
from users.models import Ghjhljkyhlkh, Hjulikuiukjhj
from .serializers import GhjhljkyhlkhSerializer, HjulikuiukjhjSerializer
from rest_framework import viewsets


class HjulikuiukjhjViewSet(viewsets.ModelViewSet):
    serializer_class = HjulikuiukjhjSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Hjulikuiukjhj.objects.all()


class GhjhljkyhlkhViewSet(viewsets.ModelViewSet):
    serializer_class = GhjhljkyhlkhSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Ghjhljkyhlkh.objects.all()

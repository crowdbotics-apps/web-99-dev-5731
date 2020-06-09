from rest_framework import authentication
from users.models import Hjulikuiukjhj
from .serializers import HjulikuiukjhjSerializer
from rest_framework import viewsets


class HjulikuiukjhjViewSet(viewsets.ModelViewSet):
    serializer_class = HjulikuiukjhjSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Hjulikuiukjhj.objects.all()

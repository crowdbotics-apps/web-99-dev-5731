from rest_framework import serializers
from users.models import Hjulikuiukjhj


class HjulikuiukjhjSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hjulikuiukjhj
        fields = "__all__"

from rest_framework import viewsets

from users.models import *
from users.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = ConfigurationSerializer

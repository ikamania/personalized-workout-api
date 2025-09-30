from rest_framework import viewsets

from user.serializers import BaseUserSerializer
from user.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = BaseUserSerializer


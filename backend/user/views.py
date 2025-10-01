from rest_framework import viewsets, permissions

from user.serializers import BaseUserSerializer
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = BaseUserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]

        return [permissions.AllowAny()] # allow any for testing


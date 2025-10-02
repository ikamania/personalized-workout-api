from rest_framework import viewsets, permissions
from rest_framework.response import Response

from user.serializers import BaseUserSerializer
from .models import User
from .permissions import IsOwner


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = BaseUserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        
        return [permissions.IsAuthenticated() and IsOwner()]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return User.objects.filter(id=user.id)

        return User.objects.none()

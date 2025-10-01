from rest_framework import serializers

from .models import User


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password"]



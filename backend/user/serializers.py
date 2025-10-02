from rest_framework import serializers

from .models import User


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password", "age", "weight", "height", "personal_records", "personal_goals"]

        extra_kwargs = {
            "password": {"write_only": True}
        }

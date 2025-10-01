from rest_framework import serializers

from .models import Workout


class BaseWorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = "__all__"


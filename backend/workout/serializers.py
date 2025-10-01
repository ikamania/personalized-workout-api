from rest_framework import serializers

from .models import Exercise, Workout


class BaseExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"


class BaseWorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ["exercise_id", "sets", "reps"]

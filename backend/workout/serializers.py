from rest_framework import serializers

from .models import Exercise, Workout


class BaseExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"


class BaseWorkoutSerializer(serializers.ModelSerializer):
    exercise_id = serializers.PrimaryKeyRelatedField(
        queryset=Exercise.objects.all(),
        source="exercise",
        write_only=True
    )

    class Meta:
        model = Workout
        fields = ["exercise_id", "sets", "reps"]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["exercise"] = BaseExerciseSerializer(instance.exercise).data

        return rep

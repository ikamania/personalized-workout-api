from rest_framework import serializers

from .models import Exercise, Workout, WorkoutPlan


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


class BaseWorkoutPlanSerializer(serializers.ModelSerializer):
    workout_ids = serializers.PrimaryKeyRelatedField(
        queryset=Workout.objects.all(),
        source="workouts",
        many=True,
        write_only=True
    )

    class Meta:
        model = WorkoutPlan
        fields = ["workout_ids", "name", "goal",  "description", "frequency_per_week", "daily_duration_minutes", "created_at"]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["workouts"] = BaseWorkoutSerializer(instance.workouts.all(), many=True).data

        return rep

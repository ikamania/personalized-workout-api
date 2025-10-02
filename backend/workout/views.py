from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied

from workout.serializers import BaseExerciseSerializer, BaseWorkoutSerializer
from .models import Exercise, Workout


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = BaseExerciseSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        return Exercise.objects.all()

    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            raise PermissionDenied("Only admins can create workouts")
        serializer.save()

    def perform_update(self, serializer):
        if not self.request.user.is_staff:
            raise PermissionDenied("Only admins can update workouts")
        serializer.save()

    def perform_destroy(self, instance):
        if not self.request.user.is_staff:
            raise PermissionDenied("Only admins can delete workouts")
        instance.delete()


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = BaseWorkoutSerializer 
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Workout.objects.none()

        return Workout.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

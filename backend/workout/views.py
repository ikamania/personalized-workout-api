from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied

from workout.serializers import BaseWorkoutSerializer
from .models import Workout


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = BaseWorkoutSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        return Workout.objects.all()

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


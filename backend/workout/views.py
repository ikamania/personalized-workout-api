from rest_framework import viewsets, permissions

from workout.serializers import BaseExerciseSerializer, BaseWorkoutSerializer, BaseWorkoutPlanSerializer
from .models import Exercise, Workout, WorkoutPlan
from .permissions import IsAdmin


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = BaseExerciseSerializer
    permission_classes = [IsAdmin]
    
    def get_queryset(self):
        return Exercise.objects.all()


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


class WorkoutPlanViewSet(viewsets.ModelViewSet):
    queryset = WorkoutPlan.objects.all()
    serializer_class = BaseWorkoutPlanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return WorkoutPlan.objects.none()
        
        return WorkoutPlan.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

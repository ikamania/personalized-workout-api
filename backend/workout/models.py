from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Exercise(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    instructions = models.TextField()
    target_muscles = models.CharField(max_length=200)
    equipment = models.CharField(max_length=100, blank=True, null=True)


class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workouts")
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()


class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workout_plans")
    workouts = models.ManyToManyField(Workout, related_name="plans")
    name = models.CharField(max_length=100, unique=True)
    goal = models.CharField(max_length=50)
    frequency_per_week = models.PositiveIntegerField()
    daily_duration_minutes = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


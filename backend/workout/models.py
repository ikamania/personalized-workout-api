from django.db import models


class Workout(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    instructions = models.TextField()
    target_muscles = models.CharField(max_length=200)
    equipment = models.CharField(max_length=100, blank=True, null=True)


import json
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from workout.models import Workout

class Command(BaseCommand):
    help = "Load workouts from JSON file into the database"

    def handle(self, *args, **kwargs):
        file_path = os.path.join(settings.BASE_DIR, 'workout', 'data', 'workouts.json')
        
        with open(file_path, 'r') as f:
            data = json.load(f)

        for item in data:
            Workout.objects.get_or_create(
                name=item['name'],
                defaults={
                    'description': item['description'],
                    'instructions': item['instructions'],
                    'target_muscles': item['target_muscles'],
                    'equipment': item.get('equipment')
                }
            )

        self.stdout.write(self.style.SUCCESS("Workouts loaded successfully!"))


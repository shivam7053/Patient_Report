import csv
from django.core.management.base import BaseCommand
from patient_data.models import HealthReport

class Command(BaseCommand):
    help = 'Import health reports from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file.')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                HealthReport.objects.create(
                    patient_id=row['patient_id'],
                    doctor_id=row['doctor_id'],
                    hospital_id=row['hospital_id'],
                    patient_name=row['patient_name'],
                    doctor_name=row['doctor_name'],
                    hospital_name=row['hospital_name'],
                    heart_rate=row['heart_rate'],
                    cholesterol_level=row['cholesterol_level'],
                    platelet_count=row['platelet_count'],
                    eyesight=row['eyesight'],
                    weight=row['weight'],
                    height=row['height'],
                    month=row['month'],
                    year=row['year'],
                )
        self.stdout.write(self.style.SUCCESS(f'Successfully imported data from {csv_file}'))

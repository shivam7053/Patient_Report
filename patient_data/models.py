from django.db import models

class HealthReport(models.Model):
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    hospital_id = models.IntegerField()
    patient_name = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    hospital_name = models.CharField(max_length=100)
    heart_rate = models.IntegerField()
    cholesterol_level = models.IntegerField()
    platelet_count = models.IntegerField()
    eyesight = models.FloatField()
    weight = models.FloatField()
    height = models.FloatField()
    month = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return f"{self.patient_name} - {self.year}/{self.month}"

# Generated by Django 5.1.1 on 2024-09-26 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HealthReport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("patient_id", models.IntegerField()),
                ("doctor_id", models.IntegerField()),
                ("hospital_id", models.IntegerField()),
                ("patient_name", models.CharField(max_length=100)),
                ("doctor_name", models.CharField(max_length=100)),
                ("hospital_name", models.CharField(max_length=100)),
                ("heart_rate", models.IntegerField()),
                ("cholesterol_level", models.IntegerField()),
                ("platelet_count", models.IntegerField()),
                ("eyesight", models.FloatField()),
                ("weight", models.FloatField()),
                ("height", models.FloatField()),
                ("month", models.IntegerField()),
                ("year", models.IntegerField()),
            ],
        ),
    ]

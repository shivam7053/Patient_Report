from django.urls import path
from . import views

urlpatterns = [
    path('', views.health_report_list, name='health_report_list'),
    path('details/', views.patient_detail, name='patient_detail'),
]

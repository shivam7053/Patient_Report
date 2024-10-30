from django.shortcuts import render, get_object_or_404
from .models import HealthReport
from .forms import HealthReportFilterForm

def health_report_list(request):
    form = HealthReportFilterForm(request.GET or None)
    reports = HealthReport.objects.all()

    if form.is_valid():
        if form.cleaned_data['patient_id']:
            reports = reports.filter(patient_id=form.cleaned_data['patient_id'])
        if form.cleaned_data['doctor_id']:
            reports = reports.filter(doctor_id=form.cleaned_data['doctor_id'])
        if form.cleaned_data['hospital_id']:
            reports = reports.filter(hospital_id=form.cleaned_data['hospital_id'])
        if form.cleaned_data['year']:
            reports = reports.filter(year=form.cleaned_data['year'])

    return render(request, 'patient_data/health_report_list.html', {'form': form, 'reports': reports})

# patient_data/views.py

def patient_detail(request):
    patient_info = None
    reports = []
    months = []
    heart_rate_data = []
    cholesterol_data = []
    platelet_count_data = []
    eyesight_data = []

    if request.method == 'POST':
        # Get patient ID from the submitted form
        patient_id = request.POST.get('patient_id')
        # Fetch all records for the specified patient ID
        reports = HealthReport.objects.filter(patient_id=patient_id).order_by('year', 'month')

        if reports.exists():
            patient_info = reports.first()
            months = [f"{report.month}-{report.year}" for report in reports]
            heart_rate_data = [report.heart_rate for report in reports]
            cholesterol_data = [report.cholesterol_level for report in reports]
            platelet_count_data = [report.platelet_count for report in reports]
            eyesight_data = [report.eyesight for report in reports]
        else:
            # Handle case where no reports are found
            patient_info = {'patient_name': 'Unknown', 'patient_id': patient_id}

    # Pass data to the template
    context = {
        'reports': reports,
        'patient_info': patient_info,
        'months': months,
        'heart_rate_data': heart_rate_data,
        'cholesterol_data': cholesterol_data,
        'platelet_count_data': platelet_count_data,
        'eyesight_data': eyesight_data,
    }

    return render(request, 'patient_data/patient_detail.html', context)
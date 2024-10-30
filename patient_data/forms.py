from django import forms

class HealthReportFilterForm(forms.Form):
    patient_id = forms.IntegerField(required=False, label='Patient ID')
    doctor_id = forms.IntegerField(required=False, label='Doctor ID')
    hospital_id = forms.IntegerField(required=False, label='Hospital ID')
    year = forms.IntegerField(required=False, label='Year')

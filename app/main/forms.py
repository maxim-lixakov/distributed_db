# forms.py in your Django app

from django import forms
from .models import Cinema


class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinema
        fields = ['cinema_id', 'name', 'address', 'operating_hours_start', 'operating_hours_end', 'contact_number']
        widgets = {
            'operating_hours_start': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'operating_hours_end': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

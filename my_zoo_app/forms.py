from django import forms
from .models import Conservation

class ConservationForm(forms.ModelForm):
    class Meta:
        model = Conservation
        fields = ['date', 'status']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }

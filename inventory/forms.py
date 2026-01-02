from django import forms
from .models import Radiator


class RadiatorForm(forms.ModelForm):
    """Form for creating and updating radiators"""
    
    class Meta:
        model = Radiator
        fields = [
            'name',
            'compatible_vehicles',
            'quantity',
            'cost_price',
            'selling_price',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter radiator name/model'
            }),
            'compatible_vehicles': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'List compatible vehicles (e.g., Toyota Corolla, Ford Focus)'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0
            }),
            'cost_price': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': 0
            }),
            'selling_price': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': 0
            }),
        }


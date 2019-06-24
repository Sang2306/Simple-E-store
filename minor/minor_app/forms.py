from django import forms
from .models import Ship


class ShipForm(forms.ModelForm):
    class Meta:
        model = Ship
        widgets = {
            'ship_mode': forms.Select(
                attrs={
                    'class': 'browser-default custom-select',
                    'id': 'ship-mode',
                }
            )
        }
        fields = ['ship_mode']

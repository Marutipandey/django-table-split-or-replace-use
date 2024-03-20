# dpr/forms.py

from django import forms
from .dps import Data

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = '__all__'  # Include all fields in the form

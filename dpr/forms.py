from django import forms
from .models import  TimeAndDate


class TimeAndDateForm(forms.ModelForm):
    class Meta:
        model = TimeAndDate
        fields = ['bookname']

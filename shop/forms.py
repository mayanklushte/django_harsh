from django import forms
from .models import *

class DemoForm(forms.ModelForm):
    
    class Meta:
        model = Demo
        fields = '__all__'


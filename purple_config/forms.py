from django import forms
from .models import *

class ConfigurationForm(forms.ModelForm):
    class Meta:
        model = Configuration

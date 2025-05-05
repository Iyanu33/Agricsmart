from django import forms
from .models import SoilImage

class SoilImageForm(forms.ModelForm):
    class Meta:
        model = SoilImage
        fields = ['image']

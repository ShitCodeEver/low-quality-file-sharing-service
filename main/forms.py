from django import forms
from .models import MediaPost

class FormFile(forms.ModelForm):
    class Meta:
        model = MediaPost
        fields = ['media']
        widgets = {
            'media': forms.FileInput(attrs={'class': 'form-control'})
        }

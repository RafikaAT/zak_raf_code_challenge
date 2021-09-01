from django import forms
from .models import Shortener

class NewUrlForm(forms.ModelForm):
    class Meta:
        model = Shortener
        fields = ['long_url']
from django import forms
from .models import Petition


class PetitionForm(forms.ModelForm):
    class Meta:
        model = Petition
        fields = ['title', 'description']


class PetitionSignForm(forms.Form):
    pass  

from django import forms;
from RegistrationApp.models import Registration

class RegistrationForm(forms.ModelForm):
    #no-separate fields are required(taken from model-Movies-class)
    class Meta:
        model=Registration
        fields='__all__'
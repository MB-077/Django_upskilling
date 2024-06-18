from django import forms

from .models import *

# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Participant
#         fields = ['email']

class RegistrationForm(forms.Form):
    email = forms.EmailField(label="Your email")
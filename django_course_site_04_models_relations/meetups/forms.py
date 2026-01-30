from django import forms

# from .models import Participant


class RegistrationForm(forms.Form):
    email = forms.EmailField(label="Your Email")
    # class Meta:
    #     model = Participant
    #     fields = ['email']

from django import forms


class ReviewForm(forms.Form):
    user_name = (forms.CharField(label='Your name', max_length=1,
                                 error_messages={
                                     'required': 'Please enter your name',
                                     "max_length": "Please enter a shorter name", }))

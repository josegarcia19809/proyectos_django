from django import forms

from reviews.models import Review


# class ReviewForm(forms.Form):
#     user_name = (forms.CharField(label='Your name', max_length=100,
#                                  error_messages={
#                                      'required': 'Please enter your name',
#                                      "max_length": "Please enter a shorter name", }))
#     review_text = (forms.CharField(label='Your review', widget=forms.Textarea,
#                                    max_length=1000, ))
#     rating = (forms.IntegerField(label='Your rating', min_value=1, max_value=5, ))


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        labels = {
            'user_name': 'Your name',
            'review_text': 'Your Feedback',
            'rating': 'Your Rating',
        }
        error_messages = {
            'user_name': {
                'required': 'Please enter your name',
                "max_length": "Please enter a shorter name"
            }
        }

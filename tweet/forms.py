from django import forms
from .models import Tweets


class NewTweet(forms.Form):

    tweet = forms.CharField(widget=forms.Textarea(
        attrs={'rows': '3', 'cols': '50'}), max_length=140, label='Tweet')

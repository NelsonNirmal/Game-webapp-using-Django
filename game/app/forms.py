from django import forms
from .models import games

class gamesform(forms.ModelForm):
    class Meta:
        model=games
        fields=['email','password']
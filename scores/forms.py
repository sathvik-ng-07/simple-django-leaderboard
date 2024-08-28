from django import forms
from .models import Score

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['game', 'score']

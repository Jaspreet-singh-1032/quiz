# django imports
from django.forms import ModelForm

# model imports
from .models import (
    Answer
)

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ('name', 'quiz','options')



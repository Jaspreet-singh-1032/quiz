from django.db import models
from django.contrib.auth import get_user_model
from django_extensions.db.models import TimeStampedModel

class Quiz(TimeStampedModel):
    
    # required
    name = models.CharField(max_length=50)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

class Question(TimeStampedModel):
    
    # required
    text = models.CharField(max_length=500)
    
    # relationship
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

class Option(TimeStampedModel):
    # required
    text = models.CharField(max_length=500)

    # optinal
    is_correct = models.BooleanField(default=False)
    
    # relationship
    question = models.ForeignKey(Question , on_delete=models.CASCADE)

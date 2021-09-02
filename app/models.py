from django.db import models
from django.contrib.auth import get_user_model
from django_extensions.db.models import TimeStampedModel

class Quiz(TimeStampedModel):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

class Question(TimeStampedModel):
    text = models.CharField(max_length=300)
    
    # relationship
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)



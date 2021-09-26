import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django_extensions.db.models import TimeStampedModel
from django.urls import reverse

class Quiz(TimeStampedModel):
    
    # required
    name = models.CharField(max_length=50)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    uuid = models.UUIDField(default=uuid.uuid4 , editable=False, unique=True)

    def __str__(self):
        return self.name

class Question(TimeStampedModel):
    
    # required
    text = models.CharField(max_length=500)
    
    # relationship
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE , related_name='questions')

    def __str__(self):
        return self.text
    

class Option(TimeStampedModel):
    # required
    text = models.CharField(max_length=500)

    # optinal
    is_correct = models.BooleanField(default=False)
    
    # relationship
    question = models.ForeignKey(Question , on_delete=models.CASCADE , related_name='options')

    def __str__(self):
        return self.text
    
class Answer(TimeStampedModel):

    # required
    name = models.CharField(max_length=50) # name of user who is attempting quiz

    # relationship
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    options = models.ManyToManyField(Option)


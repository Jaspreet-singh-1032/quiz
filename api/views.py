# drf imports
from rest_framework import mixins
from rest_framework import viewsets

# django import
from django.shortcuts import get_object_or_404
# from django.contrib.auth import login
# from django.contrib.auth.models import User

# models import
from app.models import (
    Quiz,
    Question,
    Option
)

# serializer import
from .serializers import (
    QuizSerializer,
    QuestionSerializer
)

class QuizViewSet(mixins.CreateModelMixin,
                 viewsets.GenericViewSet):
    serializer_class = QuizSerializer
    
    def get_queryset(self):
        '''
        returns quiz related to current user
        '''
        return Quiz.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class QuestionViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = QuestionSerializer
    def get_queryset(self):
        return Question.objects.filter(quiz=self.kwargs.get('quiz_pk'))
    
    def perform_create(self , serializer):
        quiz = get_object_or_404(Quiz , pk=self.kwargs.get('quiz_pk'))
        serializer.save(quiz = quiz)
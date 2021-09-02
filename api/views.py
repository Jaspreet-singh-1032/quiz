# drf imports
from rest_framework import mixins
from rest_framework import viewsets

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
    QuizSerializer
)

class QuizViewSet(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.DestroyModelMixin,
                 viewsets.GenericViewSet):
    serializer_class = QuizSerializer
    
    def get_queryset(self):
        '''
        returns quiz related to current user
        '''
        return Quiz.objects.filter(user=self.request.user)
        
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
    
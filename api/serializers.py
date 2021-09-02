# drf imports
from rest_framework import serializers

# models import
from app.models import (
    Quiz,
    Question,
    Option
)

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('id' , 'text' , 'is_correct')

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id' , 'name')
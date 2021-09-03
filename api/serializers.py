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
        extra_kwargs = {
            'is_correct':{'write_only':True}
        }

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id' , 'name')

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True , required=True , allow_null=False , validators=None)
    class Meta:
        model = Question
        fields = ('id','text','options')
    
    def create(self , validated_data):
        options = validated_data.pop('options')
        question = Question.objects.create(**validated_data)
        for option in options:
            Option.objects.create(question = question , **option)
        return question
    def validate_options(self , data):
        if len(data) < 2:
            raise serializers.ValidationError('Please add atleast 2 options')
        return data
    
    '''
    {
    "text": "test",
    "options": [{"text":"o1"}]
}
    '''
import json

from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

from rest_framework import status

# models
from django.contrib.auth import get_user_model
from app.models import (
    Quiz
)

def authenticate_client(client : Client) -> None:
        '''
        call this method to make client authenticated
        '''
        user = get_user_model().objects.create(username='test')
        user.set_password('test')
        user.save()
        client.login(username='test' , password='test')

class QuizApiTestCase(TestCase):

    def setUp(self):
        self.url = reverse('quiz-list')

    def test_create_quiz_unauthenticated_fails(self ):
        ''' 
        only authenticated users can create quiz
        '''
        data = {
            "name":"test quiz"
        }
        response = self.client.post(self.url , data = data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_quiz_authenticated(self):
        '''
        create quiz for authenticated user
        '''
        authenticate_client(self.client)
        data = {
            "name":"test quiz"
        }
        response = self.client.post(self.url , data = data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('name'), data.get('name'))
    
    def test_create_quiz_authenticated_with_empty_data_fails(self):
        '''
        create quiz for authenticated user
        '''
        authenticate_client(self.client)
        data = {}
        response = self.client.post(self.url , data = data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class QuestionApiTestCase(TestCase):


    def setUp(self):
        # setup url with invalid quiz id
        self.url = reverse('question-list' , kwargs={'quiz_pk' :1})        
    
    def test_add_question_unautnenticated_fails(self):
        response = self.client.post(self.url , data={})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_add_question_authenticated_empty_data_fails(self):
        '''
        return 400 if data is empty
        '''
        authenticate_client(self.client)
        response = self.client.post(self.url,  data={} , content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_add_question_autheticated_empty_options_fails(self):
        '''
        return 400 is options is empty
        '''
        authenticate_client(self.client)
        data = {
            'text':"test question",
            "options":[]
        }
        response = self.client.post(self.url , data=data , content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_question_authenticated_only_one_option_fails(self):
        '''
        atleast 2 options is needed
        '''
        authenticate_client(self.client)
        data = {
            "text":"test question",
            "options":[
                {
                    "text":"test option",
                    "is_correct":True
                }
            ]
        }
        response = self.client.post(self.url , data = data , content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_add_question_invalid_quiz_id_fails(self):
        authenticate_client(self.client)
        data = {
            "text":"test question",
            "options":[
                {
                    "text":"test option",
                    "is_correct":True
                },
                {
                    "text":"test option 2"
                }
            ]
        }
        response = self.client.post(self.url , data=data , content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_add_question(self):
        authenticate_client(self.client)
        data = {
            "text":"test question",
            "options":[
                {
                    "text":"test option",
                    "is_correct":True
                },
                {
                    "text":"test option 2"
                }
            ]
        }
        user = get_user_model().objects.all().get(username = 'test') # created this user in authenticated_client method
        quiz = Quiz.objects.create(name='test quiz' , user = user)
        url = reverse('question-list' , kwargs={'quiz_pk' :quiz.pk})    
        response = self.client.post(url , data = data , content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_list_questions_unauthentcated_fails(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_questions_authentcated(self):
        authenticate_client(self.client)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

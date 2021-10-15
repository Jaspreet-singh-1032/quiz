from django.test import TestCase
from django.urls import reverse

from rest_framework import status

from django.contrib.auth import get_user_model

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
        user = get_user_model().objects.create(username='test')
        user.set_password('test')
        user.save()
        self.client.login(username='test' , password='test')
        data = {
            "name":"test quiz"
        }
        response = self.client.post(self.url , data = data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('name'), data.get('name'))
    
    def test_create_quiz_authenticated_with_empty_data(self):
        '''
        create quiz for authenticated user
        '''
        user = get_user_model().objects.create(username='test')
        user.set_password('test')
        user.save()
        self.client.login(username='test' , password='test')
        data = {}
        response = self.client.post(self.url , data = data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

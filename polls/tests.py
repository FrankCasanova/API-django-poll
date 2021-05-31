from rest_framework.test import APIClient, APITestCase, APIRequestFactory
from polls import apiviews
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Create your tests here.

class TestPoll(APITestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.view = apiviews.PollViewSet.as_view({'get': 'list'})
        self.uri = '/polls/'
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()
        
    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user('test',
                                        email='testuser@test.com',
                                        password='unodostrescuatro')    
    
    def test_list(self):
        
        request = self.factory.get(self.uri,
                                   HTTP_AUTHORIZATION=f'Token {self.token.key}')
        request.user = self.user
        response = self.view(request)
        
        self.assertEqual(response.status_code, 200,
                            f'Expected Response code 200, recieved {response.status_code} instead.'
                            )    

    def test_list2(self):
        self.client.login(username='test', password='unodostrescuatro')
        response = self.client.get(self.uri)
        
        self.assertEqual(response.status_code,200,
                         f'Expected Response Code 200, recieved {response.status_code} instead')

    def test_create(self):
        self.client.login(username='test', password='unodostrescuatro')
        params = {
            'question': 'how are you?',
            'created_by': '1'
        }
        response = self.client.post(self.uri, params)
        
        self.assertEqual(response.status_code,201,
                         f'Expected Response Code 201, recieved {response.status_code}')
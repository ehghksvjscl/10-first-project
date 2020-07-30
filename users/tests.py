import json
import bcrypt
from django.test import (
    TestCase,
    Client
)
from .models import Users
class UserTest(TestCase):

    def setUp(self):
        client = Client()
        Users.objects.create(
            user = 'g@example.com',
            email = 'g@example.com',
            password = bcrypt.hashpw('asdf1234'.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
            
        )
    def tearDown(self):
        Users.objects.all().delete()
    def test_SignUpView_post_success(self):
        user = {
            'user'      : 'd@example.com',
            'email'     : 'd@example.com',
            'password'  : 'asdf1234'
        }
        response = self.client.post('/signup', json.dumps(user), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
    def test_SignInView_post_success(self):
        user = {
            'user'      : 'g@example.com',
            'email'     : 'g@example.com',
            'password'  : 'asdf1234'
        }
        response = self.client.post('/signin', json.dumps(user), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
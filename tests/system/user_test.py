from models.user import UserModel
from tests.base_test import BaseTest
import json


class UserTestSystem(BaseTest):
    def test_register_user(self):
        with self.app() as client:
            with self.app_context():
                request = client.post('/register', data={'username': 'test', 'password': '1234'})

                self.assertEqual(request.status_code, 201)
                self.assertIsNotNone(UserModel.find_by_username('test'),
                                     f"Expected to find object in the database, but found none.")
                self.assertDictEqual({'message': 'User created successfully'},
                                     json.loads(request.data))

    def test_login(self):
        with self.app() as client:
            with self.app_context():
                client.post('/register', data={'username': 'test', 'password': '1234'})
                # /auth only accepts json objects
                auth_request = client.post('/auth',
                                            data=json.dumps({'username': 'test', 'password': '1234'}),
                                            headers={'Content-type': 'application/json'})

                self.assertIn('access_token', json.loads(auth_request.data).keys())

    def test_register_duplicate_username(self):
        with self.app() as client:
            with self.app_context():
                client.post('/register', data={'username': 'test', 'password': '1234'})
                request = client.post('/register', data={'username': 'test', 'password': '1234'})

                self.assertEqual(request.status_code, 400)
                self.assertDictEqual({'message': 'User already exists on the database'},
                                     json.loads(request.data))

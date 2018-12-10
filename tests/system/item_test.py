import json

from tests.base_test import BaseTest
from models.store import StoreModel
from models.item import ItemModel
from models.user import UserModel


class ItemTestSystem(BaseTest):
    def setUp(self):
        super(ItemTestSystem, self).setUp()
        with self.app() as client:
            with self.app_context():
                client.post('/register', data={'username': 'test', 'password': '1234'})
                auth_request = client.post('/auth',
                            data=json.dumps({'username': 'test', 'password': '1234'}),
                            headers={'Content-type': 'application/json'})

                auth_token = json.loads(auth_request.data)['access_token']
                self.access_token = f'JWT {auth_token}'

    def test_get_item_without_authorization(self):
        with self.app() as client:
            with self.app_context():
                request = client.get('/item/test')

                self.assertEqual(request.status_code, 401)

    def test_get_item_not_found(self):
        with self.app() as client:
            with self.app_context():
                request = client.get('/item/test', headers={'Authorization': self.access_token})

                self.assertEqual(request.status_code, 404)
                self.assertDictEqual({'message': 'Item not found'}, json.loads(request.data))

    def test_get_item_with_authorization(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test store').save_to_db()
                ItemModel('test', 19.99, 1).save_to_db()

                request = client.get('/item/test', headers={'Authorization': self.access_token})

                self.assertEqual(request.status_code, 200)

    def test_delete_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test store').save_to_db()
                ItemModel('test', 19.99, 1).save_to_db()

                request = client.delete('/item/test')

                self.assertEqual(request.status_code, 200)
                self.assertDictEqual({'message': 'Item deleted'}, json.loads(request.data))

    def test_create_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test store').save_to_db()

                request = client.post('/item/test', data={'price': 19.99, 'store_id': 1})

                self.assertEqual(request.status_code, 201)
                self.assertDictEqual({'name': 'test', 'price': 19.99}, json.loads(request.data))

    def test_create_duplicated_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test store').save_to_db()

                client.post('/item/test', data={'price': 19.99, 'store_id': 1})
                request = client.post('/item/test', data={'price': 19.99, 'store_id': 1})

                self.assertEqual(request.status_code, 400)
                self.assertDictEqual({'message': 'An item with name \'test\' already exists.'},
                                     json.loads(request.data))

    def test_put_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test store').save_to_db()

                request = client.put('/item/test', data={'price': 19.99, 'store_id': 1})

                self.assertEqual(request.status_code, 200)
                self.assertDictEqual({'name': 'test', 'price': 19.99}, json.loads(request.data))

    def test_put_updated_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test store').save_to_db()

                client.post('/item/test', data={'price': 19.99, 'store_id': 1})
                request = client.put('/item/test', data={'price': 10.59, 'store_id': 1})

                self.assertEqual(request.status_code, 200)
                self.assertDictEqual({'name': 'test', 'price': 10.59}, json.loads(request.data))

    def test_list_items(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test store').save_to_db()

                client.post('/item/test', data={'price': 19.99, 'store_id': 1})
                client.post('/item/test-2', data={'price': 5.99, 'store_id': 1})
                request = client.get('/items')

                self.assertEqual(request.status_code, 200)
                self.assertDictEqual({'items': [
                    {
                        'name': 'test',
                        'price': 19.99
                    },
                    {
                        'name': 'test-2',
                        'price': 5.99
                    }
                ]}, json.loads(request.data))

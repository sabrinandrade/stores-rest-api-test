from tests.base_test import BaseTest
from models.store import StoreModel
from models.item import ItemModel
import json


class StoreTestSystem(BaseTest):
    def test_create_store(self):
        with self.app() as client:
            with self.app_context():
                request = client.post('/store/test')

                self.assertEqual(request.status_code, 201)
                self.assertIsNotNone(StoreModel.find_by_name('test'))
                self.assertDictEqual({'name': 'test', 'items': []},
                                     json.loads(request.data))

    def test_create_duplicated_store(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/test')
                request = client.post('/store/test')

                self.assertDictEqual({'message': 'A store with name \'test\' already exists.'},
                                     json.loads(request.data))
                self.assertEqual(request.status_code, 400)

    def test_delete_store(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/test')
                request = client.delete('/store/test')

                self.assertEqual(request.status_code, 200)
                self.assertDictEqual({'message': 'Store deleted'},
                                     json.loads(request.data))

    def test_find_store(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/test')
                request = client.get('/store/test')

                self.assertEqual(request.status_code, 200)
                self.assertDictEqual({'name': 'test', 'items': []},
                                     json.loads(request.data))

    def test_store_not_found(self):
        with self.app() as client:
            with self.app_context():
                request = client.get('/store/test')

                self.assertEqual(request.status_code, 404)
                self.assertDictEqual({'message': 'Store not found'},
                                     json.loads(request.data))

    def test_store_found_with_items(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/test')
                ItemModel('test-item', 19.99, 1).save_to_db()
                request = client.get('/store/test')

                self.assertEqual(request.status_code, 200)
                self.assertDictEqual({'name': 'test', 'items': [{'name': 'test-item', 'price': 19.99}]},
                                     json.loads(request.data))

    def test_store_list(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/test')
                client.post('/store/test-2')

                request = client.get('/stores')

                self.assertEqual(request.status_code, 200)
                self.assertDictEqual({'stores': [{
                                                    'name': 'test',
                                                    'items': []
                                                 },
                                                {
                                                    'name': 'test-2',
                                                    'items': []
                                                }]},
                                     json.loads(request.data))

    def test_store_list_with_items(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/test')
                client.post('/store/test-2')

                ItemModel('test-item-1', 19.99, 1).save_to_db()
                ItemModel('test-item-2', 5.00, 2).save_to_db()

                request = client.get('/stores')

                self.assertEqual(request.status_code, 200)
                self.assertDictEqual({'stores': [{
                                            'name': 'test',
                                            'items': [{'name': 'test-item-1', 'price': 19.99}]
                                         },
                                        {
                                            'name': 'test-2',
                                            'items': [{'name': 'test-item-2', 'price': 5.00}]
                                        }]},
                                     json.loads(request.data))

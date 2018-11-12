from models.store import StoreModel
from models.item import ItemModel
from tests.integration.integration_base_test import IntegrationBaseTest


class TestStoreIntegration(IntegrationBaseTest):
    def test_json_without_items(self):
        store = StoreModel('json store')
        expected = {
            'name': 'json store',
            'items': []}

        self.assertEqual(expected, store.json())

    def test_json_with_items(self):
        with self.app_context():
            store = StoreModel('json store')
            item = ItemModel('item', 20, 1)
            expected = {
                'name': 'json store',
                'items': [{'name': 'item', 'price': 20.0}]
            }

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(expected, store.json())

    def test_create_empty_store(self):
        store = StoreModel('test')
        self.assertListEqual(store.items.all(), [],
                             f"Expected the length of the item list for the newly created store {store.name} to be 0.")

    def test_store_crud(self):
        with self.app_context():
            store = StoreModel('crud store')
            self.assertIsNone(StoreModel.find_by_name('crud store'))

            store.save_to_db()
            self.assertIsNotNone(StoreModel.find_by_name('crud store'))

            store.delete_from_db()
            self.assertIsNone(StoreModel.find_by_name('crud store'))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('store')
            item = ItemModel('item', 20, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, 'item')

from models.item import ItemModel
from models.store import StoreModel
from tests.integration.integration_base_test import IntegrationBaseTest


class ItemTestIntegration(IntegrationBaseTest):
    def test_crud(self):
        with self.app_context():
            self.assertIsNone(StoreModel.find_by_name('test store'),
                              f"Found store named \'test store\', but expected not to.")

            store = StoreModel('test store')
            store.save_to_db()

            self.assertIsNotNone(StoreModel.find_by_name('test store'),
                                 f"Expected to find store named {store.name}, but did not found one.")

            item = ItemModel('test', 19.99, store.id)
            self.assertIsNone(ItemModel.find_by_name('test'),
                              f"Found an item with name {item.name}, but expected not to.")

            item.save_to_db()
            self.assertIsNotNone(ItemModel.find_by_name('test'))

            item.delete_from_db()
            self.assertIsNone(ItemModel.find_by_name('test'))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('test store')
            item = ItemModel('test', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(item.store.name, 'test store')

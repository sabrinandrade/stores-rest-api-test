from unittest import TestCase
from models.item import ItemModel


class ItemModelTesT(TestCase):
    def setUp(self):
        pass

    def test_create_new_item(self):
        item = ItemModel('new item', 500)

        self.assertEqual(item.name, 'new item', "The name of the item does not match")
        self.assertEqual(item.price, 500, "The price of the item does not match")

    def test_item_json(self):
        item = ItemModel('new item', 500)
        expected = {
            'name': 'new item',
            'price': 500
        }

        self.assertEqual(item.json(), expected,
                         "The information contained in the json: {} is not: {}".format(item.json(), expected))

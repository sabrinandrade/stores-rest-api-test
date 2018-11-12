# each test suite is a class
# it has to inherit TestCase

from unittest import TestCase
from post import Post


# Smallest units that can be tested
class PostTest(TestCase):
    def test_create_post(self):
        p = Post('Test title', 'Test content')

        self.assertEqual('Test title', p.title)
        self.assertEqual('Test content', p.content)

    def test_json(self):
        p = Post('Test title', 'Test content')
        expected = {
            'title': 'Test title',
            'content': 'Test content'
        }

        self.assertDictEqual(expected, p.json())

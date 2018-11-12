from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_first_post(self):
        b = Blog("Blog title", "Blog author")
        b.create_post('Title', 'Content')

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'Title')
        self.assertEqual(b.posts[0].content, 'Content')

    def test_json_with_no_posts(self):
        b = Blog("Blog title", "Blog author")

        expected = {
            'title': 'Blog title',
            'author': 'Blog author',
            'posts': [],
        }

        self.assertDictEqual(expected, b.json())

    def test_json(self):
        b = Blog("Blog title", "Blog author")
        b.create_post('Title', 'Content')

        expected = {
            'title': 'Blog title',
            'author': 'Blog author',
            'posts':
                [{
                    'title': 'Title',
                    'content': 'Content'
                }],
        }

        self.assertDictEqual(expected, b.json())

from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog("Blog title", "Blog author")

        self.assertEqual("Blog title", b.title)
        self.assertEqual("Blog author", b.author)
        self.assertListEqual([], b.posts)
        # self.assertEqual(0, len(b.posts))

    def test_repr(self):
        b = Blog("Blog title", "Blog author")
        b2 = Blog("My Day", "Rolf")

        self.assertEqual(b.__repr__(), 'Blog title by Blog author (0 posts)')
        self.assertEqual(b2.__repr__(), 'My Day by Rolf (0 posts)')

    def test_repr_multiple_posts(self):
        b = Blog("Blog title", "Blog author")
        b.posts = ['test']

        b2 = Blog("My Day", "Rolf")
        b2.posts = ['test' for x in range(5)]

        self.assertEqual(b.__repr__(), 'Blog title by Blog author (1 post)')
        self.assertEqual(b2.__repr__(), 'My Day by Rolf (5 posts)')

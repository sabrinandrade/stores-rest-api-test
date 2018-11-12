from unittest import TestCase
from unittest.mock import patch
from blog import Blog
from post import Post
import app


class AppTest(TestCase):
    def setUp(self):
        pass

    # Tests menu options
    def test_menu_call_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = (1, 'Test Create Blog', 'Blog Author', 5)
            app.menu()

            self.assertIsNotNone(app.blogs['Test Create Blog'])

    def test_menu_call_print_blogs(self):
        blog = Blog('Test Print Blog With Menu', 'Blog Author')
        app.blogs = {'Test Print Blog With Menu': blog}

        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = (2, 5)
                app.menu()
                mocked_print.assert_called_with('- Test Print Blog With Menu by Blog Author (0 posts)')

    def test_menu_call_read_blog(self):
        blog = Blog('Test Read Blog With Menu', 'Blog Author')
        post = Post('Post Title Read Blog With Menu', 'Post Content')
        blog.posts.append(post)

        app.blogs = {'Test Read Blog With Menu': blog}

        with patch('builtins.input') as mocked_input:
            with patch('app.ask_read_blog') as mocked_call:
                mocked_input.side_effect = (3, 5)
                app.menu()
                mocked_call.assert_called()

    def test_menu_call_create_post(self):
        blog = Blog('Test Create Blog Post With Menu', 'Blog Author')
        app.blogs = {'Test Create Blog Post With Menu': blog}

        with patch('builtins.input') as mocked_input:
            with patch('app.ask_create_post') as mocked_call:
                mocked_input.side_effect = (4, 5)
                app.menu()
                mocked_call.assert_called()

##

    # Tests if the input option was called with the correct input
    def test_menu_print_prompt(self):
        with patch('builtins.input', return_value=5) as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    # Tests if the menu calls the print_blogs function
    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_call:
            # If you patch the call, it does nothing, so we are stuck waiting for the user input
            # With the patch on the input function, the execution can continue
            with patch('builtins.input', return_value='5'):
                app.menu()
                mocked_call.assert_called()

    # Tests if the print_blogs presented the correct output
    def test_print_blogs(self):
        blog = Blog('Test Print Blogs', 'Test Author')
        app.blogs = {'Test Print Blogs': blog}

        # Patching the print method
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test Print Blogs by Test Author (0 posts)')

    # Tests if the blog creation is working correctly
    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            # Everytime the function is called, the value on the tuple is passed
            mocked_input.side_effect = ('Test', 'Test Author')
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get('Test'))

    # Tests if ask_read_blog calls prints_posts passing the correct argument
    def test_ask_read_blog(self):
        blog = Blog('Test Read Blog', 'Test Author')
        app.blogs = {'Test Read Blog': blog}

        with patch('builtins.input', return_value='Test Read Blog'):
            with patch('app.print_posts') as mocked_call:
                app.ask_read_blog()
                mocked_call.assert_called_with(blog)

    # Tests if print_posts calls print_post passing the correct argument
    def test_print_posts(self):
        blog = Blog('Test Print Posts', 'Test Author')
        blog.create_post('Test Post', 'Test Content')
        app.blogs = {'Test Print Posts': blog}

        with patch('app.print_post') as mocked_call:
            app.print_posts(blog)
            mocked_call.assert_called_with(blog.posts[0])

    # Tests if print_post prints the correct information
    def test_print_post(self):
        post = Post('Post Title', 'Post Content')
        expected = app.POST_TEMPLATE.format('Post Title', 'Post Content')

        with patch('builtins.print') as mocked_print:
            app.print_post(post)
            mocked_print.assert_called_with(expected)

    # Tests if the create_post function is working correctly
    def test_ask_create_post(self):
        blog = Blog('Test Create Post', 'Test Author')
        app.blogs = {'Test Create Post': blog}

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test Create Post', 'Post Title', 'Post Content')

            app.ask_create_post()

            self.assertEqual(blog.posts[0].title, 'Post Title')
            self.assertEqual(blog.posts[0].content, 'Post Content')

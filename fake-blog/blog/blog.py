from post import Post


class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    # Defines how the object will be presented when printed
    def __repr__(self):
        # return 'Blog title by Blog author (0 posts)'
        return '{} by {} ({} post{})'.format(self.title,
                                             self.author,
                                             len(self.posts),
                                             's' if len(self.posts) != 1 else '')

    def create_post(self, title, content):
        new_post = Post(title, content)
        self.posts.append(new_post)

    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': [post.json() for post in self.posts],
        }

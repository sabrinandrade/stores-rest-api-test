from blog import Blog


MENU_PROMPT = "Enter \"1\" to create a new blog" \
              "\n\"2\" to list blogs" \
              "\n\"3\" to read one" \
              "\n\"4\" to create a post or" \
              "\n\"5\" to quit: "

POST_TEMPLATE = '''
    Title: {}
    
    Content: {}
    '''

blogs = dict()  # blog_name: Blog object


def menu():
    print_blogs()
    selection = input(MENU_PROMPT)

    while selection != 5:
        if selection == 1:
            ask_create_blog()
        elif selection == 2:
            print_blogs()
        elif selection == 3:
            ask_read_blog()
        elif selection == 4:
            ask_create_post()
        else:
            break;
        selection = input(MENU_PROMPT)


def ask_create_blog():
    title = input("Type in the blog title: ")
    author = input("Type in the blog author: ")

    blogs[title] = Blog(title, author)


def print_blogs():
    for key, blog in blogs.items():
        print("- {}".format(blog))


##


def ask_read_blog():
    title = input("Type in the blog title: ")

    print_posts(blogs[title])


def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


##


def ask_create_post():
    blog_name = input('Type the name of the blog you want to write a post in: ')
    title = input('Type the post title: ')
    content = input('Type the post content: ')

    blogs[blog_name].create_post(title, content)


menu()
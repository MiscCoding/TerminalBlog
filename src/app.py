from src.database import Database
from src.model.blog import Blog
from src.model.post import Post

__author__ = 'jslvtr'

Database.initialize()

'''
#post = Post(blog_id = "123",
           ## title="Another great post",
           ## content="123432dsfasdf",
            ##author="Jose")

posts = Post.from_blog('123')
#post.save_to_mongo()
for post in posts:
    print(post)  '''

blog = Blog(author ="Jose",
            title = "Sample title",
            description="Sample description")

blog.new_post()

blog.save_to_mongo(blog.id)

from_database = Blog.from_mongo(blog.id)

print(blog.get_posts())
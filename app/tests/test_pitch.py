import unittest
from app.models import Comment, User, blog
from app import db


class blogModelTest(unittest.TestCase):
    def setUp(self):
        self.user_emma = User(
            username='emma', password='potato', email='emma@ms.com')
        self.new_blog = blog(id=1, blog_title='Test', blog_content='This is a test blog',
                               category="interview", user=self.user_emma)

    def tearDown(self):
        blog.query.delete()
        User.query.delete()
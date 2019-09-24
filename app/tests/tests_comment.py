import unittest
from app import db
from app.models import Comment, User, blog

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_emma = User(username = 'emma', password = 'potato', email = 'emma@ms.com')
        self.new_blog = blog(id = 1, blog_title = 'Test', blog_content = 'This is a test blog', category = 'interview', user = self.user_emma)
        self.new_comment = Comment(id = 1, comment = 'Test comment', user = self.user_emma, blog_id = self.new_blog)
        
    def tearDown(self):
        blog.query.delete()
        User.query.delete()
    
    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'Test comment')
        self.assertEquals(self.new_comment.user,self.user_emma)
        self.assertEquals(self.new_comment.blog_id,self.new_blog)

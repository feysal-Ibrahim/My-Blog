from app.models import Comment,User
from app import db
import unittest

class CommentTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''
    def setUp(self):
        self.user_feysal = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_comment = Comment(post_id=6737,pitch_title='Review comments',image_path="https://image.io",movie_review='This movie is the best thing since sliced bread',user = self.user_James )

    def tearDown(self):
        Comment.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.pitch_id,12345)
        self.assertEquals(self.new_comment.pitch_title,'Review for movies')
        self.assertEquals(self.new_comment.image_path,"https://image.tmdb.org/t/p/w500/jdjdjdjn")
        self.assertEquals(self.new_comment.pitch_comment,'This movie is the best thing since sliced bread')
        self.assertEquals(self.new_comment.user,self.user_James)

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

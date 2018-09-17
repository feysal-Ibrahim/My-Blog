import unittest
from app.models import Post
Pitch = Post

class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Post class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_pitch = Post(6737,'am a savage')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))

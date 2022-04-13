
from django.test import TestCase

from App.views import profile
from .models import Profile, Post,Revieww



class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile=Profile(User='Veronica')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))


class PostTestClass(TestCase):
    def setUp(self):
        self.post=Post(title='Project1')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))  

class ReviewwTestClass(TestCase):
    def setUp(self):
        self.revieww=Revieww(text='Incredible')

    def test_instance(self):
        self.assertTrue(isinstance(self.revieww, Revieww))  


        





        



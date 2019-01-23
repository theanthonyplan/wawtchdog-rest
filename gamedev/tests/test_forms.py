from django.test import TestCase
from .models import Author, Game, Report
from pprint import pprint as p # prettify our ouput
from django.contrib.auth import get_user_model




# tests for comment models
class CommentFormTest(TestCase):
    def create_dummy_user():
        from django.test import Client
        c = Client()
        response = c.post('/login/', {'username': 'john', 'password': 'smith'})


    def setUp(self):
        user = get_user_model().objects.create_user('zoidberg')
        self.entry = Entry.objects.create(author=user, title="My entry title")

    # test fields of the forms

    # test creation of form objects

    # test output of rendered forms

    # test form validators

    # exclude unneeded values

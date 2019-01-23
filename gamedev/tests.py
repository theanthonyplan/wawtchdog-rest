from django.test import RequestFactory, TestCase
from django.contrib.auth import get_user_model
from django.core.urlresolvers import resolve
from django.contrib.auth.models import AnonymousUser, User

from pprint import pprint as p              # prettify our ouput
from .models import Author, Game, Report
from .views import *



# Tests for the Project global scope
class ProjectTests(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)




# Functional Tests for homepage

class HomePageTests(TestCase):

    """Test whether our blog entries show up on the homepage"""

    def setUp(self):
        self.user = get_user_model().objects.create(username='some_user')

    """Test whether the root url resolves to our home_page view."""
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/hometest2') #
        self.assertEqual(found.func, home_page)


    # OLD SITE FUNCTIONAL TESTS
    # def test_one_game(self):
    #     Game.objects.create(title="Florp Deraux", appid=123451)
    #     response = self.client.get('/home')
    #     p(response)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'Florp Deraux')
    #     self.assertContains(response, 123451)
    #
    # def test_two_games(self):
    #     Game.objects.create(title="Florp Deraux", appid=123451)
    #     Game.objects.create(title="Apero Bitteranmint", appid=412441)
    #     response = self.client.get('/home')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'Florp Deraux')
    #     self.assertContains(response, 123451)
    #     self.assertContains(response, 'Apero Bitteranmint')
    #     self.assertContains(response, 412441)
    #
    # def test_no_entries(self):
    #     response = self.client.get('/home')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'No blog entries yet.')
    #

# from .views import MyView, my_view
# class SimpleTest(TestCase):
#     def setUp(self):
#         # Every test needs access to the request factory.
#         self.factory = RequestFactory()
#         self.user = User.objects.create_user(username='jacob', email='jacob@saa.com', password='top_secret')
#
#     def test_details(self):
#         # Create an instance of a GET request.
#         request = self.factory.get('/customer/details')
#
#         # Recall that middleware are not supported. You can simulate a
#         # logged-in user by setting request.user manually.
#         request.user = self.user
#
#         # Or you can simulate an anonymous user by setting request.user to
#         # an AnonymousUser instance.
#         request.user = AnonymousUser()
#
#         # Test my_view() as if it were deployed at /customer/details
#         response = my_view(request)
#         # Use this syntax for class-based views.
#         response = MyView.as_view()(request)
#         self.assertEqual(response.status_code, 200)

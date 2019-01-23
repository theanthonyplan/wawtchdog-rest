from django.test import TestCase
from .models import Author, Game, Report
from pprint import pprint as p # prettify our ouput
from django.contrib.auth import get_user_model

# Tests for game views
# also makes sure that the template tree is properly formed
class GameViewTest(TestCase):
    def setUp(self):
        #self.user = get_user_model().objects.create(username='some_user')
        self.game = Game.objects.create(title='asx', appid=123321)

    def test_basic_view(self):
        response = self.client.get(self.game.get_absolute_url())
        self.assertEqual(response.status_code, 200)

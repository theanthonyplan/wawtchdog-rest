from django.test import TestCase
from .models import Author, Game, Report
from pprint import pprint as p # prettify our ouput
from django.contrib.auth import get_user_model


# Tests for Author models
class AuthorModelTest(TestCase):
    def test_string_representation(self):
        author = Author(title="My author title")
        self.assertEqual(str(author), author.title)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Author._meta.verbose_name_plural), "authors")

# Tests for Game models
class GameModelTest(TestCase):
    def test_string_representation(self):
        game = Game(title="Terp", appid=123451)
        self.assertEqual(str(game), game.title)     # test the _str_ method
        game.save()             # save objects
        print '\n\n'

    def test_verbose_name_plural(self):
        self.assertEqual(str(Game._meta.verbose_name_plural), "games")

# Tests for Report models
class ReportModelTest(TestCase):
    def test_string_representation(self):
        report = Game(title="Terpaad", appid=123456)
        self.assertEqual(str(report), report.title)     # test the _str_ method
        report.save()             # save objects
        print '\n\n'

    def test_verbose_name_plural(self):
        self.assertEqual(str(Report._meta.verbose_name_plural), "reports")

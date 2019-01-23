# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings
from django.forms import ModelForm

from mezzanine.core.models import Displayable, Ownable, RichText, Slugged
from mezzanine.generic.fields import CommentsField, RatingField

# drum stuff for comments, ratings, and karma
from mezzanine.generic.models import Rating, Keyword, AssignedKeyword
from mezzanine.generic.fields import RatingField, CommentsField
# drum model for links
from drum.links.models import Link

# Import mezzanine stuff
from mezzanine.core.models import Displayable
from mezzanine.utils.models import base_concrete_model

# Import urllib to encode strings for urls
import urllib

# utility function to encode strings into urls
def build_steam_url(kind, text):
    prepend = ''
    host  = 'https://store.steampowered.com/'
    if kind == 'APP':
        prepend = 'app/'
    elif kind == 'DEV':
        prepend = 'search/?developer/'
    elif kind == 'PUB':
        prepend = 'search/?publisher/'
    else:
        prepend = 'search/?term='

    url = host +  prepend + urllib.quote_plus(text)

    return url

# AUTHOR - This is how we will represent devs/publishers
# Game objects will have foreign key fields for developer and publisher
# Games can have one, many, or none Author objects associated for these fields
class Author(models.Model):
    DEV = 'DEV'
    PUB = 'PUB'
    ROLES = (
        (DEV, 'Developer'),
        (PUB, 'Publisher')
    )

    # define some fields
    title = models.CharField(max_length=500)        # a name for our author
    role = models.CharField(                        # role/relation to game
        max_length=3,
        choices=ROLES,
        default=DEV,
    )
    steam_url = models.CharField(                   # a url to their steam page
            max_length=500,
            blank=True,
    )

    # def some functions
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        If no steam_url is provided, generates one before saving.
        """
        if not self.steam_url:
            self.steam_url = self.generate_unique_steam_url()
        super(Author, self).save(*args, **kwargs)

    def generate_unique_steam_url(self):
        """
        Create a unique steam_url by passing the result of build_steam_url().
        """
        return build_steam_url(self.role, self.title)

    def get_steam_url(self):
        """
        Allows subclasses to implement their own steam_url creation logic.
        """
        attr = "title"
        # Get self.title_xx where xx is the default language, if any.
        # Get self.title otherwise.
        return build_steam_url(self.role, getattr(self, attr, None) or self.title)

class Game(models.Model):
    title = models.CharField(max_length=500)        # a name for our Game
    appid = models.IntegerField(unique=True)

    # Use our Author model as a foreign key.
    developer = models.ForeignKey('Author', related_name='developer', on_delete=models.CASCADE, blank=True, null=True)
    publisher = models.ForeignKey('Author', related_name='publisher',on_delete=models.CASCADE, blank=True, null=True)

    # url to steam page
    steam_url = models.CharField(max_length=500,blank=True)

    price = models.CharField(max_length=8, blank=True, null=True)
    app_type =      models.CharField(max_length=50, blank=True, null=True)
    description =   models.TextField(max_length=10000, blank=True, null=True)    # product description
    categories =    models.TextField(max_length=200, blank=True, null=True)
    genres  =       models.TextField(max_length=200, blank=True, null=True)
    release_date =  models.CharField(max_length=20, blank=True, null=True)
    reviews_total = models.IntegerField(blank=True, null=True)

    product_url = models.URLField(max_length=300,blank=True, null=True)
    support_url = models.URLField(max_length=300, blank=True, null=True)
    support_email = models.EmailField(blank=True, null=True)

    header_image = models.URLField(max_length=300,blank=True, null=True)
    background_image = models.URLField(max_length=300,blank=True, null=True)
    screenshots = models.TextField(max_length=2000, blank=True, null=True)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    # def some functions
    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('game_detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        """
        If no steam_url is provided, generates one before saving.
        """
        if not self.steam_url:
            self.steam_url = self.generate_unique_steam_url()
        super(Game, self).save(*args, **kwargs)

    def generate_unique_steam_url(self):
        """
        Create a unique steam_url by passing the result of build_steam_url().
        """
        return build_steam_url('APP', str(self.appid))


class Report(Displayable, Ownable):
    game = models.ForeignKey(Game)
    # link = models.URLField(null=True,
    #     blank=(not getattr(settings, "LINK_REQUIRED", False)))
    rating = RatingField()
    # comments = CommentsField()


    # body = models.TextField()

class ReportComment(Displayable,Ownable):
    report = models.ForeignKey(Game)
    message = models.TextField(max_length=3000)    # product description


# class ReportCommentForm(ModelForm):
#     class Meta:
#         model = ReportComment
#         fields = [ 'message', 'report']
#         exclude = ['title']




class Review():
    pass

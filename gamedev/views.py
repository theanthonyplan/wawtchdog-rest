# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Author, Game


# tdd views from part 1
class HomeView(ListView):
    template_name = 'index.html'
    queryset = Game.objects.order_by('-created_at')


class GameDetail(DetailView):
    model = Game


# Create your tdd views here.
# tdd views from part 2
# Create your views here.
def home_page():
    pass

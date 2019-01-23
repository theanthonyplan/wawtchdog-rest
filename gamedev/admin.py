# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Import some mezzanine stuff
from mezzanine.pages.models import Page
# Register your models here.
from .models import Author, Game, Report,ReportComment





admin.site.register(Author)
admin.site.register(Game)
admin.site.register(Report)
admin.site.register(ReportComment)

from __future__ import unicode_literals
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework_swagger.views import get_swagger_view

from gamedev import views as gamedev_views
from gamedev import urls as gamedev_urls

from django.conf import settings
from django.conf.urls import include, url  # For django versions before 2.0

admin.autodiscover()

swagger_view = get_swagger_view(title='Mezzanine API')      # get our swagger views

urlpatterns = [
    url("^admin/", include(admin.site.urls)),            # link in urls for the admin
    url("^api/", include("mezz_api.urls")),    # REST API URLs
    url(r'^hometest1$', gamedev_views.HomeView.as_view(), name='hometest1'),  #test url
    url(r'^hometest2$', gamedev_views.home_page, name='hometest2'),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^', include(gamedev_urls)),           # link in our gamedev urls
    url("^", include("drum.links.urls")),       # drum urls
    url("^", include("mezzanine.urls")),        # mezzanine urls
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        # path('__debug__/', include(debug_toolbar.urls)),
        # For django versions before 2.0:
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns



# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"

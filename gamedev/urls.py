from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.GameDetail.as_view(), name='game_detail'),
]

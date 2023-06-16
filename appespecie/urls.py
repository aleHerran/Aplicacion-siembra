from django.urls import re_path as url, path
from . import views

urlpatterns = [ url(r'^$', views.index, name='index'),
]
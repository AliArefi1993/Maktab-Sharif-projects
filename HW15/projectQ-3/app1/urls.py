from functools import partialmethod
from django.urls import path
from . import views
urlpatterns = [path("get-name/", views.get_name, name='post_new')]

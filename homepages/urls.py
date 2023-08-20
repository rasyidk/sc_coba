# example/urls.py
from django.urls import path

from homepages.views import index


urlpatterns = [
    path("", index),
]

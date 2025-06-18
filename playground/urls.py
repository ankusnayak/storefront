# Import path funtions from django.urls
from django.urls import path
# from current folder import views module
from . import views

""" In urls module we gonna map urls to views or view function.
"""
# URLConf
urlpatterns = [
    # arrays of urlpatterns objects.
    # use path function for creating url

    # always ends routes with forward slash
    path('hello/', views.say_hello)
]

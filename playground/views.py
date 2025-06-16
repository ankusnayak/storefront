from django.shortcuts import render
from django.http import HttpResponse


""" Its kind of request handler.
"""

# Views or ViewFunction (A view function is a function that takes a request \
# and return a response)
# request handler
# In django its a view (request handler)
# So in django views module is used for handle the request.


def say_hello(request):
    return HttpResponse('Hello World')

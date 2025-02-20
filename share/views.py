from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def my_share(request):
    return HttpResponse("Hello, Book sharers!")

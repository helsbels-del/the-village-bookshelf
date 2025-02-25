from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def my_share(request):
    return HttpResponse("Hello, Book sharers!")


def home(request):
    """Homepage for the book-sharing app."""
    return render(request, 'share/index.html')
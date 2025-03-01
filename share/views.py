from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def my_share(request):
    return HttpResponse("Hello, Book sharers!")


def home(request):
    """Homepage for the book-sharing app."""
    return render(request, 'share/index.html')


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # Redirect to login page
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
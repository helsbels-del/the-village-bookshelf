from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .models import Books
from .forms import BookForm
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.core.paginator import Paginator

# Create your views here.


def about(request):
    return render(request, 'about.html')


def clear_all_sessions():
    Session.objects.all().delete()


def my_share(request):
    return HttpResponse("Hello, Book sharers!")


def home(request):
    """Homepage for the book-sharing app."""
    books = Books.objects.all()
    paginator = Paginator(books, 1000)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'share/index.html', {'page_obj': page_obj})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # Redirect to login page
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('book_list')  # Redirect after successful login
        else:
            # Handle invalid login
            pass
    return render(request, 'login.html')


def search_books(request):
    query = request.GET.get('q', '')
    books = Books.objects.filter(title__icontains=query) if query else []
    return render(request, 'books/search_results.html', {'books': books, 'query': query})


def book_list(request):
    books = Books.objects.all()
    paginator = Paginator(books, 1000)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "books/book_list.html", {"page_obj": page_obj})


def book_detail(request,  pk):
    book = get_object_or_404(Books, pk=pk)
    return render(request, "books/book_detail.html", {"book": book})


@login_required
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user  # Assign the current user as the owner
            book.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "books/book_form.html", {"form": form})


@login_required
def book_update(request, pk):
    book = get_object_or_404(Books, pk=pk, owner=request.user)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "books/book_form.html", {"form": form})


@login_required
def book_delete(request, pk):
    book = get_object_or_404(Books, pk=pk, owner=request.user)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "books/book_confirm_delete.html", {"book": book})


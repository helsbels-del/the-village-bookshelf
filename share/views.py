from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from .models import Books, SwapRequest
from .forms import BookForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.db.models import Q


def custom_404(request, exception):
    return render(request, "404.html", status=404)


def about(request):
    return render(request, 'about.html')


def clear_all_sessions():
    Session.objects.all().delete()


def my_share(request):
    return HttpResponse("Hello, Book sharers!")


def home(request):
    latest_books = Books.objects.order_by('-id')[:6]
    return render(request, 'share/index.html', {'latest_books': latest_books})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request,
                f'Account created successfully. Welcome, {user.username}!'
            )
            return redirect('book_list')
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next', '/book_list/')
            return redirect(next_url)
        else:
            messages.error(
                request,
                "Invalid email or password. Please try again."
            )
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def search_books(request):
    query = request.GET.get('q', '').strip()
    if query:
        books = Books.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
        return render(
            request,
            'books/search_results.html',
            {'books': books, 'query': query}
        )
    else:
        messages.warning(request, "Please enter a search term.")
        return redirect('home')


@login_required
def book_list(request):
    books = Books.objects.all().order_by('title')
    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "books/book_list.html", {"page_obj": page_obj})


def all_books(request):
    books = Books.objects.all().order_by('title')
    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'share/all_books.html', {'page_obj': page_obj})


def book_detail(request, pk):
    book = get_object_or_404(Books, pk=pk)
    return render(request, "books/book_detail.html", {"book": book})


@login_required
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            author = form.cleaned_data["author"]
            existing_book = Books.objects.filter(
                title__iexact=title,
                owner=request.user
            ).exists()

            if existing_book:
                messages.error(request, "You have already added this book.")
            else:
                book = form.save(commit=False)
                book.owner = request.user
                book.save()
                messages.success(
                    request,
                    "Your book has been added successfully!"
                )
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
            messages.success(
                request,
                "The book details have been updated successfully!"
            )
            return redirect("book_list")
    else:
        form = BookForm(instance=book)

    return render(request, "books/book_form.html", {"form": form})


@login_required
def book_delete(request, pk):
    book = get_object_or_404(Books, pk=pk, owner=request.user)
    if request.method == "POST":
        book.delete()
        messages.success(request, "The book has been deleted successfully!")
        return redirect("book_list")
    return render(
        request,
        "books/book_confirm_delete.html",
        {"book": book}
    )


@login_required
def request_swap(request, pk):
    book = get_object_or_404(Books, pk=pk)

    if request.user == book.owner:
        messages.error(request, "This is your own book.")
        return redirect('book_detail', pk=pk)

    existing_request = SwapRequest.objects.filter(
        requester=request.user,
        book=book
    ).exists()

    if existing_request:
        messages.warning(request, "You have already requested this book.")
        return redirect('book_detail', pk=pk)

    swap_request = SwapRequest.objects.create(
        requester=request.user,
        book=book
    )
    swap_request.save()

    if book.owner and hasattr(book.owner, "email") and book.owner.email:
        send_mail(
            subject="Book Swap Request",
            message=(
                f"Hello {book.owner.username},\n\n"
                f"{request.user.username} has requested to swap your book "
                f"'{book.title}'. Please make contact to arrange the swap."
            ),
            from_email="noreply@villagebookshelf.com",
            recipient_list=[book.owner.email],
            fail_silently=False,
        )
        messages.success(request, "Your swap request has been sent!")
    else:
        messages.error(
            request,
            "This book has no registered owner email. "
            "Your request has not been sent."
        )

    return redirect('book_detail', pk=pk)

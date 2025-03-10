from django.urls import path
from . import views  # Import views from the current app
from .views import signup
from django.contrib.auth.views import LogoutView
from .views import search_books
from .views import about
from .views import book_detail


urlpatterns = [
    path('', views.home, name='home'),  # Homepage for "share" app
    path('books/', views.book_list, name="book_list"),  # Logged in page now shows books
    path('signup/', views.signup, name='signup'),  # Signup page
    path('login/', views.login_view, name='login'),  # Custom login page
    path('logout/', LogoutView.as_view(), name='logout'),  # Built-in logout view   
    path('search/', views.search_books, name='search_books'),
    path('book/new/', views.book_create, name="book_create"),
    path('book/<int:pk>/edit/', views.book_update, name="book_update"),
    path('book/<int:pk>/delete/', views.book_delete, name="book_delete"),
    path('about/', views.about, name='about'),
    path('book/<int:pk>/', views.book_detail, name=('book_detail')),
    path('bookint:pk>/', book_detail, name='book_detail'),
    ]
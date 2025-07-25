from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

from . import views
from .views import custom_404
from .forms import CustomLoginForm


urlpatterns = [
    path('', views.home, name='home'),  # Homepage for "share" app
    path(
        'book_list/',
        views.book_list,
        name="book_list"
    ),  # Logged-in page now shows books
    path('all_books/', views.all_books, name='all_books'),
    path('signup/', views.signup, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('search/', views.search_books, name='search_books'),
    path('book/new/', views.book_create, name="book_create"),
    path(
        'book/<int:pk>/edit/',
        views.book_update,
        name="book_update"
    ),
    path(
        'book/<int:pk>/delete/',
        views.book_delete,
        name="book_delete"
    ),
    path('about/', views.about, name='about'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path(
        'book/<int:pk>/request_swap/',
        views.request_swap,
        name='request_swap'
    ),
    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset_form.html'
        ),
        name='password_reset'
    ),
    path(
        'password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html'
        ),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
    path('404/', views.custom_404, name='404'),
    path(
        'login/',
        auth_views.LoginView.as_view(
            authentication_form=CustomLoginForm,
            template_name='registration/login.html'
        ),
        name='login'
    ),
]

# Custom 404 Error Handler (defined after urlpatterns)
handler404 = custom_404

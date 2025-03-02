from django.urls import path
from . import views  # Import views from the current app
from .views import signup
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.home, name='home'),  # Homepage for "share" app
    path('signup/', views.signup, name='signup'),  # Signup page
    path('login/', views.login_view, name='login'),  # Custom login page
    path('logout/', LogoutView.as_view(), name='logout'),  # Built-in logout view   
    path('search/', views.search_books, name='search_books'), 
]
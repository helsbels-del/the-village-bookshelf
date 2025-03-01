from django.urls import path
from . import views  # Import views from the current app
from .views import signup
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.home, name='home'),  # Homepage for "share" app
    path('signup/', signup, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout-success/', TemplateView.as_view(template_name="registration/logout.html"), name='logout_success'),
]

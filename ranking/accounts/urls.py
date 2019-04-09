from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login', LoginView.as_view(template_name='accounts/login.html')),
    path('', views.home, name='home'),
]
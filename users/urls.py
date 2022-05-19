from django.contrib.auth.views import LoginView, LogoutView, logout_then_login
from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("logout-then-login/", logout_then_login, name="logout_then_login"),
    path("register/", views.register, name="register"),
]

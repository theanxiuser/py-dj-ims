from django.urls import path
from .views import LoginView, RegistrationView, logout


app_name = "userauth"
urlpatterns = [
    path("login", LoginView.as_view(), name="login"),
    path("register", RegistrationView.as_view(), name="register"),
    path("logout", logout, name="logout"),
]
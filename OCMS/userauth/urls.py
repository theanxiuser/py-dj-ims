from django.urls import path
from .views import LoginView, RegistrationView, logout, ProfileUpdateView, ProfileView

app_name = "userauth"
urlpatterns = [
    path("login", LoginView.as_view(), name="login"),
    path("register", RegistrationView.as_view(), name="register"),
    path("logout", logout, name="logout"),
    path("update-profile", ProfileUpdateView.as_view(), name="update-profile"),
    path("profile", ProfileView.as_view(), name="profile"),
]
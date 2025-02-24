from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import views
from django.contrib.auth import logout as auth_logout
from .forms import UserRegistrationForm
from django.views.generic import CreateView
from .models import CustomUser


def logout(request):
    auth_logout(request)
    return redirect("home")


class LoginView(views.LoginView):
    template_name = "auth/login.html"
    # success_url = "home"

    # def get_success_url(self):
    #     return redirect(reverse_lazy(self.success_url))


class RegistrationView(View):
    form = UserRegistrationForm
    template_name = "auth/registration.html"
    success_url = reverse_lazy("userauth:login")

    def get(self, request):
        form = self.form()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {"form": form})
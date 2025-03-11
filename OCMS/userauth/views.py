from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import views
from django.contrib.auth import logout as auth_logout
from .forms import UserRegistrationForm, ProfileForm
from django.views.generic import UpdateView, DetailView
from .models import CustomUser, Profile


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "auth/profile-update.html"
    success_url = reverse_lazy("userauth:profile")

    def get_object(self):
        return self.request.user.profile

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Your profile has been updated successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, "Please correct the errors below.")
        messages.error(self.request, form.errors)
        return self.render_to_response(self.get_context_data(form=form))


class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "auth/profile.html"

    def get_object(self):
        return self.request.user


def logout(request):
    auth_logout(request)
    messages.success(request, "You have been logged out.")
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
            messages.success(request, "Account created successfully.")
            return redirect(self.success_url)
        return render(request, self.template_name, {"form": form})
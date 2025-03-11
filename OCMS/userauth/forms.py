from django.contrib.auth.forms import UserCreationForm
from django import forms

from userauth.models import ROLE_CHOICES, CustomUser, Profile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ["bio", "phone", "image"]
        widgets = {
            "bio": forms.Textarea(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
        }


class UserRegistrationForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = CustomUser
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        }
        fields = ("username", "first_name", "last_name", "email", "role", "password1", "password2")
from django.forms.models import ModelForm
from django import forms

from .models import Course


class CourseCreationForm(ModelForm):
    class Meta:
        model = Course
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "instructor": forms.Select(attrs={"class": "form-control"}),
            "students": forms.SelectMultiple(attrs={"class": "form-control"}),
        }
        fields = ("title", "description", "instructor", "students")

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from course.models import Course
from .forms import CourseCreationForm
from .mixin import InstructorRequiredMixin


class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = "course/courses.html"
    context_object_name = "courses"

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.is_instructor():
            return Course.objects.filter(instructor=self.request.user)
        return Course.objects.filter(students=self.request.user)


class CourseCreateView(InstructorRequiredMixin, CreateView):
    form_class = CourseCreationForm
    template_name = "course/course-create.html"
    success_url = "/courses/"


class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = "course/course-detail.html"
    context_object_name = "course"

class CourseUpdateView(InstructorRequiredMixin, UpdateView):
    form_class = CourseCreationForm
    template_name = "course/course-update.html"
    success_url = "/courses/"

    def get_object(self, queryset=None):
        return Course.objects.get(pk=self.kwargs.get("pk"))

class CourseDeleteView(InstructorRequiredMixin, DeleteView):
    model = Course
    template_name = "course/course-delete.html"
    success_url = "/courses/"

    def get_object(self, queryset=None):
        return Course.objects.get(pk=self.kwargs.get("pk"))
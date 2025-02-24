from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from course.models import Course
from .forms import CourseCreationForm


class CourseListView(ListView):
    model = Course
    template_name = "course/courses.html"
    context_object_name = "courses"


class CourseCreateView(CreateView):
    form_class = CourseCreationForm
    template_name = "course/course-create.html"
    success_url = "/courses/"


class CourseDetailView(DetailView):
    model = Course
    template_name = "course/course-detail.html"
    context_object_name = "course"

class CourseUpdateView(UpdateView):
    form_class = CourseCreationForm
    template_name = "course/course-update.html"
    success_url = "/courses/"

    def get_object(self, queryset=None):
        return Course.objects.get(pk=self.kwargs.get("pk"))

class CourseDeleteView(DeleteView):
    model = Course
    template_name = "course/course-delete.html"
    success_url = "/courses/"

    def get_object(self, queryset=None):
        return Course.objects.get(pk=self.kwargs.get("pk"))
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from course.models import Course


class CourseListView(ListView):
    model = Course
    template_name = "course/courses.html"
    context_object_name = "courses"

class CourseCreateView(CreateView):
    pass

class CourseDetailView(DetailView):
    model = Course
    template_name = "course/course-detail.html"
    context_object_name = "course"

class CourseUpdateView(UpdateView):
    pass

class CourseDeleteView(DeleteView):
    pass
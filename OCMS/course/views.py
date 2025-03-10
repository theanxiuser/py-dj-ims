from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.views import View
from .models import Course, MCQ, Response
from .forms import CourseCreationForm
from .mixin import InstructorRequiredMixin, StudentRequiredMixin


class SolveMCQView(StudentRequiredMixin, View):
    def get(self, request, course_id):
        course = get_object_or_404(Course, pk=course_id)
        mcqs = course.mcqs.all()
        return render (request, "course/solve-mcq.html", {"course": course, "mcqs": mcqs})

    def post(self, request, course_id):
        correct_mcqs = 0
        student = request.user
        for key, value in request.POST.items():
            if key == "csrfmiddlewaretoken":
                continue
            mcq = MCQ.objects.get(id=key)
            res = Response.objects.create(mcq=mcq, student=student, selected_option=int(value))
            if res.is_correct:
                correct_mcqs += 1

        messages.info(request, f"{correct_mcqs} MCQs are correct.")
        return redirect("course:course-detail", pk=course_id)


class MCQCreateView(InstructorRequiredMixin, View):
    def get(self, request, course_id):
        course = get_object_or_404(Course, pk=course_id)
        return render(request, "course/create-mcq.html", {"course": course})

    def post(self, request, course_id):
        course = get_object_or_404(Course, pk=course_id)
        # print(request.POST)

        # Receiving the data from the form
        questions = request.POST.getlist("question")
        options_1 = request.POST.getlist("option_1")
        options_2 = request.POST.getlist("option_2")
        options_3 = request.POST.getlist("option_3")
        options_4 = request.POST.getlist("option_4")
        correct_options = request.POST.getlist("correct_option")

        # Saving the data to the database
        for i in range(len(questions)):
            MCQ.objects.create(
                course=course,
                question=questions[i],
                option_1=options_1[i],
                option_2=options_2[i],
                option_3=options_3[i],
                option_4=options_4[i],
                correct_option=correct_options[i]
            )
        messages.success(request, "MCQ added successfully.")
        return redirect("course:course-detail", pk=course_id)


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
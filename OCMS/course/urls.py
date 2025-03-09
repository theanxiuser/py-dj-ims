from django.urls import path

from .views import (
    CourseListView,
    CourseCreateView,
    CourseDetailView,
    CourseUpdateView,
    CourseDeleteView,
    MCQCreateView,
    SolveMCQView
)


app_name = "course"
urlpatterns = [
    path("", CourseListView.as_view(), name="course-list"),
    path("create", CourseCreateView.as_view(), name="course-create"),
    path("<int:pk>/", CourseDetailView.as_view(), name="course-detail"),
    path("<int:pk>/update", CourseUpdateView.as_view(), name="course-update"),
    path("<int:pk>/delete", CourseDeleteView.as_view(), name="course-delete"),
    path("create-mcq/<int:course_id>", MCQCreateView.as_view(), name="mcq-create"),
    path("solve-mcq/<int:course_id>", SolveMCQView.as_view(), name="mcq-solve"),
]
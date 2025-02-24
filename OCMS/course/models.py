from django.db import models
from userauth.models import CustomUser


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        related_name="courses_taught",
        limit_choices_to={"role": "instructor"}
    )
    students = models.ManyToManyField(
        CustomUser,
        related_name="courses",
        limit_choices_to={"role": "student"}
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "course"

OPTION_CHOICES = (
    (1, "Option 1"),
    (2, "Option 2"),
    (3, "Option 3"),
    (4, "Option 4"),
)

class MCQ(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="mcqs")
    question = models.TextField(null=False, blank=False)
    option_1 = models.CharField(max_length=255, null=False, blank=False)
    option_2 = models.CharField(max_length=255, null=False, blank=False)
    option_3 = models.CharField(max_length=255, null=False, blank=False)
    option_4 = models.CharField(max_length=255, null=False, blank=False)
    correct_option = models.IntegerField(choices=OPTION_CHOICES, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    class Meta:
        db_table = "mcq"


class Response(models.Model):
    student = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        limit_choices_to={"role": "student"},
        null=False,
        blank=False
    )
    mcq = models.ForeignKey(
        MCQ,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    selected_option = models.IntegerField(choices=OPTION_CHOICES, null=False, blank=False)
    is_correct = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.mcq.question} - {self.is_correct}"

    def save(self, *args, **kwargs):
        if self.selected_option == self.mcq.correct_option:
            self.is_correct = True
        super().save(*args, **kwargs)

    class Meta:
        db_table = "response"

from django.contrib.auth.models import AbstractUser
from django.db import models

ROLE_CHOICES = (
    ("student", "Student"),
    ("instructor", "Instructor"),
)

class CustomUser(AbstractUser):
    role = models.CharField(max_length=25, choices=ROLE_CHOICES, default="student")

    def is_student(self):
        return self.role == "student"

    def is_instructor(self):
        return self.role == "instructor"

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} - {self.role}"

    class Meta:
        db_table = "custom_user"


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    image = models.ImageField(upload_to="user_images/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - Profile"

    class Meta:
        db_table = "profile"

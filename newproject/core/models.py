from django.db import models

# Create your models here.

class Content(models.Model):
    title = models.CharField(max_length=255, unique=True, null=False, blank=False)
    description = models.TextField()

    class Meta:
        db_table = "content"

    def __str__(self):
        return self.title
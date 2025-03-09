from django.contrib import admin
from .models import Course, MCQ, Response


admin.site.register(Course)
admin.site.register(Response)

class MCQAdmin(admin.ModelAdmin):
    list_display = ["course", "question", "option_1", "option_2", "option_3", "option_4", "correct_option"]
    search_fields = ["question"]
    list_filter = ["course"]
    list_per_page = 20

admin.site.register(MCQ, MCQAdmin)

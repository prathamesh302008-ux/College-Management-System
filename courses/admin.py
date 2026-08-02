from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = (
        "course_name",
        "course_code",
        "department",
        "semester",
        "duration",
    )

    search_fields = (
        "course_name",
        "course_code",
    )

    list_filter = (
        "department",
        "semester",
    )
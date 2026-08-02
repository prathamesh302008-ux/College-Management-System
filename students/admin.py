from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        "enrollment_no",
        "first_name",
        "last_name",
        "course",
        "semester",
        "email",
        "user",
    )

    search_fields = (
        "enrollment_no",
        "first_name",
        "last_name",
        "email",
        "user__username",
    )

    list_filter = (
        "course",
        "semester",
    )

    autocomplete_fields = (
        "user",
    )
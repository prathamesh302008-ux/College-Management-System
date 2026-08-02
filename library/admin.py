from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = (
        "book_name",
        "book_code",
        "author",
        "available",
        "status",
    )

    search_fields = (
        "book_name",
        "book_code",
        "author",
    )

    list_filter = (
        "status",
    )
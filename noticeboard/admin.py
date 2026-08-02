from django.contrib import admin
from .models import Notice


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "notice_date",
        "status",
    )

    search_fields = (
        "title",
    )

    list_filter = (
        "status",
    )
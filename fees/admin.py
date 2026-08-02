from django.contrib import admin
from .models import Fee


@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):

    list_display = (
        "student",
        "total_fee",
        "paid_fee",
        "status",
        "payment_date",
    )

    search_fields = (
        "student__first_name",
        "student__last_name",
    )

    list_filter = (
        "status",
    )
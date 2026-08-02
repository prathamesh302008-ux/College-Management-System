from django.db import models


class Notice(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    notice_date = models.DateField()

    STATUS = [
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="Active"
    )

    def __str__(self):
        return self.title
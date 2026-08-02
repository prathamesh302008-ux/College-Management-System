from django.db import models


class Department(models.Model):

    department_name = models.CharField(
        max_length=100
    )

    department_code = models.CharField(
        max_length=50,
        unique=True
    )

    hod_name = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.department_name
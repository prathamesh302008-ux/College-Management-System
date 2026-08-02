from django.db import models

from departments.models import Department


class Course(models.Model):

    course_name = models.CharField(
        max_length=100
    )

    course_code = models.CharField(
        max_length=50,
        unique=True
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    semester = models.PositiveIntegerField()

    duration = models.CharField(
        max_length=50
    )

    description = models.TextField(
        blank=True,
        null=True
    )


    def __str__(self):

        return self.course_name
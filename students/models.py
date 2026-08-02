from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="student_profile"
    )

    enrollment_no = models.CharField(
        max_length=50,
        unique=True
    )

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=15
    )

    course = models.CharField(
        max_length=100
    )

    semester = models.CharField(
        max_length=20
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    photo = models.ImageField(
        upload_to="students/",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
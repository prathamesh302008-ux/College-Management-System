from django.db import models

from students.models import Student


class Attendance(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    attendance_date = models.DateField()

    STATUS = [

        ("Present", "Present"),

        ("Absent", "Absent"),

        ("Leave", "Leave"),

    ]

    status = models.CharField(
        max_length=10,
        choices=STATUS
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):

        return f"{self.student} - {self.attendance_date}"
from django.db import models

from students.models import Student


class Fee(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    total_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    paid_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_date = models.DateField()

    STATUS = [

        ("Paid", "Paid"),

        ("Partial", "Partial"),

        ("Pending", "Pending"),

    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS
    )


    def pending_fee(self):

        return self.total_fee - self.paid_fee


    def __str__(self):

        return str(self.student)
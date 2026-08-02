from django.db import models


class Book(models.Model):

    book_name = models.CharField(
        max_length=200
    )

    book_code = models.CharField(
        max_length=50,
        unique=True
    )

    author = models.CharField(
        max_length=150
    )

    publisher = models.CharField(
        max_length=150
    )

    quantity = models.PositiveIntegerField()

    available = models.PositiveIntegerField()

    STATUS = [

        ("Available", "Available"),

        ("Issued", "Issued"),

    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="Available"
    )


    def __str__(self):

        return self.book_name
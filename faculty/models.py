from django.db import models


class Faculty(models.Model):

    faculty_id = models.CharField(
        max_length=50,
        unique=True
    )

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    email = models.EmailField(
        unique=True
    )

    phone = models.CharField(
        max_length=15
    )

    department = models.CharField(
        max_length=100
    )

    qualification = models.CharField(
        max_length=100
    )

    joining_date = models.DateField()

    photo = models.ImageField(
        upload_to="faculty/",
        blank=True,
        null=True
    )


    def __str__(self):

        return self.first_name + " " + self.last_name
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    ROLE_CHOICES = (
        ('Principal','Principal'),
        ('HOD','HOD'),
        ('Faculty','Faculty'),
        ('Student','Student'),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )


    def __str__(self):
        return self.user.username
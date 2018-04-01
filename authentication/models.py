from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    birthday = models.DateTimeField(blank=False, null=True)

    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender =  models.CharField(max_length=1, choices=GENDERS, blank=False, null=True)

    nationality = models.CharField(max_length=255, blank=False, null=True)

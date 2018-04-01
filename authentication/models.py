from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    birthday = models.DateTimeField(blank=False, null=True)
    life_expectancy = models.IntegerField(null=True)
    GENDERS = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender =  models.CharField(max_length=10, choices=GENDERS, blank=False, null=True)

    nationality = models.CharField(max_length=255, blank=False, null=True)

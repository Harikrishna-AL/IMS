from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from buildings.models import Ticket

# Create your models here.
class AgentUser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    GENDER_CHOICES = (
        (
            "Gender",
            (
                ("M", "Male"),
                ("F", "Female"),
            ),
        ),
    )
    gender = models.CharField(max_length=200, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200, default="state")
    zip = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def _str_(self):
        return self.name


class CustomerUser(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    GENDER_CHOICES = (
        (
            "Gender",
            (
                ("M", "Male"),
                ("F", "Female"),
            ),
        ),
    )
    gender = models.CharField(max_length=200, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def _str_(self):
        return self.name

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.username



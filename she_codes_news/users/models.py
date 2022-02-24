from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify
import uuid

class CustomUser(AbstractUser):
    location = models.CharField(max_length=200, blank=True)
    bio = models.CharField(null=True, max_length=200)
    avatar = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.username

class profile(models.Model):
    CustomUser = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_img = models.URLField(default='default.jpg')

    def __str__(self):
        return f'{self.CustomUser.username} profile'

 
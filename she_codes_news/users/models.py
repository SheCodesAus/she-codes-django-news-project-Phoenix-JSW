from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=200, blank=True)
    bio = models.CharField(null=True, max_length=200)


    def __str__(self):
        return self.username

class Profile(models.Model):
    CustomUser = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    Profile_img = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.CustomUser.username} Profiles'


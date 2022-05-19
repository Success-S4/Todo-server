from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    profile_img = models.ImageField(null=True, upload_to="accounts/", blank=True)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
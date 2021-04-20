from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators    

class CustomUser(AbstractUser):
    company_name = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to='profile_pics/')
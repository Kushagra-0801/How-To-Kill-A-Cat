from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    image = models.ImageField()
    bio = models.TextField(max_length=500)
    location = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username


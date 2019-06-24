from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    upload_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    image = models.ImageField()


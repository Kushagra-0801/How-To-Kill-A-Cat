from django.db import models
from django.contrib.auth import get_user_model
from posts.models import Post
from django.utils import timezone

User = get_user_model()

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


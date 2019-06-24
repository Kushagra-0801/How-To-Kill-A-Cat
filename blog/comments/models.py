from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    upload_date = models.DateField()
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    


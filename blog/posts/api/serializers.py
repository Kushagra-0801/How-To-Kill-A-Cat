from rest_framework import serializers
from django.contrib.auth import get_user_model
from posts.models import Post
from comments.models import Comment


User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    lookup_field = 'title'
    class Meta:
        model = Post
        fields = 'title', 'content', 'author', 'upload_date', 'image'
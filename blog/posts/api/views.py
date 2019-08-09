from rest_framework import generics, permissions
from .serializers import PostSerializer
from posts.models import Post
from comments.models import Comment
from django.contrib.auth import get_user_model
User = get_user_model()

class PostRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = 'title'
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

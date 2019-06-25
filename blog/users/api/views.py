from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
User = get_user_model()

class UserCreateApiView(generics.CreateAPIView):
    model = User
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
    

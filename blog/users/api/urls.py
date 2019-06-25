from django.urls import path
from .views import UserCreateApiView



urlpatterns = [
    path("user/register/",UserCreateApiView.as_view(), name = "create-user-api-view")
]

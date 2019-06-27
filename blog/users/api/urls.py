from django.urls import path
from .views import UserCreateApiView
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path("user/register/", UserCreateApiView.as_view(), name="create-user-api-view"),
    path("auth/login/", obtain_jwt_token, name="api-login"),
]

from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path("register/", views.UserCreateAPIView.as_view(), name="create-user-api-view"),
    path("auth/login/", obtain_jwt_token, name="api-login"),
    path(
        "<str:username>/",
        views.UserProfileAPIView.as_view(),
        name="profile-user-api-view",
    ),
]


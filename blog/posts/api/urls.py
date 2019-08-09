from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("<str:title>/", views.PostRetrieveAPIView.as_view(), name='post-retrieve'),
]

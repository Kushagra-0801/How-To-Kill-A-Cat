from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class HomePage(ListView):
    model = Post
    template_name = "posts/home_page.html"
    context_object_name = "posts"

    def get_queryset(self):
        qs = Post.objects.order_by("-upload_date")[:5]
        return qs

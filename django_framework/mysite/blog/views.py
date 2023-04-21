from django.http import HttpResponse
from django.shortcuts import reverse, render
from django.views import View
from .models import Post


def home(request):
    text = "Welcome to the PythonBugs Blog"
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {"welcome_text": text, "all_posts": posts})


class PostDetail(View):
    
    def get(self, request, slug):
        blog_post = Post.objects.get(slug=slug)
        return render(request, 'blog/post-detail.html', {"post": blog_post})

    
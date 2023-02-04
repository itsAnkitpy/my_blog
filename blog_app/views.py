from django.shortcuts import render,get_object_or_404
from .models import *

def index(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
     
    context = {
        'posts':latest_posts,
    }
    return render(request, 'blog_app/index.html',context)

def posts(request):
    all_posts = Post.objects.all().order_by('-date')
     
    context = {
        'all_posts':all_posts,
    }
    return render(request, 'blog_app/posts.html',context)

def post_detail(request,slug):
    identified_post = get_object_or_404(Post, slug=slug)

    context = {
        'post':identified_post,
    }
    return render(request, 'blog_app/post-detail.html',context)

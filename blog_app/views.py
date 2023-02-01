from django.shortcuts import render

def index(request):
    return render(request, 'blog_app/index.html')

def posts(request):
    return render(request, 'blog_app/posts.html')

def post_detail(request,slug):
    return render(request, 'blog_app/post-detail.html')

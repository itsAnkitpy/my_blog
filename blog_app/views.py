from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

from .models import *
from .forms import CommentForm

class IndexPageView(ListView):
    template_name = 'blog_app/index.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'

    def get_queryset(self):
        queryset =  super().get_queryset()
        data = queryset[:3]
        return data

class AllPostsView(ListView):
    template_name = 'blog_app/posts.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'all_posts'

class SinglePostView(View):
    
    def get(self,request,slug):
        post = Post.objects.get(slug=slug)

        context = {
            'post':post,
            'post_tags':post.tags.all(),
            'comment_form': CommentForm(),
            'comments':post.comments.all().order_by('-id'),
        }

        return render(request, 'blog_app/post-detail.html',context)

    def post(self,request,slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))

        

        context = {
            'post':post,
            'post_tags':post.tags.all(),
            'comment_form': comment_form,
            'comments':post.comments.all().order_by('-id'),
        }

        return render(request, 'blog_app/post-detail.html',context)
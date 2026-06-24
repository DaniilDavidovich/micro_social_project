from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post


def posts_list(request):
   template = 'posts/posts.html'
   posts = Post.objects.order_by('-pub_date')[:10]

   # Post.objects.all() 
   # Post.objects.get(id=1)
   # Post.objects.get(pk=1).
   # Post.objects.filter(pub_date__year=1854) 
   # Post.objects.filter(text__startswith='Search entities with this text') 

   context = {
        'posts': posts,
    }
   
   return render(request, template, context=context) 


def post_detail(request, pk):
   template = 'posts/post_detail.html'
   post = get_object_or_404(Post, pk=pk)
   print(post.group)
   context = { 'post': post }
   return render(request, template, context) 


def group_posts(request, slug):
    return HttpResponse(f'Hello {slug}')








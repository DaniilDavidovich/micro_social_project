from django.shortcuts import render

from django.http import HttpResponse
from .models import Post


def index(request):
   template = 'posts/index.html'
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


def posts_list(request):
   return HttpResponse('Posts list')


def post_detail(request, pk):
   return HttpResponse(f'Posts number {pk}') 

def slug(request, slug):
    return HttpResponse(f'Hello {slug}')








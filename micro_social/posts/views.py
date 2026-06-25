from django.shortcuts import render, get_object_or_404
from django.db.models import Count, Q 
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Post
from .models import Group


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
   
   context = { 
      'post': post,
   }
   return render(request, template, context) 


def group_detail(request, slug):

    group = get_object_or_404(
        Group,
        slug=slug
    )

    posts = (
        group.posts.all().select_related('author').order_by('-pub_date')
    )

    paginator = Paginator(posts, 20)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {
        'group': group,
        'page_obj': page_obj,
    }

    return render(request, 'posts/group_detail.html', context)

def groups_list(request):
    groups = Group.objects.annotate(posts_count=Count('posts')).order_by('-posts_count')[:16]
    context = {'groups': groups}
    return render(request, 'posts/groups.html', context)

def groups_search(request):
    q = request.GET.get('q', '').strip()
    groups = Group.objects.annotate(posts_count=Count('posts')).order_by('-posts_count')
    if q:
        groups = groups.filter(
            Q(title__icontains=q) | Q(description__icontains=q)
        )
    groups = groups[:16]
    context = {'groups': groups}
    html = render_to_string('posts/_group_cards.html', context, request=request)
    return JsonResponse({'html': html, 'count': groups.count()})






from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse('Home view')


def posts_list(request):
   return HttpResponse('Posts list')


def post_detail(request, pk):
   return HttpResponse(f'Posts number {pk}') 

def slug(request, slug):
    return HttpResponse(f'Hello {slug}')






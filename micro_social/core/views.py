from django.shortcuts import render
from django.http import HttpResponse


def about(request):
   template = 'core/about.html'
   context = { "url" : "about" }
   return render(request, template, context)


def terms(request):
    template = 'core/terms.html'
    context = { "url" : "terms" }
    return render(request, template, context)


def privacy(request):
    template = 'core/privacy.html'
    context = { "url" : "privacy" }
    return render(request, template, context)


def support(request):
   template = 'core/support.html'
   context = { "url" : "support" }
   return render(request, template, context)

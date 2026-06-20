
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('posts/', views.posts_list),
    path('post/<int:pk>/', views.post_detail),
    path('group/<slug:slug>/', views.slug),
] 
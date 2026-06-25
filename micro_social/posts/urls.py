
from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name='posts_list'),
    path('<int:pk>', views.post_detail,  name='post_detail'),
    path('groups', views.groups_list, name ='groups_list'),
    path('groups/search/', views.groups_search, name='groups_search'),
    path('group/<slug:slug>/', views.group_detail, name='group_detail'),
] 

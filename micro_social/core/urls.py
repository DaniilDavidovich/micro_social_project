
from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = 'core'

urlpatterns = [
    path('', RedirectView.as_view(url='/about/', permanent=True), name='about'),
    path('about/', views.about, name='about'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('support/', views.support, name='support'),
]
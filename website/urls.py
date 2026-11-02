from django.urls import path
from . import views
from core import views as core_views

urlpatterns = [
    path('', views.home, name='home'),
   
    path('about/', views.about, name='about'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pray/', views.pray, name='pray'),
    path('serve/', views.serve, name='serve'),
    path('give/', views.give, name='give'),
    path('learn/', views.learn, name='learn'),
    path('vision/', views.vision, name='vision'),
]
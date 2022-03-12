from os import name
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact')
]

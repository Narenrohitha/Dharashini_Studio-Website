from django.contrib import admin
from django.urls import path, include
from blog.views import PostList
from . import views

urlpatterns = [
    path('',PostList.as_view()),
]

# -*- coding: utf-8 -*-
from django.urls import path

from backend.api.home.views import Posts

urlpatterns = [
    path('posts$', Posts.as_view(), name='home_posts'),
]

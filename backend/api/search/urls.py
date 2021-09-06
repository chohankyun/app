# -*- coding: utf-8 -*-
from django.urls import path

from backend.api.search.views import Posts

urlpatterns = [
    path('posts$', Posts.as_view(), name='search_posts'),
]

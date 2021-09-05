# -*- coding: utf-8 -*-
from django.urls import re_path

from backend.api.home.views import PostsForHome

urlpatterns = [
    re_path(r'^posts/(?P<order>\w+)$', PostsForHome.as_view(), name='home_posts_by_order'),
]

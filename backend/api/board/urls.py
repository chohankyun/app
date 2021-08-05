# -*- coding: utf-8 -*-
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from backend.api.board.views import Categories, PostViewSet, ReplyViewSet, RepliesInPost, PostsByCategoryNOrder

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'replies', ReplyViewSet)

urlpatterns = [
    re_path(r'^posts/(?P<category>\w+)/(?P<order>\w+)/$', PostsByCategoryNOrder.as_view(), name='board_posts_by_category_n_order'),
    re_path(r'^replies/post/(?P<id>\w+)/$', RepliesInPost.as_view(), name='replies_post_id'),
    path('categories/', Categories.as_view(), name='categories'),
    path('', include(router.urls)),
]

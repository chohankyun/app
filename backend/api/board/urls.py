# -*- coding: utf-8 -*-
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from backend.api.board.views import Categories, PostViewSet, ReplyViewSet, RepliesInPost, PostsByCategoryNOrder, RecommendViewSet, RecommendCountNOwner

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'replies', ReplyViewSet)
router.register(r'recommend', RecommendViewSet)

urlpatterns = [
    re_path(r'^posts/(?P<category>\w+)/(?P<order>\w+)/$', PostsByCategoryNOrder.as_view(), name='board_posts_by_category_n_order'),
    re_path(r'^replies/post/(?P<id>\w+)/$', RepliesInPost.as_view(), name='replies_post_id'),
    re_path(r'^recommend/count/(?P<post_id>\w+)/$', RecommendCountNOwner.as_view(), name='board_recommend_count_n_owner'),
    path('categories/', Categories.as_view(), name='categories'),
    path('', include(router.urls)),
]

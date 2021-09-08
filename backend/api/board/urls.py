# -*- coding: utf-8 -*-
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from backend.api.board.views import Categories, PostSet, ReplySet, PostReplies, RecommendSet, PostRecommendToggle

router = DefaultRouter(trailing_slash=False)
router.register(r'posts', PostSet)
router.register(r'replies', ReplySet)
router.register(r'recommend', RecommendSet)

urlpatterns = [
    re_path(r'^posts/(?P<post_id>\w+)/replies', PostReplies.as_view(), name='board_post_replies'),
    re_path(r'^posts/(?P<post_id>\w+)/recommend-toggle', PostRecommendToggle.as_view(), name='board_post_recommend_toggle'),
    path('categories', Categories.as_view(), name='board_categories'),
    path('', include(router.urls)),
]

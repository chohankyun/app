# -*- coding: utf-8 -*-
from django.urls import re_path

from backend.api.search.views import SearchPostByOrder

urlpatterns = [
    re_path(r'^posts/(?P<search_word>.+)/(?P<order>\w+)$', SearchPostByOrder.as_view(), name='search_post_by_order'),
]

# -*- coding: utf-8 -*-
from django.urls import path

from backend.api.board.views import CategoryList

urlpatterns = [
    path('category/list/', CategoryList.as_view(), name='category_list'),
]

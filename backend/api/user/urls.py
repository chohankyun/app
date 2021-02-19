# -*- coding: utf-8 -*-
from django.urls import path

from backend.api.user.views import Login

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
]

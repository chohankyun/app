# -*- coding: utf-8 -*-
from django.urls import path

from backend.api.user.views import Login, IsAuth, Logout, RegisterView

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('is_auth/', IsAuth.as_view(), name='is_auth'),
    path('register/', RegisterView.as_view(), name='register'),
]

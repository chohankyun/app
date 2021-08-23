# -*- coding: utf-8 -*-
from django.urls import path, re_path

from backend.api.user.views import Login, IsAuth, Logout, RegisterView, EmailConfirmView, AppIdFindView

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('is_auth/', IsAuth.as_view(), name='is_auth'),
    path('register/', RegisterView.as_view(), name='register'),
    re_path(r'^email/confirm/(?P<key>[-:\w]+)/$', EmailConfirmView.as_view(), name="email_confirm"),
    path('find/app_id/', AppIdFindView.as_view(), name='app_id_find'),
    path('find/password/', AppIdFindView.as_view(), name='password_find'),
]

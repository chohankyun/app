# -*- coding: utf-8 -*-
from django.urls import path, re_path

from backend.api.user.views import Login, IsAuth, Logout, RegisterView, EmailConfirmView, AppIdFindView, PasswordResetView, PasswordResetConfirmView, PasswordChangeView

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('is_auth/', IsAuth.as_view(), name='is_auth'),
    path('register/', RegisterView.as_view(), name='register'),
    re_path(r'^email/confirm/(?P<key>[-:\w]+)/$', EmailConfirmView.as_view(), name="email_confirm"),
    path('find/app_id/', AppIdFindView.as_view(), name='app_id_find'),
    path('password/reset/', PasswordResetView.as_view(), name='password_reset'),
    re_path(r'^password/reset/confirm/(?P<uid>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/(?P<password>.+)/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path(r'^password/change/$', PasswordChangeView.as_view(), name='password_change'),
]

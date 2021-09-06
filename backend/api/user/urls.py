# -*- coding: utf-8 -*-
from django.urls import path, re_path

from backend.api.user.views import Login, Logout, IsAuth, Register, EmailConfirm, AppIdFind, PasswordReset, PasswordChange, PasswordResetConfirm

urlpatterns = [
    path('login', Login.as_view(), name='user_login'),
    path('logout', Logout.as_view(), name='user_logout'),
    path('is-auth', IsAuth.as_view(), name='user_is_auth'),
    path('register', Register.as_view(), name='user_register'),
    re_path(r'^email/confirm/(?P<key>[-:\w]+)$', EmailConfirm.as_view(), name="user_email_confirm"),
    path('find/app-id', AppIdFind.as_view(), name='user_app_id_find'),
    path('password/reset', PasswordReset.as_view(), name='user_password_reset'),
    re_path(r'^password/reset/confirm/(?P<uid>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/(?P<password>.+)$', PasswordResetConfirm.as_view(), name='user_password_reset_confirm'),
    path('password/change$', PasswordChange.as_view(), name='user_password_change'),
]

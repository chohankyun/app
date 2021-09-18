# -*- coding: utf-8 -*-
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from backend.api.uauth.views import Login, Logout, IsAuth, Register, EmailConfirm, UidFind, PasswordReset, PasswordChange, PasswordResetConfirm, UserSet

router = DefaultRouter(trailing_slash=False)
router.register(r'users', UserSet)

urlpatterns = [
    path('login', Login.as_view(), name='user_login'),
    path('logout', Logout.as_view(), name='user_logout'),
    path('is-auth', IsAuth.as_view(), name='user_is_auth'),
    path('register', Register.as_view(), name='user_register'),
    re_path(r'^email/confirm/(?P<key>.+)', EmailConfirm.as_view(), name="user_email_confirm"),
    path('uid/find', UidFind.as_view(), name='user_uid_find'),
    path('password/reset', PasswordReset.as_view(), name='user_password_reset'),
    re_path(r'^password/reset/confirm/(?P<uid>.+)/(?P<token>.+)/(?P<password>.+)', PasswordResetConfirm.as_view(), name='user_password_reset_confirm'),
    path('password/change', PasswordChange.as_view(), name='user_password_change'),
    path('', include(router.urls)),
]

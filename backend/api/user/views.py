# -*- coding: utf-8 -*-
from django.contrib.auth import user_logged_in, authenticate
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from backend.com.jwt.handler import HttpHandler


class Login(GenericAPIView):
    permission_classes = (AllowAny,)
    http_handler = HttpHandler()

    def post(self, request, *args, **kwargs):
        user = self.login(app_id=request.data['app_id'], password=request.data['password'])
        request.user, jwt_user_data = self.http_handler.get_jwt_user(dict(user.__dict__))
        return Response(jwt_user_data, status=status.HTTP_200_OK)

    def login(self, **credentials):
        user = authenticate(**credentials)

        if not user:
            raise AuthenticationFailed(detail='The id or password do not match.')
        if not user.is_active:
            raise AuthenticationFailed(detail='This is disabled id.')
        if not user.is_email_verified:
            raise PermissionDenied(detail='Email verification has not been completed.')
        if user.is_staff or user.is_superuser:
            raise PermissionDenied(detail='You do not have permission.')

        user_logged_in.send(sender=user.__class__, request=self.request, user=user)
        return user

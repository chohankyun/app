# -*- coding: utf-8 -*-
from django.contrib.auth import user_logged_in, authenticate
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from backend.api.user.jwt import Handler


class Login(GenericAPIView):
    permission_classes = (AllowAny,)
    handler = Handler()

    def post(self, request, *args, **kwargs):
        user = self.login(app_id=request.data['app_id'], password=request.data['password'])
        payload = {'id': user.id, 'name': user.name,
                   'group_name': getattr(user.groups.first(), 'name', 'none'),
                   'is_authenticated': True}
        jwt_user = self.handler.jwt_user(payload)
        jwt_user['token'] = self.get_jwt(jwt_user)
        return Response(jwt_user, status=status.HTTP_200_OK)

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

    def get_jwt(self, jwt_user):
        data_for_payload = jwt_user.copy()
        data_for_payload['client_ip'] = self.handler.get_client_ip_address(self.request)
        payload = self.handler.jwt_payload_handler(data_for_payload)
        token = self.handler.jwt_encode_handler(payload)
        return token

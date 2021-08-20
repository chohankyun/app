# -*- coding: utf-8 -*-
from django.contrib.auth import user_logged_in, authenticate
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied, ParseError
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from backend.api.user.models import User
from backend.com.jwt.handler import jwt_user


class IsAuth(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)


class Logout(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request, *args, **kwargs):
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class Login(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        user = self.login(app_id=request.data['app_id'], password=request.data['password'])
        request.user = jwt_user(user)
        return Response(request.user.__dict__, status=status.HTTP_200_OK)

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


class RegisterView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        user = self.register()
        user_logged_in.send(sender=user.__class__, request=self.request, user=user)
        request.user = jwt_user(user)
        return Response(request.user.__dict__, status=status.HTTP_200_OK)

    def register(self):
        if self.request.data['password'] != self.request.data['re_password']:
            raise ParseError(detail="The two password fields didn't match.")
        if User.objects.filter(app_id=self.request.data['app_id']).exists():
            raise ParseError(detail='A user is already registered with this username.')

        emails = User.objects.values_list('email', flat=True).distinct()
        if self.request.data['email'] in emails:
            raise ParseError(detail='A user is already registered with this email.')

        user_item_names = [field.name for field in User._meta.fields if field.name != 'id']
        register_data = {key: self.request.data[key] for key in self.request.data if key in user_item_names}
        user = User.objects.create_user(**register_data)
        return user

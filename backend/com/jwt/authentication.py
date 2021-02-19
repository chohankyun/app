# -*- coding: utf-8 -*-
import jwt
from django.utils.encoding import smart_text
from rest_framework import exceptions
from rest_framework.authentication import (
    BaseAuthentication, get_authorization_header
)

from backend.com.jwt.handler import Token, jwt_salt, jwt_user
from backend.com.jwt.settings import jwt_settings


class BaseJSONWebTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        jwt_value = self.get_jwt_value(request)
        if jwt_value is None:
            return None

        try:
            token = Token(salt=jwt_salt(request))
            payload = token.jwt_decode_token(jwt_value)
        except jwt.ExpiredSignatureError:
            msg = 'Signature has expired.'
            raise exceptions.AuthenticationFailed(msg)
        except jwt.DecodeError:
            msg = 'Error decoding signature.'
            raise exceptions.AuthenticationFailed(msg)
        except jwt.InvalidTokenError:
            msg = 'Invalid token.'
            raise exceptions.AuthenticationFailed(msg)

        return jwt_user(payload), None


class JSONWebTokenAuthentication(BaseJSONWebTokenAuthentication):
    www_authenticate_realm = 'api'

    @staticmethod
    def get_jwt_value(request):
        auth = get_authorization_header(request).split()
        auth_header_prefix = jwt_settings.JWT_AUTH_HEADER_PREFIX.lower()

        if not auth:
            if jwt_settings.JWT_AUTH_COOKIE:
                return request.COOKIES.get(jwt_settings.JWT_AUTH_COOKIE)
            return None

        if smart_text(auth[0].lower()) != auth_header_prefix:
            return None

        if len(auth) == 1:
            msg = 'Invalid Authorization header. No credentials provided.'
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = 'Invalid Authorization header. Credentials string should not contain spaces.'
            raise exceptions.AuthenticationFailed(msg)

        return auth[1]

    def authenticate_header(self, request):
        return '{0} realm="{1}"'.format(jwt_settings.JWT_AUTH_HEADER_PREFIX, self.www_authenticate_realm)

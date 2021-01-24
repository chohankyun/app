# -*- coding: utf-8 -*-
from calendar import timegm
from datetime import datetime

import jwt
from django.utils.encoding import smart_text
from rest_framework import exceptions
from rest_framework.authentication import (
    BaseAuthentication, get_authorization_header
)

from backend.drf.settings import JWT_AUTH


class BaseJSONWebTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        jwt_value = self.get_jwt_value(request)
        if jwt_value is None:
            return None

        try:
            handler = Handler()
            payload = handler.jwt_decode_handler(jwt_value)
        except jwt.ExpiredSignature:
            msg = 'Signature has expired.'
            raise exceptions.AuthenticationFailed(msg)
        except jwt.DecodeError:
            msg = 'Error decoding signature.'
            raise exceptions.AuthenticationFailed(msg)
        except jwt.InvalidTokenError:
            msg = 'Invalid token.'
            raise exceptions.AuthenticationFailed(msg)

        if payload.get('client_ip') != handler.get_client_ip_address(request):
            msg = 'Error decoding data.'
            raise exceptions.AuthenticationFailed(msg)

        jwt_user = handler.jwt_user(payload)
        return jwt_user, payload


class JSONWebTokenAuthentication(BaseJSONWebTokenAuthentication):
    www_authenticate_realm = 'api'

    @staticmethod
    def get_jwt_value(request):
        auth = get_authorization_header(request).split()
        auth_header_prefix = JWT_AUTH['JWT_AUTH_HEADER_PREFIX'].lower()

        if not auth:
            if JWT_AUTH['JWT_AUTH_COOKIE']:
                return request.COOKIES.get(JWT_AUTH['JWT_AUTH_COOKIE'])
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
        return '{0} realm="{1}"'.format(JWT_AUTH['JWT_AUTH_HEADER_PREFIX'], self.www_authenticate_realm)


class Handler:
    @staticmethod
    def jwt_get_secret_key():
        """
            나중에 키 관련 로직 추가
        """
        if JWT_AUTH['JWT_GET_USER_SECRET_KEY']:
            key = str(JWT_AUTH['JWT_GET_USER_SECRET_KEY'])
            return key
        return JWT_AUTH['JWT_SECRET_KEY']

    @staticmethod
    def jwt_user(payload):
        jwt_user = {
            'id': payload.get('id'),
            'name': payload.get('name'),
            'group_name': payload.get('group_name'),
            'is_authenticated': True}
        return type('jwt_user', (object,), jwt_user)

    @staticmethod
    def jwt_payload_handler(data_for_payload):
        payload = {
            'id': data_for_payload.get('id'),
            'name': data_for_payload.get('name'),
            'group_name': data_for_payload.get('group_name'),
            'client_ip': data_for_payload.get('client_ip'),
            'exp': datetime.utcnow() + JWT_AUTH['JWT_EXPIRATION_DELTA']
        }

        if JWT_AUTH['JWT_ALLOW_REFRESH']:
            payload['orig_iat'] = timegm(
                datetime.utcnow().utctimetuple()
            )

        if JWT_AUTH['JWT_AUDIENCE']:
            payload['aud'] = JWT_AUTH.JWT_AUDIENCE

        if JWT_AUTH['JWT_ISSUER']:
            payload['iss'] = JWT_AUTH['JWT_ISSUER']

        return payload

    def jwt_encode_handler(self, payload):
        key = JWT_AUTH['JWT_PRIVATE_KEY'] or self.jwt_get_secret_key()
        return jwt.encode(payload, key, JWT_AUTH['JWT_ALGORITHM'])

    def jwt_decode_handler(self, token):
        options = {
            'verify_exp': JWT_AUTH['JWT_VERIFY_EXPIRATION'],
        }
        secret_key = self.jwt_get_secret_key()
        return jwt.decode(
            token,
            JWT_AUTH['JWT_PUBLIC_KEY'] or secret_key,
            JWT_AUTH['JWT_VERIFY'],
            options=options,
            leeway=JWT_AUTH['JWT_LEEWAY'],
            audience=JWT_AUTH['JWT_AUDIENCE'],
            issuer=JWT_AUTH['JWT_ISSUER'],
            algorithms=[JWT_AUTH['JWT_ALGORITHM']])

    @staticmethod
    def get_client_ip_address(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            client_ip = x_forwarded_for.split(',')[0]
        else:
            client_ip = request.META.get('REMOTE_ADDR')
        return client_ip

